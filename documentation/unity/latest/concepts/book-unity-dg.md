---
title: Unity Developer Guide
---

Welcome to the Oculus Unity Developer Guide.

This guide describes development using Unity's first-party Oculus support, and the contents and features of the Oculus Utilities for Unity package.

## Unity VR Support

All Unity versions 5.1 and later ship with a bundled version of the Oculus OVRPlugin that provides built-in support for Rift, Oculus Go, and Samsung Gear VR support. Oculus support is enabled by checking `Virtual Reality Supported` in the `Other Settings &gt; Configuration` tab of `Player Settings`.

When Unity virtual reality support is enabled, any camera with no render texture is automatically rendered in stereo to your device. Positional and head tracking are automatically applied to your camera, overriding your camera’s transform.

Unity applies head tracking to the VR camera within the reference frame of the camera's local pose when the application starts. If you are using OVRCameraRig, that reference frame is defined by the TrackingSpace GameObject, which is the parent of the CenterEyeAnchor GameObject that has the Camera component.

The Unity Game View does not apply lens distortion. The image corresponds to the left eye buffer and uses simple pan-and-scan logic to correct the aspect ratio.

You may update the Oculus OVRPlugin version of your Unity Editor at any time by installing the most recent Utilities for Unity package for access to the latest features. For more information, see [OVRPlugin](/documentation/unity/latest/concepts/unity-utilities-overview/#unity-utilities-ovrplugin).

For more information and instructions for using Unity’s VR support, see the [Virtual Reality section](http://docs.unity3d.com/Manual/VROverview.html) of the Unity Manual. 

* **[Oculus Utilities for Unity](/documentation/unity/latest/concepts/unity-utilities-overview/#unity-utilities-overview)**  
This section provides an overview of the Utilities package, including its directory structure, the supplied prefabs, and several key C# scripts.
* **[Input](/documentation/unity/latest/concepts/unity-input/)**  
This guide describes Unity input features supported by the Oculus integration.
* **[Advanced Rendering Features](/documentation/unity/latest/concepts/unity-rendering/)**  
This guide describes advanced rendering features that can assist performance.
* **[Mobile Development](/documentation/unity/latest/concepts/unity-mobile-performance-intro/#unity-mobile-performance-intro)**  
This section provides guidelines to help your Unity app perform well with Samsung Gear VR. 
* **[Unity Audio](/documentation/unity/latest/concepts/unity-audio/)**  
This guide describes guidelines and resources for creating a compelling VR audio experience in Unity.
* **[Oculus Dash in Unity](/documentation/unity/latest/concepts/unity-dash/)**  
This guide describes how to add Oculus Dash support to Unity applications.
* **[Application Lifecycle Handling](/documentation/unity/latest/concepts/unity-lifecycle/)**  
This guide describes the process to handle the lifecycle for applications built in Unity.
* **[Unity Mixed Reality Capture](/documentation/unity/latest/concepts/unity-mrc/)**  
This guide describes how to add and configure mixed reality capture support for your Unity application. Mixed reality capture is supported for Rift applications only.
* **[Cubemap Screenshots](/documentation/unity/latest/concepts/unity-cubemap/)**  
The OVR Screenshot Wizard allows you to easily export a 360 screenshot in cubemap format.
* **[Best Practices for Rift and Mobile](/documentation/unity/latest/concepts/unity-best-practices-intro/)**  
This section describes performance targets and offers recommendations for developers. 
* **[Testing and Performance Analysis](/documentation/unity/latest/concepts/unity-perf/#unity-perf)**  
In this guide, weâ€™ll review baseline targets, recommendations, tools, resources, and common workflows for performance analysis and bug squashing for Unity VR applications.
* **[Troubleshooting and Known Issues](/documentation/unity/latest/concepts/unity-troubleshooting/)**  
This section outlines some currently known issues with the Oculus Unity Integration and the Oculus Utilities for Unity.

