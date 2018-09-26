---
title: 1.12 Oculus Utilities for Unity 5 Release Notes
---



## Oculus Utilities for Unity 5 version 1.12.0

This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Utilities for Unity 5. For information on first-party changes to Unity VR support for Oculus, see the Unity Release Notes for the appropriate version. You will find a scripting reference for the included C# scripts in our [Unity Reference Content](/documentation/unity/latest/concepts/book-unity-reference/).

## Version Compatibility

On initial release, Utilities v 1.12.0 is compatible with our recommended Unity 5.3.8f1 and 5.4.5f1. For up-to-date compatibility information, see [Compatibility and Version Requirements](/documentation/unity/latest/concepts/unity-req/).

## New Features

* Added support for the Gear VR Controller to OVRInput. For more information, see [OVRInput](/documentation/unity/latest/concepts/unity-ovrinput/#unity-ovrinput "OVRInput exposes a unified input API for multiple controller types.").


## API Changes

* Added OVRPlugin.GetAppFramerate() to OVRDisplay.cs; returns frame rate reported by Oculus plugin (Rift and Gear VR). Requires a Unity Editor version we recommend for use with Utilities 1.12 - see [Compatibility and Version Requirements](/documentation/unity/latest/concepts/unity-req/ "This guide describes Unity Editor version recommendations and system requirements.") for details.


## Bug Fixes

* Changed OVRInput.GetAngularVelocity(..) and OVRInput.GetAngularAcceleration(..) to return Vector3 instead of Quaternion, avoiding issues for rates above 2*pi. Developers who need the old behavior for any reason may use Quaternion.Euler(..).
* Gear VR: 
	+ Fixed bug causing mobile applications built with Unity versions compatible with Utilities 1.11.0 to crash when returning to focus from Universal Menu or Quit to Home dialog, or when the Gear VR is taken off for several seconds, then put back on.
	+ Fixed black screen during launch with developer mode enabled in some Unity 5.3 versions using our 1.11 integration.
	+ Fixed bug causing mobile apps using Utilities 1.11.0 to appear tilted when enabling a virtual reality splash screen.
	
* VR Compositor Layers:
	1. Added OVRUnderlayTransparentOccluder, which was missing in previous versions.
	2. Fixed issue causing layer colors to appear washed out when using render targets as input textures on PC.
	3. Fixed issue where right-side textures were lost when using stereo pairs of OVROverlays.
	


## Known Issues

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
	+ Due to a Unity bug, the Camera pose can be corrupted by scripts in the first frame after being enabled with VR support. As a workaround, use Utilities 1.12 or zero out the eye anchor poses when a new OVRCameraRig is spawned and the first frame after usePerEyeAnchors changes.
	+ With Unity 5.3, the world may appear tilted. As a workaround, use Utilities 1.12 or disable the virtual reality splash image.
	+ Mobile developers should not use Unity versions 5.3.6p1-2 and 5.4.0p1-2 due to incorrect positional movement of the head.
	+ Unity 5.3.4-5.3.6p3 and Unity 5.4.0b16-Unity 5.4.0p3: Do not set **DSP Buffer Size** to **Best** in Audio Manager in the Inspector for now or you will encounter audio distortion. Set it to **Good** or **Default** instead.
	
* Mobile App Submission to Oculus Store 
	+ All mobile applications using Utilities 1.9 and 1.10 will fail Oculus Store submission due to a bug affecting reserved interaction handling for the Universal Menu. Please remove previously-imported project files as described in [Importing the Oculus Utilities Package](/documentation/unity/latest/concepts/unity-import/ "Oculus Utilities for Unity is an optional Unity Package that includes scripts, prefabs, and other resources to assist with development.") and import Utilities version 1.12, and update your Unity editor to a [compatible version](/documentation/unity/latest/concepts/unity-req/ "This guide describes Unity Editor version recommendations and system requirements.") if necessary. 
	+ When building a mobile application for submission to the Oculus Store, you must set **Install Location** to **Auto** in addition to generating a custom manifest as described in [Building Mobile Applications](/documentation/unity/latest/concepts/unity-build-android/#unity-build-android "This section describes the steps necessary for building Unity applications for Oculus Go and Samsung Gear VR.").
		1. Click **Edit &gt; Project Settings &gt; Player**.
		2. Expand the **Other Settings** properties.
		3. Set **Install Location** to **Auto**.
		
	

