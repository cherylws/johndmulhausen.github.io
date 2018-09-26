---
title: 1.24 Unity Sample Framework
---



This version of the Oculus Sample Framework for Unity pulls in the most recent Avatar SDK and Utilities for Unity versions. Importing the Avatar SDK and Utilities for Unity separately is not required. It is compatible with Unity 5.4 and later - please check [Compatibility and Version Requirements](/documentation/unity/latest/concepts/unity-req/) for up-to-date Unity version recommendations.

The Sample Framework is also available from the Unity Asset Store.

## Bug Fixes

* Fixed compatibility issue with the Avatars SDK and certain versions of the Unity Editor (Unity 2017.2 and up).
* Updates to the Android Manifest settings to support the latest mobile APIs.


**Known Issues**

* In versions earlier than 1.181., layers of the UI Overlay sample may remain visible after exiting the scene with the Sample Framework UI. 
* Building the Sample Framework project for mobile using Unity 5.6 creates an APK that immediately crashes.
* Sample Framework Android builds use a custom manifest and are not visible from Applications, and cannot be launched from Oculus Home or the Android Application Launcher. To launch: 
	1. Install the APK to your phone.
	2. Open **Settings** &gt; **Applications** &gt; **Application Manager** &gt; **Gear VR Service**.
	3. Select **Storage**.
	4. Select **Manage Storage**.
	5. Toggle **Add icon to app list to On**.
	6. Close **Settings**.
	7. Open **Apps**.
	8. Select **Gear VR Service**.
	9. Select **Oculus Sample Framework** to launch.
	

