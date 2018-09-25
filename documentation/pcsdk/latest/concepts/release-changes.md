---
title: Changes in Version 1.28.x
---
## New Features for 1.28.x

* The function CompositorGpuEndToVsyncElapsedTime has been added to OVR\_CAPI. This function returns the amount of time that is left within a frame after the compositor is finished using the GPU, prior to the associated V-Sync time. This function can be helpful for optimizing your applications within your application code. 
* The function ovr\_GetFovStencil has been added to OVR\_CAPI. This function returns a viewport stencil mesh to be used for defining the area or outline the user can see through the lens on an area defined by a given ovrFovPort. 
* The debug console now uses its own layer, which is backed by a texture. As of the 1.28 release, the compositor reads directly from the texture when compositing and distorting the scene. Previously, the debug console was rendered into the Eye layers. This meant that the quality of the debug console varied with the size of the eye layer. This also introduced sampling artifacts, because the layer was rendered to a quad in the eye buffers. See https://developer.oculus.com/documentation/pcsdk/latest/concepts/dg-render/#dg-render-layers for a description of layers. 
* The sample applications were improved so that it is easier to build them. 
## API Changes

* There are no breaking API changes in this release.
## Bug Fixes

* n/a
## Known SDK Issues

* There's a bug affecting the Guardian System API by which color set operations to the visualized grid don't work if they are called while the HMD is not being worn.
