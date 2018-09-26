---
title: 0.5 Release Notes
---

This document provides an overview of new features, improvements, and fixes included in the version 0.5 of the Oculus Mobile SDK.

## 0.5.1

## Overview of Major Changes

This document provides an overview of new features, improvements and fixes that are included in this distribution of the Oculus Mobile SDK.

The most significant change in 0.5.1 is to System Activities event handling in Unity. The 0.5.0 code for handling System Activities events in Unity was doing heap allocations each frame. Though this was not a leak, it would cause garbage collection to trigger much more frequently. Even in simple applications, garbage collection routinely takes 1 to 2 milliseconds. In applications that were already close to dropping below 60 Hz, the increased garbage collection frequency could cause notable performance drops. The event handling now uses a single buffer allocated at start up.

Other notable changes were to HMT sensor prediction — specifically clamping of the delta time used for prediction. Without this change delta times on application startup could sometimes be huge, causing an apparent jump in screen orientation.

**Unity Developers**: As with Mobile SDK v 0.5.0, Unity developers using this SDK version must install the Oculus Runtime for Windows or OS X. This requirement will be addressed in a future release of the SDK.

## API Changes

* Sensor Prediction: Make sure Predicted deltaTime can never be negative or become huge.
* Sensor Prediction: Clamp delta time used for sensor prediction to 1/10th of a second instead of 1/60th so that we donâ€™t under-predict if the target frame rate is not being met.
* Better handling for a case where SystemActivities resumes without an explicit command. This can happen if the top app crashes or does a finish() instead of launching Home to exit.


## Bug Fixes

* Unity Integration
	+ Rework System Activities Event handling to prevent any per-frame allocations that could trigger Garbage Collector.
	
* Native Framework
	+ Fixed potential MessageQueue deadlock
	+ Bitmapfont - Fix case where billboarded text is right on top of the view position and results in a zero-length normal vector.
	+ Bitmapfont - Fix for font info height not being y-scaled.
	+ Renamed VERTICAL\_BOTTOM to VERTICAL\_BASELINE because it aligns to the first row’s baseline rather than the bottom of the entire text bounds.
	+ Bitmapfont - Fix for VERTICAL\_CENTER\_FIXEDHEIGHT to correctly account for the ascent / descent when rendering single and multi-line text.
	+ VrMenu Fader - Update only performed if frame time is &gt; 0.0f.
	+ VrMenu - Add ProgressBar component.
	+ VrMenu - Parent / child rotation order in menus was backwards, causing confusion when local rotations were used.
	+ VrMenu - Don’t use an old view matrix to reposition menus on a reorient. Since we reorient to identity (with respect to yaw) we should reposition with respect to identity instead of the last frame’s view matrix.
	+ AppLocal::RecenterYaw() now adjusts lastViewMatrix so that it instantly reflects the recenter of the sensor fusion state.
	+ FolderBrowser - Allow implementers to create their own panel object.
	


## Known Issues

* Application version number remains 0.5.0 and was not incremented to 0.5.1. This does not affect app functionality and will be addressed in a future release.
* For use with the Mobile SDK, we recommend Unity versions 4.6.3. The Mobile SDK is compatible with Unity 5.0.1p2, which addresses a problem with OpenGL ES 3.0, but there is still a known Android ION memory leak. Please check back for updates.


## 0.5.0

## Overview of Major Changes

The Universal Menu has been removed from VrLib, allowing modifications to the Universal Menu without requiring each app to upgrade to the latest SDK. The Universal Menu is now part of the Oculus System Activities application and is downloaded and updated alongside Oculus Home and Horizon. Make sure you update your version of Home in order to test your application with the new Universal Menu. If you are migrating from a previous SDK, please refer to the "Migrating from Earlier Versions" sections of the Native Development and Unity Integration guides.

The Mobile Unity Integration is now synced with the Oculus PC SDK 0.5.0.1 Beta. Please ensure you have installed the corresponding 0.5.0.1 Oculus runtime; it can be found at the following location: [https://developer.oculus.com/downloads/](/downloads/)

VrPlatform entitlement checking is now disabled by default in Unity; handling for native development is unchanged. If your application requires this feature, please refer to the Mobile SDK Documentation for information on how to enable entitlement checking.

Applications built with Mobile SDK 0.5.0 or later will be compatible with the Samsung GALAXY S6.

## New Features

* Android Manifest
	+ Mobile SDK 0.5.0 no longer requires PlatformActivity in the AndroidManifest.xml file. If you have previously worked with an earlier SDK, the following block must be removed: &lt;activity android:name='com.oculusvr.vrlib.PlatformActivity' android:theme='@android:style/Theme.Black.NoTitleBar.Fullscreen' android:launchMode='singleTask' android:screenOrientation='landscape' android:configChanges='screenSize|orientation|keyboardHidden|keyboard'&gt;
	+ The camera permission is also no longer required and can be removed from your manifest if your app does not rely on it: &lt;uses-permission android:name='android.permission.CAMERA'/'&gt;
	+ For additional information on manifest requirements, see the relevant documentation in the Native Development Guide, Unity Integration Guide, and Mobile App Submission Guide.
	


* Native Framework
	+ Folder Browser
		- Added support for dynamically loaded categories.
		- Factored out MetaData from FolderBrowser into MetaDataManager.h/cpp.
		- Improved wrap-around controls.
		
	+ Sound Limiter
		- Application sound\_asset.json files may now override specific menu sounds.
		
	+ VrMenu
		- Added hit test result to VRMenuEvent.
		- Added debugMenuHierarchy console command for debug drawing of VrMenu hierarchy.
		- Now uses current view matrix for gaze cursor and menu positions.
		- Added options for horizontal and vertical text justification.
		- Multi-Line text justification.
		- Added option to allow text to line up horizontally with different descenders.
		
	
* Unity Integration
	+ Synced with the Oculus PC SDK 0.5.0.1 Beta.
	+ VrPlatform entitlement checking is now disabled by default.
	
* Cinema SDK
	+ UI reworked using new UI components.
	
* 360 Photos SDK
	+ Added libjpeg.a directly to projects in order to avoid dependency on libjpeg source.
	+ Metadata is now app-extensible. Added functionality for reading and writing extended metadata during app loading and saving.
	
* 360 Videos SDK
	+ Added libjpeg.a directly to projects in order to avoid dependency on libjpeg source.
	+ Metadata is now app-extensible. Added functionality for reading and writing extended metadata during app loading and saving.
	


## API Changes

* VrLib
	+ Universal Menu moved from VrLib into a separate application.
	+ Universal Menu specific functionality removed from VrLib.
	+ Adds Oculus Remote Monitor support.
	+ VrApi restructured for future modularity and ease of development.
	+ Local preferences are now allowed in Developer Mode. Please refer to the Mobile SDK Documentation for more information.
	+ Default eye height and interpupillary distance have been changed to conform to the default values used by the PC SDK.
	+ The native head-and-neck model has been re-parameterized to use a depth/height pair rather than angle/length to conform to the PC SDK.
	+ HMDState sensor acquisition code has been re-written to make it reliable and thread safe.
	+ Now restores last-known good HMD sensor yaw when recreating the HMD sensor.
	


## Bug Fixes

* Unity Integration
	+ Health and Safety Warning no longer displays in editor Play Mode if a DK2 is not attached.
	
* Cinema SDK
	+ Fixed playback controls reorienting screen in void theater when user clicks on controls when they are off the screen on portrait videos.
	
* OvrGuiSys
	+ RemoveMenu is now DestroyMenu and will now free the menu.
	


## Known Issues

* Unity Integration
	+ For use with the Mobile SDK, we recommend Unity versions 4.6.3, which includes Android 5.0 - Lollipop support as well as important Android bug fixes. While the Mobile SDK is compatible with Unity 5.0.0p2 and higher, several issues are still known to exist, including an Android ION memory leak and compatibility issues with OpenGL ES 3.0. Please check back for updates.
	

