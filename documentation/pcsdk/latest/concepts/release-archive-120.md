---
title: Changes in Version 1.20.x
---



## New Features for 1.20.x

* Depth Buffer Support – The new depth buffer layer specifies a monoscopic or stereoscopic view, with depth textures (in addition to color textures). This layer is equivalent to ovrLayerEyeFov, but with the addition of depth textures and a projection description. Depth buffers allow Dash overlays to be drawn without conflicting with scene objects. Depth buffers may also be used to support positional time warp. For more information, see the ovrLayerEyeFovDepth struct. Also see the “Layers” section in [Rendering to the Oculus Rift](https://developer.oculus.com/documentation/pcsdk/latest/concepts/dg-render). 
* Cylindrical Layer Support – It is now possible to use Cylinder layers to create curved quads, instead of flat quads. To do this, place the center of the cylinder at the camera origin in order to present a quad equidistant from the viewer. This can create more readable text for user interfaces and quads. For more information, see the ovrLayerCylinder struct. Also see the “Layers” section in [Rendering to the Oculus Rift](https://developer.oculus.com/documentation/pcsdk/latest/concepts/dg-render).
*  Rectilinear Capture Support – This feature enables your applications to obtain screenshots (at 90 frames per second) of a single non-distorted image that corresponds to what the user is seeing in the VR experience. You might use this feature to mirror the VR experience to an external monitor. See ovr\_CreateMirrorTextureWithOptionsDX (for DirectX), ovr\_CreateMirrorTextureWithOptionsGL (for OpenGL), and ovr\_CreateMirrorTextureWithOptionsVk (for Vulkan). Also see the “Rectilinear Capture” section in [Rendering to the Oculus Rift](https://developer.oculus.com/documentation/pcsdk/latest/concepts/dg-render). 


## API Changes

* ovrLayerEyeFovDepth struct has been added to enable depth buffer support. See the [API reference section](https://developer.oculus.com/documentation/pcsdk/latest/concepts/api-reference). Also see the “Layers” section in [Rendering to the Oculus Rift](https://developer.oculus.com/documentation/pcsdk/latest/concepts/dg-render).
* ovrLayerCylinder struct has been added to enable cylindrical layer support. See the [API reference section](https://developer.oculus.com/documentation/pcsdk/latest/concepts/api-reference). Also see the “Layers” section in [Rendering to the Oculus Rift](https://developer.oculus.com/documentation/pcsdk/latest/concepts/dg-render).
* ovr\_CreateMirrorTextureWithOptionsDX (for DirectX), ovr\_CreateMirrorTextureWithOptionsGL (for OpenGL), and ovr\_CreateMirrorTextureWithOptionsVk (for Vulkan) have been added to enable rectilinear capture support. See the [API reference section](https://developer.oculus.com/documentation/pcsdk/latest/concepts/api-reference). Also see the “Rectilinear Capture” section in [Rendering to the Oculus Rift](https://developer.oculus.com/documentation/pcsdk/latest/concepts/dg-render).
* There is a new OVR\_CAPI\_Prototypes.h file that is part of the SDK's shim. You only need to use this if your application compiles OVR\_CAPIShim.c, as opposed to linking LibOVR.lib.


## Known SDK Issues

* If you encounter intermittent tracking issues, remove the batteries from any Engineering Sample Oculus Remotes that you paired with your headset and contact Developer Relations for replacement remotes.
* If you bypass the shim and communicate with the DLL directly, without specifying a version to ovr\_Initialize, the DLL has no way of knowing the SDK version with which the application was built. This can result in unpredictable or erratic behavior which might cause the application to crash.

