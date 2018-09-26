---
title: Oculus Unreal Engine 4 Integration 1.27 Release Notes
---

These release notes describe changes to Oculus's Unreal Engine 4.19 available from the Oculus GitHub repository.

## 1.27.0

New Features

* **Mask-Based Foveated Rendering (MBFR)** – MBFR is now available for Unreal developers who are targeting the Oculus Rift. MBFR reduces GPU pixel shading cost by dropping a subset of the pixels in the world rendering passes. Please see .[Oculus Rift: Mask-Based Foveated Rendering](https://developer.oculus.com/documentation/unreal/latest/concepts/unreal-mbfr/).
* **UE4 Documentation Enhancements** – This document has been significantly enhanced, in order to make it easier for developers to use the Unreal Game Engine. Please see the blog article [Improved Guidance for Unreal Developers](https://developer.oculus.com/blog/improved-guidance-for-unreal-developers/).


Bug Fixes

* Not applicable


Known Issues

* There is a bug affecting the ovr\_SetBoundaryLookAndFeel API by which color set operations to the visualized boundary grid do not work if they are called while the HMD is not being worn.
* A significant drop in frame rate occurs when UE4 is not in focus in VR preview mode. To avoid this issue, uncheck the Use Less CPU when in **Background** in **Edit** &gt; **Editor Preferences** &gt; **General** (left sidebar) &gt; **Miscellaneous** (left sidebar) &gt; **Performance**.
* Exclusive Mode issue: Setting the mirror window to full-screen exclusive mode will not work correctly if the monitor and HMD are connected to different GPUs.
* Stereo Layer Depth Ordering does not support head-locked layers. It only supports world-locked and tracker-locked layers.

