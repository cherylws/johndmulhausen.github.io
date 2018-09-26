---
title: 1.11 Unity Sample Framework
---



## 1.11.0

The Oculus Unity Sample Framework assists developers in implementing Unity applications by providing sample scenes and guidelines for common VR-specific features such as hand presence, crosshairs, driving, and first-person movement.

This download includes a Unity Package of the Sample Framework. VR applications of the Sample Framework are also available for the Oculus Rift from our [Downloads page](/downloads/), and for the Samsung Gear VR from the Gallery section of the Oculus Store.

This version of the Oculus Sample Framework for Unity 5 pulls in the most recent Avatar SDK and Utilities for Unity versions. Importing the Avatar SDK and Utilities for Unity 5 separately is not required. It is compatible with Unity 5.4 and up - please check [Compatibility and Version Requirements](/documentation/unity/latest/concepts/unity-req/) for up-to-date Unity version recommendations.

For complete instructions on downloading and using the Sample Framework, see [Unity Sample Framework](/documentation/unity/latest/concepts/unity-sample-framework/) in our developer documentation.

**New Features**

* Added Hands category with three new scenes.
	+ AvatarWithGrab uses the Unity Avatar SDK and the Utilities for Unity scripts OVRGrabber and OVRGrabbable to illustrate hands presence with Touch. Pick up and throw blocks from a table using the Touch grip buttons. 
	+ CustomControllers is a simple sample displaying tracked and animated Touch models in a scene.
	+ CustomHands uses low-resolution custom hand models and the Utilities for Unity scripts OVRGrabber and OVRGrabbable to illustrate hands presence with Touch. Pick up and throw blocks from a table using the Touch grip buttons. May be used as a reference for implementing your own hand models.
	
* Added Touch support.
* The Sample Framework now pulls in the Avatar SDK, which is also available separately from our [Downloads page](https://developer.oculus.com/downloads/).
* The project download now ships as a unitypackage rather than a zipped Unity project.


**Known Issues**

* In Oculus Rift builds, Oculus Remote support is currently limited to opening and closing the menu system.
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
	

