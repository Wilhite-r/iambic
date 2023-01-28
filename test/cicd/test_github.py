from __future__ import annotations

import tempfile
from unittest.mock import patch

import pytest

from iambic.cicd.github import (
    BODY_MAX_LENGTH,
    MERGEABLE_STATE_BLOCKED,
    MERGEABLE_STATE_CLEAN,
    HandleIssueCommentReturnCode,
    ensure_body_length_fits_github_spec,
    format_github_url,
    handle_issue_comment,
    handle_pull_request,
    prepare_local_repo,
)


@pytest.fixture
def mock_github_client():
    with patch("iambic.cicd.github.Github", autospec=True) as mock_github:
        yield mock_github


@pytest.fixture
def issue_comment_context():
    return {
        "server_url": "https://github.com",
        "run_id": "12345",
        "run_attempt": "1",
        "token": "fake-token",
        "sha": "fake-sha",
        "repository": "example.com/iambic-templates",
        "event_name": "issue_comment",
        "event": {
            "comment": {
                "body": "iambic git-apply",
            },
            "issue": {
                "number": 1,
            },
            "repository": {
                "clone_url": "https://github.com/example-org/iambic-templates.git",
            },
        },
    }


@pytest.fixture
def mock_lambda_run_handler():
    with patch(
        "iambic.cicd.github.lambda_run_handler", autospec=True
    ) as _mock_lambda_run_handler:
        with patch("iambic.cicd.github.SHARED_CONTAINER_GITHUB_DIRECTORY", "/tmp") as _:
            with tempfile.TemporaryDirectory() as tmpdirname:
                with patch("iambic.cicd.github.lambda_repo_path", tmpdirname):
                    yield _mock_lambda_run_handler


@pytest.fixture
def mock_repository():
    with patch("iambic.core.git.Repo", autospec=True) as _mock_repository:
        yield _mock_repository


def test_issue_comment_with_non_clean_mergeable_state(
    mock_github_client, issue_comment_context, mock_lambda_run_handler
):
    mock_pull_request = mock_github_client.get_repo.return_value.get_pull.return_value
    mock_pull_request.mergeable_state = MERGEABLE_STATE_BLOCKED
    handle_issue_comment(mock_github_client, issue_comment_context)
    assert mock_lambda_run_handler.called is False
    assert mock_pull_request.merge.called is False


def test_issue_comment_with_not_applicable_comment_body(
    mock_github_client, issue_comment_context, mock_lambda_run_handler
):
    issue_comment_context["event"]["comment"]["body"] = "foo"
    return_code = handle_issue_comment(mock_github_client, issue_comment_context)
    assert return_code == HandleIssueCommentReturnCode.NO_MATCHING_BODY


def test_issue_comment_with_clean_mergeable_state(
    mock_github_client, issue_comment_context, mock_lambda_run_handler, mock_repository
):
    mock_pull_request = mock_github_client.get_repo.return_value.get_pull.return_value
    mock_pull_request.mergeable_state = MERGEABLE_STATE_CLEAN
    mock_pull_request.head.sha = issue_comment_context["sha"]
    mock_repository.clone_from.return_value.head.commit.hexsha = issue_comment_context[
        "sha"
    ]
    handle_issue_comment(mock_github_client, issue_comment_context)
    assert mock_lambda_run_handler.called
    assert mock_pull_request.merge.called


# invariant: PR is only merged if and only if git-apply is successful
def test_issue_comment_with_clean_mergeable_state_and_lambda_handler_crashed(
    mock_github_client, issue_comment_context, mock_lambda_run_handler, mock_repository
):
    mock_pull_request = mock_github_client.get_repo.return_value.get_pull.return_value
    mock_pull_request.mergeable_state = MERGEABLE_STATE_CLEAN
    mock_pull_request.head.sha = issue_comment_context["sha"]
    mock_repository.clone_from.return_value.head.commit.hexsha = issue_comment_context[
        "sha"
    ]
    mock_lambda_run_handler.side_effect = Exception("unexpected failure")
    with pytest.raises(Exception):
        handle_issue_comment(mock_github_client, issue_comment_context)
    assert mock_lambda_run_handler.called
    assert not mock_pull_request.merge.called


def test_format_github_url():
    pr_url = "https://github.com/example-org/iambic-templates.git"
    fake_token = "foobar"
    expected_url = "https://oauth2:foobar@github.com/example-org/iambic-templates.git"
    url = format_github_url(pr_url, fake_token)
    assert url == expected_url


def test_prepare_local_repo():
    temp_templates_directory = tempfile.mkdtemp(
        prefix="iambic_test_temp_templates_directory"
    )
    prepare_local_repo(
        "https://github.com/noqdev/consoleme", temp_templates_directory, "master"
    )


def test_ensure_body_length_fits_github_spec():
    body = "m" * (BODY_MAX_LENGTH + 1)
    assert len(body) > BODY_MAX_LENGTH
    new_body = ensure_body_length_fits_github_spec(body)
    assert len(new_body) <= BODY_MAX_LENGTH


@pytest.fixture
def pull_request_context():
    return {
        "server_url": "https://github.com",
        "run_id": "12345",
        "run_attempt": "1",
        "token": "fake-token",
        "sha": "fake-sha",
        "repository": "example.com/iambic-templates",
        "event_name": "pull_request",
        "event": {
            "pull_request": {
                "number": 1,
            },
            "repository": {
                "clone_url": "https://github.com/example-org/iambic-templates.git",
            },
        },
    }


def test_pull_request_plan(
    mock_github_client, pull_request_context, mock_lambda_run_handler, mock_repository
):
    mock_pull_request = mock_github_client.get_repo.return_value.get_pull.return_value
    mock_pull_request.head.sha = pull_request_context["sha"]
    mock_repository.clone_from.return_value.head.commit.hexsha = pull_request_context[
        "sha"
    ]
    handle_pull_request(mock_github_client, pull_request_context)
    assert mock_lambda_run_handler.called is True