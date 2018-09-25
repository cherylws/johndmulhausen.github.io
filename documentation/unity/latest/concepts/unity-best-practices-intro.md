---
title: Best Practices for Rift and Mobile
---
This section describes performance targets and offers recommendations for developers. 

## General Best Practices

* Use trilinear or anisotropic filtering on textures. See [Textures](https://docs.unity3d.com/Manual/class-TextureImporter.html) in the Unity Manual for more information.
* Use mesh-based occlusion culling (see [Occlusion Culling](https://docs.unity3d.com/Manual/OcclusionCulling.html) in the Unity Manual).
* Always use the Forward Rendering path (see [Forward Rendering Path Details](https://docs.unity3d.com/Manual/RenderTech-ForwardRendering.html) in the Unity Manual).
* Enable Use Recommended MSAA Levels in OVRManager (see [OVRManager](/documentation/unity/latest/concepts/unity-utilities-overview/#unity-components "This section gives a general overview of the Components provided by the Utilities package.") for more information). Generally, the recommended MSAA level is 4x if you don't plan to enable Use Recommended MSAA Level.
* Watch for excessive texture resolution after LOD bias (greater than 4k by 4k on PC, greater than 2k by 2k on mobile).
* Verify that non-static objects with colliders are not missing rigidbodies in themselves or in the parent chain.
* Avoid inefficient effects such as SSAO, motion blur, global fog, parallax mapping.
* Avoid slow physics settings such as Sleep Threshold values of less than 0.005, Default Contact Offset values of less than 0.01, or Solver Iteration Count settings greater than 6.
* Avoid excessive use of multipass shaders (e.g., legacy specular).
* Avoid large textures or using a lot of prefabs in startup scenes (for bootstrap optimization). When using large textures, compress them when possible.
* Avoid realtime global illumination.
* Disable shadows when approaching the geometry or draw call limits.
* Avoid excessive pixel lights (>1 on Gear VR; >3 on Rift).
* Avoid excessive render scale (>1.2).
* Avoid excessive shader passes (>2).
* Be cautious using Unity WWW and avoid for large file downloads. It may be acceptable for very small files.
