---
title: 1.11 Oculus Utilities for Unity 5 Release Notes
---



## Oculus Utilities for Unity 5 version 1.11.0

This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Utilities for Unity 5. For information on first-party changes to Unity VR support for Oculus, see the Unity Release Notes for the appropriate version. You will find a scripting reference for the included C# scripts in our [Unity Reference Content](/documentation/unity/latest/concepts/book-unity-reference/).

If you have previously imported a Unity integration package, you must delete all Oculus Integration content before importing the new Unity package. For more information, see [Importing the Oculus Utilities Package](/documentation/unity/latest/concepts/unity-import/).

## Unity 5.3 and 5.6 Support

Unity 5.3 support is deprecated and not all features are guaranteed to work. Please update to 5.4 or 5.5. We do not currently support preview versions of 5.6.

## New Features

* Added Performance Auditing Tool for Rift and mobile development. This tool verifies that your VR project configuration and settings are consistent with our recommendations. For more information, see [Performance Auditing Tool (OVRLint)](/documentation/unity/latest/concepts/unity-perf/#unity-perf-auditing "The performance auditing tool may be used to verify that your Rift or mobile VR project configuration and settings are consistent with our recommendations.").
* Added OVRGrabber and OVRGrabbable scripts for Oculus Touch to the Room sample in Assets/Scenes/. For details, see our [Unity Reference Content](/documentation/unity/latest/concepts/book-unity-reference/).
* (Mobile only) Added off-center cubemap support to OVROverlay, allowing you to display an overlay as a cubemap with a texture coordinate offset to increase resolution for areas of interest. For more information, see OVROverlay in our [Unity Reference Content](/documentation/unity/latest/concepts/book-unity-reference/).


## API Changes

* Deprecated OVRProfile.


## Bug Fixes

* Fixed bug affecting reserved interaction handling for the Universal Menu that caused all mobile applications using Utilities 1.9 and 1.10 to fail Oculus Store submission.


## Known Issues

* Adaptive Resolution is not currently working and should be disabled. If applications using Adaptive Resolution reach 45 Hz, they will remain stuck at that frame rate until relaunched. A fix is planned for the Rift 1.12 runtime release and should not require any application changes.
* The following versions of Unity require the [Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/en-us/download/details.aspx?id=48145) or Rift builds will fail to run in VR, and the error “Security error. This plugin is invalid!” will be reported in output\_log.txt:
	+ 5.3.6p3-5.3.6p7
	+ 5.4.0f1-5.4.2p1
	+ 5.5.0b1-5.5.0b8
	
* Rift
	+ All Unity versions prior to 5.4.3p3 leak 5MB/s if you have a Canvas in your scene, enable **Run In Background**, and dismount the Rift. You can check OVRManager.hasVrFocus in an Update function to disable your Canvases while the HMD is dismounted.
	
* Gear VR
	+ Due to a Unity bug, the Camera pose can be corrupted by scripts in the first frame after being enabled with VR support. As a workaround, use Utilities 1.11 or zero out the eye anchor poses when a new OVRCameraRig is spawned and the first frame after usePerEyeAnchors changes.
	+ With Unity 5.3, the world may appear tilted. As a workaround, use Utilities 1.10 or disable the virtual reality splash image.
	+ All mobile applications using Utilities 1.9 and 1.10 will fail Oculus Store submission due to a bug affecting reserved interaction handling for the Universal Menu. Please remove previously-imported project files as described in [Importing the Oculus Utilities Package](/documentation/unity/latest/concepts/unity-import/ "Oculus Utilities for Unity is an optional Unity Package that includes scripts, prefabs, and other resources to assist with development.") and import Utilities version 1.11, and update your Unity editor to a [compatible version](/documentation/unity/latest/concepts/unity-req/ "This guide describes Unity Editor version recommendations and system requirements.") if necessary. 
	+ Mobile developers should not use Unity versions 5.3.6p1-2 and 5.4.0p1-2 due to incorrect positional movement of the head.
	+ Unity 5.3.4-5.3.6p3 and Unity 5.4.0b16-Unity 5.4.0p3: Do not set **DSP Buffer Size** to **Best** in Audio Manager in the Inspector for now or you will encounter audio distortion. Set it to **Good** or **Default** instead.
	

