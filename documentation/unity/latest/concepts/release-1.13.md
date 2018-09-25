---
title: 1.13 Oculus Utilities for Unity 5 Release Notes
---
## Oculus Utilities for Unity 5 version 1.13.0

This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Utilities for Unity 5. For information on first-party changes to Unity VR support for Oculus, see the Unity Release Notes for the appropriate version. You will find a scripting reference for the included C# scripts in our [Unity Reference Content](/documentation/unity/latest/concepts/book-unity-reference/).

Unity 5.6.0f3 is the only supported version of 5.6 at this time. Earlier versions of 5.6.0 are not supported, and 5.6.0p1 has a crashing bug affecting Gear VR applications.

## New Features

* Added android:installLocation="auto" to store-compatible AndroidManifest.xml.
## Bug Fixes

* Fixed double-counting of orientation when recentering OVRPlayerController.
* Fixed NullReferenceExceptions on edit-and-continue.
* Fixed signature checking on non-English platforms.
* Fixed white flash.
* Fixed incorrect overlay states for ATW splash.
* Fixed VRAPI crash: "Invalid parms passed to vrapi\_SubmitFrame".
* Fixed crashes in OVR::D3DUtil::Blitter::Blt due to inconsistent overlay lifetimes.
## Known Issues

* Unity 5.6.0f3 is the only supported version of 5.6 at this time. Gear VR applications built with Unity 5.6.0f2 crash immediately upon launch, and Gear VR applications built with 5.6.0p1 may crash when Multi-View is enabled.
* The following versions of Unity require the [Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/en-us/download/details.aspx?id=48145) or Rift builds will fail to run in VR, and the error “Security error. This plugin is invalid!” will be reported in output\_log.txt:
	+ 5.3.6p3-5.3.6p7
	+ 5.4.0f1-5.4.2p1
	+ 5.5.0b1-5.5.0b8
	
* Unity has a known issue such that parenting one VR camera to another will compound tracking twice. As a workaround, make them siblings in the GameObject hierarchy.
* Rift
	+ All Unity versions prior to 5.4.3p3 leak 5MB/s if you have a Canvas in your scene, enable **Run In Background**, and dismount the Rift. You can check OVRManager.hasVrFocus in an Update function to disable your Canvases while the HMD is dismounted.
	+ Transparent VR Compositor Layers do not currently support multiple layers of occlusion.
	
* Gear VR
	+ Do not use Utilities 1.11.0 due to a crash when returning to focus from Universal Menu or Quit to Home dialog.
	+ Due to a Unity bug, the Camera pose can be corrupted by scripts in the first frame after being enabled with VR support. As a workaround, use the latest Utilities version or zero out the eye anchor poses when a new OVRCameraRig is spawned and the first frame after usePerEyeAnchors changes.
	+ With Unity 5.3, the world may appear tilted. As a workaround, use the latest Utilities version or disable the virtual reality splash image.
	+ Mobile developers should not use Unity versions 5.3.6p1-2 and 5.4.0p1-2 due to incorrect positional movement of the head.
	+ Unity 5.3.4-5.3.6p3 and Unity 5.4.0b16-Unity 5.4.0p3: Do not set **DSP Buffer Size** to **Best** in Audio Manager in the Inspector for now or you will encounter audio distortion. Set it to **Good** or **Default** instead.
	
* Mobile App Submission to Oculus Store 
	+ All mobile applications using Utilities 1.9 and 1.10 will fail Oculus Store submission due to a bug affecting reserved interaction handling for the Universal Menu. Please remove previously-imported project files as described in [Importing the Oculus Utilities Package](/documentation/unity/latest/concepts/unity-import/ "Oculus Utilities for Unity is an optional Unity Package that includes scripts, prefabs, and other resources to assist with development.") and import the latest Utilities version, and update your Unity editor to a [compatible version](/documentation/unity/latest/concepts/unity-req/ "This guide describes Unity Editor version recommendations and system requirements.") if necessary. 
	
