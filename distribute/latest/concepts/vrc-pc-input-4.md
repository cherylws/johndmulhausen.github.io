---
title: VRC.PC.Input.4
---

Selecting Exit to Oculus Home from the Universal Menu must exit to Oculus Home.

**Required** - Yes

## Additional Details

No additional details for this VRC.

## Steps to Test

1. Run the [VRC Validator](https://developer.oculus.com/documentation/pcsdk/latest/concepts/dg-vrcvalidator/) with the TestAppShouldQuit argument.


Optional, manual tests.

1. Launch the title.
2. Press the Oculus Home Button.
3. Observe: This should launch Oculus Home and bring up the Universal Menu.
4. Select "Exit to Home".
5. Observe: Warning says that game will exit.


## Expected Result

App successfully exits to Oculus Home.
