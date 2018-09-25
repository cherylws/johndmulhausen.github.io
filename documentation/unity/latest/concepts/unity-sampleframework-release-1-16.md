---
title: 1.16 Unity Sample Framework
---
## 1.16.0-beta

This version of the Oculus Sample Framework for Unity 5 pulls in the most recent Avatar SDK and Utilities for Unity versions. Importing the Avatar SDK and Utilities for Unity 5 separately is not required. It is compatible with Unity 5.4 and up - please check [Compatibility and Version Requirements](/documentation/unity/latest/concepts/unity-req/ "This guide describes Unity Editor version recommendations and system requirements.") for up-to-date Unity version recommendations.

For complete instructions on downloading and using the Sample Framework, see [Unity Sample Framework](/documentation/unity/latest/concepts/unity-sample-framework/ "The Oculus Unity Sample Framework provides sample scenes and guidelines for common VR-specific features such as hand presence with Oculus Touch, crosshairs, driving, hybrid mono rendering, and video rendering to a 2D textured quad.") in our developer documentation.

## Unity Sample Framework now available through Asset Store

We now offer the Unity Sample Framework through the Unity Asset Store [here](https://www.assetstore.unity3d.com/en/#!/content/82503) in addition to our Downloads page. The Oculus Integration, also available from the Asset Store [here](https://www.assetstore.unity3d.com/en/#!/content/82022), provides several unityPackages in a single download, including our Utilities for Unity, Oculus Platform SDK Unity plugin, Oculus Avatar SDK Unity Plugin, and Oculus Native Spatializer Plugin.

**New Features**

* Added MRCTest scene illustrating mixed reality capture to Assets/SampleScenes/MixedRealityCapture/.
**Known Issues**

* Building the Sample Framework project for mobile using Unity 5.6 creates an APK that immediately crashes. The APK is available through the Gallery section of the Oculus Store.
* Sample Framework Android builds use a custom manifest and are not visible from Applications, and cannot be launched from Oculus Home or the Android Application Launcher. To launch: 
	1. Install the APK to your phone.
	2. Open **Settings** > **Applications** > **Application Manager** > **Gear VR Service**.
	3. Select **Storage**.
	4. Select **Manage Storage**.
	5. Toggle **Add icon to app list to On**.
	6. Close **Settings**.
	7. Open **Apps**.
	8. Select **Gear VR Service**.
	9. Select **Oculus Sample Framework** to launch.
	
