---
title: 0.4 Release Notes
---

This document provides an overview of new features, improvements, and fixes included in version 0.4 of the Oculus Mobile SDK.

## 0.4.3.1

## Overview of Major Changes

This release adds support for Unity 5.0.0p2. Developers using Unity 5 must update to this version, and make sure that they are using the latest patch release from Unity.

We would like to highlight the inclusion of the new Mobile Unity Integration with full DK2 support based on the Oculus PC SDK 0.4.4. As this is a significant API refactor, please refer to the Unity Development Guide: Migrating From Earlier Versions section for information on how to upgrade projects built with previous versions of the Mobile Unity Integration.

## 0.4.3

## New Features

* Android Manifest
	+ Applications will now be required to specify the following permission to support distortion configuration updates by the system service. &lt;uses-permission android:name='android.permission.READ\_EXTERNAL\_STORAGE' /&gt;
	+ **Note**: Always refer to the *Oculus Mobile Submission Guidelines* for the latest information regarding the submission process.
	
* VrPlatform
	+ Support for entitlement checking with VrPlatform. Integration steps and instructions are included in the Oculus Mobile Developer Guideâ€™s *Mobile SDK Setup section*.
	


* Unity Integration
	+ New Mobile Unity Integration Based on Oculus PC SDK 0.4.4
	
* Miscellaneous
	+ The Mobile SDK Documentation folder hierarchy has been re-organized into a single document.
	


## API Changes

* VrLib
	+ Localized string updates for the Universal Menu.
	+ Improvements to yaw drift correction.
	+ Fixed vsync possibly being turned off by the Universal Menu when selecting reorient.
	+ Pre-register nativeSetAppInterface to work around a JNI bug where JNI functions are not always linked.
	+ Do not allow nativeSurfaceChanged to use a deleted AppLocal in case surfaceDestroyed is executed after onDestroy.
	+ Removed resetting the time warp when sensor device information is not populated on application launch.
	+ Improved Passthrough Camera latency by disabling Optical Image Stabilization (Exynos chipset only).
	+ Free EGL sync objects on time warp thread shutdown.
	


## Bug Fixes

* 360 Videos SDK
	+ Fixed bug where a few 360 videos would not play.
	+ Fixed several UI bugs.
	+ Added extra error handling.
	
* 360 Photos SDK
	+ Fixed several UI bugs.
	


## 0.4.2

## Overview of Major Changes

If you are developing with Unity, we recommend updating to Unity 4.6.1, which contains Android 5.0 – Lollipop support.

We would like to highlight the inclusion of the new Mobile Unity Integration with full DK2 support based on the Oculus PC SDK 0.4.4. As this is a significant API refactor, please refer to the Unity Development Guide: Migrating From Earlier Versions section for information on how to upgrade projects built with previous versions of the Mobile Unity Integration.

## API Changes

* VrLib
	+ Universal Menu localization support: English, French, Italian, German, Spanish, Korean.
	+ Move Direct Render out of VrApi and into TimeWarp.
	+ Print battery temperature to logcat.
	+ Fix rendering of TimeWarp Debug Graph.
	
* Unity Integration
	+ Fix for camera height discrepancies between the Editor and Gear VR device.
	+ Moonlight Debug Util class names now prefixed with OVR to prevent namespace pollution.
	+ Provide callback for configuring VR Mode Parms on OVRCameraController; see OVRModeParms.cs for an example.
	


* Native Framework
	+ Fixed bug in which Volume toast is not dismissed if user transitions to Universal Menu while the toast is active.
	+ Allow for app-specific handling when the user selects Reorient in the Universal Menu.
	+ SearchPaths: Now correctly queries Android storage paths.
	+ SearchPaths: Refactored to OvrStoragePaths.
	+ FolderBrowser: Improved load time by removing check for thumbnails in the application package.
	+ FolderBrowser: Improved scrolling and swiping physics.
	FolderBrowser: Added bound back and wrap around effects.
* Sample Project Changes
	+ 360 Photos SDK
		- Fixed bug in which the user could easily close the menu unintentionally when returning from a photo.
		- Fixed crash that occurred when photos stored in the physical "Favorites" folder were untagged as "Favorites".
		- Fixed crash caused by swiping on the "no media found" screen.
		
	+ 360 Videos SDK
		- Background star scene now fades to black when starting a video.
		- Changed corrupted media message to show only filename so it fits in the view.
		- Fixed rendering artifact that occurred when starting to play a video.
		
	


## 0.4.1

## Overview of Major Changes

Added support for Android 5.0 (Lollipop) and Unity Free.

## New Features

* Mobile SDK
	+ Added support for Android 5.0 (Lollipop).
	
* Unity
	+ Added Unity Free support for Gear VR developers.
	


## 0.4.0

## Overview of Major Changes

First public release of the Oculus Mobile SDK.

## New Features

* First public release of the Oculus Mobile SDK.


## API Changes

* The Mobile SDK is now using API Level 19. Please make the following change to your manifest file: &lt;android:minSdkVersion='19' android:targetSdkVersion='19' /&gt;


## Bug Fixes

* Health and Safety Message no longer required on mount.
* Lens distortion updated for final Gear VR lenses.
* Improved Mag Yaw drift correction.
* Option ability to update distortion file without the need for app rebuild.
* Changed default font to Clear Sans.
* Unity vignette rendering updated to match native (slightly increases effective FOV).
* Unity volume pop-up distance to match native.
* Fix Gaze Cursor Timer scale.

