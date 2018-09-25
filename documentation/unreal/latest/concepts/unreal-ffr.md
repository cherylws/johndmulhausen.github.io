---
title: Oculus Go: Fixed Foveated Rendering
---
Oculus Go supports Fixed Foveated Rendering (FFR) which enables the edges of the eye buffers to be rendered at a lower resolution than the center portion of the eye buffers. 

## Overview

For a general introduction to Fixed Foveated Rendering (FFR), please see the blog article [Optimizing Oculus Go for Performance](/blog/optimizing-oculus-go-for-performance/).

The effect of using FFR is nearly imperceptible, but it provides important benefits, including:

* Significantly improves GPU fill performance
* Reduces power consumption, and thereby reduces heat and increases battery life
* Enables applications to increase the resolution of eye textures, which improves the viewing experience, while maintaining performance and power consumption levels
**When to use Fixed Foveated Rendering**It is recommended that you use FFR as much as possible, and set it to as high a level as possible. (The FFR settings are described later in this section.) 

Here are some considerations regarding the tradeoffs when using FFR:

* FFR is most useful for low contrast textures, including background images and large objects.
* FFR is less useful for high-contrast items, such as text and fine detailed images, and can cause noticeable degradation in the image quality.
* Complex fragment shaders benefit from FFR.
You can adjust the FFR level on a frame-by-frame basis in order to achieve the best tradeoff between performance and visual quality. It is a good idea to test your content and look for any undesirable visual artifacts. 

Note that, unlike some other forms of foveation technologies, FFR is not based on eye tracking. Rather, the high-resolution pixels are “fixed” in the center of the eye buffers.

**Quantifying Performance Gains**The API for Fixed Foveated Rendering allows developers to tune the FFR level (even from frame to frame) in order to minimize visible artifacts, as necessary. In most cases it may be sufficient to simply turn FFR on for in-game scenes and turn it down or off for menus or other UI objects. 

The gains (or losses) provided by FFR typically depend of your application’s pixel shader costs. FFR can result in a 25% gain in performance with pixel-intensive applications. On the other hand, applications with very simple shaders, which are not bound on GPU fill, will likely not see a significant improvement from FFR. A highly ALU-bound application will benefit from this, as shown in the graph below that collects GPU % on a scene. Given a 16% GPU utilization coming from timewarp (and therefore not affected by FFR), this graph shows a 6.5% performance improvement from the low setting, 11.5% improvement from medium setting, and a 21% improvement from the high setting. However, this is a best case scenario for using FFR. If you perform the same test on an application which has very simple pixel shaders, it is possible to actually have a net loss on the low setting, due to the fact that the fixed overhead of using FFR can be higher than the rendering savings on a relatively small number of few pixels. In fact, in this situation, you might experience a slight gain with the high setting, but it won’t be worth the image quality loss.

![](/images/documentation-unreal-latest-concepts-unreal-ffr-0.png)  
**How Fixed Foveated Rendering Works**Unlike traditional 2D screens, VR devices require that the image displayed to the viewer be warped to match the curvature of the lenses in the headset. This distortion allows us to perceive a larger field of view than we would by simply looking at a raw display. The image below shows the effect of distortion, where a 2D plane (the horizontal line) is warped into a spherical shape:

![](/images/documentation-unreal-latest-concepts-unreal-ffr-1.png)  
As you can see, the pixels that make up an eye texture are very unevenly represented due to the distortion. Many more pixels are needed to create the post-distortion areas at the edge of the FOV than the center of the FOV. This results in a higher pixel density at the edge of the FOV than in the middle. This is highly counterproductive since users generally look toward the center of the screen. On top of that, lenses blur the edge of the field of view, so even though many pixels have been rendered in that part of the eye texture, the sharpness of the image is lost. The GPU spends a lot of time rendering pixels at the edge of the FOV that can't be clearly seen. This is very inefficient. 

**How the pixel resolution is reduced**Fixed Foveated Rendering reclaims some of the wasted GPU processing resources by lowering the resolution of the output image during its computation. On Oculus Go, this is implemented by controlling the resolution of individual render tiles on the GPU. Oculus Go uses a Qualcomm 821 SoC which, like most mobile chipsets, is a tiled renderer. Rather than execute render commands sequentially as a desktop GPU would, a tiled renderer divides its work into rectangles (or tiles) and renders those in parallel. By controlling the resolution of individual tiles, and ensuring that the tiles that fall on the edges of the eye buffer are lower resolution than the center, it is possible to reduce the number of pixels that the GPU needs to fill without perceptibly lowering the quality of the post-distortion image. This translates to a very significant improvement in GPU performance for applications that render a large number of pixels – as is the case with very high-resolution eye buffers – or employ an expensive fragment shader, e.g. to produce dynamic lighting and shadows.

High Setting

The screenshot below shows the tile resolution multiplier map for a 1024x1024 eye buffer on Oculus Go with FFR set to its highest (LMSHigh) foveation level:

![](/images/documentation-unreal-latest-concepts-unreal-ffr-2.png)  
The colors represent the following resolution levels:

* White = Full resolution: This is the center of the FOV. Every pixel of the texture is computed independently by the GPU.
* Red = 1/2 resolution: Only half of the pixels are calculated by the GPU. The missing pixels are interpolated from the calculated pixels at resolve time, when the GPU stores the result of its computation in general memory.
* Green = 1/4 resolution: Only one quarter of the pixels are calculated by the GPU. The missing pixels are interpolated from the calculated pixels at resolve time, when the GPU stores the result of its computation in general memory.
* Blue = 1/8 resolution: Only one eighth of the pixels are calculated by the GPU. The missing pixels are interpolated from the calculated pixels at resolve time, when the GPU stores the result of its computation in general memory.
* Pink = 1/16 resolution: Only one sixteenth of the pixels are calculated by the GPU. The missing pixels are interpolated from the calculated pixels at resolve time, when the GPU stores the result of its computation in general memory.
Medium Setting

The screenshot below shows a similar map with FFR set to its medium (LMSMedium) foveation level:

![](/images/documentation-unreal-latest-concepts-unreal-ffr-3.png)  
The colors represent the following resolution levels:

* White = Full resolution: This is the center of the FOV. Every pixel of the texture is computed independently by the GPU.
* Red = 1/2 resolution: Only half of the pixels are calculated by the GPU. The missing pixels are interpolated from the calculated pixels at resolve time, when the GPU stores the result of its computation in general memory.
* Green = 1/4 resolution: Only one quarter of the pixels are calculated by the GPU. The missing pixels are interpolated from the calculated pixels at resolve time, when the GPU stores the result of its computation in general memory.
* Blue = 1/8 resolution: Only one eighth of the pixels are calculated by the GPU. The missing pixels are interpolated from the calculated pixels at resolve time, when the GPU stores the result of its computation in general memory. 
Low Setting

The screenshot below shows a similar map with FFR set to its lowest (LMSLow) foveation level:

![](/images/documentation-unreal-latest-concepts-unreal-ffr-4.png)  
The colors represent the following resolution levels:

* White = Full resolution: This is the center of the FOV. Every pixel of the texture is computed independently by the GPU.
* Red = 1/2 resolution: Only half of the pixels are calculated by the GPU. The missing pixels are interpolated from the calculated pixels at resolve time, when the GPU stores the result of its computation in general memory.
* Green = 1/4 resolution: Only one quarter of the pixels are calculated by the GPU. The missing pixels are interpolated from the calculated pixels at resolve time, when the GPU stores the result of its computation in general memory.
**Setting FFR Levels with Blueprints**You can set the level of FFR to any the following indexes into the ETiledMultiResLevel enum: 

* ETiledMultiResLevel\_Off (index = 0): No reduction of resolution. (Default) 
* ETiledMultiResLevel\_LMSLow (index = 1): The lowest level of resolution reduction. 
* ETiledMultiResLevel\_LMSMedium (index = 2): The medium level of resolution reduction. 
* ETiledMultiResLevel\_LMSHigh (index = 3): The highest level of resolution reduction. 
You can use the following Blueprints to set and get the FFR level:

* [Get Tiled Multires Level](/documentation/unreal/latest/concepts/unreal-blueprints-get-tiled-multires-level/ "Returns the current multi-resolution level, which applies to fixed foveated rendering.")
* [Set Tiled Multires Level](/documentation/unreal/latest/concepts/unreal-blueprints-set-tiled-multires-level/ "Sets the multi-resolution level for fixed foveated rendering.")
These Blueprints are located under the Unreal Blueprints folder path Input/Oculus Library:

![](/images/documentation-unreal-latest-concepts-unreal-ffr-5.png)  
The [Set Tiled Multires Level](/documentation/unreal/latest/concepts/unreal-blueprints-set-tiled-multires-level/ "Sets the multi-resolution level for fixed foveated rendering.") blueprint enables you to set the FFR level to one of the four possible values:

![](/images/documentation-unreal-latest-concepts-unreal-ffr-6.png)  
The [Get Tiled Multires Level](/documentation/unreal/latest/concepts/unreal-blueprints-get-tiled-multires-level/ "Returns the current multi-resolution level, which applies to fixed foveated rendering.") blueprint returns the current FFR level setting:

![](/images/documentation-unreal-latest-concepts-unreal-ffr-7.png)  
