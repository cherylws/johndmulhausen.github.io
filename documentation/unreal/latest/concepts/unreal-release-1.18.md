---
title: Oculus Unreal Engine 4 Integration 1.18 Release Notes
---

These release notes describe changes to Oculus's Unreal Engine 4.17 available from the Oculus GitHub repository.

## 1.18.0

New Features

* Added Input Focus and System Overlay support - see [unresolvable-reference.xml](unresolvable-reference) for more information.
	+ Added Has Input Focus flag to Oculus Library. When an application loses input focus, applications should typically hide tracked controllers in the scene.
	+ Added Has System Overlay Present flag to Oculus Library. When system overlay status changes, applications should typically pause and mute.
	+ Added depth buffer sharing with the compositor. Depth buffer rendering is enabled by default.
	
* Touch Sample
	+ Added VRCharacter Blueprint illustrating how to hide tracked controllers when an application loses input focus.
	+ Added Pose Actor illustrating how to pause a simple application using SystemOverlayPresent flag.
	


Known Issues

* A significant drop in frame rate occurs when UE4 is not in focus in VR preview mode. To avoid this issue, uncheck the Use Less CPU when in **Background** in **Edit** &gt; **Editor Preferences** &gt; **General** (left sidebar) &gt; **Miscellaneous** (left sidebar) &gt; **Performance**.
* Exclusive Mode issues: Setting the mirror window to full-screen exclusive mode will not work correctly if the monitor and HMD are connected to different GPUs.
* Stereo Layer Depth Ordering: Doesnâ€™t support head-locked layers, only world-locked and tracker-locked.
* Oculus UE4 1.15 and earlier: Oculus Blueprints not visible in Level Blueprint in Epic launcher and Epic source versions when Gear VR Plugin is enabled. Workaround for source version: open the file GearVR.uplugin and replace "WhitelistPlatforms" : ["Android"] with "WhitelistPlatforms" : [ "Android", "Win64", "Win32" ]. This does not affect source shipped through the Oculus Unreal GitHub repository.
* UE4 Issue - UE4 builds fail when using Android SDK tools 25 or newer. Please review the [UE Answers](https://answers.unrealengine.com/questions/570870/latest-android-sdk-is-not-supported.html) page related to this issue for more information.
* Hybrid Monoscopic Rendering: In Unreal version 4.15, this feature is available for mobile only, and may not be used with Multi-view.

