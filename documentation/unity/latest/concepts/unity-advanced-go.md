---
title: Advanced Rendering on the Oculus Go
---
This section describes advanced rendering features available for the Oculus Go.

## Fixed Foveated Rendering

Fixed Foveated Rendering (FFR) renders the edges of your eye textures at a lower resolution than the center. The effect, which is nearly imperceptible, lowers the fidelity of the scene in the viewer's peripheral vision. This reduces the GPU load as a result of the reduction in pixel shading requirements. FFR can dramatically increase performance, improving the image show in the headset. Complex fragment shaders also benefit from this form of multi-resolution rendering.

Unlike some other forms of foveation technologies, Oculus Go's Fixed Foveation system is not based on eye tracking. The high-resolution pixels are fixed in the center of the eye texture.

Fixed Foveated Rendering is only available on the Oculus Go. A detailed look at the benefits of using FFR can be found in our [Optimizing Oculus Go for Performance](/blog/optimizing-oculus-go-for-performance/) blog post.

**Implementing Fixed Foveated Rendering**

To use FFR, call the following to set the degree of foveation -

OVRManager.tiledMultiResLevel = OVRManager.TiledMultiResLevel.{Off/LMSLow/LMSMedium/LMSHigh};Where level can be Off, LMSLow, LMSMedium, LMSHigh.

* Off disables multi-resolution
* LMSLow is the low FFR setting
* LMSMedium is the mid FFR setting
* LMSHigh is the high FFR setting
These values set the degree of foveation. The images below demonstrate the degree to which the resolution will be affected.

![](/images/documentation-unity-latest-concepts-unity-advanced-go-0.jpg)  
LMSLow FFR Setting

![](/images/documentation-unity-latest-concepts-unity-advanced-go-1.jpg)  
LMSMedium FFR Setting

![](/images/documentation-unity-latest-concepts-unity-advanced-go-2.jpg)  
LMSHigh FFR Setting

In the images above, the white areas at the center of our FOV, the resolution is native: every pixel of the texture will be computed independently by the GPU. However, in the red areas, only 1/2 of the pixels will be calculated, 1/4 for the green areas, 1/8 for the blue areas, and 1/16 for the magenta tiles. The missing pixels will be interpolated from the calculated pixels at resolve time, when the GPU stores the result of its computation in general memory.

You may choose to change the degree of foveation based on the scene elements. Apps or scenes with high pixel shader costs will see the most benefit from using FFR. Apps with very simple shaders may see a net performance loss from the overhead of using FFR. Proper implementation of FFR requires testing and tuning to balance visual quality and GPU performance. 

## 72 Hz Mode

The Oculus Go can optionally render your application at 72 frames per second rather than the normal 60 frames. The resulting output has lower latency and less flicker, which improves comfort and reduces eye strain.

To query the available refresh rates on the device:

float[] freqs = OVRManager.display.displayFrequenciesAvailable;To change the refresh rate, update displayFrequency in OVRDisplay. For example, to set the refresh rate to 72 Hz on a Go app:

OVRManager.display.displayFrequency = 72.0f;An app rendering at 72 Hz may require additional performance optimizations to maintain the same framerate as an app rendering at 60 Hz. Our [Optimizing Oculus Go for Performance](/blog/optimizing-oculus-go-for-performance/) blog post contains recommendations for when and how to use 72 Hz mode.

