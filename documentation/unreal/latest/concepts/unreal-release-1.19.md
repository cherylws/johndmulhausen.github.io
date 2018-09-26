---
title: Oculus Unreal Engine 4 Integration 1.19 Release Notes
---

These release notes describe changes to Oculus's Unreal Engine 4.17 and 4.18 available from the Oculus GitHub repository.

## Dash Support

At Oculus Connect 4 we announced Rift Core 2.0, which includes substantial changes to Oculus Home and will replace our Universal Menu with Oculus Dash. We plan to make it available with the 1.21 runtime in early December.

Dash re-implements Universal Menu as a VR compositor layer. Have a look at our Blog announcement and watch the Dash video to get a sense of how it works.

We have added new application lifecycle support to our 1.18 integration in preparation for Dash. When Dash draws a menu overlay, the new Has Input Focus flag will return false, indicating that the application should pause and mute and the tracked controllers and hands be hidden from the scene, as Dash provides its own UI. Depending on the application, additional action may also be warranted when input focus is lost (e.g., during a multi-player combat game, you may wish to freeze the player’s avatar and make it temporarily invulnerable to other players).

In Oculus Unreal Integration 1.19 and later, Dash may be enabled with bSupportsDash=true under Oculus.Settings in defaultengine.ini.

For more information, see [unresolvable-reference.xml](unresolvable-reference).

Additional information about supporting Dash will be available soon.

## 1.19.0

New Features

* Mixed Reality Capture - see [Oculus Rift: Mixed Reality Capture](/documentation/unreal/latest/concepts/unreal-mrc/ "This guide describes how to add and configure mixed reality capture support for your Unreal application. Mixed reality capture is supported for Rift applications only.") for more information.
	+ Added Chroma Key options for direct composition. Removed green screen tolerance, alpha cutoff, and color shadows settings.
	+ Added configuration support using Engine.ini.
	+ Added a dynamic lighting option, which illuminates video content with application lights and flashes (e.g., the interpolated person in the scene is illuminated by explosions).
	+ Added ZED camera support. ZED cameras provide depth information that can be used to present more realistic dynamic lighting in direct composition. Requires ZED SDK 2.1.x or later.
	+ Added Virtual Green Screen, which confines interpolated camera stream content to an area defined by Guardian System configuration.
	+ Added hand pose latency correction.
	
* Added bSupportsDash support to Oculus.Settings in Engine.ini (default is false). Setting to true will signal Oculus runtime that the application supports in-application input focus loss for the Dash UI menu (expected to ship in early December). 


API Changes

* Removed Has System Overlay Present. All application lifecycle handling is currently enabled by Has Input Focus.


Bug Fixes

* Fixed bug causing inconsistent Guardian System Boundary Component rotation and position when camera is in implicit mode. 


Known Issues

* A significant drop in frame rate occurs when UE4 is not in focus in VR preview mode. To avoid this issue, uncheck the Use Less CPU when in **Background** in **Edit** &gt; **Editor Preferences** &gt; **General** (left sidebar) &gt; **Miscellaneous** (left sidebar) &gt; **Performance**.
* Exclusive Mode issues: Setting the mirror window to full-screen exclusive mode will not work correctly if the monitor and HMD are connected to different GPUs.
* Stereo Layer Depth Ordering: Doesnâ€™t support head-locked layers, only world-locked and tracker-locked.
* Oculus UE4 1.15 and earlier: Oculus Blueprints not visible in Level Blueprint in Epic launcher and Epic source versions when Gear VR Plugin is enabled. Workaround for source version: open the file GearVR.uplugin and replace "WhitelistPlatforms" : ["Android"] with "WhitelistPlatforms" : [ "Android", "Win64", "Win32" ]. This does not affect source shipped through the Oculus Unreal GitHub repository.
* UE4 Issue - UE4 builds fail when using Android SDK tools 25 or newer. Please review the [UE Answers](https://answers.unrealengine.com/questions/570870/latest-android-sdk-is-not-supported.html) page related to this issue for more information.
* Hybrid Monoscopic Rendering: In Unreal version 4.15, this feature is available for mobile only, and may not be used with Multi-view.

