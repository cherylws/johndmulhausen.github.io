---
title: Oculus Unreal Engine 4 Integration 1.13 Release Notes
---

These release notes describe changes to Oculus's Unreal Engine 4.14 and 4.15 available from the Oculus GitHub repository.

## 1.13.0

New Features

* 4.15: Added GearVRControllerComponent, which creates a MotionController with a Gear VR Controller mesh as a child. The Gear VR Controller mesh may be found in Plugins/GearVR/Content/. 


Bug Fixes

* Fixed black screen issue caused by lowering pixel density to certain values on Qualcomm devices.
* Fixed a race condition causing the GearVRController plugin to crash while the game was shutting down.


Known Issues

* A significant drop in frame rate occurs when UE4 is not in focus in VR preview mode. To avoid this issue, uncheck the Use Less CPU when in **Background** in **Edit** &gt; **Editor Preferences** &gt; **General** (left sidebar) &gt; **Miscellaneous** (left sidebar) &gt; **Performance**.
* Exclusive Mode issues: Setting the mirror window to full-screen exclusive mode will not work correctly if the monitor and HMD are connected to different GPUs.
* Stereo Layer Depth Ordering: Doesnâ€™t support head-locked layers, only world-locked and tracker-locked.
* Oculus Blueprints not visible in Level Blueprint in Epic launcher and Epic source versions when Gear VR Plugin is enabled. Workaround for source version: open the file GearVR.uplugin and replace "WhitelistPlatforms" : ["Android"] with "WhitelistPlatforms" : [ "Android", "Win64", "Win32" ]. This does not affect source shipped through the Oculus Unreal GitHub repository.

