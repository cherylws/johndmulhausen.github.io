---
title: Oculus Unreal Engine 4 Integration 1.22 Release Notes
---

These release notes describe changes to Oculus's Unreal Engine 4.18 and 4.19 available from the Oculus GitHub repository.

## 1.22.0

## Oculus Dash Support

Rift Core 2.0 introduces substantial changes to Oculus Home and replaces the Universal Menu with Oculus Dash.

We recommend adding Dash support to your application to provide the best possible user experience. Developers who would like to add Dash support before upgrading to PC-SDK 1.22 can test it using Oculus runtime 1.21, which includes preview support. Runtime 1.21 is available through our opt-in Public Test Channel (PTC).

For more information, please see [Oculus Dash](/documentation/unreal/latest/concepts/unreal-dash/). 

New Features

* Added support for Unreal Engine 4.19.


Bug Fixes

* Not applicable


Known Issues

* A significant drop in frame rate occurs when UE4 is not in focus in VR preview mode. To avoid this issue, uncheck the Use Less CPU when in **Background** in **Edit** &gt; **Editor Preferences** &gt; **General** (left sidebar) &gt; **Miscellaneous** (left sidebar) &gt; **Performance**.
* Exclusive Mode issues: Setting the mirror window to full-screen exclusive mode will not work correctly if the monitor and HMD are connected to different GPUs.
* Stereo Layer Depth Ordering: Doesnâ€™t support head-locked layers, only world-locked and tracker-locked.
* Hybrid Monoscopic Rendering: In Unreal version 4.15, this feature is available for mobile only.

