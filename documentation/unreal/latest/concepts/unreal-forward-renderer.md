---
title: "Oculus Rift: Unreal Forward Shading Renderer"
---

Unreal Engine provides a forward shading renderer optimized for VR. We recommend that all PC titles use the forward shading renderer. 

The primary advantage of the forward renderer is that it is substantially faster than the deferred renderer. It outputs lit pixels directly, whereas the deferred renderer outputs material properties to a set of buffers, and then reads them back to apply lighting in a separate pass.

Because the forward renderer does not render to intermediate buffers, it can take advantage of multi-sample anti-aliasing (MSAA). We recommend using MSAA for anti-aliasing, as it not only increases image sharpness, but often provides a significant savings in GPU utilization over temporal anti-aliasing (TAA).

Not all features from the deferred renderer are available in the forward renderer, but many of these features require tradeoffs that disproportionately impact VR development. For example, space screen effects may introduce stereo disparities that can be uncomfortable for users.

Given the substantial advantages the forward shading renderer offers VR developers, we anticipate that the forward shading renderer will become the target for future VR optimizations.

For more information on the forward shading renderer, see Epic’s [New: Forward Shading Renderer with MSAA](https://www.unrealengine.com/blog/unreal-engine-4-14-released).
