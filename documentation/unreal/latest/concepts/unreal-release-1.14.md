---
title: Oculus Unreal Engine 4 Integration 1.14 Release Notes
---

These release notes describe changes to Oculus's Unreal Engine 4.14, 4.15, and 4.16 available from the Oculus GitHub repository.

## 1.14.0

The Oculus Avatar SDK now provides a plugin for Unreal to assist developers with implementing first-person hand presence for the Rift and Touch controllers. It includes avatar hand and body assets viewable by other users in social applications for Rift and Gear VR. For installation and use instructions, please see [Getting Started with Unreal](/documentation/avatarsdk/latest/concepts/avatars-gsg-unreal/) in our Avatar documentation. 

**Preview of Unified OculusVR Plugin**

With the 1.14 integration we are releasing versions of 4.15 and 4.16 that include a preview of a substantial refactor of our Unreal plugins. Our OculusRiftHMD, GearVR, OculusInput, and OculusFunctionLibrary plugins have been combined into a unified OculusVR plugin. All functionality may be accessed by enabling the OculusVR plugin.

This plugin refactor will provide a consistent and unified interface to develop against for all current and future Oculus devices. All feature development will be based on the OculusVR plugin going forward.

Note that in the 4.16 version no longer supports the exec-style “hmd …” console commands - they have been replaced by console variables. See “UE4-Oculus.txt” in the root directory for a description of available console variables.

Preview releases containing the unified OculusVR plugin are available here:

* [Unreal 4.15 Unified](https://github.com/Oculus-VR/UnrealEngine/tree/4.15-unified)
* [Unreal 4.16 Unified](https://github.com/Oculus-VR/UnrealEngine/tree/4.16-unified)


Access requires a GitHub account subscribed to the private EpicGames/UnrealEngine repository (instructions [here](https://www.unrealengine.com/ue4-on-github)). If you are not logged into a subscribed account, you will get a 404 error from GitHub.

Please let us know if you have any questions, suggestions, or problems in our [Unreal Developer Forum](https://forums.oculus.com/developer/categories/unreal) .

New Features

* Online Subsystems
	+ Added a warning if the message task that handles popping OVR messages does not run in four seconds (it should run every tick).
	+ If the initial NetDriver connection times out, it now retries until the amount of time specified by InitialConnectTimeout in DefaultEngine.ini passes.
	


Known Issues

* A significant drop in frame rate occurs when UE4 is not in focus in VR preview mode. To avoid this issue, uncheck the Use Less CPU when in **Background** in **Edit** &gt; **Editor Preferences** &gt; **General** (left sidebar) &gt; **Miscellaneous** (left sidebar) &gt; **Performance**.
* Exclusive Mode issues: Setting the mirror window to full-screen exclusive mode will not work correctly if the monitor and HMD are connected to different GPUs.
* Stereo Layer Depth Ordering: Doesnâ€™t support head-locked layers, only world-locked and tracker-locked.
* Oculus Blueprints not visible in Level Blueprint in Epic launcher and Epic source versions when Gear VR Plugin is enabled. Workaround for source version: open the file GearVR.uplugin and replace "WhitelistPlatforms" : ["Android"] with "WhitelistPlatforms" : [ "Android", "Win64", "Win32" ]. This does not affect source shipped through the Oculus Unreal GitHub repository.

