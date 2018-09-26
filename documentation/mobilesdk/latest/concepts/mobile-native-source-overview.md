---
title: Native Source Code
---

This section describes mobile native source code development.

The native SDK provides four basic native libraries:

* **VrApi**: the minimal API for VR;
* **VrAppFramework**: the application framework used by native apps;
* **VrAppSupport**: support for GUI, Locale handling, sound, etc.; 
* **LibOVRKernel**: a low-level Oculus library for containers, mathematical operations, etc.


VrApi provides the minimum required API for rendering scenes in VR. Applications may query VrApi for orientation data, and submit textures to apply distortion, sensor fusion, and compositing. The VrApi Input API allows developers to query the state of connected devices, such as the Gear VR Controller. Developers working with a third-party engine other than Unity or Unreal will use VrApi to integrate the mobile SDK. For detailed information, see [Native Engine Integration](/documentation/mobilesdk/latest/concepts/book-engine-integration/).

The VrAppFramework handles VrApi integration and provides a wrapper around Android activity that manages the Android lifecycle. The VrAppFramework is the basis for several of our samples and first-party applications, including Oculus Video and Oculus 360 Photos. If you are not using Unity, Unreal, or another integration and you would like a basic framework to help get started, we recommend that you have a look. See [Native Application Framework](/documentation/mobilesdk/latest/concepts/book-native-appframework/) for more information.

VrAppSupport and LibOVRKernel provide minimal functionality to applications using VrAppFramework such as GUI, sound, and locale management. See [Other Native Libraries](/documentation/mobilesdk/latest/concepts/mobile-native-other-libraries/) for more information.

The Vr App Interface (part of VrAppFramework) has a clearly-defined lifecycle, which may be found in VrAppFramework/Include/App.h.

LibOVRKernel and VrAppFramework ship with full source as well as pre-built libs and aar files. The VrApi is shipped as a set of public include files, and a pre-built shared library. Providing the VrApi in a separate shared library allows the VrApi implementation to be updated after an application has been released, making it easy to apply hot fixes, implement new optimizations, and add support for new devices without requiring applications to be recompiled with a new SDK. The VrApi is periodically updated automatically to Samsung phones - for release notes, see [System Activities/VrApi Release Notes](/documentation/mobilesdk/latest/concepts/sa-release-archive/). 

See the VrSamples/Native/VrCubeWorld projects for examples of how to integrate VrApi into third party engines as well as how to use VrAppFramework. Please see [Native Samples](/documentation/mobilesdk/latest/concepts/mobile-native-samples/) for more details. 

## Main Components

|        Component        |                                                                                                                                              Description                                                                                                                                              |   Source code folder   |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
|          VrApi          |                                                                                The Virtual Reality API provides a minimal set of entry points for enabling VR rendering in native applications and third-party engines.                                                                                |         VrApi         |
|     VrApi Includes     |                                                                                                                                  Header files for the VrApi library.                                                                                                                                  |     VrApi/Includes     |
|  Application Framework  | Framework and support code for native applications. Includes code for rendering, user interfaces, sound playback, and more. It is not meant to provide the functionality of a full-fledged engine, but it does provide structure and a lot of useful building blocks for building native applications. |   VrAppFramework/Src   |
| VrAppFramework Includes |                                                                                                                              Header files for the VrAppFramework library.                                                                                                                              | VrAppFramework/Include |
|     Native Samples     |                                                                                                                     Sample projects illustrating use of VrApi and VrAppFramework.                                                                                                                     |    VrSamples/Native    |
|      LibOVRKernel      |                                                                                                                                          The Oculus library.                                                                                                                                          |    LibOVRKernel/Src    |
