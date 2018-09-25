---
title: VRC.PC.Input.3
---
Selecting Reset View in the Universal Menu must reset the userâ€™s position and orientation.

**Required** - Yes

## Additional Details

No additional details for this VRC.

## Steps to Test

1. Run the [VRC Validator](/documentation/pcsdk/latest/concepts/dg-vrcvalidator/) with the TestResponseToRecenterRequest argument.
Optional, manual tests.

1. Launch the title.
2. Press the Oculus Home Button.
3. Observe: This should launch Oculus Home and bring up the Universal Menu.
4. Reorient through the Universal Menu.
5. Return to game and observe that reorientation has been accounted for.
## Expected Result

1. Apps that do not use the Oculus Guardian System play area should reset the user's home position and orientation to their current position and orientation, using the built-in Oculus API functionality.
2. Apps that use the Oculus Guardian System play area may use more advanced reorientation logic.
3. If Oculus Guardian System bounds are not configured, re-center must work regardless of app tracking or movement type.
