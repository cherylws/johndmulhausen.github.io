---
title: Oculus Unreal Engine 4 Integration 1.26 Release Notes
---
These release notes describe changes to Oculus's Unreal Engine 4.19 available from the Oculus GitHub repository.

## 1.26.0

New Features

* **Name Change for UE4 Editor Setting** – The setting called “Configure the AndroidManifest for deployment to GearVR” in the Unreal Editor, under Project Settings>Android>Advanced APK Packaging, has been renamed to “Configure the AndroidManifest for deployment to Oculus Mobile”. This change was made because Oculus now supports two mobile platforms, Oculus Go and Gear VR. 
* **Vibration and Global Sound Settings for Android** – By default when you package an Android application, it asks for permissions to vibrate the phone and modify the global sound volume. These settings are counterproductive with VR applications, and have been removed.
* **Reduced Dependency on Google GMS** – The Oculus Unreal integration is now less dependent on Google Mobile Services (GMS) API calls, when compiled for Gear VR.
* **Blueprint Support for Orientation/Positional Tracking** – Blueprints are now provided to enable/disable orientation tracking and positional tracking. Orientation tracking is supported by the blueprint Enable Orientation Tracking, and is available on all Oculus headsets. Positional tracking is supported by the blueprint Enable Position Tracking, and is only available for the Oculus Rift. This feature can be useful, for example, if you wish to analyze an application's performance when tracking is disabled, and compare that to the performance characteristics when tracking is enabled. 
* **Mirror Window FPS with Vulkan** – A temporary feature has been applied so that rendering to a mirror window with the Vulkan API is not limited by the display refresh rate of the monitor where the mirror window is shown. An improved method for handling this will be provided in the future.
Bug Fixes

* **Controller Input Read from Previous Frame** – Fixed a bug where controller input was being read from the previous frame's data (causing a potential race condition).
Known Issues

* There is a bug affecting the ovr\_SetBoundaryLookAndFeel API by which color set operations to the visualized boundary grid do not work if they are called while the HMD is not being worn.
* A significant drop in frame rate occurs when UE4 is not in focus in VR preview mode. To avoid this issue, uncheck the Use Less CPU when in **Background** in **Edit** > **Editor Preferences** > **General** (left sidebar) > **Miscellaneous** (left sidebar) > **Performance**.
* Exclusive Mode issue: Setting the mirror window to full-screen exclusive mode will not work correctly if the monitor and HMD are connected to different GPUs.
* Stereo Layer Depth Ordering does not support head-locked layers. It only supports world-locked and tracker-locked layers.
