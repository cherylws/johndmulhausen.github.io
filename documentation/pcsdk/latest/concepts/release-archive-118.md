---
title: Changes in Version 1.18.x
---



## New Features for 1.18.x

* PC SDK 1.18 adds two Vulkan-specific functions that **must be used** by an application using the Vulkan API. Note that both NVIDIA and AMD released drivers very recently which address Vulkan issues. See API Changes below for more information.


## API Changes

* Added the Vulkan-specific functions ovr\_GetInstanceExtensionsVk and ovr\_GetDeviceExtensionsVk, which return a list of strings that identify the Vulkan extensions which must be enabled in order for the Oculus runtime to support Vulkan-based applications. See OVR\_CAPI\_Vk.h for documentation and code samples.


## Known SDK Issues

* Recentering a mixed reality capture application will corrupt the camera pose when using a static camera. As a temporary workaround, attach a VR Object to your camera (e.g., by using a third Touch), and it will recenter normally.
* If you encounter intermittent tracking issues, remove the batteries from any Engineering Sample Oculus Remotes that you paired with your headset and contact Developer Relations for replacement remotes.
* If you bypass the shim and communicate with the DLL directly, without specifying a version to ovr\_Initialize, the DLL has no way of knowing the SDK version with which the application was built. This can result in unpredictable or erratic behavior which might cause the application to crash.
* If you are running your application from the Unity Editor and you press the controller's home button to return to Oculus Home, you will be prompted to close the application. If you select OK, Unity might remain in a state where it is running, but will never get focus. To work around this, restart Unity.

