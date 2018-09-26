---
title: VRC.PC.SDK.3
---

Unity apps must be built with a supported version.

**Required** - Yes

## Additional Details

Some versions of Unity are not compatible with Oculus or VR development. You must ensure you are building your app using a supported version of Unity. Supported versions can be found on the [Unity Compatibility and Version Requirements](/documentation/unity/latest/concepts/unity-req/) page. 

## Steps to Test

Run the [VRC Validator](/documentation/pcsdk/latest/concepts/dg-vrcvalidator/) with the `TestSdkVersion` argument.

This is also checked immediately after you upload each build, and the upload will fail if the test fails.

## Expected Result

The VRC Validator will report "INFO: Test PASSED".
