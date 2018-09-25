---
title: Oculus Unreal Engine 4 Integration 1.9 Release Notes
---
## 1.9.0

These release notes describe changes to Oculus's Unreal Engine 4.12 and 4.13 available from the Oculus GitHub repository.

New Features

* Added VoIP and moderated room finding/joining support, available through the Online Subsystems interface. 
Bug Fixes

* Fixed near clipping plane calculation, which was incorrect when WorldToMetersScale was set to a value other than 100.
Known Issues

* UE4.12 and 4.13 in Oculus GitHub repository: A significant drop in frame rate occurs when UE4 is not in focus in VR preview mode. To avoid this issue, uncheck the Use Less CPU when in **Background** in **Edit** > **Editor Preferences** > **General** (left sidebar) > **Miscellaneous** (left sidebar) > **Performance**.
* Exclusive Mode issues: Multiple initializations of the DXGISwapChain may cause flickering as the screen switches modes and a black screen when rendering to the Rift with a different GPU from the one the game is using to render the eye buffers.
* **Stereo Layer Position Type**: **World Locked** is not currently supported for cylinder TimeWarp overlays. 
