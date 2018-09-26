---
title: VRC.PC.SDK.4
---

Unreal Engine apps must be built with a supported distribution.

**Required** - Yes

## Additional Details

Some versions of Unreal Engine are not compatible with Oculus or VR development. You must ensure you are building your app using a supported distribution of Unreal Engine. 

Supported distributions can be found on the [Unreal Engine](/documentation/unreal/latest/concepts/unreal-engine/) page. 

## Steps to Test

Run the [VRC Validator](/documentation/pcsdk/latest/concepts/dg-vrcvalidator/) with the `TestSdkVersion` argument.

This is also checked immediately after you upload each build, and the upload will fail if the test fails.

## Expected Result

The VRC Validator will report "INFO: Test PASSED".
