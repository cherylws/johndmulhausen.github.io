---
title: Audio SDK 1.24 Release Notes
---
This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Audio SDK.

## 1.24.0

## New Features

* **Spatializer plugin sizes reduced by half**: A technique known as half floats was applied to the Unity, Wwise, and FMOD spatializer plugins. This reduced the code size of those plugins by half.
## Big Fixes

* In the Unity Spatializer plugin, rotation for ambisonic sounds was incorrectly handled so that when the listener turned their head to the right or left, the ambisonic sound field rotated with the listener. This has been fixed so that the ambisonic sound field is rotated in the opposite direction from the headset rotation. This makes it sound as if it is fixed in place, which is the proper effect.
* There was a typo in the Unity Spatializer plugin, where \_AssignRaycastCallback was typed in as AssignRayCastCallback. This caused the function not to work properly, which broke the Dynamic Room Modeling feature in the Unity Spatializer plugin. This has been corrected.
## API Changes

* There are no breaking API changes in this release.
