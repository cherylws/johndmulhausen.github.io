---
title: Oculus Unreal Engine 4 Integration 1.16 Release Notes
---
These release notes describe changes to Oculus's Unreal Engine 4.16 available from the Oculus GitHub repository.

## 1.16.0

Oculus-1.16 adds support for mixed reality capture (Rift only), which places real-world objects in VR. It allows live video footage of a Rift user to be composited with the output from a game to create combined video that showed the player in a virtual scene. For more information, see [Oculus Rift: Mixed Reality Capture](/documentation/unreal/latest/concepts/unreal-mrc/ "This guide describes how to add and configure mixed reality capture support for your Unreal application. Mixed reality capture is supported for Rift applications only.").

New Features

* Oculus-1.16 adds support for mixed reality capture (Rift only), which allows live video footage of a Rift user to be composited with the output from a game to create combined video that showed the player in a virtual scene. For more information, see [Oculus Rift: Mixed Reality Capture](/documentation/unreal/latest/concepts/unreal-mrc/ "This guide describes how to add and configure mixed reality capture support for your Unreal application. Mixed reality capture is supported for Rift applications only.").
* Added sample map with mixed reality capture enabled to Collaboration\Oculus\Public\MixedRealitySample.
* Refactored Blueprints for unified Oculus plugin model. See [Blueprints Reference](/documentation/unreal/latest/concepts/unreal-blueprints/ "This section serves as a reference guide for the Blueprints in the Online Subsystem Oculus library.") for more information.
* Added Blueprints for simplified Loading Screen support.
* Added Android graphics debugging support to our 4.16 branch. See [unresolvable-reference.xml](unresolvable-reference) for more information.
	+ 4.16-oculus added RenderDoc graphics debugging support (Android only, experimental) 
	+ 4.16-oculus added Mali Graphics Debugger support (Android only, requires a Mali phone such as the Android GALAXY S6).
	
API Changes

* Removed default loading screen. Use defaultengine.ini or loading screen Blueprints to add a loading screen to your application. See [Splash Screens](/documentation/unreal/latest/concepts/unreal-loading-screens/ "We strongly recommend adding a loading splash screen to your Rift or mobile application. Loading splash screens are required by the Oculus Store.") for more information. 
* Added anyhand setting to motion controller component. It will attach to any Gear VR Controller, whether left-handed or right-handed.
Known Issues

* A significant drop in frame rate occurs when UE4 is not in focus in VR preview mode. To avoid this issue, uncheck the Use Less CPU when in **Background** in **Edit** > **Editor Preferences** > **General** (left sidebar) > **Miscellaneous** (left sidebar) > **Performance**.
* Exclusive Mode issues: Setting the mirror window to full-screen exclusive mode will not work correctly if the monitor and HMD are connected to different GPUs.
* Stereo Layer Depth Ordering: Doesnâ€™t support head-locked layers, only world-locked and tracker-locked.
* Oculus UE4 1.15 and earlier: Oculus Blueprints not visible in Level Blueprint in Epic launcher and Epic source versions when Gear VR Plugin is enabled. Workaround for source version: open the file GearVR.uplugin and replace "WhitelistPlatforms" : ["Android"] with "WhitelistPlatforms" : [ "Android", "Win64", "Win32" ]. This does not affect source shipped through the Oculus Unreal GitHub repository.
* UE4 Issue - UE4 builds fail when using Android SDK tools 25 or newer. Please review the [UE Answers](https://answers.unrealengine.com/questions/570870/latest-android-sdk-is-not-supported.html) page related to this issue for more information.
