---
title: 1.5 Oculus Utilities for Unity 5 Release Notes
---



## Oculus Utilities for Unity 5 version 1.5.0

This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Utilities for Unity 5. For information on first-party changes to Unity VR support for Oculus, see the Unity Release Notes for the appropriate version. You will find an updated scripting reference for the included C# scripts in our [Unity Developer Reference](/documentation/game-engines/latest/concepts/book-unity-reference/).

## New Features

* Added OVR Screenshot and OVR Capture Probe tools, which exports a 360 screenshot of game scenes in cube map format. See [Cubemap Screenshots](/documentation/unity/latest/concepts/unity-cubemap/ "The OVR Screenshot Wizard allows you to easily export a 360 screenshot in cubemap format.") for more information.
* Switched to built-in volume indicator on mobile.
* Exposed OVRManager.vsyncCount to allow half or third-frame rate rendering on mobile.
* Added bool OVRManager.instance.isPowerSavingActive (Gear VR).


## Bug Fixes

* Repeatedly changing resolution or MSAA level no longer causes slowdown or crashing.
* Fixed scale of OVRManager.batteryLevel and OVRManager.batteryTemperature.
* Fixed race condition leading to black screens on Rift in some CPU-heavy cases.
* Fixed memory bloat due to unpooled buffers when using MSAA.


## Known Issues

* **Gear VR developers** using Unity 5.3.4 or later, or using Unity 5.4.0b16 and later: Do not set **DSP Buffer Size** to **Best** in **Audio Manager** in the Inspector for now or you will encounter audio distortion. Set it to **Good** or **Default** instead.

