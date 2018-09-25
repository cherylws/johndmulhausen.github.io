---
title: VRC.Mobile.Security.2
---
The app must request the minimum number of permissions required to function.

**Required** - Yes

## Additional Details

The review team will be paying close attention to the list of permissions that Google considers "dangerous," which includes camera, location, microphone, reading and writing external storage, and others. A list of which permissions are considered dangerous can be found in Android's [Permissions Overview](https://developer.android.com/guide/topics/permissions/overview.html#normal-dangerous) guide. 

## Steps to Test

1. Look at permissions requested in the android manifest. From a command line, you can also run "aapt dump badging" and search the output for "uses-permission."
2. Verify that all permissions are utilized by the application.
## Expected Result

There must be a rationale behind every permission your app requests in the app manifest.

