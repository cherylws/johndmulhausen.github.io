---
title: Single Pass Stereo Rendering (Preview, Mobile Only)
---
Single Pass stereo rendering is a preview rendering feature for Oculus Go and Gear VR available in Unity 5.6. If your application is CPU-bound or draw call bound, we strongly recommend using Single Pass rendering to improve performance. 

In typical OpenGL stereo rendering, each eye buffer must be rendered in sequence, doubling application and driver overhead. When Single Pass is enabled, objects are rendered once to the left eye buffer, then duplicated to the right buffer automatically with appropriate modifications for vertex position and view-dependent variables such as reflection.

While Single Pass rendering primarily reduces CPU usage, GPU usage may be affected. On Exynos devices, Single Pass rendering slightly reduces the GPU load as well as the CPU load. Unfortunately, on Qualcomm devices, Single Pass currently causes a slight increase in GPU load of a few percent. Qualcomm is looking into optimizing this to reduce the increase in GPU load.

For additional technical information, you may wish to review [Multi-View](/documentation/mobilesdk/latest/concepts/mobile-multiview/) in our Mobile SDK documentation, which discusses the underlying framework that makes Single Pass rendering possible in our Unity integration.

For additional information, see [Single-Pass Stereo Rendering](https://docs.unity3d.com/Manual/SinglePassStereoRendering.html) and [Single-Pass Stereo Rendering for Android](https://docs.unity3d.com/Manual/Android-SinglePassStereoRendering.html) in Unity's documentation.

## Requirements

Single Pass rendering is currently supported by Note5, S6, S7, S7 Edge, S8 and S8+ phones using ARM Exynos processors and running Android M or N. It is also supported on S7 and S7 Edge phones using Qualcomm processors and running Android N.

Single Pass rendering requires OpenGL ES 3.

Although it can substantially reduce CPU overhead, keep in mind that applications submitted to the Oculus Store must maintain minimum frame rate per our requirements, even on devices that do not support multi-view.

## Enabling Single Pass Rendering

1. Open **Player Settings** and go to **Rift**.
2. Set **Stereo Rendering Method** to **Single Pass (Preview)**.
![](/images/documentation-unity-latest-concepts-unity-single-pass-0.png)  
