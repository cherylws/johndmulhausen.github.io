---
title: "Oculus Go and Gear VR: Multi-View"
---
Multi-View is an advanced rendering feature for Oculus Go and Gear VR. If your application is CPU-bound, we strongly recommend using Multi-View to improve performance.

In typical OpenGL stereo rendering, each eye buffer must be rendered in sequence, doubling application and driver overhead. When Multi-View is enabled, objects are rendered once to the left eye buffer, then duplicated to the right buffer automatically with appropriate modifications for vertex position and view-dependent variables such as reflection.

For Gear VR, Multi-View is supported on Note5, S6, S7, S8, and S9 (and later) phones using ARM Exynos processors and running Android M or N. It is also supported on S7, S8, and S9 (and later) phones using Qualcomm processors and running Android N.

Oculus Go and all supported Samsung phones support Multi-View with OpenGL ES 2.

Oculus Go, S8, and S9 phones also support Multi-View with OpenGL ES 3.1.

Although Multi-View can substantially reduce CPU overhead, keep in mind that applications submitted to the Oculus Store must maintain minimum frame rate per our requirements, even on devices that do not support Multi-View.

## Enabling Multi-View

Open **Edit** > **Project Settings** > **Engine** > **Rendering**. In the VR section, enable **Mobile Multi-View** and **Mobile Multi-View Direct** :

![](/images/documentation-unreal-latest-concepts-unreal-multi-view-0.png)  
Note: The Mobile Multi-View Direct option reduces the number of full-screen copies that must be rendered. In most cases, it provides a substantial reduction in GPU overhead. If you plan to use Multi-View, it is strongly recommended that you use Mobile Multi-View Direct. **Using Multi-View without the direct option is not guaranteed to work properly, and is not supported.**For Exynos devices, verify that **Support OpenGL ES2** is checked in the **Build** section in **Platforms** > **Android**, and that **Support OpenGL ES3** is **not** selected.

## Console Window Output

When Multi-View is enabled, the console output, such as debug messages and **stat** command output, cannot be displayed directly on the screen. To address this, select the checkbox "Debug Canvas in Layer" to display the output in a cylindrical layer around the player. This improves the non-Multi-View experience too, but is required for Multi-View

![](/images/documentation-unreal-latest-concepts-unreal-multi-view-1.png)  
