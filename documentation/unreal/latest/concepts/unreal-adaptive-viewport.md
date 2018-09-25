---
title: "Oculus Rift: Adaptive Pixel Density"
---
Adaptive Pixel Density allows applications to scale down the application viewport as GPU resources exceed 85% utilization, and to scale up as they become more available. This feature is currently available for Rift development only.

For CPU-bound applications, this feature has the potential to improve visual quality.

The following charts illustrate pixel density (gold) and frames per second (blue) on a demo application with Adaptive Pixel Density off and on, respectively.

![](/images/documentation-unreal-latest-concepts-unreal-adaptive-viewport-0.png)  
![](/images/documentation-unreal-latest-concepts-unreal-adaptive-viewport-1.png)  
To enable Adaptive Pixel Density, use the console command hmd pdadaptive on or the console variable vr.oculus.PixelDensity.adaptive on. You may specify a minimum and maximum scaling factor (default 1 = normal density).

To enable Adaptive Pixel Density on startup, specify the appropriate settings in Engine/Config/BaseEngine.ini. For example:

[Oculus.Settings] PixelDensityMin=0.5 PixelDensityMax=1.0 PixelDensityAdaptive=trueSee [Loading Console Variables](https://docs.unrealengine.com/latest/INT/Programming/Development/Tools/ConsoleManager/#loadingconsolevariables) in Epicâ€™s [Console Manager: Console Variables in C++](https://docs.unrealengine.com/latest/INT/Programming/Development/Tools/ConsoleManager/) for more information.

If you do not want some Actors within your level (e.g., text displays) to be scaled, they should be drawn using separate VR Compositor Layers which are not scaled by pixel density. For more information, see [All Headsets: VR Compositor Layers](/documentation/unreal/latest/concepts/unreal-overlay/ "With Unreal, you may add transparent or opaque quadrilateral, cubemap, or cylindrical overlays to your level as compositor layers.").

Note: To minimize the perceived artifacts from changing resolution, there is a two-second minimum delay between every resolution change.
