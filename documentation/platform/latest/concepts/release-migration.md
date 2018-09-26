---
title: Migrating from a Previous Version
---



## Migrating to Platform SDK 1.10+ 

If you're migrating to a recent version (v1.10+) from a previous SDK version (v1.9 or earlier). 

**Native Gear VR only** - After downloading the latest Platform SDK version, you'll need delete all `svcloader.jar`, `libovrplatform.so`, and `svcjar.jar` files manually.

**If You're Currently Using Version 1.0 or 1.1**

If you're currently using version 1.0 or 1.1, find and replace the following variables in the `ovrMatchmakingCriterion` class:

* Remove System.LoadLibrary() calls from your app.
* Change paramterArrayCount to parameterArrayCount.
* Change paramterArray to parameterArray.


For complete information about each release, please see the [Current Platform SDK Version Release Notes](/documentation/platform/latest/concepts/release-changes/).
