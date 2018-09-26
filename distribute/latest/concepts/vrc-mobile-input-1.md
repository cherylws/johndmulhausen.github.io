---
title: VRC.Mobile.Input.1
---

If the app cannot be used without an external input device (e.g. gamepad or 3DOF controller), and no input device is detected when the app starts up, the app must warn the user to connect the necessary device.

**Required** - Yes

## Additional Details

The Oculus Go controller notification is handled by the system and doesn't require a specific app-level message.

## Steps to Test

1. Disconnect the controller.
2. Launch the title.


## Expected Result

An error message is displayed saying that the app requires a controller.
