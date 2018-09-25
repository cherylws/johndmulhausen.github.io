---
title: VRC.PC.Performance.1
---
App should display graphics and respond to head tracking within 4 seconds of launch.

**Required** - Yes

## Additional Details

If your app takes longer than 4 seconds to launch, you must provide a head-tracked loading indicator. Head-tracked means the UI elements must remain stationary in space when the user turns their head. Do not lock any logos or progress indicators to the userâ€™s face.

## Steps to Test

1. Run the [VRC Validator](/documentation/pcsdk/latest/concepts/dg-vrcvalidator/) with the TestLaunchIntoVR argument.
Optional, manual tests.

1. Launch the title.
2. Count the number of seconds it takes to display something and respond to head tracking.
## Expected Result

App begins accepting input, responds to head tracking, and displays graphics within 4 seconds of app startup. 

