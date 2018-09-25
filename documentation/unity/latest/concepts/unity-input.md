---
title: Input
---
This guide describes Unity input features supported by the Oculus integration.

## Oculus Touch

We have provided several resources and samples to help get you started using Touch with Rift. 

**OVRInput**, our unified input API for interacting with Touch, is included with our Utilities for Unity package. See [OVRInput](/documentation/unity/latest/concepts/unity-ovrinput/#unity-ovrinput "OVRInput exposes a unified input API for multiple controller types.") for more information.

The **Oculus Avatar SDK**, includes a Unity package to assist developers with implementing first-person hand presence for the Rift and Touch controllers. It includes avatar hand and body assets viewable by other users in social applications for Rift and Gear VR. The first-person hand models and third-person hand and body models supported by the Avatar SDK automatically pull the avatar configuration choices the user has made in Oculus Home to provide a consistent sense of identity across applications. The SDK includes a Unity package with scripts, prefabs, art assets, and sample scenes. For more information, see our [Avatar SDK Developer Guide](/documentation/avatarsdk/latest/concepts/avatars-gsg-intro/).

Our **Unity Sample Framework** includes samples demonstrating important Touch functionality. For example, the AvatarWithGrab sample uses the Avatar SDK and the scripts OVRGrabber and OVRGrabbable to add the ability to pick up and throw objects in the scene to the Avatar hand assets. The DistanceGrab sample demonstrates a method for interacting with and grasping distant objects in a scene. See [Unity Sample Framework](/documentation/unity/latest/concepts/unity-sample-framework/ "The Oculus Unity Sample Framework provides sample scenes and guidelines for common VR-specific features such as hand presence with Oculus Touch, crosshairs, driving, hybrid mono rendering, and video rendering to a 2D textured quad.") for more information.

Oculus Utilities for Unity, Avatar SDK, and Unity Sample Framework are available with our [Oculus Integration](https://www.assetstore.unity3d.com/en/#!/content/82022) on the Unity Asset Store, or from our [Downloads page](/downloads/).

Touch may be used to emulate Microsoft XInput API gamepads without any code changes. However, you must account for the missing logical and ergonomic equivalences between the two types of controllers. For more information, see [Emulating Gamepad Input with Touch](/documentation/pcsdk/latest/concepts/dg-gamepad-emulation-touch/) in our PC SDK Developer Guide.

For more useful recommendations, have a look at the [Oculus Developer Blog](/blog/) for several relevant posts.

* **[OVRInput](/documentation/unity/latest/concepts/unity-ovrinput/#unity-ovrinput)**  
OVRInput exposes a unified input API for multiple controller types.
* **[OVRBoundary Guardian System API](/documentation/unity/latest/concepts/unity-ovrboundary/)**  
OVRBoundary exposes an API for interacting with the Rift Guardian System for Touch.
* **[OVRHaptics for Oculus Touch](/documentation/unity/latest/concepts/unity-ovrhaptics/)**  
This guide reviews OVRHaptics and OVRHapticsClip, two C# scripts that programmatically control haptics feedback for Touch. 
