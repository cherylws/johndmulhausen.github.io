---
title: 1.8 Oculus Utilities for Unity 5 Release Notes
---
## Oculus Utilities for Unity 5 version 1.8.0

This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Utilities for Unity 5. For information on first-party changes to Unity VR support for Oculus, see the Unity Release Notes for the appropriate version. You will find an updated scripting reference for the included C# scripts in our [Unity Developer Reference](/documentation/game-engines/latest/concepts/book-unity-reference/).

If you have previously imported a Unity integration package, you must delete all Oculus Integration content before importing the new Unity package. For more information, see [Importing the Oculus Utilities Package](/documentation/unity/latest/concepts/unity-import/ "Oculus Utilities for Unity is an optional Unity Package that includes scripts, prefabs, and other resources to assist with development.").

Mobile SDK Examples has been deprecated; use the [Unity Sample Framework](/documentation/unity/latest/concepts/unity-sample-framework/ "The Oculus Unity Sample Framework provides sample scenes and guidelines for common VR-specific features such as hand presence with Oculus Touch, crosshairs, driving, hybrid mono rendering, and video rendering to a 2D textured quad.") instead.

Note: Due to issues with earlier releases, we now recommend all developers update to 5.3.6p5 or version 5.4.1p1 or later.## New Features

* Added support for the Oculus Guardian System, which visualizes the bounds of a user-defined Play Area. Note that it is currently unsupported by public versions of the Oculus runtime. See [OVRBoundary Guardian System API](/documentation/unity/latest/concepts/unity-ovrboundary/ "OVRBoundary exposes an API for interacting with the Rift Guardian System for Touch.") for more information.
* Added underlay support allowing VR compositor layers to be rendered behind the eye buffer.
* Added support for stereoscopic cubemap VR compositor layers (mobile only). 
## API Changes

* Added OVRBoundary API for interacting with the Oculus Guardian System.
* Removed OVRTrackerBounds.
## Bug Fixes

* Fixed black screen issue related to unplugging the HDMI cable and re-plugging it back in.
* Fixed Touch judder issue. 
## Known Issues

* Due to issues with earlier releases, we now recommend all developers update to 5.3.6p5 or version 5.4.1p1 or later. 5.3.6p3-5.3.6p4 are also known to work.
* Gear VR
	+ Mobile developers should not use Unity versions 5.3.6p1-2 and 5.4.0p1-2 due to incorrect positional movement of the head.
	+ Unity 5 automatically generates manifest files with Android builds that will cause them to be automatically rejected by the Oculus Store submission portal. If this is blocking your application submission, please let us know on our [Developer Forum](https://forums.oculus.com/developer/) and we will work with you on a temporary workaround.
	+ Gear VR developers using Unity 5.3.4 or later, or using Unity 5.4.0b16 and later: Do not set DSP Buffer Size to Best in Audio Manager in the Inspector for now or you will encounter audio distortion. Set it to Good or Default instead.
	
