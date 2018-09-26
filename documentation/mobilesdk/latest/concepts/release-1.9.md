---
title: 1.9 Release Notes
---

This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Mobile SDK.

## 1.9.0

This release provides support for a new frame submission path which allows for new layer types such as Cylinder, Cube, and Equirect, enables you to specify a user-defined tracking transform, and adds support for a new performance API.

FBX Converter has been removed from the SDK.

For additional information, see [Migrating to Mobile SDK 1.9.0](/documentation/mobilesdk/latest/concepts/mobile-native-migration/#unique_1124688052).

## New Features

* The Android NDK build version has changed to r15c.


## API Changes

* Added a new frame submission API which supports flexible layer lists and only requires a single fence for signaling frame completion.
* Added a new layer API which supports the following layer types: Projection, Cylinder, Cube, and Equirect.
* Added a new performance API for specifying clock levels, application performance threads, and extra latency mode setting.
* Added a new tracking transform API which allows the application to specify the space that tracked poses are reported in, i.e., Floor Level or Eye Level. The default tracking transform is Eye Level.
* Head Model Parameters are no longer provided on the API. Since the VrApi runtime is responsible for applying the head model, applications should no longer do so. The new tracking transform API can be used to achieve the desired Floor or Eye Level space.
* MinimumVsyncs was renamed to SwapInterval.
* Marked vrapi\_RecenterInputPose as deprecated.
* Removed VRAPI\_SYS\_STATUS\_HEADPHONES\_PLUGGED\_IN, VRAPI\_SYS\_UI\_GLOBAL\_MENU, and VRAPI\_SYS\_STATUS\_THROTTLED2 from API.


## Bug Fixes

* Fixed bug in VrAppFramework where MemBufferT took ownership of a buffer allocated with malloc and freed the buffer using delete[].


## Known Issues

* The 1.7.0 SDK changed how head poses were reported. Before 1.7.0, applications were expected to apply a head model if necessary. With 1.7.0, head poses were returned with the head model already applied, but also with a pose y position relative to the floor instead of relative to the nominal eye height. With 1.9.0, head poses are reported with a head model applied, but the default space they are reported in is again relative to nominal eye height. The space that poses are reported in can be changed with vrapi\_{Get/Set}TrackingTransform().

