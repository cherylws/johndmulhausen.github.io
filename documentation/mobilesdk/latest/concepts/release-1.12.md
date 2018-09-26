---
title: 1.12 Release Notes
---

This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Mobile SDK.

## 1.12.0

This release provides support for Oculus Go and Samsung Galaxy A8/A8+ (2018) smartphones.

For additional information, see [Migrating to Mobile SDK 1.12.0](/documentation/mobilesdk/latest/concepts/mobile-native-migration/#unique_845979132).

## New Features

The following build tool versions have been changed to:

* Android NDK r16b
* Gradle 4.3.1
* Android Plugin for Gradle 3.0.1
* Android SDK Build-Tools 26.0.2


## API Changes

* Added a mechanism to specify the Foveation Level for the Eye-Buffer SwapChain Textures.
* Added Oculus Go Device Types to the API.
* Added Samsung A-series (2018) Device Types to the API.
* Added a new ovrModeFlags flag, VRAPI\_MODE\_FLAG\_CREATE\_CONTEXT\_NO\_ERROR, to support applications which want to create a no-error GL context.
* VRAPI\_TEXTURE\_SWAPCHAIN\_FULL\_MIP\_CHAIN has been removed. Applications will need to explicitly pass in the number of mipLevels on SwapChain creation.
* Controllers are now affected by the application specified Tracking Transform.
* The SwapChain represented by VRAPI\_DEFAULT\_TEXTURE\_SWAPCHAIN now defaults to white instead of black. This is to support solid color frames of more than just black. The application layerâ€™s ColorScale parameter will determine the solid color used.
* The ovrMobile structure will now always be freed on vrapi\_LeaveVrMode.
* Applications are now required to pass through explicit EGL objects (Display, ShareContext, NativeWindow) to vrapi\_EnterVrMode, otherwise the call will fail.
* VRAPI\_SYS\_PROP\_BACK\_BUTTON\_DOUBLETAP\_TIME has been removed. If applications implement double-tap logic, they can still detect this by checking if the time is less than the VRAPI\_SYS\_PROP\_BACK\_BUTTON\_SHORTPRESS\_TIME.


## Bug Fixes

* Fixed a bug in VrSamples where incorrect texture target was specified for GL\_TEXTURE\_BORDER\_COLOR when multi-view was enabled.
* Fixed the “ndk-build not found” error in ovrbuild.py script when building solely from Android Studio.


## Known Issues

* There are no known issues in this release. 

