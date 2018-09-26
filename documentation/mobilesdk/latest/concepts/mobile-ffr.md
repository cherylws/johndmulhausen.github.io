---
title: Fixed Foveated Rendering
---



Fixed Foveated Rendering (FFR) renders the edges of your eye textures at a lower resolution than the center. The effect, which is nearly imperceptible, lowers the fidelity of the scene in the viewer's peripheral vision. This reduces the GPU load as a result of the reduction in pixel shading requirements. FFR can dramatically increase the resolution of the eye texture, improving the image show in the headset. Complex fragment shaders also benefit from this form of multi-resolution rendering.

Unlike some other forms of foveation technologies, Oculus Go's Fixed Foveation system is not based on eye tracking. The high-resolution pixels are fixed in the center of the eye texture.

Fixed Foveated Rendering is only available on Oculus Go. A detailed look at the benefits of using FFR can be found in our [Optimizing Oculus Go for Performance](/blog/optimizing-oculus-go-for-performance) blog post.

## Implementing Fixed Foveated Rendering

First, you may wish to check if the device supports foveated rendering. Check the system property `VRAPI_SYS_PROP_FOVEATION_AVAILABLE`, which will return `VRAPI_TRUE` if foveated rendering is supported. 

Then, to use FFR, call the following to set the degree of foveation -

```
vrapi_SetPropertyInt( &amp;Java, VRAPI_FOVEATION_LEVEL, level );
```

* 0 disables multi-resolution
* 1 low FFR setting
* 2 medium FFR setting
* 3 high FFR setting


These values set the degree of foveation. The images below demonstrate the degree to which the resolution will be affected.



![](/images/documentationmobilesdklatestconceptsmobile-ffr-0.jpg)



**Low FFR**



![](/images/documentationmobilesdklatestconceptsmobile-ffr-1.jpg)



**Medium FFR**



![](/images/documentationmobilesdklatestconceptsmobile-ffr-2.jpg)



**High FFR**

In the images above, the white areas at the center of our FOV, the resolution is native: every pixel of the texture will be computed independently by the GPU. However, in the red areas, only 1/2 of the pixels will be calculated, 1/4 for the green areas, 1/8 for the blue areas, and 1/16 for the magenta tiles. The missing pixels will be interpolated from the calculated pixels at resolve time, when the GPU stores the result of its computation in general memory.

You may choose to change the degree of foveation based on the scene elements. Apps or scenes with high pixel shader costs will see the most benefit from using FFR. Apps with very simple shaders may see a net performance loss from the overhead of using FFR. Proper implementation of FFR requires testing and tuning to balance visual quality and GPU performance. 
