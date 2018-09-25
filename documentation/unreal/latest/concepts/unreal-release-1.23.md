---
title: Oculus Unreal Engine 4 Integration 1.23 Release Notes
---
These release notes describe changes to Oculus's Unreal Engine 4.18 and 4.19 available from the Oculus GitHub repository.

## 1.23.0

## Oculus Dash Support

As of release 1.22, Rift Core 2.0 introduces substantial changes to Oculus Home and replaces the Universal Menu with Oculus Dash.

We recommend adding Dash support to your application to provide the best possible user experience.

For more information, please see [Oculus Dash](/documentation/unreal/latest/concepts/unreal-dash/ "This guide describes how to add Oculus Dash support to Unreal applications."). 

New Features

* A latency reduction for late-update has been integrated into this release. This is particularly helpful for Oculus mobile platforms. 
Bug Fixes

* Not applicable
Known Issues

* There's a bug affecting the ovr\_SetBoundaryLookAndFeel API by which color set operations to the visualized boundary grid don't work if they're called while the HMD is not being worn.
* A significant drop in frame rate occurs when UE4 is not in focus in VR preview mode. To avoid this issue, uncheck the Use Less CPU when in **Background** in **Edit** > **Editor Preferences** > **General** (left sidebar) > **Miscellaneous** (left sidebar) > **Performance**.
* Exclusive Mode issues: Setting the mirror window to full-screen exclusive mode will not work correctly if the monitor and HMD are connected to different GPUs.
* Stereo Layer Depth Ordering: Doesnâ€™t support head-locked layers, only world-locked and tracker-locked.
* Hybrid Monoscopic Rendering: In Unreal version 4.15, this feature is available for mobile only.
