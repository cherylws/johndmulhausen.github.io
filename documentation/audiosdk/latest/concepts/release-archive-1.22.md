---
title: Audio SDK 1.22 Release Notes
---

This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Audio SDK.

## 1.22.0

## New Features

* **Dynamic Room Modeling**: The Oculus Native Spatializer plugin for Unity 5.2+ now supports Dynamic Room Modeling. This enables sound reflections and reverb to be generated based on a dynamically updated model of the current room (or space) within the VR experience, as well as the user's position within that room. For example, if the user moves from a small room to a larger room within the VR experience, the natural echos and reverb that are associated with the larger room are automatically applied. These effects also change naturally as the user moves about within a room. This feature can be enabled by adding a script to an object within the scene, in the Unity Editor. You can then optionally configure a number of public variables, including: Layer Mask, Visualize Room, Rays Per Second, Room Interp Speed, Max Wall Distance, Ray Cache Size, Dynamic Reflections Enabled, and Legacy Reverb. The associated documentation has also been enhanced to more clearly explain the difference between sound reflections and reverb. For more information, please see [Dynamic Room Modeling](/documentation/audiosdk/latest/concepts/ospnative-unity-dynroom/ "The Oculus Spatializer provides dynamic room modeling, which enables sound reflections and reverb to be generated based on a dynamically updated model of the current room within the VR experience and the user's position within that space.")


## API Changes

* The new or updated API function calls associated with Dynamic Room Modeling include: ovrAudio\_AssignRaycastCallback, ovrAudio\_SetDynamicRoomRaysPerSecond, ovrAudio\_SetDynamicRoomInterpSpeed, ovrAudio\_SetDynamicRoomMaxWallDistance, ovrAudio\_SetDynamicRoomRaysRayCacheSize, ovrAudio\_UpdateRoomModel, ovrAudio\_GetRoomDimensions, and ovrAudio\_GetRaycastHits.

