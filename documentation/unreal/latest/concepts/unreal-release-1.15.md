---
title: Oculus Unreal Engine 4 Integration 1.15 Release Notes
---
These release notes describe changes to Oculus's Unreal Engine 4.15 and 4.16 available from the Oculus GitHub repository.

## 1.15.0

**OculusVR Plugin**

With the 1.15 integration we are releasing versions of 4.15 and 4.16 that include a substantial refactor of our Unreal plugins. Our OculusRiftHMD, GearVR, OculusInput, and OculusFunctionLibrary plugins have been combined into a unified OculusVR plugin. All functionality may be accessed by enabling the OculusVR plugin.

This plugin refactor will provide a consistent and unified interface to develop against for all current and future Oculus devices. All feature development will be based on the OculusVR plugin going forward.

Note that in the 4.16 version no longer supports the exec-style “hmd …” console commands - they have been replaced by console variables. See “UE4-Oculus.txt” in the root directory for a description of available console variables.

Please let us know if you have any questions, suggestions, or problems in our [Unreal Developer Forum](https://forums.oculus.com/developer/categories/unreal).

New Features

* Added Rift support to cylinder VR Compositor Layers. 
Known Issues

* A significant drop in frame rate occurs when UE4 is not in focus in VR preview mode. To avoid this issue, uncheck the Use Less CPU when in **Background** in **Edit** > **Editor Preferences** > **General** (left sidebar) > **Miscellaneous** (left sidebar) > **Performance**.
* Exclusive Mode issues: Setting the mirror window to full-screen exclusive mode will not work correctly if the monitor and HMD are connected to different GPUs.
* Stereo Layer Depth Ordering: Doesn’t support head-locked layers, only world-locked and tracker-locked.
* Oculus Blueprints not visible in Level Blueprint in Epic launcher and Epic source versions when Gear VR Plugin is enabled. Workaround for source version: open the file GearVR.uplugin and replace "WhitelistPlatforms" : ["Android"] with "WhitelistPlatforms" : [ "Android", "Win64", "Win32" ]. This does not affect source shipped through the Oculus Unreal GitHub repository.
* UE4 Issue - UE4 builds fail when using Android SDK tools 25 or newer. Please review the [UE Answers](https://answers.unrealengine.com/questions/570870/latest-android-sdk-is-not-supported.html) page related to this issue for more information.
