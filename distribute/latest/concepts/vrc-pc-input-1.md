---
title: VRC.PC.Input.1
---
The app must not submit frames or accept input when the user removes the HMD or opens the Universal Menu.

**Required** - Yes

## Additional Details

No additional details for this VRC.

## Steps to Test

1. Run the [VRC Validator](/documentation/pcsdk/latest/concepts/dg-vrcvalidator/) with the TestSubmitFramesWhenNotVisible argument.
Optional, manual test.

1. Launch the title.
2. Press the Oculus Home Button.
3. Observe: This should launch Oculus Home and bring up the Universal Menu.
## Expected Result

Performance shouldn't drop, and moving the controllers shouldn't cause interaction within the app.

