---
title: 1.18 Unity Sample Framework
---
## 1.18.1

This version of the Oculus Sample Framework for Unity pulls in the most recent Avatar SDK and Utilities for Unity versions. Importing the Avatar SDK and Utilities for Unity separately is not required. It is compatible with Unity 5.4 and later - please check [Compatibility and Version Requirements](/documentation/unity/latest/concepts/unity-req/ "This guide describes Unity Editor version recommendations and system requirements.") for up-to-date Unity version recommendations.

The Sample Framework is also available from the Unity Asset Store. VR builds of the Sample Framework are available for Rift and Gear VR from the Gallery section of the Oculus Store.

**Bug Fixes**

* Fixed bug causing UI Overlay sample layers to remain visible after exiting the scene with the Sample Framework UI.
## 1.18.0

**New Features**

* Added the Distance Grab sample illustrating how to select and grab distant objects using Touch controllers. For more information, see [Distance Grab sample now available in Oculus Unity Sample Framework](https://developer3.oculus.com/blog/distance-grab-sample-now-available-in-oculus-unity-sample-framework/) on our Developer Blog.
* Added Guardian Boundary System sample illustrating use of the OVRBoundary API to interact with the Guardian System.
* Added Input Focus System Overlay sample to illustrate Input Focus and System Overlay handling. A simple application is paused and muted when it loses input focus, and tracked controllers are hidden when a menu VR Compositor Layer is displayed.
## Bug Fixes

* Fixed missing quad layer in OverlayUIDemo.
**Known Issues**

* The mobile Sample Framework APK available through the Gallery is currently out of date. For now, we recommend focusing on the Unity project. 
* Layers of the UI Overlay sample may remain visible after exiting the scene with the Sample Framework UI. Fixed in 1.18.1.
* Building the Sample Framework project for mobile using Unity 5.6 creates an APK that immediately crashes.
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
	
