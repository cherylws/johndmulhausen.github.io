---
title: 0.5 Mobile Unity Integration Release Notes
---

This document provides an overview of new features, improvements, and fixes included in the Oculus Unity Integration that shipped with version 0.5 of the Oculus Mobile SDK.

## Mobile Unity Integration 0.5.1

## Overview of Major Changes

The most significant change in 0.5.1 is to System Activities event handling in Unity. The 0.5.0 code for handling System Activities events in Unity was doing heap allocations each frame. Though this was not a leak, it would cause garbage collection to trigger much more frequently. Even in simple applications, garbage collection routinely takes 1 to 2 milliseconds. In applications that were already close to dropping below 60 Hz, the increased garbage collection frequency could cause notable performance drops. The event handling now uses a single buffer allocated at start up.

As with Mobile SDK v 0.5.0, Unity developers using this SDK version must install the Oculus Runtime for Windows or OS X. This requirement will be addressed in a future release of the SDK.

## Bug Fixes

* Rework System Activities Event handling to prevent any per-frame allocations that could trigger Garbage Collector.


## Known Issues

* For use with the Mobile SDK, we recommend Unity versions 4.6.3. The Mobile SDK is compatible with Unity 5.0.1p2, which addresses a problem with OpenGL ES 3.0, but there is still a known Android ION memory leak. Please check back for updates.


## Mobile Unity Integration 0.5.0

## Overview of Major Changes

The Mobile Unity Integration is now synced with the Oculus PC SDK 0.5.0.1 Beta. Please ensure you have installed the corresponding 0.5.0.1 Oculus runtime; it can be found at the following location: [https://developer.oculus.com/downloads/](/downloads/)

VrPlatform entitlement checking is now disabled by default in Unity; handling for native development is unchanged. If your application requires this feature, please refer to the Mobile SDK Documentation for information on how to enable entitlement checking.

## New Features

* Synced with the Oculus PC SDK 0.5.0.1 Beta.
* VrPlatform entitlement checking is now disabled by default.


## Bug Fixes

* Health and Safety Warning no longer displays in editor Play Mode if a DK2 is not attached.


## Known Issues

* For use with the Mobile SDK, we recommend Unity versions 4.6.3, which includes Android 5.0 - Lollipop support as well as important Android bug fixes. While the Mobile SDK is compatible with Unity 5.0.0p2 and higher, several issues are still known to exist, including an Android ION memory leak and compatibility issues with OpenGL ES 3.0. Please check back for updates.


## Mobile Unity Integration 0.5.0

## Overview of Major Changes

The Mobile Unity Integration is now synced with the Oculus PC SDK 0.5.0.1 Beta. Please ensure you have installed the corresponding 0.5.0.1 Oculus runtime; it can be found at the following location: [https://developer.oculus.com/downloads/](/downloads/)

VrPlatform entitlement checking is now disabled by default in Unity; handling for native development is unchanged. If your application requires this feature, please refer to the Mobile SDK Documentation for information on how to enable entitlement checking.

## New Features

* Synced with the Oculus PC SDK 0.5.0.1 Beta.
* VrPlatform entitlement checking is now disabled by default.


## Bug Fixes

* Health and Safety Warning no longer displays in editor Play Mode if a DK2 is not attached.


## Known Issues

* For use with the Mobile SDK, we recommend Unity versions 4.6.3, which includes Android 5.0 - Lollipop support as well as important Android bug fixes. While the Mobile SDK is compatible with Unity 5.0.0p2 and higher, several issues are still known to exist, including an Android ION memory leak and compatibility issues with OpenGL ES 3.0. Please check back for updates.

