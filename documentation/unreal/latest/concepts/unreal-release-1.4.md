---
title: Oculus Unreal Engine 4 Integration 1.4 Release Notes
---
## 1.3.2

Unreal provides built-in support for Oculus Rift and Gear VR development on Windows.

Unreal apps run on the Oculus platform automatically apply stereoscopic rendering to the main camera as well as positional and orientation tracking for the Rift, or orientation tracking for Gear VR.

For more information on downloading and using the Oculus Unreal integration, please see [Unreal Game Engine](/documentation/unreal/latest/concepts/unreal-engine/ "Unreal is distributed with Oculus plugins which make it easy to develop applications that work with Oculus Go, Oculus Rift, and Samsung Gear VR.").

## New Features

* Updated integration up to 4.11.2.
* Added Oculus Rift video layer support to 4.11 integration.
* Upgraded Oculus Mobile SDK to VrApi 1.0.2; Volume Control layer is now rendered correctly.
## Bug Fixes

* Fixed potential Gear VR crash when EnterVRMode is called before RenderThread is started.
* Switched LOD calculation from view-vector dot product to pure distance for more consistent result (otherwise, LOD could be different for each eye).
* Fixed incorrect logic for ATW splash rotation (PC).
## Known Issues

* Mirror window may appear stretched with hmd mirror mode 2 until you switch focus to another application and back.
