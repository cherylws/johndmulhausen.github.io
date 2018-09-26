---
title: "Oculus Rift: Mask-Based Foveated Rendering"
---

Oculus Rift supports Mask-Based Foveated Rendering (MBFR) which enables the edges of the eye buffers to be rendered at a lower resolution than the center portion of the eye buffers, based on a superimposed mask. 

## Overview

Mask-Based Foveated Rendering (MBFR) decreases the shading rate of the peripheral region of the eye buffers by dropping pixels based on a checkboard pattern.

![](/images/documentationunreallatestconceptsunreal-mbfr-0.png)

There are four rings in the masked image. The center circle preserves all the pixels. The other three rings drop 25%, 50%, and 75% of the pixels, respectively. The pixels are dropped in 2x2 quads.

Here is the reconstructed image:

![](/images/documentationunreallatestconceptsunreal-mbfr-1.png)

Here is the full resolution scene that serves as the ground truth in this example:

![](/images/documentationunreallatestconceptsunreal-mbfr-2.png)

Here is a side-by-side comparison (magnified). The top is the masked image, the middle is the reconstructed image, and the bottom is the ground truth image.

![](/images/documentationunreallatestconceptsunreal-mbfr-3.png)

Here is another comparison:

![](/images/documentationunreallatestconceptsunreal-mbfr-4.png)

## Integration

MBFR is included in the Oculus GitHub UE4 Repository. (See the [Version Compatibility Reference](/documentation/unreal/latest/concepts/unreal-compatibility-matrix/).) It works with the Unreal Engine 4.19 and 4.20-preview versions.

To activate MBFR in your project:

1. Check “Forward Shading” in the UE4 Editor Project Settings, Rendering section
2. Without restarting the editor, check “[VR] Enable Mask-based Foveated Rendering” in Rendering/Experimental section
3. Restart the editor as prompted. The editor will take a while to rebuild the shaders
4. MBFR will be activated in your project when previewing or running in VR mode


![](/images/documentationunreallatestconceptsunreal-mbfr-5.png)

Here are some useful console commands for testing MBFR and adjusting the quality levels:

* vr.Foveated.Mask.Enable 1 – Activate MBFR
* vr.Foveated.Mask.Enable 0 – Deactivate MBFR
* vr.Foveated.Mask.VisualizeMode 1 – Disable the pixel reconstruction to reveal the masks
* vr.Foveated.Mask.VisualizeMode 0 – Enable the pixel reconstruction
* vr.Foveated.Mask.HighResFov – The FOV (in degrees) of the full resolution region. Default is 46.
* vr.Foveated.Mask.MediumResFov – The FOV (in degrees) of the region where 25% of pixels are dropped. Default is 60.
* vr.Foveated.Mask.LowResFov – The FOV (in degrees) of the region where 50% of pixels are dropped. Default is 78.
* The region outside the LowResFov will have 75% of the pixels dropped.


## Implementation

**Pixel Dropping**

The pixels to drop are culled through a bit in the stencil buffer. Here are the visibility patterns in each density region.

![](/images/documentationunreallatestconceptsunreal-mbfr-6.png)

**Reconstruction**

The dropped pixels are reconstructed in the PostProcessing stage, when the scene textures are fetched.

<u>Mid/high density region</u>

We use the 4 neighbor pixels to reconstruct each dropped pixel in the mid/high density regions, where the pixel dropping rate is less than or equal to 50%.

![](/images/documentationunreallatestconceptsunreal-mbfr-7.png)

The naïve formula is to set the dropped pixel A to the linear interpolation of B, C, D and E:

* A = (C + B) * 0.667 + (D + E) * 0.333


But it doesn’t work well and causes too much aliasing in the high contrast / high frequency areas. The artifact can be easily observed in the screenshots below. It causes heavy flickering in VR.

![](/images/documentationunreallatestconceptsunreal-mbfr-8.png)

The visual quality can be greatly improved by applying the directional weights computed from the neighborhood luminance. It enhances the edges and reduces the aliasing.

![](/images/documentationunreallatestconceptsunreal-mbfr-9.png)

Finally, we achieve a good overall reconstruction quality on the high/medium density regions. Here is a side-by-side comparison on the high-density region (dropped 25% pixels; the middle is the reconstructed result and the right is the ground truth):

![](/images/documentationunreallatestconceptsunreal-mbfr-10.png)

And two comparisons on the medium-density region (dropped 50% pixels, the middle is the reconstructed result and the right is the ground truth):

![](/images/documentationunreallatestconceptsunreal-mbfr-11.png)

![](/images/documentationunreallatestconceptsunreal-mbfr-12.png)

<u>Low density region (75% drop rate)</u>

We have fewer known pixels in the low-density region, which is furthest out on the peripheral area. We reconstruct each dropped pixel with linear interpolation of the two neighbor pixels.

![](/images/documentationunreallatestconceptsunreal-mbfr-13.png)

* A = P * 0.667 + Q * 0.333
* B = P * 0.667 + T * 0.333
* C = P * 0.667 + S * 0.333


Since we only have ¼ of the effective pixels, the fidelity of the reconstruction is restricted, with significant quality loss and distortion.

Since we only have 1/4 of the effective pixels, the fidelity of reconstruction is restricted, with significant quality loss and distortion. Here is a side-by-side comparison with the pre-distortion images (left: masked, middle: reconstructed, right: original):

![](/images/documentationunreallatestconceptsunreal-mbfr-14.png)

Because the low-density region is at the peripheral area, where the effective pixel density is low, it reduces the quality loss, but would not eliminate all the distortion artifacts. Here is approximately the same area on the post-distortion images:

![](/images/documentationunreallatestconceptsunreal-mbfr-15.png)

<u>Coarse quality reconstruction</u>

The high-fidelity mask reconstruction is GPU expensive, and not every post-processing stage requires this level of precision. So, we also have a coarse-quality mask reconstruction routine which reduces the reconstruction cost to single texture fetch, from 2 or 4 texture fetches in the regular reconstruction. The coarse quality reconstruction is currently used in Bloom, Depth of field, Down-sampling, Velocity flattening, and Screen-space reflection.

## Performance

MBFR reduces GPU pixel shading cost by dropping a subset of the pixels in the world rendering passes. But it also introduces extra cost in the post-processing passes for reconstructing the dropped pixels.

By testing on a 4.65ms scene of Robo Recall (on GTX1080), it reduced the overall GPU cost to 4.25ms (-9%). Specifically, it reduced the world rendering (BasePass) cost from 2.51ms to 2.19ms (-13%); and the PostProcessing cost was increased from 0.47ms to 0.65ms (+0.18ms).

Since the cost of PostProcessing is relatively fixed in a game, and the world rendering is dynamic, we can expect more than 10% of GPU performance savings from a scene with heavy world objects rendering.

Of course, the overall GPU performance is also heavily dependent on the FOVs of the density rings. An effective way to further optimize the GPU cost from MBFR is to configure them according to the content being rendered in each map. We can apply bigger density rings in maps which contains high frequency objects/textures to preserve the visual quality (like the cityscape maps in Robo Recall that were tested) and reduce the size of the density rings in other maps, to obtain the greatest performance benefit.

## Considerations when using MBFR

* MBFR effectively reduces the pixel shading cost from the world rendering.
* MBFR is compatible with D3D11 level hardware, independent of IHV private extensions.
* MBFR is relatively stable, temporally and spatially. It can be combined with existing AA techniques, including MSAA and TAA.
* However, MBFR results in extra performance cost, due to reconstructing the dropped pixels. Most VR projects do not use heavy post processing. But for projects which use heavy post processing with little world rendering, MBFR may not bring any performance benefit.
* MBFR may not work effectively on Mobile GPUs with tiled on-chip memory.
* The perceptual visual quality of MBFR can vary significantly, depending on the style of the content. The perceptual quality can be quite good when rendering low-contrast, low-frequency contents, but is generally less optimal when there are a lot of high frequency details in the content. 
* Tweaking the radius of the foveation density rings may be necessary to balance the performance and perceptual visual quality according to the content being rendered.

