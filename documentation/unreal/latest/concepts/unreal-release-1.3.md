---
title: Oculus Unreal Engine 4 Integration 1.3 Release Notes
---
## 1.3.2

Unreal provides built-in support for Oculus Rift and Gear VR development on Windows.

Unreal apps run on the Oculus platform automatically apply stereoscopic rendering to the main camera as well as positional and orientation tracking for the Rift, or orientation tracking for Gear VR.

For more information on downloading and using the Oculus Unreal integration, please see [Unreal Game Engine](/documentation/unreal/latest/concepts/unreal-engine/ "Unreal is distributed with Oculus plugins which make it easy to develop applications that work with Oculus Go, Oculus Rift, and Samsung Gear VR.").

## New Features

* Updated integration up to 4.11.1 and 4.10.4.
* Added quad layer support for Gear VR.
* Added Gear VR video layer support to 4.11 integration.
* Separated Alt-Enter from switching between stereo/mono; currently, Alt-Enter switches between fullscreen/windowed mode for mirror window.
* Added proper support for fullscreen mirror window.
## Bug Fixes

* Fixed base orientation issue with quad layers rendering.
* Fixed Steam VR compatibility issue.
* Fixed Oculus Touch haptic logic: vibration won’t be send to Oculus Touch unless the controllers are currently active.
