---
title: Compatibility and Version Requirements
---
This guide describes Unity Editor version recommendations and system requirements.

## Supported Unity Versions

We recommend using Unity version 2017.4.11f1 for all Oculus development.

If you must use a different version, our tests show that the following builds have the best performance and least number of issues for that version.

* 5.6.6f2* (Does not support Dash)
* 2017.1.4f1*
* 2017.2.3p4
* **2017.4.11f1 (Most recommended)**
* 2018.1.9f2*
* 2018.2.7f1
 *No longer supported by Unity. Our [Troubleshooting and Known Issues](/documentation/unity/latest/concepts/unity-troubleshooting/ "This section outlines some currently known issues with the Oculus Unity Integration and the Oculus Utilities for Unity.") page describes known issues with specific versions on Unity.

All Unity versions 5.1 and later ship with the Oculus OVRPlugin, providing built-in support for Rift, Oculus Go, and Samsung Gear VR.

The optional Oculus Utilities for Unity package offers additional developer resources, and includes the latest version of OVRPlugin. When you import Utilities for Unity into a project, if the OVRPlugin version included with the Utilities is later than the version built into your editor, a pop-up dialog will give you the option to update it in your project. We always recommend using the latest available OVRPlugin version. For more information, see [OVRPlugin](/documentation/unity/latest/concepts/unity-utilities-overview/#unity-utilities-ovrplugin "OVRPlugin provides Rift and mobile support to the Unity Editor.").

Legacy support is available for Unity 4 - see our [Unity 4.x Legacy Integration Developer Guide](/documentation/unity/latest/concepts/book-integration-unity/ "The Unity Legacy Integration Developer Guide is designed to get you started with creating great VR experiences in Unity 4.") for more information.

For complete details Oculus SDK or Integration version compatibility with Unity, see [Unity-SDK Version Compatibility](/documentation/unity/latest/concepts/unity-sdk-version-compatibility/ "This reference describes the relationship between Unity versions, Oculus PC and Mobile SDKs, and Oculus Unity plugin and Utilities packages.").

## System and Hardware Requirements

To verify that you are using supported hardware, please review the relevant PC or mobile setup documentation:

* PC SDK: [Getting Started with the SDK](/documentation/pcsdk/latest/concepts/gsg-intro/)
* Mobile SDK: [System and Hardware Requirements](/documentation/mobilesdk/latest/concepts/mobile-reqs/)
## OS Compatibility

* **Windows**: Windows 7, 8, 10
* **Mac**: OS X Yosemite, El Capitan, Sierra
OS X development requires the Oculus Rift Runtime for OS X, available from our [Downloads page](/downloads/). Note that runtime support for OS X is legacy only. It does not support consumer versions of Rift.

## Unity Personal and Professional Licenses

The Unity Personal and Professional licenses both provide built-in Rift support. Mobile developers using the Unity Free license receive basic Android support automatically. Mobile developers using a Professional license require an Android Pro Unity license.

For more information, see [License Comparisons](http://unity3d.com/unity/licenses) in Unityâ€™s documentation.

## Controllers

You may wish to have a controller for development or to use with the supplied demo applications. Available controllers include the Oculus Touch or Xbox 360 controller for Rift, and the Gear VR Controller and Oculus Go Controller for mobile development.

