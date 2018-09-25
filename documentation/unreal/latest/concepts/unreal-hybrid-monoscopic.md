---
title: Oculus Go and Gear VR: Hybrid Monoscopic Rendering
---
Hybrid monoscopic rendering (available in Unreal 4.15 or later) renders objects close to the viewer in stereoscopic 3D, while rendering all objects that lie past a culling plane only once.

## Overview

Enabling hybrid monoscopic rendering can produce performance improvements by drawing many objects only once instead of twice at a slight stereo disparity. In one test scenario, we measured a 25% decrease in rendering times on Epic’s SunTemple sample. In most cases, the visual effect of rendering objects monoscopically with default settings is unnoticeable for typical users.

When hybrid monoscopic rendering feature is enabled, a third monoscopic camera is placed between the left and right cameras on the same plane. In mobile applications, the eye cameras have symmetric frusta, so the monoscopic camera shares the same projection matrix as the stereoscopic cameras.

The UE4 mobile forward renderer then does the following: 

1. Renders non-transparent content with the stereo cameras.
2. Shifts and combines the output to create a monoscopic occlusion mask, which pre-populates the monoscopic depth buffer.
3. Renders non-transparent content with the monoscopic camera.
4. Composites the monoscopic camera’s result into the stereo buffers.
5. Render all transparent content and perform all post processing in stereo.
To separate stereo and mono content, hybrid monoscopic rendering uses a depth buffer. All pixels beyond the culling plane are discarded in the stereo view by clearing the stereo depth buffer to that depth. The monoscopic projection near plane is also initialized at that depth to discard fragments that have already been rendered in stereo.

For additional technical details, see [Hybrid Mono Rendering in UE4 and Unity](/blog/hybrid-mono-rendering-in-ue4-and-unity/) in our Developer Blog.

## Enabling Hybrid Monoscopic Rendering

Open **Edit > Project Settings > Engine > Rendering**. In the VR section, enable Monoscopic Far Field (Experimental).

![](/images/documentation-unreal-latest-concepts-unreal-hybrid-monoscopic-0.png)  
## Culling Plane

When hybrid monoscopic rendering is enabled, a split plane parallel to the z-axis is added to the level, and objects falling on the far side of the plane are rendered using the monoscopic camera. Objects straddling the culling plane are rendered by both the monoscopic and stereoscopic cameras - see **Best Practices** below for more information.

The distance of the culling plane may be configured in **Settings > World Settings > VR > Mono Culling Distance** (default setting is 750.0, or 7.5 meters).

## Console Commands

When hybrid monoscopic rendering is enabled, you may set its mode with the following console command: vr.MonoscopicFarFieldMode [0-4]

Mode

Description

0

Off

1

On (default)

2

Stereo only

3

Stereo only with no culling plane

4

Mono only

## Best Practices

This section describes how to implement and tune hybrid monoscopic rendering. We recommend reading it carefully - the substantial performance improvements this feature provides when properly implemented make it worth spending some time to get it working properly. However, if it is improperly used, it may actually decrease performance.

Due to limitations of the frustum culling algorithm we use to cull meshes, large objects around the scene such as environment cubemaps or skyboxes are still drawn to the stereoscopic cameras that have a close culling plane, even if no pixel of those objects makes it past the far plane. Those draw calls are unnecessary and create bandwidth and vertex costs to the GPU and CPU. 

To prevent unnecessary draw calls in the stereo buffer, we strongly recommend that you identify objects that are further than the culling plane and still render, and force them to render in the monoscopic buffer only. To identify all objects rendered to the stereoscopic cameras, set your level to display objects drawn to the stereoscopic buffer only with the console command vr.MonoscopicFarFieldMode 2. You will only see objects that lie on the near side of the culling plane, like this:

![](/images/documentation-unreal-latest-concepts-unreal-hybrid-monoscopic-1.png)  
Stereo OnlyNext, set your level to display all draw calls to the stereoscopic buffer with the console command vr.MonoscopicFarFieldMode 3. This will display the stereo buffer without culling:

![](/images/documentation-unreal-latest-concepts-unreal-hybrid-monoscopic-2.png)  
Stereo Only with No CullingAny mesh that appears when vr.MonoscopicFarFieldMode is set to 3 but not when it is set to 2 is redundantly rendered and should be set to render in the monoscopic buffer only. In the pictures above, that includes anything visible in the second image that does not appear in the first image. 

Notice in this example the mountains in the scene are drawn to the stereoscopic buffer - this is a typical case. Any very large object that the user is inside of will typically be a candidate for forcing to mono only. 

To force any mesh to render in the monoscopic buffer only, select the mesh and check the **Render in Mono** option under Rendering.

![](/images/documentation-unreal-latest-concepts-unreal-hybrid-monoscopic-3.png)  
Hybrid monoscopic rendering is usually a better fit for levels that contain a lot of distant content, such as outdoor scenes. In a small room where nearly everything lies before or straddles the culling plane, it will probably not improve performance.

Note that you may enable or disable hybrid monoscopic rendering dynamically in an application, enabling it in levels where it provides a performance improvement, and disabling it when it does not.

One way to quickly assess the performance impact is to use the console command stat RHI to configure your application to display the number of triangles being drawn in your level in real time. Then run the level with hybrid monoscopic rendering disabled and compare it to running the same level with the feature enabled, with different values for the culling plane, with different meshes tagged with **Render in Mono**, and so forth.

