---
title: 0.1 Beta Utilities for Unity Release Notes
---
This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Utilities for Unity.

## Utilities for Unity 0.1.3.0 Beta

## Overview of Major Changes

Note: For detailed information about Unity version compatibility, please see [Compatibility and Requirements](/documentation/unity/latest/concepts/unity-req/ "This guide describes Unity Editor version recommendations and system requirements.").This document provides an overview of new features, improvements, and fixes included in the latest version of the Utilities for Unity 5.x. For information on first-party changes to Unity VR support for Oculus, see the Unity Release Notes for the appropriate version.

Utilities for Unity 0.1.3 extends OVRInput support to mobile. OVRInputControl and OVRGamepadController are now deprecated and will be removed in a future release.

Mobile input bindings are now automatically added to InputManager.asset if they do not already exist - it is no longer required to replace InputManager.asset with Oculus’ version. However, this asset is still provided for now to maintain legacy support for the deprecated OVRGamepadController and OVRInputControl scripts.

## New Features

* Default mobile input bindings are now programmatically generated when projects are imported if they do not already exist.
* Replacing InputManager.asset is no longer required to enable gamepad support on mobile. 
## API Changes

* Added mobile support OVRInput.
* Deprecated OVRInputControl and OVRGamepadController.
## Bug Fixes

* Fixed mobile gamepad thumbstick deadzone/drift handling and axis scaling.
* Fixed mobile gamepad support when multiple gamepads are paired.
* Fixed mobile gamepad bindings for triggers, D-pad, thumbstick presses, etc.
## Utilities for Unity 0.1.2.0 Beta

## Overview of Major Changes

This version adds an alpha preview release of OVRInput, which provides a unified input API for accessing Oculus Touch and Microsoft Xbox controllers.

## New Features

* Redesigned input API for Oculus Touch controllers and Xbox gamepads.
* Added h264 hardware-decoder plugin for Gear VR.
* Added “face-locked” layer support to OVROverlay when parented to the camera.
* Reduced latency in the pose used by the main thread for raycasting, etc.
* Updated to PC SDK 0.7 and Mobile SDK 0.6.2.0.
* Enabled VRSettings.renderScale on Gear VR.
* Several minor performance optimizations.
* SDKExamples
	+ Restored MoviePlayerSample
	
## API Changes

* The Utilities package now requires Unity 5.1 or higher.
* Added OVRInput API alpha. Refer to documentation for usage.
* Exposed LeftHand/RightHand anchors for tracked controllers in OVRCameraRig.
## Bug Fixes

* Restored ability to toggle settings such as monoscopic rendering and position tracking.
* HSWDismissed event is now correctly raised when the HSW is dismissed.
* Fixed handedness of reported velocity and acceleration values.
* OVRPlayerController now moves at a consistent speed regardless of scale.
## Known Issues

* Tearing in OS X: Editor preview and standalone players do not vsync properly, resulting in a vertical tear and/or judder on DK2.
* When switching between a mobile application and System Activities screen, the back button becomes stuck in the "down" state. For more information and workarounds, please see Troubleshooting and Known Issues.
## Utilities for Unity 0.1.0.0 Beta

## Overview

This is the initial release of Oculus Utilities for Unity, for use with Unity versions 5.1.2 and later. The Utilities extend Unity's built-in virtual reality support with the following features:

* Standard camera rig with head-tracked "anchors".
* Detailed tracking information such as head acceleration, velocity, and latency and the IR tracker pose.
* Control over the tracking method (positional, head model only, rotation-only).
* Information about the current user's IPD, eye relief, and eye height.
* Control over graphics performance/quality features such as monoscopic rendering, queue-ahead (PC-only), and chromatic aberration.
* Experimental overlay support for high-quality text and video on a world-space quad.
* First-person shooter-style locomotion.
* Screen dimming on scene transitions.
* Notification when out of positional tracking range.
* Cross-platform gamepad support.
* Debug overlay with real-time performance and latency graphs.
* (Android only) Access to the Oculus platform UI.
* (Android only) Performance and power management.
The Oculus Utilities for Unity expose largely the same API as the Oculus Unity Integration, but they offer all the benefits of Unity's built-in VR support:

* Improved rendering efficiency with less redundant work performed for each eye.
* Seamless integration with the Unity Editor, including in-Editor preview and direct mode support.
* Improved stability and tighter integration with features like anti-aliasing and shadows.
* Non-distorted monoscopic preview on the main monitor.
* Oculus SDK 0.6.0.1 support (PC and mobile).
## API Changes in 0.1.0 Beta

The following Unity API changes were made:

* Unity 5.1.1p3 or higher is now required.
* Some script functionality was replaced by UnityEngine.VR.
* Added Crescent Bay support.
* Removed Linux support, for now.
* Removed OvrCapi, the low-level C# wrapper for LibOVR.
* Removed Gear VR MediaSurface functionality. Use Mobile Movie Texture or similar.
* The integration now uses a single stereo camera instead of two separate cameras for the left and right eyes.
* Direct mode now works in the Editor.
* To use VR, you must enable Player Settings -> Virtual Reality Supported.
* DirectToRift.exe no longer applies.
* Editor preview is now monoscopic and does not include lens correction.
* The experimental overlay quad script OVROverlay also works on the PC.
## Known Issues

* Pitch, roll, and translation are off for the tracking reference frame in Unity 5.1.1, especially in apps with multiple scenes.
* Mac OS X tearing. VSync is currently broken on the Mac, but works when you build for Gear VR.
* Performance loss. CPU utilization may be slightly higher than in previous versions of Unity.
* OVRPlayerController might end up in an unexpected rotation after OVRDisplay.RecenterPose() is called. To fix it, call RecenterPose() again.
