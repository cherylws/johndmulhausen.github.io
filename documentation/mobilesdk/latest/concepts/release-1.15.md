---
title: 1.15 Release Notes
---

This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Mobile SDK.

## 1.15.0

For additional information, see [Migrating to Mobile SDK 1.15.0](/documentation/mobilesdk/latest/concepts/mobile-native-migration/#mobile-native-migration-1-15-0).

## New Features

The following new features can be found in 1.15:

* Support for the Samsung Galaxy A8 Star smartphone.


* Android Build Tools have been upgraded to the March 2018 release.




## API Changes

* Added Samsung Galaxy A8 Star Device Type to the API.


* Added a new entry point, vrapi\_SetTextureSwapChain3, for creating a texture SwapChain by passing a platform specific texture format instead of the ovrTextureFormat type. The available formats may be queried by passing VRAPI\_SYS\_PROP\_SUPPORTED\_SWAPCHAIN\_FORMATS to vrapi\_GetSystemPropertyInt64Array.


* vrapi\_SetTextureSwapChainHandle has been marked deprecated and should no longer be used.


* Deprecated ovrFrameLayerFlags flag, VRAPI\_FRAME\_LAYER\_FLAG\_WRITE\_ALPHA, and corresponding ovrFrameLayerBlend blend modes, VRAPI\_FRAME\_LAYER\_BLEND\_DST\_ALPHA and VRAPI\_FRAME\_LAYER\_BLEND\_ONE\_MINUS\_DST\_ALPHA, have been removed from the API.


* Added new entry points for creating and obtaining a cross-process friendly Android Surface SwapChain, vrapi\_CreateAndroidSurfaceSwapChain and vrapi\_GetTextureSwapChainAndroidSurface.


* ovrTextureType VRAPI\_TEXTURE\_TYPE\_2D\_EXTERNAL and corresponding ovrLayerHeader2 SurfaceTextureObject are marked deprecated and should no longer be used. Instead, the application should use the new cross-process friendly Android Surface texture SwapChain creation method, vrapi\_CreateAndroidSurfaceSwapChain.


* ovrSystemProperty VRAPI\_SYS\_PROP\_BACK\_BUTTON\_SHORTPRESS\_TIME has been removed as it should no longer be necessary when using the Input API.


* Emulation of the remote controllers as a headset now defaults to false for applications built with 1.15.0 and higher, as applications are expected to use the Input API for querying remote and headset input. To maintain the old behavior, pass false to vrapi\_SetRemoteEmulation.


* Remote controllers will no longer send Java input events when headset emulation is off. This behavior can be changed by setting the ovrProperty VRAPI\_BLOCK\_REMOTE\_BUTTONS\_WHEN\_NOT\_EMULATING\_HMT to true.


* When a back button press is detected, the Input API now reports the back button as down for an entire frame instead of only for the next input query. This behavior can be changed by setting the ovrProperty VRAPI\_LATCH\_BACK\_BUTTON\_ENTIRE\_FRAME to false.




## Bug Fixes

* For Oculus Go, TrackpadSizeX and TrackpadSizeY now correctly return the size in millimeters instead of tenths of millimeters for applications built with 1.15 and above.


* Gear VR devices that have a screen size other than 2560x1440 now report TrackpadPosition based on the actual screen size.




## Known Issues

* There are no known issues in this release.



