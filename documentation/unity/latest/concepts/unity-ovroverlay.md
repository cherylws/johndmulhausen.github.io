---
title: VR Compositor Layers
---
OVROverlay is a script in OVR/Scripts that allows you to render Game Objects as VR Compositor Layers instead of drawing them to the eye buffer. 

## OVROverlay

Game Objects rendered as VR compositor layers render at the frame rate of the compositor instead of rendering at the application frame rate. They are less prone to judder, and they are raytraced through the lenses, improving the clarity of textures displayed on them. This is useful for displaying easily-readable text.

Quadrilateral, cubemap, and cylinder compositor layers are currently supported by Rift and mobile. Equirectangular and offset cubemap compositor layers are currently available in mobile only.

**Overlay sample:** A sample illustrating the use of quad and cylinder VR Compositor Layers for a UI is included with the rendering samples of our Unity Sample Framework. See [Unity Sample Framework](/documentation/unity/latest/concepts/unity-sample-framework/ "The Oculus Unity Sample Framework provides sample scenes and guidelines for common VR-specific features such as hand presence with Oculus Touch, crosshairs, driving, hybrid mono rendering, and video rendering to a 2D textured quad.") for more information. 

All layer types support both stereoscopic and monoscopic rendering, though stereoscopic rendering only makes sense for cubemaps in most cases. Stereoscopically-rendered overlays require two textures, specified by setting Size to 2 in the Textures field of OVROverlay in the Inspector.

![](/images/documentation-unity-latest-concepts-unity-ovroverlay-0.png)  
When using OVROverlay, only textures with a Texture Type of Default are supported. This can be set in the Inspector for each texture.

Gaze cursors and UIs are good candidates for rendering as quadrilateral compositor layers. Cylinders may be useful for smooth-curve UI interfaces. Cubemaps may be used for startup scenes or skyboxes.

We recommend using a cubemap compositor layer for your loading scene, so it will always display at a steady minimum frame rate, even if the application performs no updates whatsoever.

## Compositing Limitations

Applications may add up to fifteen compositor layers (OVROverlays) to a scene. You may use no more than one cylinder and one cubemap compositor layer per scene.

Note that if a compositor layer fails to render (e.g., you attempt to render more than the maximum number of compositor layers), only quads will fall back and be rendered as scene geometry, and cubemaps and cylinders will not display at all.

If you need to support more than 15 high quality objects, you can use other strategies such as combining planar UIs into a single RenderTexture and using only one instance of OVROverlay. You can also enable only the most prominent of the active OVROverlay instances based on the user's view. Also, similar results can be achieved with scene geometry such as Unity’s Skybox component or Cylinder MeshFilter.

## World-locked vs Head-locked Overlays

There are 2 main types of overlays, world-locked and head-locked. Both overlay types use a special per-pixel distortion shader that samples directly from a texture on a transformed quad. World-locked overlays use TimeWarp, similar to non-overlay content, and are much less prone to judder. Head-locked overlays bypass TimeWarp and exactly follow head motion.

Overlays are world-locked by default. To make a head-locked overlay, make the Quad a child of the OVRCameraRig's center eye anchor.

## Ordering and Transparency

The depth ordering of compositor layers is controlled by two factors: 

1. Whether objects are rendered in front of or behind the scene geometry rendered to the eye buffer, and
2. The sequence in which the compositor layers are enabled in the scene.
By default, VR compositor layers are displayed as overlays in front of the eye buffer. To place them behind the eye buffer, set **Current Overlay Type** to Underlay in the Inspector. Note that underlay compositor layers are more bandwidth-intensive, as the compositor must “punch a hole” in the eye buffer with an alpha mask so that underlays are visible. Texture bandwidth is often a VR bottleneck, so use them with caution and be sure to assess their impact on your application.

Underlays depend on the alpha channel of the render target. If a scene object that should occlude an underlay is opaque, set its alpha to 1. If the occluder is transparent, you must use the OVRUnderlayTransparentOccluder shader provided in the Utilities in Assets/OVR/Shaders. Overlays do not require any special handling for transparency.

Compositor layers are depth ordered by the sequence in which they are enabled in the scene, but the order is reversed for overlays and underlays. Underlays should be enabled in the scene in the sequence in which you want them to appear, enabling the underlays in front first and the layers in the back last. Overlays should be enabled in the opposite order.

Basic usage

1. Attach OVROverlay.cs to a Game Object.
2. Specify the **Current Overlay Shape**:
	* Quad (Rift and Mobile)
	* Cubemap (Rift and Mobile)
	* Cylinder (Mobile only)
	
3. Specify the OVROverlay Texture. If you leave it as **None** (default), it will use the Renderer material’s main texture, if available.
4. Disable all compositor layers (both overlays and underlays),
5. Enable them sequentially to set the order in which you wish them to appear, enabling overlays in front last and underlays in front first.
## Example

In this example, most of the scene geometry is rendered to the eye buffer. The application adds a gaze cursor as a quadrilateral monoscopic overlay and a skybox as a monoscopic cubemap underlay behind the scene.

![](/images/documentation-unity-latest-concepts-unity-ovroverlay-1.png)  
Note the dotted sections of the eye buffer, indicating where OVROverlay has “punched a hole” to make the skybox visible behind scene geometry.

In this scene, the quad would be set to **Current Overlay Type: Overlay** and the cubemap would be set to **Current Overlay Type: Underlay**. Both would be disabled, then the quad overlay enabled, then the skybox enabled.

Note that if the cubemap in our scene were transparent, we would need to use the OVRUnderlayTransparentOccluder, which is required for any underlay with alpha less than 1. If it were stereoscopic, we would need to specify two textures and set Size to 2.

## Cylinder and Offset Cubemap Overlays (Mobile Only)

The center of a cylinder overlay Game Objects is used as the cylinder’s center. The dimensions of the cylinder are encoded in transform.scale as follows:

* [scale.z] cylinder radius
* [scale.y] cylinder height
* [scale.x] length of the cylinder arc
To use a cylinder overlay, your camera must be placed inside the inscribed sphere of the cylinder. The overlay will fade out automatically when the camera approaches to the inscribed sphere's surface.

![](/images/documentation-unity-latest-concepts-unity-ovroverlay-2.png)  
Only half of the cylinder may be displayed, so the arc angle must be smaller than 180 degrees.

Offset cubemap compositor layers are useful for increasing resolution for areas of interest/visible areas by offsetting the cubemap sampling coordinate.

They are similar to the same as standard cubemap compositor layers. Attach the OVROverlay script to an Empty Game Object, and specify the texture coordinate offset in the Position Transform. For more information, see OVROverlay in our [Unity Scripting Reference](/documentation/unity/latest/concepts/unity-reference-scripting/ "The Unity Scripting Reference contains detailed information about the data structures and files included with the Utilities and Legacy Integration packages."). 

## Create HDCP Protected Content Using OvrOverlay

Use the **Is Protected Content** checkbox when creating an OVROverlay layer to protect the layer with HDCP.

![](/images/documentation-unity-latest-concepts-unity-ovroverlay-3.png)  
