---
title: Oculus Unreal Engine 4 Integration 1.21 Release Notes
---

These release notes describe changes to Oculus's Unreal Engine 4.17 and 4.18 available from the Oculus GitHub repository.

## 1.21.0

## Oculus Dash Support

Rift Core 2.0 introduces substantial changes to Oculus Home and replaces the Universal Menu with Oculus Dash. We plan to roll it out to Rift users with the 1.22 runtime in early 2018.

We recommend adding Dash support to your application to provide the best possible user experience. Developers who would like to add Dash support before it rolls out in early 2018 can test it using Oculus runtime 1.21, which includes preview support. Runtime 1.21 is now available through our opt-in Public Test Channel (PTC).

For more information, please see [Oculus Dash](/documentation/unreal/latest/concepts/unreal-dash/). 

New Features

* Added Oculus Go to GetHMDDeviceName.
* Improved Single-Pass Stereo Rendering by injecting masking code only for translucent objects.


Bug Fixes

* Fixed affinity problem that slowed the render thread in some cases.
* Fixed Gear VR Controller touchpad issue affecting capacitive touch.
* Fixed 10 FPS lock initialization bug when the HMD not mounted.
* Unreal 4.18 and 4.18.1 mobile fixed issue causing UOculusFunctionLibrary::IsDeviceTracked() to return false even if a Gear VR Controller is connected and active.


Known Issues

* A significant drop in frame rate occurs when UE4 is not in focus in VR preview mode. To avoid this issue, uncheck the Use Less CPU when in **Background** in **Edit** &gt; **Editor Preferences** &gt; **General** (left sidebar) &gt; **Miscellaneous** (left sidebar) &gt; **Performance**.
* Exclusive Mode issues: Setting the mirror window to full-screen exclusive mode will not work correctly if the monitor and HMD are connected to different GPUs.
* Stereo Layer Depth Ordering: Doesnâ€™t support head-locked layers, only world-locked and tracker-locked.
* Oculus UE4 1.15 and earlier: Oculus Blueprints not visible in Level Blueprint in Epic launcher and Epic source versions when Gear VR Plugin is enabled. Workaround for source version: open the file GearVR.uplugin and replace "WhitelistPlatforms" : ["Android"] with "WhitelistPlatforms" : [ "Android", "Win64", "Win32" ]. This does not affect source shipped through the Oculus Unreal GitHub repository.
* UE4 Issue - UE4 builds fail when using Android SDK tools 25 or newer. Please review the [UE Answers](https://answers.unrealengine.com/questions/570870/) page related to this issue for more information.
* Hybrid Monoscopic Rendering: In Unreal version 4.15, this feature is available for mobile only.

