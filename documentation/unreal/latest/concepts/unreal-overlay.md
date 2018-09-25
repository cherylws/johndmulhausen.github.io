---
title: All Headsets: VR Compositor Layers
---
With Unreal, you may add transparent or opaque quadrilateral, cubemap, or cylindrical overlays to your level as compositor layers.

Asynchronous TimeWarp compositor layers (such as world-locked overlays) are rendered at the same frame rate as the compositor, rather than rendering at the application frame rate. They are less prone to judder, and are raytraced through the lenses, which improves the clarity of textures displayed on them. 

We recommend using compositor layers for text and for headlocked elements. Text rendered on compositor layers is more legible, and headlocked layers remain headlocked when Asynchronous TimeWarp interpolates dropped frames.

Gaze cursors and UIs are good candidates for rendering as quadrilateral compositor layers. Cylinders may be useful for smooth-curve UI interfaces. Cubemaps may be used for startup scenes or skyboxes. 

We recommend using a cubemap compositor layer for your loading scene, so it will always display at a steady minimum frame rate, even if the application performs no updates whatsoever. This can significantly improve application startup times.

Quadrilateral, cylinder, and cubemap layers are supported in Unreal versions 4.13 and later. 

By default, VR compositor layers are always displayed on top of all other objects in the scene. You may set compositor layers to respect depth positioning by enabling **Supports Depth**. If you are using multiple layers, use the **Priority** setting to control the depth order in which the layers will be displayed, with lower values indicating greater priority (e.g., 0 is before 1). 

Note that enabling **Supports Depth** may affect performance, so use it with caution and be sure to assess its impact.

![](/images/documentation-unreal-latest-concepts-unreal-overlay-0.png)  
To create an overlay:

1. Create a Pawn and add it to the level. You can use the UMG UI Designer to add any desired UI elements to the Pawn. 
2. Select the Pawn, select **Add Component**, and choose **Stereo Layer**.
3. Under the Stereo Layer options, set **Stereo Layer Type** to **Quad Layer** or **Cylinder Layer**.
4. Set **Stereo Layer Type** to **Face Locked**, **Torso Locked**, or **World Locked**.
5. Set the overlay dimensions in world units in **Quad Stereo Layer Properties** or **Cylinder Stereo Layer Properties**.
6. Select **Supports Depth** in **Stereo Layer** to set your compositor layer to not always appear on top of other scene geometry. Note that this may affect performance.
7. Configure Texture and additional attributes as appropriate.
The Pawn you slave the component to will be fixed at the center of the quad or the cylinder.

You may add up to three VR compositor layers to mobile applications, and up to fifteen to Rift applications. 

## Layers Sample

The LayerSample, available from our Unreal GitHub repository, illustrates the use of VR Compositor Layers to display a UMG UI. For more information, see [Unreal Samples](/documentation/unreal/latest/concepts/unreal-samples/ "Oculus provides samples which illustrate basic VR concepts in Unreal such as Touch, haptics, and the Boundary Component API for interacting with the Guardian System.").

