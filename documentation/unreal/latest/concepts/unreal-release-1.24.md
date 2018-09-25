---
title: Oculus Unreal Engine 4 Integration 1.24 Release Notes
---
These release notes describe changes to Oculus's Unreal Engine 4.18 and 4.19 available from the Oculus GitHub repository.

## 1.24.0

New Features

* The Oculus Unreal Engine 4 integration for Android now takes advantage of 64-bit CPU features. You can select this option within the UE4 editor. Depending on what your application does, this may improve performance. Oculus will publish more detailed guidance on how this can affect performance in the near future.
Bug Fixes

* Not applicable
Known Issues

* There's a bug affecting the ovr\_SetBoundaryLookAndFeel API by which color set operations to the visualized boundary grid don't work if they're called while the HMD is not being worn.
* A significant drop in frame rate occurs when UE4 is not in focus in VR preview mode. To avoid this issue, uncheck the Use Less CPU when in **Background** in **Edit** > **Editor Preferences** > **General** (left sidebar) > **Miscellaneous** (left sidebar) > **Performance**.
* Exclusive Mode issues: Setting the mirror window to full-screen exclusive mode will not work correctly if the monitor and HMD are connected to different GPUs.
* Stereo Layer Depth Ordering: Doesnâ€™t support head-locked layers, only world-locked and tracker-locked.
* Hybrid Monoscopic Rendering: In Unreal version 4.15, this feature is available for mobile only.
