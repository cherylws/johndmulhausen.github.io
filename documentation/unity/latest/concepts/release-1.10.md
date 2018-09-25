---
title: 1.10 Oculus Utilities for Unity 5 Release Notes
---
## Oculus Utilities for Unity 5 version 1.10.0

This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Utilities for Unity 5. For information on first-party changes to Unity VR support for Oculus, see the Unity Release Notes for the appropriate version. You will find a scripting reference for the included C# scripts in our [Unity Developer Reference](/documentation/game-engines/latest/concepts/book-unity-reference/).

If you have previously imported a Unity integration package, you must delete all Oculus Integration content before importing the new Unity package. For more information, see [Importing the Oculus Utilities Package](/documentation/unity/latest/concepts/unity-import/ "Oculus Utilities for Unity is an optional Unity Package that includes scripts, prefabs, and other resources to assist with development.").

Utilities 1.10 adds an option to build in APK for submission to the Oculus Store in **Tools** > **Oculus**. It also includes a fix for an issue that caused poor performance or freezing when using multiple VR cameras or VR Compositor underlays with Gear VR. Any mobile application using either of these should update to this version. 

## New Features

* Added option to **Tools** > **Oculus** to build APK for submission to Oculus Store.
* Added Rift support for cubemap overlays to VR Compositor Layers.
## Bug Fixes

* Fixed poor performance or freezing bug when using multiple VR cameras or VR Compositor underlays with Gear VR.
* Fixed memory leak in OVROverlay.
* Fixed uncommon issue in which setting mirror to full screen caused app rendering to freeze in Rift.
## Known Issues

* The following versions of Unity require the [Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/en-us/download/details.aspx?id=48145) or Rift builds will fail to run in VR, and the error “Security error. This plugin is invalid!” will be reported in output\_log.txt:
	+ 5.3.6p3-5.3.6p7
	+ 5.4.0f1-5.4.2p1
	+ 5.5.0b1-5.5.0b8
	
* Rift
	+ All Unity versions leak 5MB/s if you have a Canvas in your scene, enable Run In Background, and dismount the Rift. You can check OVRManager.hasVrFocus in an Update function to disable your Canvases while the HMD is dismounted.
	
* Gear VR
	+ Mobile developers should not use Unity versions 5.3.6p1-2 and 5.4.0p1-2 due to incorrect positional movement of the head.
	+ Unity 5.3.4-5.3.6p3 and Unity 5.4.0b16-Unity 5.4.0p3: Do not set DSP Buffer Size to Best in Audio Manager in the Inspector for now or you will encounter audio distortion. Set it to Good or Default instead.
	
* Touch
	+ For PCs using Oculus runtime 1.10, OVRInput.GetConnectedControllers() does not mark Touch controllers as disconnected when batteries are removed, and the input mask returns Touch (Left+Right) active when only one controller is on. This issue will resolve automatically when runtime 1.11 is released. 
	
