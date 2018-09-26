---
title: Changes in Version 1.16.x
---



## New Features for 1.16.x

* Mixed Reality Capture - The Oculus SDK now supports mixed reality capture. Mixed reality capture places real-world objects in VR. In other words, it mixes images from the real world with the virtual one. Read more about mixed reality capture in the [setup](https://support.oculus.com/guides/rift/latest/concepts/mr-intro/) and [integration](/documentation/pcsdk/latest/concepts/dg-mrc/ "Mixed reality capture places real-world people and objects in VR. This guide will review how to add support for mixed reality capture in your native Rift app.") guides. 


## API Changes for 1.16.x

* There are no breaking changes to version 1.16.x. 


## Known SDK Issues

The following are known issues:

* Recentering a mixed reality capture application will corrupt the camera pose when using a static camera. As a temporary workaround, attach a VR Object to your camera (e.g., by using a third Touch), and it will recenter normally.
* If you encounter intermittent tracking issues, remove the batteries from any Engineering Sample Oculus Remotes that you paired with your headset and contact Developer Relations for replacement remotes.
* If you bypass the shim and communicate with the DLL directly, without specifying a version to ovr\_Initialize, the DLL has no way of knowing the SDK version with which the application was built. This can result in unpredictable or erratic behavior which might cause the application to crash.
* If you are running your application from the Unity Editor and you press the controller's home button to return to Oculus Home, you will be prompted to close the application. If you select OK, Unity might remain in a state where it is running, but will never get focus. To work around this, restart Unity.

