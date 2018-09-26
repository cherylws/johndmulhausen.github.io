---
title: 1.6 Oculus Utilities for Unity 5 Release Notes
---



## Oculus Utilities for Unity 5 version 1.6.0

This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Utilities for Unity 5. For information on first-party changes to Unity VR support for Oculus, see the Unity Release Notes for the appropriate version. You will find an updated scripting reference for the included C# scripts in our [Unity Developer Reference](/documentation/game-engines/latest/concepts/book-unity-reference/).

## New Features

* Added Adaptive Resolution to OVRManager, which automatically scales down app resolution when GPU utilization exceeds 85%. See “OVRManager” in [Unity Components](/documentation/unity/latest/concepts/unity-utilities-overview/#unity-utilities-overview "This section provides an overview of the Utilities package, including its directory structure, the supplied prefabs, and several key C# scripts.") for details. (Rift only, requires Unity v 5.4 or later)
* OVR Screenshot Wizard size parameter is now freeform instead of dropdown selection for greater flexibility.
* Added recommended anti-aliasing level to help applications choose the right balance between performance and quality.
* Added support for more than one simultaneous OVROverlay. Now apps can show up to 3 overlay quads on Gear VR and 15 on Rift.


## API Changes

* Added OVRHaptics.cs and OVRHapticsClip.cs to programmatically control haptics for Oculus Touch controller. See [OVRHaptics for Oculus Touch](/documentation/unity/latest/concepts/unity-ovrhaptics/ "This guide reviews OVRHaptics and OVRHapticsClip, two C# scripts that programmatically control haptics feedback for Touch.") for more information.
* Added public members Enable Adaptive Resolution, Max Render Scale, and Min Render Scale to OVRManager.
* Added OVRManager.useRecommendedMSAALevel to enable auto-selection of anti-aliasing level based on device performance.
* Added OVRManager.useIPDInPositionTracking to allow apps to separately disable head position tracking (see OVRManager.usePositionTracking) and stereopsis.


## Bug Fixes

* Fixed bug preventing power save from activating on Gear VR.
* Fixed counter-intuitive behavior where disabling OVRManager.usePositionTracking prevented proper eye separation by freezing the eye camera positions at their original offset.


## Known Issues

* Gear VR
	+ Unity 5 automatically generates manifest files with Android builds that will cause them to be automatically rejected by the Oculus Store submission portal. If this is blocking your application submission, please let us know on our [Developer Forum](https://forums.oculus.com/developer/) and we will work with you on a temporary workaround.
	+ Gear VR developers using Unity 5.3.4 or later, or using Unity 5.4.0b16 and later: Do not set DSP Buffer Size to Best in Audio Manager in the Inspector for now or you will encounter audio distortion. Set it to Good or Default instead.
	

