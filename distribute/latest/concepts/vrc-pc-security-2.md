---
title: VRC.PC.Security.2
---
The app must not contain extraneous files such as marketing assets, copies of the Oculus SDK, or libraries for other VR APIs and distribution platforms.

**Required** - Yes

## Additional Details

No additional details for this VRC.

## Steps to Test

1. Run the [VRC Validator](/documentation/pcsdk/latest/concepts/dg-vrcvalidator/) with the CheckForExtraneousFiles and TestOculusDLLIncludes arguments.
2. Navigate to the installed app folder and check for other unnecessary files.
## Expected Result

The VRC Validator will report "INFO: Test PASSED".

Extraneous files are not included in the installation folder.

