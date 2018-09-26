---
title: 1.9 Oculus Utilities for Unity 5 Release Notes
---



## Oculus Utilities for Unity 5 version 1.9.0

This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Utilities for Unity 5. For information on first-party changes to Unity VR support for Oculus, see the Unity Release Notes for the appropriate version. You will find a scripting reference for the included C# scripts in our [Unity Developer Reference](/documentation/game-engines/latest/concepts/book-unity-reference/).

If you have previously imported a Unity integration package, you must delete all Oculus Integration content before importing the new Unity package. For more information, see [Importing the Oculus Utilities Package](/documentation/unity/latest/concepts/unity-import/).

This release adds Gear VR touchpad and back button support to OVRInput.

Be sure to check out the new Mono Optimization sample included in [Unity Sample Framework](/documentation/unity/latest/concepts/unity-sample-framework/) v1.5.1. Monoscopically rendering distant content in a scene can offer significant rendering performance improvements.

## New Features

* Added Gear VR Touchpad and back button support to OVRInput.
* OVRInput.Controller.Active now automatically switches away from Touch if the user is not holding it.
* OVRBoundary now supports more than 256 Guardian System bounds points.
* Improved image quality for higher values in VRSettings.renderScale due to mipmapping. (Rift)


## API Changes

* OVRInput.Button and OVRInput.RawButton events now report Gear VR touchpad swipes and back button presses.


## Bug Fixes

* Unity 5.3.6p8, 5.4.2p2, and 5.5.0b9 correct a failure to report shoulder button events in OVRInput when used with Utilities 1.9.0.
* Fixed dependency on the Visual C++ Redistributable for Visual Studio 2015 causing Rift builds to fail to run in VR in some versions of Unity (see Known Issues for more information).
* Fixed 5MB/s memory leak when using OVROverlay.


## Known Issues

* OVRInput fails to report shoulder button events when Utilities 1.9.0 is used with Unity versions 5.4.2p1 and 5.5.0b8 or earlier.
* The following versions of Unity require the [Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/en-us/download/details.aspx?id=48145) or Rift builds will fail to run in VR, and the error “Security error. This plugin is invalid!” will be reported in output\_log.txt:
	+ 5.3.6p3-5.3.6p7
	+ 5.4.0f1-5.4.2p1
	+ 5.5.0b1-5.5.0b8
	
* Rift
	+ All Unity versions leak 5MB/s if you have a Canvas in your scene, enable Run In Background, and dismount the Rift. You can check OVRManager.hasVrFocus in an Update function to disable your Canvases while the HMD is dismounted.
	
* Gear VR
	+ Mobile developers should not use Unity versions 5.3.6p1-2 and 5.4.0p1-2 due to incorrect positional movement of the head.
	+ Unity 5 automatically generates manifest files with Android builds that will cause them to be automatically rejected by the Oculus Store submission portal. If this is blocking your application submission, please let us know on our [Developer forum](https://forums.oculus.com/developer) and we will work with you on a temporary workaround.
	+ Unity 5.3.4-5.3.6p3 and Unity 5.4.0b16-Unity 5.4.0p3: Do not set DSP Buffer Size to Best in Audio Manager in the Inspector for now or you will encounter audio distortion. Set it to Good or Default instead.
	

