---
title: 1.5 Release Notes
---
This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Mobile SDK.

## 1.5.0

## Overview of Major Changes

This version adds support for the Samsung Gear VR Controller.

For details on migrating to Mobile SDK 1.5.0 from previous versions, see [Migrating to Mobile SDK 1.5.0](/documentation/mobilesdk/latest/concepts/mobile-native-migration/#mobile-native-migration-1-5-0 "This section is intended to help you upgrade from the Oculus Mobile SDK version 1.0.4 to 1.5.0.").

Note: With release 1.5.0, the Mobile SDK versioning scheme has changed to MAJOR.MINOR.PATCH.## New Features

* Added support for Gear VR Controller. For more information, see [VrApi Input API](/documentation/mobilesdk/latest/concepts/mobile-vrapi-input-api/ "This document describes using the VrApi Input API.").
* Added VrController sample illustrating VrApi Input API.
## API Changes

* Added VrApi Input API for Gear VR Controller and Gear VR headset. For more information, see VrApi Input API.
* Added ovrFrameLayerFlags flag for clipping fragments outside the layer's TextureRect: VRAPI\_FRAME\_LAYER\_FLAG\_CLIP\_TO\_TEXTURE\_RECT.
* Removed deprecated ovrLayerType.
* Removed deprecated ovrFrameFlags.
