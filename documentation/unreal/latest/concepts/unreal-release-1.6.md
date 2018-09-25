---
title: Oculus Unreal Engine 4 Integration 1.6 Release Notes
---
## 1.6.0

Unreal provides built-in support for Oculus Rift and Gear VR development on Windows.

Unreal apps run on the Oculus platform automatically apply stereoscopic rendering to the main camera as well as positional and orientation tracking for the Rift, or orientation tracking for Gear VR.

For more information on downloading and using the Oculus Unreal integration, please see [Unreal Game Engine](/documentation/unreal/latest/concepts/unreal-engine/ "Unreal is distributed with Oculus plugins which make it easy to develop applications that work with Oculus Go, Oculus Rift, and Samsung Gear VR.").

The Wwise redirection patch is no longer required in Unreal Engine 4.11 or 4.12. Requires the WwiseUE4Plugin from AudioKinetic’s ‘master’ branch on GitHub.

## 4.12

New Features

* Added adaptive viewport scaling, which automatically changes pixel density based on resource availability, with configurable min/max. See [unresolvable-reference.xml](unresolvable-reference) for details. (Rift only) UPDATE: This feature has been delayed until a future release.
* Added Blueprints plugin that supports calls for Gear VR functionality such as GPU/GPU throttling, querying headphone connection, querying device temperature, and more.
* Added Blueprint for Oculus Platform entitlement checks.
API Changes

* Oculus Touch: Added PlayHapticsSoundwave to Blueprints, which permits playback of soundwaves (stored in UE4 in USoundWave assets) directly to the Oculus Touch controller.
* Added SetHapticFeedbackBuffer to the C++ Haptics interface, to submit byte arrays to be played at 320 Hz on the Oculus Touch controller.
Bug Fixes

* Fixed bug where unfocused Wwise apps continued playing audio. Requires the WwiseUE4Plugin from AudioKinetic’s ‘master’ branch on Github.
## 4.11

New Features

* Added adaptive viewport scaling, which automatically changes pixel density based on resource availability, with configurable min/max. See [unresolvable-reference.xml](unresolvable-reference) for details. (Rift only) UPDATE: This feature has been delayed until a future release.
API Changes

* Oculus Touch: Added PlayHapticsSoundwave to Blueprints, which permits playback of soundwaves (stored in UE4 in USoundWave assets) directly to the Touch controller.
* Added SetHapticFeedbackBuffer to the C++ Haptics interface, to submit byte arrays to be played at 320 Hz on the Touch controller.
Bug Fixes

* Fixed bug where unfocused Wwise apps continued playing audio. Requires the WwiseUE4Plugin from AudioKinetic’s ‘master’ branch on GitHub.
