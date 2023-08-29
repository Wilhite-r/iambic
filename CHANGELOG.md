
# Change Log

## 0.11.73 (Aug 23, 2023)

DOCS:
* Update README with IAMbic/TF Differences ; Video img [#605](https://github.com/noqdev/iambic/pull/605)
* IAC Comparison Table [#598](https://github.com/noqdev/iambic/pull/598)
* Update doc on how to turn on Cloudtrail logs integration [#597](https://github.com/noqdev/iambic/pull/597)
* Fix doc links [#596](https://github.com/noqdev/iambic/pull/596)
* Rewrite the getting started section. [#590](https://github.com/noqdev/iambic/pull/590)

BUG FIXES:
* Fixed #608 Implement import filtering protocol for SCP [#609](https://github.com/noqdev/iambic/pull/609)
* Fixed #602 Propagate errors if invalid user or group assignment [#606](https://github.com/noqdev/iambic/pull/606)
* Optimize GitHub PR plan time [#607](https://github.com/noqdev/iambic/pull/607)
* Fix IdentityCenter access rules not being updated [#604](https://github.com/noqdev/iambic/pull/604)
* Fixed EN-2401 Check parent directory truthy-ness before attempt to create it [#603](https://github.com/noqdev/iambic/pull/603)
* Enhance error message during PrincipalID resolution [#599](https://github.com/noqdev/iambic/pull/599)
* Fix error handling for detect not able to create gist [#595](https://github.com/noqdev/iambic/pull/595)

DEV:
* Fix flaky functional test on account assignment [#612](https://github.com/noqdev/iambic/pull/612)

THANKS:
* `hilyas` contributing better docs [#590](https://github.com/noqdev/iambic/pull/590)
* `rodolphoescobar` reporting NOQ::AWS::Organizations::SCP Filter does not work [#608](https://github.com/noqdev/iambic/issues/608)
* `dushyantbhardwaj9` reporting iambic does not throw warning/error for users/groups that do not exists in the Idp [#602](https://github.com/noqdev/iambic/issues/602)
* `dushyantbhardwaj9` reporting import not updating existing IdentityCenter access rules in templates.

## 0.11.59 (Aug 18, 2023)

BUG FIXES:
* Fix #593 PermissionSet InlinePolicy to support single statement syntax [#594](https://github.com/noqdev/iambic/pull/594)

THANKS:
`rodolphoescobar` reporting Permission Set InlinePolicy issue [#593](https://github.com/noqdev/iambic/issues/593)

## 0.11.58 (Aug 18, 2023)

ENHANCEMENTS:
* Cloudtrail logs as git notes on 'detect' commit [#522](https://github.com/noqdev/iambic/pull/522)

BUG FIXES:
* Use alternative implementation of list_users and list_groups [#591](https://github.com/noqdev/iambic/pull/591)

THANKS:
* `dushyantbhardwaj9` for contributing the alternate implementation of list_users and list_groups to workaround some AD + IdentityCenter issues [#557](https://github.com/noqdev/iambic/issues/557)

## 0.11.56 (Aug 17, 2023)

DOCS:
* Update JSON Schema and Schema markdown [#586](https://github.com/noqdev/iambic/pull/586)

BUG FIXES:
* EN-2348: add guards when schema generator fails [#582](https://github.com/noqdev/iambic/pull/582)
* Fix #587 when describe_user and describe_group fail to lookup PrincipalID [#588](https://github.com/noqdev/iambic/pull/588)

ENHANCEMENTS:
* Allow disabling variable substitution [#589](https://github.com/noqdev/iambic/pull/589)

THANKS:
* `rodolphoescobar` reporting ResourceNotFoundException in import resources [#587](https://github.com/noqdev/iambic/issues/587)

## 0.11.52 (Aug 16, 2023)

DOCS:
* Simplify installation instructions [#567](https://github.com/noqdev/iambic/pull/567)

ENHANCEMENTS:
* EventBridge Schedule to invoke detect, expire, enforce, and import periodic tasks [#567](https://github.com/noqdev/iambic/pull/567)

BUG FIXES:
* Fix #581 Relax Target to stay as account id if we cannot look up its account name [#583](https://github.com/noqdev/iambic/pull/583)
* Fix #555 Duplicate menu item [#584](https://github.com/noqdev/iambic/pull/584)

DEV EXPERIENCE:
* Fix pre-commit complaints [#580](https://github.com/noqdev/iambic/pull/580)

THANKS:
* `rodolphoescobar` reporting SCP import issue [#581](https://github.com/noqdev/iambic/issues/581)

## 0.11.48 (Aug 16, 2023)

BUG FIXES:
* Workaround for #557 Defer GUID resolution [#558](https://github.com/noqdev/iambic/pull/558)
* Fix EN-2380 clear known cf stacksets state if user enter into add org flow [#573](https://github.com/noqdev/iambic/pull/573)
* Fix for exception raised when iambic plan command is run on empty template file [#578](https://github.com/noqdev/iambic/pull/578)
* Fix for encoding error when writing proposed_changes.txt [#576](https://github.com/noqdev/iambic/pull/576)

THANKS:
* `dushyantb` reporting [#557](https://github.com/noqdev/iambic/issues/557) and testing [#558](https://github.com/noqdev/iambic/pull/558)
* ` 0xAJX` reporting [#577](https://github.com/noqdev/iambic/issues/577) and contributed the fix [#578](https://github.com/noqdev/iambic/pull/578)
* ` 0xAJX` reporting [#575](https://github.com/noqdev/iambic/issues/575) and contributed the fix [#576](https://github.com/noqdev/iambic/pull/576)

## 0.11.43 (Aug 15, 2023)

BUG FIXES:
* EN-2381 Fixed identity center handling of suspended account [#568](https://github.com/noqdev/iambic/pull/568)
* Added a check to skip code if OS is Windows fixes #570 [#571](https://github.com/noqdev/iambic/pull/571)
* EN-2379 Turn on CF Stacksets for Organizations when possible [#569](https://github.com/noqdev/iambic/pull/569)

THANKS:
* `0xAJX` for reporting [#570](https://github.com/noqdev/iambic/issues/570) and the fix [#571](https://github.com/noqdev/iambic/pull/571)

## 0.11.39 (Aug 11, 2023)

BUG FIXES:
* Fix template generation details [#566](https://github.com/noqdev/iambic/pull/566)

## 0.11.38 (Aug 11, 2023)

DOCS:
* Fix EN-2239 Instruction to set GitHub App icon [#563](https://github.com/noqdev/iambic/pull/563)
* Optimize readme for clarity [#564](https://github.com/noqdev/iambic/pull/564)

BUG FIXES:
* Fix EN-2377 Use list instead of set for deterministic iteration order [#565](https://github.com/noqdev/iambic/pull/564)

## 0.11.35 (Aug 10, 2023)

BUG FIXES:
* Docs and script to update deployed lambda function [#552](https://github.com/noqdev/iambic/pull/552)
* Enhance GitHub App local secrets handling [#559](https://github.com/noqdev/iambic/pull/559)
* Fix condition in policy statement [#560](https://github.com/noqdev/iambic/pull/560)
* Ignore extra fields because of forward compatibility reasons [#561](https://github.com/noqdev/iambic/pull/561)

THANKS:
* `datfinesoul` for giving feedback on need to have docs or automation to update the IAMbic GitHub integration

## 0.11.33 (Aug 9, 2023)

BUG FIXES:
* EN-2373: change regions [#556](https://github.com/noqdev/iambic/pull/556)

THANKS:
* `dushyantb` for reporting issues when IAMbic is used in unsupported AWS regions

## 0.11.32 (Aug 8, 2023)

ENHANCEMENTS:
* Address part of #490. Name the hyperlink with more details [#549](https://github.com/noqdev/iambic/pull/549)
* Added a template_schema_url to all IAMbic templates. [#534](https://github.com/noqdev/iambic/pull/534)
* Addresses some of #490 Plan output improvement [#550](https://github.com/noqdev/iambic/pull/550)

BUG FIXES:
* EN-2345 Runs lint before plan [#547](https://github.com/noqdev/iambic/pull/547)
* EN-2343: Show message when credentials are not provided  [#539](https://github.com/noqdev/iambic/pull/539)
* Fix #489 Handle change_summary differently during rendering [#548](https://github.com/noqdev/iambic/pull/548)
* Fix #507 git apply exceptions is not properly reported in comments [#554](https://github.com/noqdev/iambic/pull/554)

DEV EXPERIENCE:
* Track *.png and *.jpg using Git LFS [#551](https://github.com/noqdev/iambic/pull/551)


THANKS:
* `datfinesoul` for giving feedback on auto formatting and relative time -> absolute timestamp commits made by automation
* `datfinesoul` on reporting plan output is incorrect [#489](https://github.com/noqdev/iambic/issues/489)
* `datfinesoul` on giving feedback on the need of ease of use to lookup schema reference in templates
* `mike.p` on community slack for reporting the issue when the PR contains invalid AWS principal during git apply cycle.

## 0.11.23 (Aug 4, 2023)

DOCS:
* Update IAMbic GitHub Integration docs [#540](https://github.com/noqdev/iambic/pull/540)

ENHANCEMENTS:
* Support both iambic and /iambic syntax [#542](https://github.com/noqdev/iambic/pull/542)
* Support iambic version in GitHub comments [#542](https://github.com/noqdev/iambic/pull/542)

BUG FIXES:
* iambic lint no longer converts expires_at relative time to an absolute [#530](https://github.com/noqdev/iambic/pull/530)
* Fix issue when identity center details is lost during 2nd setup [#541](https://github.com/noqdev/iambic/pull/541)
* Handling TooManyRequestsException in boto_crud_call [#544](https://github.com/noqdev/iambic/pull/544)
* Improved logging in boto_crud_call [#544](https://github.com/noqdev/iambic/pull/544)

THANKS:
* `Rodrigo C.` from community slack on reporting the TooManyRequestsException issue on large orgs.

## 0.11.17 (Aug 3, 2023)

DOCS:
* Fix typo [#533](https://github.com/noqdev/iambic/pull/533)

ENHANCEMENTS:
* Report unhandled exceptions [#516](https://github.com/noqdev/iambic/pull/516)

BUG FIXES:
* Handle multiple iam paths [#536](https://github.com/noqdev/iambic/pull/536)
* Verify GitHub access before proceeding [#537](https://github.com/noqdev/iambic/pull/537)

DEV TOOLS:
* EN-2355 Implement dev workflow to test IAMbic GitHub webhook [#535](https://github.com/noqdev/iambic/pull/535)

THANKS:
* `Rodrigo C.` from community slack on reporting AWS multiple iam paths issue.
* `Shatoria` from community slack on testing out the new IAMbic GitHub integration setup process.

## 0.11.11 (Aug 2, 2023)

ENHANCEMENTS:
* GitHub App creation flow in iambic wizard [#515](https://github.com/noqdev/iambic/pull/515)

## 0.11.8 (Aug 1, 2023)

DOCS:
* Change project description on PyPI [#527](https://github.com/noqdev/iambic/pull/527)
** There were some reference to the old project name. Those were cleaned up.

BUG FIXES:
* Fix #491 Support "merge", "squash", and "rebase" merge method  [#525](https://github.com/noqdev/iambic/pull/525)
* Fix security/dependabot/26 Bump certifi [#524](https://github.com/noqdev/iambic/pull/524)
* Fixed bug where none type description was causing an exception on role [#528](https://github.com/noqdev/iambic/pull/528)
* Attaching and detaching role tags now 2 distinct operations. Fixes to role attribute value resolver on Role._apply_to_account. [#528](https://github.com/noqdev/iambic/pull/528)

THANKS:
`datfinesoul` for reporting GitHub linear history use case. [#491](https://github.com/noqdev/iambic/issues/491)
`Simon D.` in community slack for reporting the old project name references. [#527](https://github.com/noqdev/iambic/pull/527)

## 0.11.03 (July 31, 2023)

BUG FIXES:
* Git commit message not reflecting the linting changes [#521](https://github.com/noqdev/iambic/pull/521)

THANKS:
`datfinesoul` for reporting git commit message not reflecting the actual changes. [#520](https://github.com/noqdev/iambic/issues/520)

## 0.11.01 (July 31, 2023)

DOCS:
* Add Youtube Video reference to README [#517](https://github.com/noqdev/iambic/pull/517)

BUG FIXES:
* Add help text to CLI commands [#510](https://github.com/noqdev/iambic/pull/510)
* Update App Manifest to subscribe to Workflow run [#509](https://github.com/noqdev/iambic/pull/509)
* Update iambic_base_container to 2.0.0 [#511](https://github.com/noqdev/iambic/pull/511)
** Amazon Linux 2023 as the base linux distribution for the Lambda Container Image
** Python 3.10.12 as the python runtime for the Lambda Container Image
* Opportunistically import resource module [#506](https://github.com/noqdev/iambic/pull/506)
** Windows user does not have the resource module available
* Fix #512 Handle FileNotFoundException [#513](https://github.com/noqdev/iambic/pull/513)
* Bump aiohttp from 3.8.4 to 3.8.5 [#514](https://github.com/noqdev/iambic/pull/514)

THANKS:
* `Wilhite-r` contributing [#510](https://github.com/noqdev/iambic/pull/510)

## 0.10.15 (July 21, 2023)

BUG FIXES:
* Fixed error encountered when configuring change detection in the setup wizard. [#508](https://github.com/noqdev/iambic/pull/508)
* Use markdown syntax for links [#501](https://github.com/noqdev/iambic/pull/501)

## 0.10.13 (July 18, 2023)

BUG FIXES:
* Fixed Google Groups paginated response [#500](https://github.com/noqdev/iambic/pull/500)

THANKS:
* `jonathan.silva` in community slack reporting the pagination issue on Google Workspace

## 0.10.12 (July 18, 2023)

BUG FIXES:
* Handle CUSTOMER type as Google Group member  [#499](https://github.com/noqdev/iambic/pull/499)

THANKS:
* `jonathan.silva` in community slack reporting the CUSTOMER type issue on Google Workspace

## 0.10.11 (July 17, 2023)

BUG FIXES:
* [#498](https://github.com/noqdev/iambic/pull/498)
* Fixed race condition on iambic detect not using templated resource id grouping resources.
* Fixed issue where a resource could show as excluded on a resource it was never evaluated on.

ENHANCEMENTS:
* Improved ordering of template attributes.
* `base_group_dict_attribute` is now more deterministic in its grouping.
* `iambic detect` performance optimizations.
  * Now only evaluates on the account a resource id change is detected on as opposed to all accounts.
  * Example if `engineering` is on all accounts and detect is ran for account a, only `engineering` on account a is evaluated.
* Removed remaining AWS provider references from core.

## 0.10.10 (July 14, 2023)

DOCS:
* Fix GoogleWorkspace docs [#496](https://github.com/noqdev/iambic/pull/496)
* Instruction to deploy GitHub integration on non-mgmt account [#494](https://github.com/noqdev/iambic/pull/494)

BUG FIXES:
* Validate google response data [#497](https://github.com/noqdev/iambic/pull/497)

ENHANCEMENTS:
* Add 'notes' core template attribute [#485](https://github.com/noqdev/iambic/pull/485)

THANKS:
* `jonathan.silva` in community slack reporting the Google Workspace setup issue.

## 0.10.7 (July 12, 2023)

BUG FIXES:
* Update Structlog and other dependencies [#495](https://github.com/noqdev/iambic/pull/495)

## 0.10.4 (July 6, 2023)

BUG FIXES:
* AWS - Fixing missing change details [#487](https://github.com/noqdev/iambic/pull/487)

THANKS:
* `mikegrima` for contributing AWS fix [#487](https://github.com/noqdev/iambic/pull/487)

## 0.10.3 (July 5, 2023)

BUG FIXES:
* Google Workspace - Fix SUSPENDED support in Google Workspace Groups [#483](https://github.com/noqdev/iambic/pull/483)
* AWS - Added Managed Policy ARN to ProposedChange [#484](https://github.com/noqdev/iambic/pull/484)

THANKS:
* `victorSouza-DevOPS` for contributing Google Workspace fix [#483](https://github.com/noqdev/iambic/pull/483)
* `mikegrima` for contributing AWS fix [#484](https://github.com/noqdev/iambic/pull/484)

## 0.10.1 (July 3, 2023)

DOCS:
* Docs for setting up iambic approve in GitHub integration [#467](https://github.com/noqdev/iambic/pull/467)
* Add FAQ to docs ; Add GHA readme [#479](https://github.com/noqdev/iambic/pull/479)

BUG FIXES:
* Fixed add single AWS account in setup flow. The bug was checking CloudFormation StackSets status when single AWS account setup does not use StackSets [#478](https://github.com/noqdev/iambic/pull/478)
* Updated `semver` to `7.5.2+` [#474](https://github.com/noqdev/iambic/pull/474)

ENHANCEMENTS:
* Adds support for AWS Import Rules. IAMbic will obey import rules to either ignore resources with certain attributes, or to flag them as import_only. [#469](https://github.com/noqdev/iambic/pull/469)
* Implement GitHub App interaction error protocol [#471](https://github.com/noqdev/iambic/pull/471)
* Allow `iambic apply` to be triggered by GitHub Apps [#470](https://github.com/noqdev/iambic/pull/470)

THANKS:
* `datfinesoul` to champion the user story for AWS Import Rules

## 0.9.8 (Jun 20, 2023)

ENHANCEMENTS:

* Explicit allow list GitHub bots interactions (iambic approve, iambic apply)  [#470](https://github.com/noqdev/iambic/pull/470)

## 0.9.6 (Jun 15, 2023)

BUG FIXES:

* Fixed IAMbic import errors when AWS Organization that has no permission sets in IdentityCenter [#459](https://github.com/noqdev/iambic/pull/459)
* Fixed broken links on README.md [#465](https://github.com/noqdev/iambic/pull/465)
* Fixed import issue when AWS policy document uses `Id` element [#464](https://github.com/noqdev/iambic/pull/464)

ENHANCEMENTS:

* Improve IAMbic wizard prompting when AWS Organization has not yet enabled trusted access for CloudFormation StackSets. [#459](https://github.com/noqdev/iambic/pull/459)
* Only configure structlog if it's not already configured. More friendly when `iambic-core` is used as a library [#462](https://github.com/noqdev/iambic/pull/462)

THANKS:
* `sidick` for reporting AWS Organization import issue when there is no permission sets in IdentityCenter [#460](https://github.com/noqdev/iambic/issues/460)
* `sidick` for reporting lack of prompts when AWS Organization has not yet enabled trusted organization access for Cloudformation StackSets. [#458](https://github.com/noqdev/iambic/issues/458)
* `sourcefrog` for contribution in fixing README [#461](https://github.com/noqdev/iambic/pull/461)
* `sidick` for reporting AWS Role import issue when `Id` element is used [#463](https://github.com/noqdev/iambic/issues/463)

## 0.9.1 (Jun 9, 2023)

BUG FIXES:
* Fixed [#419](https://github.com/noqdev/iambic/issues/419): Deleted file should not be removed again during Git workflow [#441](https://github.com/noqdev/iambic/pull/441)
* Fixed functional test [#451](https://github.com/noqdev/iambic/pull/451)
* Skip a key from new_model if old_model already mark it as metadata [#453](https://github.com/noqdev/iambic/pull/453)
* Do not override logging settings when used as library [#454](https://github.com/noqdev/iambic/pull/454)

ENHANCEMENTS:
* Bump `cryptography` from `39.0.1` to `41.0.1`  [#443](https://github.com/noqdev/iambic/pull/443)
* Skip wizard prompts if AWS SDK can verify settings [#444](https://github.com/noqdev/iambic/pull/444)
* Move module level templates symbol to config to allow ease of use of `iambic-core` as library [#440](https://github.com/noqdev/iambic/pull/440)
* Dependency Cleanup [#448](https://github.com/noqdev/iambic/pull/448)
* Included empty tags dict when decribing role without tags [#449](https://github.com/noqdev/iambic/pull/449)
* Implemented "iambic approve" for GitHub workflow [#452](https://github.com/noqdev/iambic/pull/452). It's now possible to have IAMbic GitHub integration to approve PR. The workflow allows another GitHub App to open a PR and mark the PR as `approved`. See the pull request for the full discussion on security considerations. It's secure by default, because without an actual configuration with a public/private key, the IAMbic GitHub integration's approve command will not work.

DOCS:
* Create 001-AWS-Managed-Resources-Attributes [#395](https://github.com/noqdev/iambic/pull/395). We recommend contributor to write up the design prior to creating a large pull request, so the community can give feedback prior to a significant change.
* Improve GitHub App creation docs to have most of the settings included in the query params [#402](https://github.com/noqdev/iambic/pull/402)


THANKS:
* `mxw-sec` for reporting issue [#419](https://github.com/noqdev/iambic/issues/419) regarding AWS IAM Delete File issue Github APP
* `mxw-sec` for discussing how to improve GitHub App creation using GitHub App Manifest
* `datfinesoul` for reporting issue [#405](https://github.com/noqdev/iambic/issues/405) regarding Automatically Detect Management Account for AWS Organizations to confirm an existing prompt.
* `mikegrima` for contributing [#448](https://github.com/noqdev/iambic/pull/448). This shrinks the install dependencies when using `iambic-core` as library.
* `mikegrima` for contributing [#449](https://github.com/noqdev/iambic/pull/449). This makes AWS role tags before/after value much easier to compare by handling boto3 quarks.

## 0.8.1 (May 30, 2023)

BUG FIXES:

* Explicitly setting `account_id` and `account_name` variables during AWS Account Setup Wizard [#430](https://github.com/noqdev/iambic/pull/430)
* Create iambic docker user before assigning file permissions [#435](https://github.com/noqdev/iambic/pull/435)
* Handled unbound changes variable on plan_git_changes [#434](https://github.com/noqdev/iambic/pull/434)
* Detect changes between policy documents [#436](https://github.com/noqdev/iambic/pull/436)
* More robust yaml comments interaction between templates and subsequent import [#437](https://github.com/noqdev/iambic/pull/437)

ENHANCEMENTS:

* AWS SCP (Service Control Policy) support. [#384](https://github.com/noqdev/iambic/pull/384)
* Development experience changes on removing pytest.ini for ease for run-and-debug [#428](https://github.com/noqdev/iambic/pull/428)
* Docs for AWS Change Detection [#429](https://github.com/noqdev/iambic/pull/429)
* Docs for IAMbic gist repo usage [#432](https://github.com/noqdev/iambic/pull/432)
* SCP Quickstart Docs [#433](https://github.com/noqdev/iambic/pull/433)

## 0.7.18 (May 24th, 2023)

BUG FIXES:

* Fix merge model int handling (impact subsequent importing) [#410](https://github.com/noqdev/iambic/pull/410)
* Fixed wizard prompt when editing an AWS account. [#415](https://github.com/noqdev/iambic/pull/415)
* Fix missing tags on IambicSpokeRole in the management account [#416](https://github.com/noqdev/iambic/pull/416)
* Fix change detection setup for isolated runs [#417](https://github.com/noqdev/iambic/pull/417)
* Ignore extra fields provided by Azure AD [#424](https://github.com/noqdev/iambic/pull/425)
* Upgrade requests from 2.30.0 to 2.31.0 [#425](https://github.com/noqdev/iambic/pull/425)
* Move IAMbic default docker image to ship with Python 3.10.8 instead of 3.11.1 Setup Wizard [#427](https://github.com/noqdev/iambic/pull/427)

ENHANCEMENTS:

* Development experience changes on customizing hub and spoke role  [#422](https://github.com/noqdev/iambic/pull/422)
* Docs referencing IAMOps flow [#420](https://github.com/noqdev/iambic/pull/420)
* Development experience changes on requiring greater than 75% coverage [#422](https://github.com/noqdev/iambic/pull/422)

THANKS:

* `datfinesoul` for reporting missing tags on IambicSpokeRole creation in management account [#406](https://github.com/noqdev/iambic/pull/406)
* `datfinesoul` for reporting AWS change detection setup issue [#407](https://github.com/noqdev/iambic/pull/407)
* `mxw-sec` for reviewing [#420](https://github.com/noqdev/iambic/pull/420)
* `sprkyco` for reporting directory extension Azure AD issue [#423](https://github.com/noqdev/iambic/pull/423)

## 0.7.6 (May 15th, 2023)

BUG FIXES:

* Handling merge models when the new value is an int
* Flatten multiline comment when they are not attached to a YAML dict key

ENHANCEMENTS:
* Added an `iambic convert` command to convert an AWS policy to the IAMbic formatted yaml
* Default relative directory leverages `path` information from IAM resources. [#400](https://github.com/noqdev/iambic/pull/400)

THANKS:

* `Shreyas D` for reporting the merge model issue
* `Phil H, Michael W` for suggesting the `iambic convert` command

## 0.7.3 (May 10th, 2023)

BUG FIXES:

* AWS plugin now supports legacy policy document schema. (This is an undocumented
schema in which statement can be a single statement not wrapped inside an array.
New policy editor will always use the array syntax; however, there are old policies
that have the legacy syntax. IAMbic should handle it gracefully without crashing.)

THANKS:

* `Shreyas D` reported the issue [#397](https://github.com/noqdev/iambic/pull/397)


## 0.7.1 (May 9th, 2023)

ENHANCEMENTS:

* Tag support on CloudFormation stack. These tags will propagate to IambicHubRole and
IambicSpokeRole created. Wizard will prompt the user to either enter blank or
in `key1=value1` format. To add multiple tags, use `key1=value1, key2=value2` format.

BUG FIXES:

* Fixes in wizard when user does not grant Iambic write access.
* Fixes in wizard when setting up an individual AWS account instead of AWS Organization.

THANKS:

* `Phil H.`, `David B.` in [NoqCommunity](https://noqcommunity.slack.com/archives/C02P9E8BDK6/p1683275443604049) proposing tags support during IAMbic setup.

## 0.6.1 (May 3rd, 2023)

ENHANCEMENTS:

* Additional clarity in the wizard as it relates to AWS cloudformation changes.
* Added the ability to check the IAMbic version from the CLI.

BUG FIXES:

* AWS read only spoke role is now working as designed
* Fixes to text being truncated in the wizard on smaller terminal windows.

THANKS:

* [rjulian](https://github.com/rjulian) for reporting [#377](https://github.com/noqdev/iambic/pull/377).

## 0.5.1 (May 2nd, 2023)

PERMISSION CHANGES:

* IambicHubRole now uses a region agnostic resource definition in the SQS `IAMbicChangeDetectionQueue` permission (CloudFormation Template)

ENHANCEMENTS:

* The AWS region IAMbic uses is now configurable in the wizard.
* Added region awareness to cloud formation util functions.

BREAKING CHANGES:

* The `AwsIdentityCenterPermissionSetTemplate` schema has changed. In particular, `permissions_boundary.policy_arn` has become `permissions_boundary.managed_policy_arn`. This is due to the PermissionSet API distinguishing attached
permissions_boundary either owned by AWS or owned by Customer. To align with AWS API response, we have decided
to follow the AWS naming convention. The old name `permissions_boundary.policy_arn` never quite worked correctly
in `AwsIdentityCenterPermissionSetTemplate`. We decide to go through with the breaking change route.

BUG FIXES:

* Fixed import of `AwsIdentityCenterPermissionSetTemplate` in which permission boundary is set to `managed_policy_arn`

THANKS:

* [perpil](https://github.com/perpil) for reporting [#372](https://github.com/noqdev/iambic/issues/372).

## 0.4.1 (May 1st, 2023)

PERMISSION CHANGES:
* IambicHubRole added SQS read/write access to queue named `IAMbicChangeDetectionQueue` to support IAM resource detection. [#355](https://github.com/noqdev/iambic/pull/355)
* IambicHubRole added sts:SetSourceIdentity to `IambicSpokeRole` to be compatible with Idp that enforce SetSourceIdentityForwarding [#361](https://github.com/noqdev/iambic/pull/361)

ENHANCEMENTS:
* Be compatible with Idp that enforces sts:SetSourceIdentity [reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html) [#361](https://github.com/noqdev/iambic/pull/361)

BUG FIXES:
* IAM resource detect mechanism cannot remove SQS message that is already been processed in `IAMbicChangeDetectionQueue` [#355](https://github.com/noqdev/iambic/pull/355)
* If environment variables contains AWS credentials, IAMbic wizard shall not ask what profile to write into configuration file. [#358](https://github.com/noqdev/iambic/pull/358)

THANKS:
* [perpil](https://github.com/perpil) for [#359](https://github.com/noqdev/iambic/pull/359) and multiple doc suggestions. [#363](https://github.com/noqdev/iambic/pull/363), and [#365](https://github.com/noqdev/iambic/pull/365)

## 0.3.0 (April 21, 2023)

BREAKING CHANGES:
* AWS templates containing account_id or account_name will need to be updated from `{{ account_id }}` to `{{ var.account_id }}` and from `{{ account_name }}` to `{{ var.account_name }}`. Alternatively, you can remove the files and re-import them.

You can use your favorite editor for find and replace, or give the following bash two-liner a try.

```bash
find . -type f -name "*.yaml" -print0 | xargs -0 sed -i '' -e 's/{{account_id}}/{{var.account_id}}/g'
find . -type f -name "*.yaml" -print0 | xargs -0 sed -i '' -e 's/{{account_name}}/{{var.account_name}}/g'
```

ENHANCEMENTS:
* Removed AWS package imports from core
* Standardized variable naming in templates
* Improved exception handling in the AWS package
* Cleaned up additional import only checks on AWS IAM role, user, and group models.

BUG FIXES:
* Resolved type error on merge template when new value is None.



## 0.2.0 (April 17, 2023)

Initial plan is to do a every 2-week release cycle.

ENHANCEMENTS:
* Improve memory footprint in templates reading
* Minimize I/O in templates reading
