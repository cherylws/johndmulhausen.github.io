---
title: 1.25 Unity Sample Framework
---
This version of the Oculus Sample Framework for Unity pulls in the most recent Avatar SDK and Utilities for Unity versions. Importing the Avatar SDK and Utilities for Unity separately is not required. It is compatible with Unity 5.4 and later - please check [Compatibility and Version Requirements](/documentation/unity/latest/concepts/unity-req/ "This guide describes Unity Editor version recommendations and system requirements.") for up-to-date Unity version recommendations.

The Sample Framework is also available from the Unity Asset Store.

## Integration Changes

* The Oculus Unity packaging structure has changed. When upgrading to 1.25 we recommend deleting your old copy of the Sample Framework and restarting Unity, then adding the 1.25 package. 
**Known Issues**

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
	
* The hybrid mono optimization sample has a skewed display on the right eye in Unity 2018.1.b5 +.
