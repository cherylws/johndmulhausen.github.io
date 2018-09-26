---
title: Oculus Unreal Engine 4 Integration 1.5 Release Notes
---



## 1.5.0

Unreal provides built-in support for Oculus Rift and Gear VR development on Windows.

Unreal apps run on the Oculus platform automatically apply stereoscopic rendering to the main camera as well as positional and orientation tracking for the Rift, or orientation tracking for Gear VR.

For more information on downloading and using the Oculus Unreal integration, please see [Unreal Game Engine](/documentation/unreal/latest/concepts/unreal-engine/).

## 4.12

New Features

* Added async splash (Gear VR).
* Refactored layers management (Gear VR).
* Enabled default loading icon mode (Gear VR).
* Added ability to capture cube maps for Oculus Store preview (see [unresolvable-reference.xml](unresolvable-reference) for usage instructions).
* Added call ovr\_IdentifyClient to identify client to service.
* Added OnlineSubsystemOculus to interface Oculus platform.


API Changes

* Added GetNumOfTrackingSensors / GetTrackingSensorProperies to IHeadMountedDisplay.


Bug Fixes

* Fixed issue with BeginPlay.
* Fixed rounding error that could cause incorrect viewport sizes.
* Now use ovr\_GetSessionStatus() instead of SubmitFrame result to determine VR focus.
* Fixed crash creating HMD when it is attached to D3D11 adapter with no other monitors.
* Fixed issue where IHeadMountedDisplayModule::IsHMDConnected would be called more than necessary.


## 4.11

New Features

* Added async splash (Gear VR).
* Refactored layers management (Gear VR).
* Enabled default loading icon mode (Gear VR).
* Added ability to capture cube maps for Oculus Store preview (see [unresolvable-reference.xml](unresolvable-reference) for usage instructions).
* Added ovr\_IdentifyClient call to identify client to service.


API Changes

* Added GetNumOfTrackingSensors / GetTrackingSensorProperies to IHeadMountedDisplay.


Bug Fixes

* Now uses ovr\_GetSessionStatus() instead of SubmitFrame result to determine VR focus.
* Fixed issue where IHeadMountedDisplayModule::IsHMDConnected would be called more than necessary.

