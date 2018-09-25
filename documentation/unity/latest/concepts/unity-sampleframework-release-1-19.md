---
title: 1.19 Unity Sample Framework
---
## 1.19.0

This version of the Oculus Sample Framework for Unity pulls in the most recent Avatar SDK and Utilities for Unity versions. Importing the Avatar SDK and Utilities for Unity separately is not required. It is compatible with Unity 5.4 and later - please check [Compatibility and Version Requirements](/documentation/unity/latest/concepts/unity-req/ "This guide describes Unity Editor version recommendations and system requirements.") for up-to-date Unity version recommendations.

The Sample Framework is also available from the Unity Asset Store. VR builds of the Sample Framework are available for Rift and Gear VR from the Gallery section of the Oculus Store.

## New Features

* Renamed “Input Focus System Overlay” sample to “Input Focus.” Removed Is System Overlay Present? handling. That flag was removed in our Unity Integration 1.19. 
**Known Issues**

* The mobile Sample Framework APK available through the Gallery is currently out of date. For now, we recommend using the Unity project. 
* In versions earlier than 1.181., layers of the UI Overlay sample may remain visible after exiting the scene with the Sample Framework UI. 
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
	
