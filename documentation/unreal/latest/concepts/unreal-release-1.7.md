---
title: Oculus Unreal Engine 4 Integration 1.7 Release Notes
---



## 1.7.0

Unreal provides built-in support for Oculus Rift and Gear VR development on Windows.

Unreal apps run on the Oculus platform automatically apply stereoscopic rendering to the main camera as well as positional and orientation tracking for the Rift, or orientation tracking for Gear VR.

For more information on downloading and using the Oculus Unreal integration, please see [Unreal Game Engine](/documentation/unreal/latest/concepts/unreal-engine/).

## Online Subsystems

Several features of the Oculus Platform SDK may be accessed through the Unreal Online Subsystems interface:

* Achievements
* Rooms 
* Matchmaking
* Identity
* Entitlements
* P2P networking
* Friends leaderboards


Friends leaderboards is not currently available through Online Subsystems in Epic’s 4.13 Preview build. 

Not all functionality of these features is available through the Online Subsystems interface. Developers who need unsupported features should use the Oculus Platform Plugin available with our Platform SDK.

Online Subsystems access is available in the following ways:

* Oculus Platform SDK v. 1.6 and 1.7 include a standalone OSS plugin (Rift only)
* Epic GitHub: 4.13.0-preview-2 includes OSS support (Rift and Gear VR)
* Oculus GitHub: oculus-4.12.5-release-1.7.0 and oculus-4.13.0-preview-2-1.7.0 includes OSS support (Rift and Gear VR)


For more information on Unreal Subsystems, see Epic’s Online Subsystems Overview.

New Features

* Added adaptive viewport scaling, which automatically changes pixel density based on resource availability, with configurable min/max. See [unresolvable-reference.xml](unresolvable-reference) for details. (Rift only)
* Added Oculus Platform SDK support to mobile VR applications to 4.12 and 4.13 in the Oculus repository.
* Added Blueprint for Oculus Platform entitlement checks (available in SI 1.6).
* A subset of Oculus Platform features are now available through the Unreal Online Subsystems interface.
* Added cylinder TimeWarp overlay support (Gear VR only) for UI components, etc. For more information, see [All Headsets: VR Compositor Layers](/documentation/unreal/latest/concepts/unreal-overlay/ "With Unreal, you may add transparent or opaque quadrilateral, cubemap, or cylindrical overlays to your level as compositor layers.").
* Added ability develop using GearVR plugin and Mobile renderer on the PC using the Oculus Rift. To use, disable OculusRift and SteamVR plugins for your project, and add -OpenGL -FeatureLevelES2 to your command line.


API Changes

* Added Cylinder layer type to FHMDLayerDesc in HeadMountedDisplayCommon.h.
* In IInputInterface.h, FHapticFeedbackBuffer uint8* RawData was changed to TArray&lt;uint8&gt; RawData, and uint8 *CurrentPtr; was changed to uint32 CurrentPtr.
* IInputInterface::SetHapticFeedbackBuffer was removed and HapticBuffer was added to FHapticFeedbackValues::FHapticFeedbackBuffer* HapticBuffer. You should now use IInputInterface::SetHapticFeedbackValues, whether you are using a buffer or not.
* APlayerController::SetHatpicsByValue calls to Oculus Touch are now limited to 30 per second due to performance issues. Additional calls with a value other than zero (i.e., stop commands) are discarded upon receipt. 


Known Issues

* UE4.12 and 4.13 in Oculus GitHub repository: A significant drop in frame rate occurs when UE4 is not in focus in VR preview mode. To avoid this issue, uncheck the Use Less CPU when in **Background** in **Edit** &gt; **Editor Preferences** &gt; **General** (left sidebar) &gt; **Miscellaneous** (left sidebar) &gt; **Performance**.
* **Stereo Layer Position Type**: **World Locked** is not currently supported for cylinder TimeWarp overlays. 

