---
title: 1.22 Unity Sample Framework
---
This version of the Oculus Sample Framework for Unity pulls in the most recent Avatar SDK and Utilities for Unity versions. Importing the Avatar SDK and Utilities for Unity separately is not required. It is compatible with Unity 5.4 and later - please check [Compatibility and Version Requirements](/documentation/unity/latest/concepts/unity-req/ "This guide describes Unity Editor version recommendations and system requirements.") for up-to-date Unity version recommendations.

The Sample Framework is also available from the Unity Asset Store.

## New Features

* Added a new sample that demonstrates a variety of teleport and locomotion behaviors using an architecture that can be extended to fit various designs. This sample supports switching between any combination of teleports and linear motion at run time.
**Known Issues**

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
	
