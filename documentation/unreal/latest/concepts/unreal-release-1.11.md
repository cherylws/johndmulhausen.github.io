---
title: Oculus Unreal Engine 4 Integration 1.11 Release Notes
---
These release notes describe changes to Oculus's Unreal Engine 4.13, 4.14, and 4.15 available from the Oculus GitHub repository.

## 1.11.0

Oculus distributes integrations of the Unreal Engine which include the latest Oculus SDKs to provide up-to-date support for Oculus Rift and Gear VR.

New Features

* Added GDB debugging support. See “GDB” in [unresolvable-reference.xml](unresolvable-reference) in Unreal for more information.
* Added three Blueprint samples, available from our [GitHub repository](https://github.com/Oculus-VR/UnrealEngine). For more on how to access our repository, see our Developer Guide Introduction.
	+ BoundarySample illustrates use of the [Boundary Component API](/documentation/unreal/latest/concepts/unreal-boundary/ "OculusBoundaryComponent exposes an API for interacting with the Oculus Guardian System.") for interacting with our Guardian System.
	+ LayerSample illustrates the use of [VR Compositor Layers](/documentation/unreal/latest/concepts/unreal-overlay/ "With Unreal, you may add transparent or opaque quadrilateral, cubemap, or cylindrical overlays to your level as compositor layers.").
	+ TouchSample illustrates basic use of Oculus Touch, including [haptics](/documentation/unreal/latest/concepts/unreal-haptics/ "This guide describes how to use Unreal Blueprints to control haptic effects on Touch or Xbox controllers.").
	
* Online Subsystems
	+ LeaderboardInterface now allows for querying of just the user's entry by calling ReadLeaderboards() with an array of just the current user id.
	+ SessionInterface
		- Added the ability to populate the LocalOwnerId with the current user.
		- DumpSessionState() now dumps out all individual existing named sessions.
		
	
Bug Fixes

* Added support for wire frame representation of objects while using the 11:11:10 LDR format
* Online Subsystems
	+ AchievementInterface: Fixed casting WriteAchievement for Count values for Int64, UInt32, and UInt64.
	+ Fixed bug preventing the UE4 Read Leaderboard blueprint node from working with the Oculus OSS.
	+ SessionInterface: Fixed a NullPointerException when getting the oculus id from a session
		- Allow for updating the Room Data Store through the UpdateSession(). Will save the UE4 Session Settings into the Room Data Store.
		- Fixed a bug causing TriggerMatchmakingCompleteDelegates to fire too early
		- Session.bHosting now returns if the current user is the host/owner of the session.
		
	
Known Issues

* Adaptive Pixel Density is not currently working and should be disabled. If applications using Adaptive Pixel Density reach 45 Hz, they will remain stuck at that frame rate until relaunched. A fix is planned for the Rift 1.12 runtime release and should not require any application changes.
* A significant drop in frame rate occurs when UE4 is not in focus in VR preview mode. To avoid this issue, uncheck the Use Less CPU when in **Background** in **Edit** > **Editor Preferences** > **General** (left sidebar) > **Miscellaneous** (left sidebar) > **Performance**.
* Exclusive Mode issues: Multiple initializations of the DXGISwapChain may cause flickering as the screen switches modes and a black screen when rendering to the Rift with a different GPU from the one the game is using to render the eye buffers.
* Stereo Layer Depth Ordering: Doesn’t support head-locked layers, only world-locked and tracker-locked.
* Oculus Blueprints not visible in Level Blueprint in Epic launcher and Epic source versions when Gear VR Plugin is enabled. Workaround for source version: open the file GearVR.uplugin and replace "WhitelistPlatforms" : ["Android"] with "WhitelistPlatforms" : [ "Android", "Win64", "Win32" ]. This does not affect source shipped through the Oculus Unreal GitHub repository.
