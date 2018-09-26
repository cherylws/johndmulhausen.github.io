---
title: 1.7 Oculus Utilities for Unity 5 Release Notes
---



## Oculus Utilities for Unity 5 version 1.7.0

This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Utilities for Unity 5. For information on first-party changes to Unity VR support for Oculus, see the Unity Release Notes for the appropriate version. You will find an updated scripting reference for the included C# scripts in our [Unity Developer Reference](/documentation/game-engines/latest/concepts/book-unity-reference/).

If you have previously imported a Unity integration package, you must delete all Oculus Integration content before importing the new Unity package. For more information, see [Importing the Oculus Utilities Package](/documentation/unity/latest/concepts/unity-import/).

## New Features

* Updated OVROverlay.cs to support cubemap (skybox) and hemicylinder overlay shapes (mobile only) in addition to the existing quadrilateral Game Object shape.
* Added OVRRTOverlayConnector to stream Render Texture contents to an OVROverlay. For more information, see [VR Compositor Layers](/documentation/unity/latest/concepts/unity-ovroverlay/ "OVROverlay is a script in OVR/Scripts that allows you to render Game Objects as VR Compositor Layers instead of drawing them to the eye buffer.").
* Added runtime support for Adaptive Resolution (see description in [OVRManager](/documentation/unity/latest/concepts/unity-utilities-overview/#unity-components "This section gives a general overview of the Components provided by the Utilities package.")).


## API Changes

* Unity versions prior to 5.3.4p5 (or 5.3.3p3 + OVRPlugin 1.3) are no longer supported.
* OVRInput.SetControllerVibration may no longer address a pair of Touch controllers with OVRinput.Controller.Touch; you must address each controller individually using OVRinput.Controller.LTouch or OVRinput.Controller.RTouch.
* Removed OVRDebugGraph.cs from Assets/OVR/Scripts/.


## Bug Fixes

* Fixed backwards head-neck model z translation on Gear VR.
* When targeting Oculus Touch, OVRInput.SetControllerVibration calls are now limited to 30 per second due to performance issues; additional calls are discarded. (Note: we recommend using OVRHaptics to control Touch vibrations - it provides better haptics quality without the performance issues of OVRInput.SetControllerVibration().
* Fixed crash in CreateDirect3D11SurfaceFromDXGISurface after eye buffer re-allocation on Rift.
* Fixed OVRInput Xbox controller detection with Unity on Windows 10 Anniversary Edition.
* Fixed delay when loading with “Run in Background” enabled.
* Fixed missing runtime support for adaptive viewport scaling.


## Known Issues

* Gear VR
	+ Mobile developers should not use Unity versions 5.3.6p1-2 and 5.4.0p1-2 due to incorrect positional movement of the head.
	+ Unity 5 automatically generates manifest files with Android builds that will cause them to be automatically rejected by the Oculus Store submission portal. If this is blocking your application submission, please let us know on our [Developer Forum](https://forums.oculus.com/developer/) and we will work with you on a temporary workaround.
	+ Gear VR developers using Unity 5.3.4 or later, or using Unity 5.4.0b16 and later: Do not set DSP Buffer Size to Best in Audio Manager in the Inspector for now or you will encounter audio distortion. Set it to Good or Default instead.
	

