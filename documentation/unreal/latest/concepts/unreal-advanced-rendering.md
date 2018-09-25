---
title: Rendering
---
This section describes important rendering options and tools that can significantly improve your application.

## Overview

In order to create the best VR experience for your users, your application should produce high quality images, e.g. with rich textures, while meeting the frame rate for the headset:

* Oculus Rift: 90 Hz
* Samsung Gear VR: 60 Hz
* Oculus Go: Configurable on a frame-by-frame basis to 60 Hz or 72 Hz
If your application does not hit frame rate, it may exhibit judder, flickering black areas on the peripheries, or other performance-related problems. Reducing the graphical richness of the experience may cut down on the render time, but can result in a less realistic or less immersive user experience. 

This section covers several techniques that can be used on Oculus headsets to improve the quality of the rendered images, while reducing render time. Most of these techniques are specific to one or two of the Oculus headsets.

* **[Oculus Go: Fixed Foveated Rendering](/documentation/unreal/latest/concepts/unreal-ffr/)**  
Oculus Go supports Fixed Foveated Rendering (FFR) which enables the edges of the eye buffers to be rendered at a lower resolution than the center portion of the eye buffers. 
* **[Oculus Go: Switching Display Refresh Rate](/documentation/unreal/latest/concepts/unreal-switching-display-refresh-rate-go/)**  
With Oculus Go, you can switch the frame rate between 60 Hz and 72 Hz. 
* **[Oculus Go and Gear VR: Multi-View](/documentation/unreal/latest/concepts/unreal-multi-view/)**  
Multi-View is an advanced rendering feature for Oculus Go and Gear VR. If your application is CPU-bound, we strongly recommend using Multi-View to improve performance.
* **[Oculus Go and Gear VR: Hybrid Monoscopic Rendering](/documentation/unreal/latest/concepts/unreal-hybrid-monoscopic/)**  
Hybrid monoscopic rendering (available in Unreal 4.15 or later) renders objects close to the viewer in stereoscopic 3D, while rendering all objects that lie past a culling plane only once.
* **[Oculus Rift: Mask-Based Foveated Rendering](/documentation/unreal/latest/concepts/unreal-mbfr/)**  
Oculus Rift supports Mask-Based Foveated Rendering (MBFR) which enables the edges of the eye buffers to be rendered at a lower resolution than the center portion of the eye buffers, based on a superimposed mask. 
* **[Oculus Rift: Unreal Forward Shading Renderer](/documentation/unreal/latest/concepts/unreal-forward-renderer/)**  
Unreal Engine provides a forward shading renderer optimized for VR. We recommend that all PC titles use the forward shading renderer. 
* **[Oculus Rift: Adaptive Pixel Density](/documentation/unreal/latest/concepts/unreal-adaptive-viewport/)**  
Adaptive Pixel Density allows applications to scale down the application viewport as GPU resources exceed 85% utilization, and to scale up as they become more available. This feature is currently available for Rift development only. 
* **[All Headsets: VR Compositor Layers](/documentation/unreal/latest/concepts/unreal-overlay/)**  
With Unreal, you may add transparent or opaque quadrilateral, cubemap, or cylindrical overlays to your level as compositor layers.
