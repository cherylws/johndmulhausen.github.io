---
title: Oculus Unreal Engine 4 Integration 1.12 Release Notes
---
These release notes describe changes to Oculus's Unreal Engine 4.14 and 4.15 available from the Oculus GitHub repository.

## 1.12.0

New Features

* Added support for Gear VR Controller. See [Gear VR Controller and Headset Touchpad](/documentation/unreal/latest/concepts/unreal-gear-vr-controller/ "The Gear VR Controller is an orientation-tracked input device that can be accessed through standard Unreal Blueprints, and through Oculus-specific Blueprints. The Gear VR Touchpad is mounted on the side of the headset, and can be accessed via Oculus-specific Blueprints.") for more information.
* Added Direct Multi-View support, which can substantially reduce GPU overhead. See [Oculus Go and Gear VR: Multi-View](/documentation/unreal/latest/concepts/unreal-multi-view/ "Multi-View is an advanced rendering feature for Oculus Go and Gear VR. If your application is CPU-bound, we strongly recommend using Multi-View to improve performance.") for more information.
Bug Fixes

* Fixed Adaptive Pixel Density flickering when ASW is enabled.
Known Issues

* A significant drop in frame rate occurs when UE4 is not in focus in VR preview mode. To avoid this issue, uncheck the Use Less CPU when in **Background** in **Edit** > **Editor Preferences** > **General** (left sidebar) > **Miscellaneous** (left sidebar) > **Performance**.
* Exclusive Mode issues: Setting the mirror window to full-screen exclusive mode will not work correctly if the monitor and HMD are connected to different GPUs.
* Stereo Layer Depth Ordering: Doesnâ€™t support head-locked layers, only world-locked and tracker-locked.
* Oculus Blueprints not visible in Level Blueprint in Epic launcher and Epic source versions when Gear VR Plugin is enabled. Workaround for source version: open the file GearVR.uplugin and replace "WhitelistPlatforms" : ["Android"] with "WhitelistPlatforms" : [ "Android", "Win64", "Win32" ]. This does not affect source shipped through the Oculus Unreal GitHub repository.
