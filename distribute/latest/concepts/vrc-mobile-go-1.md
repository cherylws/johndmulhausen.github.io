---
title: VRC.Mobile.Go.1
---

Apps for Oculus Go must not require Android features that aren't supported on Go.

**Required** - Yes, Go only

## Additional Details

Apps can't require Google Mobile Services, camera access, HMD touchpad, etc. See the [Mobile SDK Getting Started](/documentation/mobilesdk/latest/concepts/book-intro/) guide for information about Go development.

## Steps to Test

This is checked immediately after you upload each build, and the results will display within minutes on http://dashboard.oculus.com under Manage Build &gt; Specs.

## Expected Result

Test passes without error and you are able to select the Oculus Go checkbox.
