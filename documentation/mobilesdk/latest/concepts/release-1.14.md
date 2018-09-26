---
title: 1.14 Release Notes
---

This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Mobile SDK.

## 1.14.0

For additional information, see [Migrating to Mobile SDK 1.14.0](/documentation/mobilesdk/latest/concepts/mobile-native-migration/#mobile-native-migration-1-9-0).

## New Features

The following new features can be found in 1.14:

* Support for the Samsung Galaxy S9 and S9+ smartphones.


* Gamepads are now exposed and enumerated through the input API.


* Opt in ability to combine the controller recenter and headset reorient action. This new behavior provides the most benefit for experiences that are focused in front of the user (for instance, UI-centric applications). Full 360 degree experiences may wish to retain the old behavior if the developer feels it is more intuitive to leave the recenter of the controller independent of the headset reorient.




## API Changes

* vrapi\_Initialize can now return a new error code on failure, VRAPI\_INITIALIZE\_ALREADY\_INITIALIZED.


* Added a mechanism to adjust the display refresh rate for Oculus Go: vrapi\_SetDisplayRefreshRate.


* Added Samsung Galaxy S9 Device Types to the API.


* VRAPI\_FRAME\_FLAG\_INHIBIT\_SRGB\_FRAMEBUFFER has been deprecated in favor of using the per-layer flag VRAPI\_FRAME\_LAYER\_FLAG\_INHIBIT\_SRGB\_FRAMEBUFFER.


* Input API now exposes and enumerates Gamepads.


* vrapi\_ReturnToHome has been removed.


* vrapi\_ShowSystemUIWithExtra is marked deprecated and should no longer be used.


* VRAPI\_REORIENT\_HMD\_ON\_CONTROLLER\_RECENTER property has been provided to allow apps the ability to opt into a behavior that combines the controller recenter action with reorienting the headset. To enable this, set the property to 1 using vrapi\_SetPropertyInt. This feature is disabled by default. 


## Bug Fixes

* Removed code path in samples that always forced a maximum screen brightness.


## Known Issues

* There are no known issues in this release. 

