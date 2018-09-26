---
title: Oculus Unreal Engine 4 Integration 1.8 Release Notes
---



## 1.8.0

These release notes describe changes to the Unreal Engine versions 4.12 and 4.13 available from the Oculus GitHub repository.

The Oculus UE4 integration ships with various versions of Unreal, and there is no external SDK per se. Clicking on the "Download" link above will redirect you to our [Unreal Game Engine](/documentation/unreal/latest/concepts/unreal-engine/), which walks through various options for working with the Oculus Unreal integration.

Unreal provides built-in support for Oculus Rift and Gear VR development on Windows, and Unreal apps run on the Oculus platform automatically apply stereoscopic rendering to the main camera as well as positional and orientation tracking for the Rift, or orientation tracking for Gear VR.

New Features

* Added support for the Oculus Guardian System, which visualizes the bounds of a user-defined Play Area. Note that it is currently unsupported by public versions of the Oculus runtime. See [Guardian System Boundary Component](/documentation/unreal/latest/concepts/unreal-boundary/ "OculusBoundaryComponent exposes an API for interacting with the Oculus Guardian System.") for more information.
* Added depth ordering support to VR compositor layers.
* Added cubemap support for VR compositor overlays to 4.13 (mobile only).
* Added Online Subsystem support for Regular Leaderboards and Cloudsaves.
* Added a Blueprint for retrieving Oculus ID/Username.
* Added Blueprints for UOculusRiftBoundaryComponent public methods.


API Changes

* Added OculusRiftBoundaryComponent API for the Oculus Guardian System.


Bug Fixes

* Fixed black screen issue affecting Samsung Note4 and certain Adreno-based devices.


Known Issues

* UE4.12 and 4.13 in Oculus GitHub repository: A significant drop in frame rate occurs when UE4 is not in focus in VR preview mode. To avoid this issue, uncheck the Use Less CPU when in **Background** in **Edit** &gt; **Editor Preferences** &gt; **General** (left sidebar) &gt; **Miscellaneous** (left sidebar) &gt; **Performance**.
* Exclusive Mode issues: Multiple initializations of the DXGISwapChain may cause flickering as the screen switches modes and a black screen when rendering to the Rift with a different GPU from the one the game is using to render the eye buffers.
* **Stereo Layer Position Type**: **World Locked** is not currently supported for cylinder TimeWarp overlays. 

