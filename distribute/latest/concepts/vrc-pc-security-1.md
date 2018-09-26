---
title: VRC.PC.Security.1
---

The app must perform an Oculus Platform entitlement check within 10 seconds of launch.

**Required** - Yes

## Additional Details

See the [Platform SDK Getting Started Guide](/documentation/platform/latest/concepts/book-pgsg/) for information about how to implement the Entitlement Check.

## Steps to Test

1. Run the [VRC Validator](https://developer.oculus.com/documentation/pcsdk/latest/concepts/dg-vrcvalidator/) with the TestEntitlementCheck argument.


Optional, manual tests.

1. Sign in with a valid Oculus ID.
2. Download copy of app.
3. Log out and sign in with a new Oculus ID.
4. Navigate to the folder and try to launch the app.


## Expected Result

The VRC Validator will report "INFO: Test PASSED".

If testing manually, the title should either exit, display an error message, or enter a limited demo mode.
