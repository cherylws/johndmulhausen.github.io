---
title: Other Native Libraries
---
This guide describes other native libraries included with the Mobile SDK.

## Overview

Additional supplemental libraries included with this SDK include:

* VrAppSupport
* LibOVRKernel
## VrAppSupport

The **VrGui library** contains functionality for a fully 3D UI implemented as a scene graph. Each object in the scene graph can be functionally extended using components. This library has dependencies on VrAppFramework and must be used in conjunction with it. See the CinemaSDK, Oculus360PhotosSDK and Oculus360Videos SDKs for examples.

The **VrLocale library** is a wrapper for accessing localized string tables. The wrapper allows for custom string tables to be used seamlessly with Androidâ€™s own string tables. This is useful when localized content is not embedded in the application package itself. This library depends on VrAppFramework.

The **VrModel library** implements functions for loading 3D models in the .ovrScene format. These models can be exported from .fbx files using the FbxConverter utility (see FBXConverter). This library depends on rendering functionality included in VrAppFramework.

The **VrSound library** implements a simple wrapper for playing sounds using the android.media.SoundPool class. This library does not provide low latency or 3D positional audio and is only suitable for playing simple UI sound effects.

## LibOVRKernel

LibOVRKernel is a reduced set of libraries primarily of low-level functions, containers, and mathematical operations. 

It is an integral part of VrAppFramework, but may generally be disregarded by developers using VrApi. 

