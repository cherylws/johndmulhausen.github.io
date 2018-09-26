---
title: Oculus Unreal Engine 4 Integration 1.10 Release Notes
---



## 1.10.0

These release notes describe changes to Oculus's Unreal Engine 4.12, 4.13, and 4.14 available from the Oculus GitHub repository.

New Features

* Added experimental multi-view support for mobile development, which reduces CPU overhead by duplicating objects to both eye buffers during rendering. Currently supports Note5, S6, S7, and S7 Edge phones running Android M or N and using ARM Exynos processors. Requires OpenGL ES 2. For more information, see **Multi-View** in [Unreal Mobile Development](unreal-gsg-mobile "HOW DOES THIS JIVE WITH THE PREVIOUS SECTION, GETTING STARTED? This guide covers environment setup, project configuration, and development for the Oculus mobile platform using Unreal.").
* Added “Browse” matchmaking support in OnlineSessionOculus.
	+ Added ability to create a matchmaking room.
	+ Added ability to find matchmaking rooms in Browse mode.
	+ Added Blueprints to Create and Find matchmaking rooms.
	


Bug Fixes

* Fixed Oculus Blueprints error calling Activate() twice.
* Fixed crash when Oculus Cloud Saves used when the application is not installed.


Known Issues

* A significant drop in framerate occurs when UE4 is not in focus in VR preview mode. To avoid this issue, uncheck the Use Less CPU when in **Background** in **Edit** &gt; **Editor Preferences** &gt; **General** (left sidebar) &gt; **Miscellaneous** (left sidebar) &gt; **Performance**.
* Exclusive Mode issues: Multiple initializations of the DXGISwapChain may cause flickering as the screen switches modes and a black screen when rendering to the Rift with a different GPU from the one the game is using to render the eye buffers.
* Stereo Layer Depth Ordering: Doesnâ€™t support head-locked layers, only world-locked and tracker-locked.

