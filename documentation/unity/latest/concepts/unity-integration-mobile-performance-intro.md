---
title: "Best Practices: Mobile"
---

This section provides simple guidelines to help your Unity app perform well with Samsung Gear VR. 

Good performance is critical for all VR applications, but the limitations inherent to mobile development warrant special consideration.

We recommend that you also review **Design Guidelines** and **Mobile VR Design and Performance Guidelines** in the [Mobile SDK documentation](/documentation/mobilesdk/latest/).

## Design Considerations



### Startup Sequence

For good VR experiences, all graphics should be rendered such that the user is always viewing a proper three-dimensional stereoscopic image. Additionally, head-tracking must be maintained at all times.

An example of how to do this during application startup is demonstrated in the SDKExamples Startup_Sample scene:

* Solid black splash image is shown for the minimum time possible.
* A small test scene with 3D logo and 3D rotating widget or progress meter is immediately loaded.
* While the small startup scene is active, the main scene is loaded in the background.
* Once the main scene is fully loaded, the start scene transitions to the main scene using a fade.


### Universal Menu Handling

Applications must handle the Back Key long-press action which launches the Universal Menu as well as the Back Key short-press action which launches the “Confirm-Quit to Home” Menu and exits the current application, returning to the Oculus Home application.

## Best Practices



* Be **Batch Friendly**. Share materials and use a texture atlas when possible.
* Prefer **lightmapped, static geometry**.
* **Prefer lightprobes instead of dynamic lighting** for characters and moving objects.
* **Bake as much detail into the textures as possible.** E.g., specular reflections, ambient occlusion.
* **Only render one view per eye.** No shadow buffers, reflections, multi-camera setups, et cetera.
* **Keep the number of rendering passes to a minimum.** No dynamic lighting, no post effects, don't resolve buffers, donâ€™t use grabpass in a shader, et cetera.
* **Avoid alpha tested / pixel discard transparency.** Alpha-testing incurs a high performance overhead. Replace with alpha-blended if possible.
* Keep **alpha blended transparency** to a minimum.
* **Use Texture Compression.** Favor ETC2.
* **MSAA may be enabled on the Eye Render Textures.**


## General CPU Optimizations



To create a VR application or game that performs well, careful consideration must be given to how features are implemented. It must run at 60 FPS. Avoid any hitching or laggy performance during any point that the player is in your game.

### Recommendations

* Be mindful of the total number of GameObjects and components your scenes use.
* Model your game data and objects efficiently. You will generally have plenty of memory.
* Minimize the number of objects that actually perform calculations in Update() or FixedUpdate().
* Reduce or eliminate physics simulations when they are not actually needed.
* Use object pools to respawn frequently-used effects or objects instead of allocating new ones at runtime.
* Use pooled AudioSources versus PlayOneShot sounds, as the latter allocate a GameObject and destroy it when the sound is done playing.
* Avoid expensive mathematical operations whenever possible.
* Cache frequently-used components and transforms to avoid lookups each frame.
* Use the Unity Profiler to:
	+ Identify expensive code and optimize as needed.
	+ Identify and eliminate Garbage Collection allocations that occur each frame.
	+ Identify and eliminate any spikes in performance during normal play.
	
* Do not use Unityâ€™s OnGUI() calls.
* Do not enable gyro or the accelerometer. In current versions of Unity, these features trigger calls to expensive display calls.
* All best practices for mobile app and game development generally apply.


## Rendering Optimization



Be conservative on performance from the start.

* Keep draw calls down.
* Be mindful of texture usage and bandwidth.
* Keep geometric complexity to a minimum.
* Be mindful of fillrate.


### Reducing Draw Calls

Keep the total number of draw calls to a minimum. A conservative target would be less than **100 draw calls per frame**.

Unity provides several built-in features to help reduce draw calls such as batching and culling.

### Draw Call Batching

Unity attempts to combine objects at runtime and draw them in a single draw call. This helps reduce overhead on the CPU. There are two types of draw call batching: Static and Dynamic.

Static batching is used for objects that will not move, rotate or scale, and must be set explicitly per object. To mark an object static, select the Static checkbox in the object Inspector.

![](/images/documentationunitylatestconceptsunity-integration-mobile-performance-intro-0.jpg)

Dynamic batching is used for moving objects and is applied automatically when objects meet certain criteria, such as sharing the same material, not using real-time shadows, or not using multipass shaders. More information on dynamic batching criteria may be found here: [https://docs.unity3d.com/Documentation/Manual/DrawCallBatching.html](https://docs.unity3d.com/Documentation/Manual/DrawCallBatching.html)

### Culling

Unity offers the ability to set manual per-layer culling distances on the camera via Per-Layer Cull Distance. This may be useful for culling small objects that do not contribute to the scene when viewed from a given distance. More information about how to set up culling distances may be found here: [https://docs.unity3d.com/Documentation/ScriptReference/Camera-layerCullDistances.html](https://docs.unity3d.com/Documentation/ScriptReference/Camera-layerCullDistances.html).

Unity also has an integrated Occlusion Culling system. The advice to early VR titles is to favor modest “scenes” instead of “open worlds,” and Occlusion Culling may be overkill for modest scenes. More information about the Occlusion Culling system can be found here: [http://blogs.unity3d.com/2013/12/02/occlusion-culling-in-unity-4-3-the-basics/](http://blogs.unity3d.com/2013/12/02/occlusion-culling-in-unity-4-3-the-basics/).

### Reducing Memory Bandwidth

* **Texture Compression**: Texture compression offers a significant performance benefit. Favor ETC2 compressed texture formats.
* **Texture Mipmaps**: Always use mipmaps for in-game textures. Fortunately, Unity automatically generates mipmaps for textures on import. To see the available mipmapping options, switch **Texture Type** to **Advanced** in the texture inspector.
* **Texture Filtering**: Trilinear filtering is often a good idea for VR. It does have a performance cost, but it is worth it. Anisotropic filtering may be used as well, but keep it to a single anisotropic texture lookup per fragment.
* **Texture Sizes**: Favor texture detail over geometric detail, e.g., use high-resolution textures over more triangles. We have a lot of texture memory, and it is pretty much free from a performance standpoint. That said, textures from the Asset Store often come at resolutions which are wasteful for mobile. You can often reduce the size of these textures with no appreciable difference.
* **Framebuffer Format**: Most scenes should be built to work with a 16 bit depth buffer resolution. Additionally, if your world is mostly pre-lit to compressed textures, a 16 bit color buffer may be used.
* **Screen Resolution**: Setting Screen.Resolution to a lower resolution may provide a sizeable speedup for most Unity apps.


### Reduce Geometric Complexity

Keep geometric complexity to a minimum. 50,000 static triangles per-eye per-view is a conservative target.

Verify model vert counts are mobile-friendly. Typically, assets from the Asset Store are high-fidelity and will need tuning for mobile.

Unity Pro provides a built-in **Level of Detail** System (not available in Unity Free), allowing lower-resolution meshes to be displayed when an object is viewed from a certain distance. For more information on how to set up a LODGroup for a model, see the following: [https://docs.unity3d.com/Documentation/Manual/LevelOfDetail.html](https://docs.unity3d.com/Documentation/Manual/LevelOfDetail.html)

Verify your vertex shaders are mobile friendly. And, when using built-in shaders, favor the Mobile or Unlit version of the shader.

Bake as much detail into the textures as possible to reduce the computation per vertex, for example, baked bumpmapping as demonstrated in the Shadowgun project: [https://docs.unity3d.com/430/Documentation/Manual/iphone-PracticalRenderingOptimizations.html](https://docs.unity3d.com/430/Documentation/Manual/iphone-PracticalRenderingOptimizations.html)

Be mindful of GameObject counts when constructing your scenes. The more GameObjects and Renderers in the scene, the more memory consumed and the longer it will take Unity to cull and render your scene.

### Reduce Pixel Complexity and Overdraw

**Pixel Complexity**: Reduce per-pixel calculations by baking as much detail into the textures as possible. For example, bake specular highlights into the texture to avoid having to compute the highlight in the fragment shader.

Verify your fragment shaders are mobile friendly. And, when using built-in shaders, favor the Mobile or Unlit version of the shader.

**Overdraw**: Objects in the Unity opaque queue are rendered in front to back order using depth-testing to minimize overdraw. However, objects in the transparent queue are rendered in a back to front order without depth testing and are subject to overdraw.

Avoid overlapping alpha-blended geometry (e.g., dense particle effects) and full-screen post processing effects.
