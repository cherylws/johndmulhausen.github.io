---
title: VRC.Mobile.Security.1
---

The app must perform an Oculus Platform entitlement check within 10 seconds of launch and exit the app if the check fails.

**Required** - Yes

## Additional Details

See the Platform SDK [Getting Started Guide](/documentation/platform/latest/concepts/book-pgsg/) for information about implementing the Entitlement Check.

## Steps to Test

1. On your device, ensure developer mode is enabled and log in to Oculus Home with a user who doesn't have an entitlement to the app (either via release channel, keys, or store purchase).
2. In a terminal window, install the app with the command "adb install path-to-apk".
3. Launch the app from the Oculus Home library.


## Expected Result

App should either exit, display an error message, or go into a limited functionality mode.
