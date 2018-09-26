---
title: VRC.Mobile.Android.2
---

The application must be signed with your unique digital certificate. All subsequent versions of your app must also be signed with the same certificate. 

**Required** - Yes

## Additional Details

See the [Application Signing](/distribute/latest/concepts/publish-mobile-app-signing/) page for more information.

## Steps to Test

This is checked immediately after you upload each build, and the upload will fail if the test fails.

1. Ensure you have the Android SDK installed.
2. Open a command prompt and type "apksigner verify app.apk".


## Expected Result

Command runs without error or other output.

Note that it isn't possible to verify that you've used the same signature until you upload a subsequent build, in which case the upload will fail.
