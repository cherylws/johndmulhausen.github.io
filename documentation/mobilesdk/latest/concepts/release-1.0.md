---
title: 1.0 Release Notes
---

This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Mobile SDK.

## 1.0.4

## Overview of Major Changes

The VrApi implementation is now distributed through the Oculus System Driver application.

Long-press back button handling (including gaze timer rendering) and recenter-on-mount are now detected and handled directly by VrApi. Applications should no longer implement this logic.

The System Utilities library dependency has been removed and its functionality is now handled directly within VrApi. Applications which require VrApi only no longer need to link to anything else.

The VrApi Loader is now Java free, further reducing the number of dependencies an application is required to link against.

TimeWarp Debug Graph has been removed. Please use OVRMonitor instead.

For details on migrating to Mobile SDK 1.0.4 from previous versions, see [Migrating to Mobile SDK 1.0.4](/documentation/mobilesdk/latest/concepts/mobile-native-migration/#mobile-native-migration-1-0-4).

## New Features

* Gaze Cursor Timer is now rendered automatically in VrApi as a TimeWarp Layer.


## API Changes

* Back-button long press handling and recenter-on-mount are now handled directly by VrApi. Apps should not implement this logic any longer.
* VrApi now provides an interface for displaying System UIs, returning to Home, and displaying fatal error messages. See VrApi\_SystemUtils.h.
* System Level Button Timings are now exposed on the VrApi System Properties interface. See VRAPI\_SYS\_PROP\_BACK\_BUTTON\_SHORTPRESS\_TIME and VRAPI\_SYS\_PROP\_BACK\_BUTTON\_DOUBLTAP\_TIME.
* A recenter count has been added to the VrApi System Status interface. See VRAPI\_SYS\_STATUS\_RECENTER\_COUNT.
* Applications are no longer responsible for managing the SystemUtils app events and should remove the following function calls:
	+ SystemActivities\_Init
	+ SystemActivities\_Shutdown
	+ SystemActivities\_Update
	+ SystemActivities\_PostUpdate
	


## 1.0.3

**Overview of Major Changes**

**Multi-view**

Mobile SDK 1.0.3 adds multi-view rendering support. Multi-view rendering allows drawing to both eye views simultaneously, significantly reducing driver API overhead. It includes GPU optimizations for geometry processing.

Preliminary testing has shown that multi-view can provide:

* 25-50% reduction in CPU time consumed by the application
* 5% reduction in GPU time on the ARM Mali
* 5%-10% reduction in power draw


Obviously the freed up CPU time could be used to issue more draw calls. However, instead of issuing more draw calls, we recommend that applications maintain the freed up CPU time for use by the driver threads to reduce/eliminate screen tears.

While current driver implementations of multi-view primarily reduce the CPU usage, the GPU usage is not always unaffected. On the Exynos based devices, multi-view not only reduces the CPU load, but slightly reduces the GPU load by only computing the view-independent vertex attributes once for both eyes, instead of separately for each eye.

Even though there are significant savings in CPU time, these savings do not directly translate into a similar reduction in power draw. The power drawn by the CPU is only a fraction of the total power drawn by the device (which includes the GPU, memory bandwidth, display etc.).

Although all applications will have their unique set of challenges to consider, multi-view should allow most applications to lower the CPU clock frequency (CPU level) which will in turn improve power usage and the thermal envelope. However, this does not help on the Exynos based devices where CPU level 1, 2 and 3 all use the same clock frequency.

Multi-view will not be available on all Gear VR devices until driver and system updates become available.

The current set of supported devices as of the date of this release is:

* S6 / Android M
* S6+ / Android M
* S6 Edge / Android M
* Note 5 / Android M
* Exynos S7 / Android M
* Exynos S7+ / Android M


For detailed instructions on how to structure a native application for multi-view rendering, see [Migrating to Mobile SDK 1.0.3](/documentation/mobilesdk/latest/concepts/mobile-native-migration/#mobile-native-migration-1-0-3).

We are working with Unity and Epic to support multi-view in Unity and Unreal Engine.

**VrAppInterface**

VrAppInterface has been refactored to simplify the interface, support multi-view rendering, and enforce per-frame determinism. We highly recommend updating your VrAppInterface based application to support multi-view. However, even if you are not planning on supporting multi-view, it would be good to adopt the VrAppInterface changes because they also pave the way for Vulkan support in the future.

**VrApi**

VrAppFramework-based applications now explicitly pass EGL objects to VrApi. Previously, the various VrApi functions had to be called from a thread with a specific EGLContext current. The current EGLContext and EGLSurface were basically invisible parameters to the VrApi functions. By explicitly passing the necessary EGL objects to the API, there are no threading restrictions.

Volume notifier is now rendered automatically in VrApi as a TimeWarp layer - the application is no longer responsible for generating and displaying this notification. Be sure not to render your own volume interface!

**Build process**

Various build steps have been moved from the Python build scripts into Gradle.

## New Features

* Volume Notifier now rendered automatically in VrApi as a TimeWarp Layer.
* VrAppFramework now supports multi-view rendering path.
* VrAppFramework now uses explicit EGL objects.
* GlTexture now supports RGBA ASTC compressed textures.


## API Changes

* VrAppInterface::OneTimeInit and VrAppInterface::NewIntent have been replaced by VrAppInterface::EnteredVrMode. This function is called right after an application entered VR mode.
* VrAppInterface::OneTimeShutdown has been removed in favor of moving shutdown code to the destructor of the VrAppInterface derived class.
* VrAppInterface::LeavingVrMode is now called right before the application is about to leave VR mode.
* VrAppInterface::Frame now takes an ovFrameInput structure and returns an ovrFrameResult structure.
* VrAppInterface::OnKeyEvent was removed. Key events are now explicitly handled in VrAppInterface::Frame.
* VrApi ovrModeParmFlags now provide VRAPI\_MODE\_FLAG\_NATIVE\_WINDOW for specifying the ANativeWindow explicitly.


## Bug Fixes

* Fixed docked / mounted queries to be accurate without requiring an initial event.
* Sample apps no longer prompt for an SD card on devices that donâ€™t support external memory.


## Known Issues

* When converting your app to be multi-view compliant, ensure that your System Activities version is at least 1.0.3.1 or you will receive a required system update message.


## 1.0.0.1

## Overview of Major Changes

This minor patch release fixes problems with OS X development and splits Oculus Remote Monitor from the Mobile SDK to make it easier to access for developers using a third-party game engine.

## New Features

* Oculus Remote Monitor
	+ VR Developer Mode is no longer required if you have System Activities 1.0.2 or greater and an app built with Oculus Mobile SDK 1.0 or greater.
	+ Exposed experimental layer texel density and complexity visualizers (supported by apps built with Oculus Mobile SDK 1.0 or later).
	+ Now available as a separate downloadable package from the full Mobile SDK download.
	


## Bug Fixes

* Fixed OS X "No such file or directory" build problem.
* Oculus Remote Monitor
	+ Improved network stability on Windows
	
* Increased VR thread stack size.


## 1.0.0

## Overview of Major Changes

VrApi is now dynamically loaded from a separate APK, allowing it to be updated without requiring developers to recompile applications. This will allow us to fix bugs, support new devices, and add new OS versions without disrupting development.

VrApi now presents the core minimal API for VR rendering. System-level functionality not necessary for VR rendering has been moved to a VrAppSupport/SystemUtils library. This library primarily deals with loading, and with receiving events from the Universal Menu.

Various OpenGL objects may now be explicitly passed to the VrApi. In this case, functions such as vrapi_EnterVrMode and vrapi_SubmitFrame do not need to be called from a thread with a specific OpenGL context current.

All native applications are now built and developed using Gradle and Android Studio instead of ANT and Eclipse. It is important to note that while the command-line Gradle build path is mature, Android Studio support for native development should still be considered experimental. Feedback on our [developer forums](https://forums.oculus.com/developer) is appreciated!

## Important Change to SystemActivities

The VrApi implementation is now deployed as part of SystemActivities, which is automatically updated. When updating to the latest SDK, **it is important to make sure the device is online to allow the SystemActivities to be automatically updated**. If for some reason the SystemActivities is not up to date when launching a new application, you may get the message "Oculus updates needed." **To allow the application to run, the SystemActivities must be updated.**

If the auto-update function has not delivered the latest SystemActivities to your device, please ensure that you are connected to a working Wi-Fi network. It may take up to 24 hours for the update to trigger, so please be patient. If your development schedule requires a timely update, you may download the SystemActivities APK [from this location](https://s3.amazonaws.com/o.oculuscdn.com/staging/SystemActivities-P4-119024-FB-16656924.apk) as temporary relief during this transition period. Future updates should always be processed by the automatic update system on the Gear VR platform.

## New Features

* VrApi now dynamically loads from a separate APK.
* Various OpenGL objects may now be explicitly passed to VrApi, lifting some threading restrictions.
* Added support for Gradle and experimental support for Android Studio.
* Added support for the Samsung Galaxy S6 Edge+ and Note 5.
* TimeWarp Debug Graph may now be toggled on and off during runtime via VrApi Frame flags.


## API Changes

* vrapi\_Initialize now returns an ovrInitializeStatus.
* vrapi\_GetHmdInfo has been replaced with vrapi\_GetSystemPropertyInt and vrapi\_GetSystemPropertyFloat.
* ovr\_DeviceIsDocked, ovr\_HeadsetIsMounted, ovr\_GetPowerLevelStateThrottled and ovr\_GetPowerLevelStateMinimum have been replaced with vrapi\_GetSystemStatusInt and vrapi\_GetSystemStatusFloat.
* Various functions from VrApi\_Android.h have been moved to the VrAppSupport/SystemUtils library.
* Various performance metrics can now be queried through vrapi\_GetSystemStatusInt and vrapi\_GetSystemStatusFloat.


## Bug Fixes

* Fixed reorient on mount.
* Fixed spurious incorrect long-press event after a short-press plus a long frame.
* Fixed invalid input clock levels resulting in dynamic clock frequency mode.

