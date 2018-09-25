---
title: 0.6 Release Notes
---
This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Mobile SDK.

## 0.6.2.0

## Overview of Major Changes

The 0.6.2.0 version of the Oculus Mobile SDK includes a change to how we link with OpenGL ES. Previous versions of the SDK had a hard link to libGLESv3.so, which is problematic for engines which integrate the VrApi and must support non-VR devices. Beginning with 0.6.2, the mobile SDK dynamically loads all OpenGL ES symbols.

The source for the Unity SDKExample MediaSurface Plugin is now provided. The Media Surface Plugin provides a native library which is used with the Android MediaPlayer for hardware decoding of a single video to a texture. Note that the SDKExample MediaSurface Plugin is not intended to be production quality, and is provided for reference purposes. We have made the source available in case you would like to modify it for your use. The source and build files are located at the following SDK path: VrAppSupport/MediaSurfacePlugin.

For detailed instructions on updating native projects to this SDK version, see [Mobile Native SDK: Migration](/documentation/mobilesdk/latest/concepts/mobile-native-migration/#mobile-native-migration "This section details migrating from earlier versions of the Mobile SDK for native development.").

## New Features

* VrApi
	+ Dynamically loads OpenGL ES symbols instead of hard-linking to libGLESv3.so.
	
* VrCapture
	+ Added mode to capture straight to local flash storage instead of waiting for a remote connection. Useful for automated testing, capturing the startup sequence, and working around issues caused by low-bandwidth WiFi networks.
	
## API Changes

* VrApi
	+ Remove several non-VR android-specific interface calls.
	
* Native Application Framework
	+ VrGUI Library project now contains Java source and resources.
	+ VrAppInterface::DrawEyeView() takes an additional parameter.
	
## Bug Fixes

* VrApi
	+ Fixed thread affinity failing to be set for the TimeWarp and DeviceManager threads.
	+ Fixed device reset when repeatedly plugging and unplugging the Travel Adapter on the Samsung GALAXY S6.
	
* VrAppFramework
	+ Optimized GazeCursor to render in two draw calls per eye instead of 32.
	+ Fixed GlGeometry BuildGlobe so that equirect center is at -Z (forward).
	
## 0.6.1.0

## Overview of Major Changes

The 0.6.1.0 version of the Oculus Mobile SDK includes major structural changes to the native VrAppFramework library. Several subsystems that were previously part of VrAppFramework have been moved into individual libraries under the VrAppSupport folder, making the application framework leaner and reducing its focus to handling the Android application lifecycle.

LibOVR has now been renamed to LibOVRKernel to better represent its intended functionality and to maintain parity with the PC SDK.

The Java activity code has been refactored to remove dependencies on the VrActivity class for applications that do not use VrAppFramework.

The SDK Native Samples were updated to a cross-platform friendly structure. Android Library Projects are now found at [ProjectName]/Projects/Android.

## Changes to Unity Integration

The Oculus Unity Integration is no longer bundled with the Mobile SDK and must now be downloaded separately from our Downloads page: [https://developer.oculus.com/downloads/](/downloads/)

We now provide a Utilities for Unity package for use with Unity’s first-party VR support (available in Unity 5.1+). For legacy project development, we currently offer a legacy Unity Integration package for use with Unity 4.6.7 and later. Please see our Unity documentation for more information.

If you are using the Utilities for Unity Package with Unity 5.1+, the SDKExamples are now available for download separately.

If you are using the Legacy Unity Integration, update to Oculus Runtime for OS X 0.5.0.1. Before updating your runtime, be sure to run uninstall.app (found in /Applications/Oculus/) to remove your previous installation.

## New Features

* VrApi
	+ Images composited by the time warp are now allocated through the VrApi as "texture swap chains".
	+ Performance params (CPU/GPU level, thread ids) can now be adjusted every frame through vrapi\_SubmitFrame.
	+ adb logcat -s VrApi now reports the thread affinity.
	+ ovr\_GetSystemProperty now provides options for querying GpuType, Device external memory, and max fullspeed framebuffer samples, see ovrSystemProperty in VrApi\_Types.h
	
* VrCubeWorld
	+ Added example to VrCubeWorld\_SurfaceView and VrCubeWorld\_NativeActivity samples to reduce the latency by re-sampling the tracking state later in the frame.
	
* VrTemplate
	+ make\_new\_project script is now converted to Python for cross-compatibility.
	
* VrCapture / OVRMonitor
	+ VrCapture may now be integrated into and collect data from multiple shared libraries in your app simultaneously (previously you could capture from VrApi or from your app, but not both at the same time).
	+ OpenGL and logcat calls are now captured throughout the entire process.
	+ Applications may now expose user-adjustable variables via OVR::Capture::GetVariable() and tweak the values in real-time in OVRMonitor.
	+ Frame Buffer capturing now does basic block-based compression on the GPU, reducing network bandwidth by 50%.
	+ GPU Zones are enabled, but we recommend only using them on the Samsung GALAXY S6.
	+ Added Settings View for toggling VR Developer Mode.
	+ Sensor Graphs now turn red when values exceed max defined by SetSensorRange().
	
## API Changes

* Native Application Framework
	+ VRMenu, OvrGuiSys, OvrGazeCursor and related classes have been moved to the VrAppSupport/VrGui library.
	+ OvrSceneView, ModelFile and related classes have been moved to the VrAppSupport/VrModel library.
	+ Localization-related functionality has been moved to the VrAppSupport/VrLocale library.
	+ The sound pool and related classes have been moved to the VrAppSupport/VrSound library.
	+ The VrGui library now uses the SoundEffectPlayer interface for sound playback, replacing SoundManager. This simple interface can be overloaded to allow VrGui sounds to be played by any sound library.
	+ VrActivity java class now subclasses Android Activity instead of ActivityGroup.
	
## Bug Fixes

* VrAPI
	+ Fixed adb logcat -s VrApi failure to report memory stats.
	
* Native Application Framework
	+ Fixed a bug where missing font glyphs were skipped instead of rendering as an asterisk.
	
* Cinema SDK
	+ Fixed last media poster showing up as the first poster for another category.
	+ Play/Pause icon does not function correctly after unmount/mount.
	+ Unmount/Mount does not pause media immediately.
	+ Fixed bad camera orientation in Void theater when auto-switching from another theater due to starting a video with a resolution greater than 1920x1080.
	
* 360 Photos SDK
	+ Fixed Favorites and Folder Browser icon switching in the attribution menu. 
	+ Fixed menu state bug causing background scene not to be drawn.
	+ Fixed menu orientations not resetting on reorient.
	+ Increased vertical spacing between categories in Folder Browser to improve thumbnail scrollbar fit.
	
* 360 Videos SDK
	+ Fixed media failure to pause immediately when unmounted.
	+ Fixed movie not pausing on launching system activities. 
	+ Fixed menu orientation when resuming app.
	+ Fixed gaze cursor not showing up when in Browser.
	
* Build Scripts
	+ Fix for devices over adb tcpip: If the phone was connected over TCP, it was trying to find oculussig\_WWW.XXX.YYY.ZZZ:PPP when checking for the oculussig file.
	+ If an install and run was requested but no devices found, now reports to user rather than quitting silently.
	+ Change directories in an exception-safe manner.
	
* VrCapture / Remote Monitor
	+ Fixed rare crash when disconnecting from remote host on OS X.
	+ Reconnecting to an app multiple times no longer puts the capture library in an undefined state.
	
## Known Issues

* Unity 4 with Oculus Runtime for OS X 0.4.4 and Legacy Integration 0.6.1.0 or 0.6.0.2
	+ Editor crashes when building APK or pressing play in Play View; Mac standalone player crashes. To fix, update to Oculus Runtime for OS X 0.5.0.1. Before updating your runtime, be sure to run uninstall.app (found in /Applications/Oculus/) to remove your previous installation.VrApi implicitly links to libGLESv3.so, so currently you cannot load libvrapi.so on devices without OpenGL ES 3.0 support.
	
* VrCapture / Remote Monitor 
	+ GPU Zones currently work on the Galaxy S6 only.
	+ Timer Queries are not functional on Adreno based devices.
	+ Integrated systrace support is under development and is currently disabled.
	+ Some VPNs break auto-discovery.
	
## 0.6.0.1

## Overview

This release of the Mobile SDK includes a fix to performance issues related to our Universal Menu and a hitching problem associated with data logging in VrApi, as well as some other minor updates. If you are upgrading from Mobile SDK v 0.5, be sure to review the 0.6.0 release notes for additional information on significant changes to our native development libraries as well as other updates.

Note that our Mobile SDK documentation is now available online here: [https://developer.oculus.com/documentation/mobilesdk/latest/](/documentation/mobilesdk/latest/)

## New Features

* Allow Unity MediaSurface dimensions to be modified via plugin interface.
## Bug Fixes

* Fixed performance regression triggered when coming back from the Universal Menu.
* Fixed not being able to enable chromatic aberration correction in the Unity plugin.
* Reduced once per second frame drop due to gathering stats.
* Fixed Do Not Disturb setting.
* Fixed adjusting clock levels from Unity during load.
## Known Issues

* adb logcat -s VrApi always reports the amount of available memory as 0.
## 0.6.0

## Overview of Native Changes

The 0.6.0 version of the Oculus Mobile SDK introduces several major changes that necessitate updates to the VRLib structure, native app interface, and development workflow. If you are migrating from a previous SDK, please refer to the "Migrating from Earlier Versions" sections of the Native Development guide.

VRLib has been restructured into three separate libraries in order to make the code more modular and to provide a smoother workflow:

* LibOVR – the Oculus Library
* VrApi – the minimal API for VR
* VrAppFramework – the application framework used by native apps
Both LibOVR and VrAppFramework ship with full source. The VrApi is shipped as a set of public include files, a pre-built shared library, and a jar file. Shipping VrApi as a separate shared library allows the VrApi implementation to be updated and/or changed after an application has been released. This allows us to apply hot fixes, implement new optimizations, and add support for new devices without requiring applications to be recompiled with a new SDK. VrApi source is no longer included with the SDK.

The Vr App Interface (now part of VrAppFramework) has been simplified and now has a clearly-defined lifecycle. The order in which functions are called has been clarified – previously, some functions could be called either in VR mode or outside of VR mode. The lifecycle can be found in VrAppFramework/Src/App.h.

The VRMenu code has been refactored in preparation for moving it into its own static library. User Interface-related interfaces that were previously passed to functions individually are now part of OvrGuiSys.

There are three new native samples. These samples implement the same simple scene in three different ways, illustrating three approaches to Native application development

* VrCubeWorld\_SurfaceView – uses a plain Android SurfaceView and handles all Activity and Surface lifecycle events in native code. This sample uses only the VrApi and uses neither the Oculus Mobile Application Framework nor LibOVR.
*  VrCubeWorld\_NativeActivity – uses the Android NativeActivity class. This sample uses only the VrApi and uses neither the Oculus Mobile Application Framework nor LibOVR.
* VrCubeWorld\_NativeActivity – uses the Oculus Mobile Application Framework.
For developers who prefer to use command-line scripts to build native projects, this SDK provides a robust cross-platform set of python build scripts to replace the platform specific build scripts provided with previous SDKs.

## Overview of Unity Integration Changes

* Oculus Runtime is no longer required for mobile development.
* Synced with the Oculus PC SDK 0.6.0.0 beta.
* Allows clients to re-map plugin event IDs.
For both the PC and Mobile SDKs we recommend the following Unity versions or higher: Unity Pro 4.6.3, Unity Professional 5.0.2.p2, Unity Free 4.6, or Unity Personal 5.0.2.p2. For mobile development, compatibility issues are known to exist with Unity 5 and OpenGL ES 3.0 – please check back for updates. Earlier versions of Unity 5 should not be used with the Mobile SDK.

Note: Before installing or integrating this distribution, we strongly recommend backing up your project before attempting any merge operations.## New Features

* VrAPI
	+ Improved frame prediction, in particular for Unity.
	+ Leaving the CPU clock unlocked until the application starts rendering frames to make application loading/resuming faster.
	+ Improved Performance Metrics via Logcat (see Basic Performance Stats through Logcat section of the Native Development Guide for more information).
	
* Native Application Framework
	+ Improved Android Activity and Android Surface lifecycle handling.
	+ Fixed volume bar not showing on first click of the volume adjustment.
	
* 360 Photos SDK
	+ Gaze Cursor now disappears when looking away from Attribution menu.
	
* Blocksplosion
	+ Added OS X input mappings.
	
## API Changes

* Native Application Framework
	+ Automatic caching of files extracted from apk.
	
## Bug Fixes

* VrAPI
	+ Removed additional frame of latency between synthesis and display.
	+ Fixed intra frame object motion judder due to TimeWarp displaying eye buffers too early when eye buffer rendering completed early.
	+ Fixed TimeWarp getting more than one frame behind after a bad hitch.
	+ Workaround for "loss of head tracking" after closing and re-opening the device 96 times.
	
* Native Application Framework
	+ Fixed volume bar not showing on first click of the volume adjustment.
	
* Unity Integration
	+ Fixed prediction glitch every 64 frames.
	+ Use correct prediction for OVR\_GetCameraPositionOrientation.
	+ Fixed location of the PlatformMenu Gaze Cursor Timer.
	
* Cinema SDK
	+ Fixed playback control reorienting screen in Void theater when user clicks on controls when they're off the screen on portrait videos.
	+ Fixed divide by zero in SceneManager::GetFreeScreenScale() which caused Void theater to crash when starting a movie.
	
* 360 Photos SDK
	+ Fixed Favorites button not creating Favorites folder.
	
* Blocksplosion
	+ Fixed launch blocks falling straight down when launched when built with Unity 5.
	+ Fixed touch triggering "next level" after returning from the System Activity.
	+ Fixed launch block being offset when looking left or right.
	
## Known Issues

* Initial launch of 360Photos SDK Sample can crash if a duplicate category folder name is present on the target device’s sdcard. Subsequent launches of the app will not crash. A fix is in the works for the next release.
