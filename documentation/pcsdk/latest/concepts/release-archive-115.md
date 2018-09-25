---
title: Changes in Version 1.15.x
---
## New Features for 1.15.x

* The Oculus SDK now supports [Vulkan](https://www.khronos.org/vulkan/) for rendering. Read about using Vulkan in our [Rendering to the Oculus Rift](/documentation/pcsdk/latest/concepts/dg-render/#dg_render) guide.
## API Changes for 1.15.x

* There are no breaking changes to version 1.15.x. 
## Known SDK Issues

The following are known issues:

* If you encounter intermittent tracking issues, remove the batteries from any Engineering Sample Oculus Remotes that you paired with your headset and contact Developer Relations for replacement remotes.
* If you bypass the shim and communicate with the DLL directly, without specifying a version to ovr\_Initialize, the DLL has no way of knowing the SDK version with which the application was built. This can result in unpredictable or erratic behavior which might cause the application to crash.
* If you are running your application from the Unity Editor and you press the controller's home button to return to Oculus Home, you will be prompted to close the application. If you select OK, Unity might remain in a state where it is running, but will never get focus. To work around this, restart Unity.
