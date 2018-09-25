---
title: Changes For Release 1.3.x
---
This section describes changes to the Oculus SDK, the Oculus App, Oculus Home, and the runtime.

## Overview of Release 1.3.2

The 1.3.2 release focuses on performance improvements and minor bug fixes. 

## Overview of Release 1.3.0

Release 1.3.0 is the first public release since SDK Version 0.8 and represents significant changes.

The Oculus SDK now provides Asynchronous TimeWarp (ATW). With ATW, TimeWarp is automatically applied to the last rendered frame by the Oculus Compositor at the same time as distortion. For more information, see [Asynchronous TimeWarp](/documentation/pcsdk/latest/concepts/dg-render/#dg-asynchronous-timewarp "Asynchronous TimeWarp (ATW) is a technique for reducing latency and judder in VR applications and experiences.").

Oculus now provides guidance and APIs for VR focus management, which helps you smoothly transition users between your game or experience and Oculus Home. For more information, see [VR Focus Management](/documentation/pcsdk/latest/concepts/dg-vr-focus/ "When you submit your application to Oculus, you provide the application and metadata necessary to list it in the Oculus Store and launch it from Oculus Home.").

## New Features for 1.3.2

The following are new features for the Oculus SDK and runtime:

* Added support for installing Oculus and VR applications to different drives.
* Support for multiple payment options.
## New Features for 1.3.0

The following are new features for the Oculus SDK and runtime:

* Added Asynchronous TimeWarp (ATW). For more information, see [Asynchronous TimeWarp](/documentation/pcsdk/latest/concepts/dg-render/#dg-asynchronous-timewarp "Asynchronous TimeWarp (ATW) is a technique for reducing latency and judder in VR applications and experiences.").
* Replaced the legacy runtime download with Oculus Setup. To download Oculus Setup, go to <https://www.oculus.com/setup/>.
* Added features for VR focus management, which helps you smoothly transition users between your game or experience and Oculus Home. For more information, see [VR Focus Management](/documentation/pcsdk/latest/concepts/dg-vr-focus/ "When you submit your application to Oculus, you provide the application and metadata necessary to list it in the Oculus Store and launch it from Oculus Home.").
* Updated queue ahead to be adaptive. Queue ahead previously processed frames 2.8 milliseconds in advance to improve CPU and GPU parallelism. Adaptive queue ahead works similarly, but automatically adjusts the start time from 0 to -1 frame (depending on the current performance).
* Added the performance indicator, which displays when the application is slow or not maintaining frame rate. For more information, see [unresolvable-reference.xml](unresolvable-reference)
* Added the Oculus Compositor performance HUD (ovrPerfHud\_CompRenderTiming) and renamed the application performance HUD (ovrPerfHud\_RenderTiming) to ovrPerfHud\_CompRenderTiming>.
* Support for DirectX 12 (DX12). For more information, refer to the Oculus Room Tiny (DX12) sample.
## Runtime Changes for 1.3.0

Changes include:

* Added Oculus Setup, which installs and configures the Oculus Rift, installs the Oculus App, and installs Oculus Home.
* Added the Oculus App, which replaces the Oculus Configuration Utility. To open the Oculus App, double-click the Oculus desktop icon.
* Added Oculus Home, the VR-based application for launching games and experiences. If the Oculus App is open, Oculus Home automatically runs whenever you put on the headset.
* Added the universal menu to perform many common tasks, such as recentering and lens adjustment. To open the universal menu, press the Oculus button on the Oculus remote or the Xbox button on the Xbox Controller 
* Account, device, and privacy management tasks are now performed through the Oculus App. To make changes, click the menu icon (three dots) in the upper right corner of the Oculus App and select Settings.
* Previously, when you locked your computer, any VR content continued to display in the headset. Now, when you lock the computer, the headset displays a blank screen.
## API Updates for 1.3.0

* Added ovrTrackerFlags, which returns whether the sensor is present and is in a valid position.
* Added ovrSessionStatus flags to for focus management. For more information, see [VR Focus Management](/documentation/pcsdk/latest/concepts/dg-vr-focus/ "When you submit your application to Oculus, you provide the application and metadata necessary to list it in the Oculus Store and launch it from Oculus Home.").
* Added ovrTrackerPose to get the position of a specific sensor.
* Added bit masks that provide button touch states (ovrTouch\_RButtonMask and ovrTouch\_LButtonMask), button press states (ovrButton\_RMask and ovrButton\_LMask), and finger poses (ovrTouch\_RPoseMask and ovrTouch\_LPoseMask) for the Oculus Touch controllers. 
* Added ovrTrackingState::CalibratedOrigin, which is the initial origin configured by the user when he or she set up the headset. Every time a user recenters a headset, the updated location is relative to this value.
* Added the ovr\_ClearShouldRecenterFlag function for applications that want to manually calculate a recentered tracking pose instead of using the provided SDK function ovr\_RecenterTrackingOrigin.
* Added the utility function ovrPosef\_FlipHandedness to help applications easily flip any ovrPosef from a left to right-handed coordinate system.
## API Changes for 1.3.0

This release represents a major revision of the API. Changes to the API include:

* The previous API returned a mutable struct which had to be modified in a specific way and passed back to the API. The Oculus SDK now returns an Opaque handle that represents the TextureSwapChain.
* Removed the deprecated ovrHmdStruct synonym for ovrHmd. 
* Removed the ovrStatusBits::ovrStatus\_CameraPoseTracked and ovrStatusBits::ovrStatus\_PositionConnected flags. 
* Moved CameraFrustumHFovInRadians, CameraFrustumVFovInRadians, CameraFrustumNearZInMeters, and CameraFrustumFarZInMeters from ovrHmdDesc to ovrTrackerDesc. Renamed them FrustumHFovInRadians, FrustumVFovInRadians, FrustumNearZInMeters, and FrustumFarZInMeters
* Removed CameraPose and LeveledCameraPose from ovrTrackingState and added them to ovrTrackerPose (as Pose and LeveledPose).
* Renamed HmdToEyeViewOffset to HmdToEyeOffset.
* Renamed ovrSwapTextureSet to ovrTextureSwapChain.
* Removed the deprecated functions ovr\_ResetBackOfHeadTracking and ovr\_ResetMulticameraTracking.
* Removed ovr\_SetEnabledCaps.
* Removed ovr\_ConfigureTracking.
* Removed the ovr\_GetEnabledCaps function.
* Removed the ovr\_GetTrackingCaps function.
* Removed the ovrLayerDirect layer type.
* Renamed the ovr\_RecenterPose function to ovr\_RecenterTrackingOrigin.
* Changed ovrMaxLayerCount from 32 to 16.
* Moved the bindFlags parameter in function ovr\_CreateTextureSwapChainDX to be part of the ovrTextureSwapChainDesc structure.
* Added the output parameter outSensorSampleTime to the utility function ovr\_GetEyePoses.
* Modified ovrMatrix4f\_Projection to be right-handed by default and changed ovrProjection\_RightHanded to ovrProjection\_LeftHanded.
* Modified the default handedness of ovrMatrix4f\_Projection to be right-handed by default and changed ovrProjection\_RightHanded to be ovrProjection\_LeftHanded.
* Added the ovrPosef\_FlipHandedness utility function.
* Renamed ovrControllerType\_SID to ovrControllerType\_Remote.
* Renamed ovrMirrorTextureDesc::Flags to ovrMirrorTextureDesc::MiscFlags and ovrTextureSwapChainDesc::Flags to ovrTextureSwapChainDesc::MiscFlags.
* Removed the OVR\_Kernel.h header file.
## Fixed Issues for 1.3.2

The following are fixed issues:

* Oculus App


	+ Purchase totals now display with correct local currency code.
	+ The back button now retains scroll position.
	+ Rift options are responsive if no internet connection is available.
	+ Fixed issue where user profile displays if no internet connection is available.
	+ Fixed timing and caching issues related to displaying the status of friend requests.
	
* Oculus Home


	+ Recently played apps only appear if the app is launchable.
	+ Better notification for USB chipsets that do not meet the USB 3.0 specification.
	+ Better processing and management of paid purchases.
	+ Purchase totals now display with correct local currency code.
	+ Additional UI fixes and updates.
	
* Platform SDK


	+ Improved UE4 linking.
	+ Fix message parsing resulting from ovr\_Matchmaking\_JoinRoom.
	
## Known Issues

The following are known issues:

* There are some USB chipsets that do not meet the USB 3.0 specification and are incompatible with the Oculus Rift sensor. If you receive a notification in Oculus Home or the Oculus App, plug the sensor into a different USB 3.0 port (blue). If none of the USB 3.0 ports work, plug the sensor into a USB 2.0 port (black). 
* Antivirus software, such a McAfee, can cause installation issues. To work around the issue, make sure you have the latest updates and disable real-time scanning.
* If you encounter installation issues, delete the Oculus folder and install the software again.
* If the Rift displays a message that instructs you to take off the headset, remove it and place it on a flat surface for 10-15 seconds.
* The keyboard and mouse do not work in Oculus Home. To select an item, gaze at it and select it using the Oculus Remote or Xbox controller.
* Bandwidth-intensive USB devices, such as web cams and high-end audio interfaces, might not work when using the Rift. To work around this issue, install the device on another USB host controller or a separate computer.
* For dual-boot systems using DK2 or CB1 HMDs, the OS selection screen might appear on the HMD instead of the monitor. To work around this, try plugging the HMD into a different port or unplug the HMD while booting.
* If you are running your application from the Unity Editor and you press the controller's home button to return to Oculus Home, you will be prompted to close the application. If you select OK, Unity might remain in a state where it is running, but will never get focus. To work around this, restart Unity.
## Migrating from SDK 1.3.0 to SDK 1.3.2

There are no breaking SDK changes or migration requirements other than installing the new SDK.

## Migrating from SDK 1.2 to SDK 1.3.x

There are no breaking SDK changes or migration requirements other than installing the new SDK.

## Migrating from SDK 0.8 to SDK 1.3.x

One of the most significant changes is that the SwapTextureSet internals are no longer exposed.

The previous API returned a mutable struct which had to be modified in a specific way and passed back to the API. The 0.9 API returns an Opaque handle that represents the TextureSwapChain.

To modify your application loop:

1. Replace calls that use the ovrSwapTextureSet structure to determine the count and textures with ovr\_GetTextureSwapChainLength and ovr\_GetTextureSwapChainBufferDX/GL.
2. Instead of indexing into the texture (and/or render target) arrays with the CurrentIndex field, use ovr\_GetTextureSwapChainCurrentIndex to obtain the index.
3.  Instead of manually modifying the index, use ovr\_CommitTextureSwapChain to advance the state of the chain. Note that this should occur after rendering into the texture and before referencing the texture swap chain in a SubmitFrame call.
4. Instead of using ovrTexture and pointer typecasting to obtain the specific texture object, use ovr\_GetMirrorTextureBufferDX/GL.
For more information, see [Rendering to the Oculus Rift](/documentation/pcsdk/latest/concepts/dg-render/#dg_render "The Oculus Rift requires split-screen stereo with distortion correction for each eye to cancel lens-related distortion.").

You will also need to update your application to support VR focus management. For more information, see [VR Focus Management](/documentation/pcsdk/latest/concepts/dg-vr-focus/ "When you submit your application to Oculus, you provide the application and metadata necessary to list it in the Oculus Store and launch it from Oculus Home."). 

Make the following additional changes:

1. Update your code to use ovr\_GetSessionStatus::DisplayLost instead of ovr\_GetSessionStatus::HmdPresent. For more information, see [VR Focus Management](/documentation/pcsdk/latest/concepts/dg-vr-focus/ "When you submit your application to Oculus, you provide the application and metadata necessary to list it in the Oculus Store and launch it from Oculus Home.").
2. Update your code to call ovr\_RecenterTrackingOrigin when ovr\_GetSessionStatus::ShouldRecenter is true.
3. When calling ovr\_CreateTextureSwapChainDX, update your code to start passing BindFlags as part of the ovrTextureSwapChainDesc structure.
4. When calling ovr\_GetEyePoses, retrieve the outSensorSampleTime provided by the function instead of manually querying it with ovr\_GetTimeInSeconds.
5. When calling ovrMatrix4f\_Projection, the default is now right-handed. If needed, flip the handedness flag to ovrProjection\_LeftHanded.
There are also several smaller changes:

1. Replace references to HmdToEyeViewOffset with HmdToEyeOffset. 
2. Replace ovrTrackingState::CameraPose and ovrTrackingState::LeveledCameraPose with ovrTrackerPose::Pose and ovrTrackerPose::LeveledPose
3. Replace ovrSessionStatus::HasVrFocus with ovrSessionStatus::IsVisible.
4. Remove calls to ovr\_GetTrackingCaps, as it is no longer supported.
5. Remove calls to ovr\_GetEnabledCaps, as it is no longer supported.
6. Remove usage of ovrLayerType\_Direct, as it is no longer supported.
7. Rename usage of ovrTextureFlag\_Typeless to ovrTextureMisc\_DX\_Typeless.
8. Rename calls to ovr\_RecenterPose to ovr\_RecenterTrackingOrigin.
9. Rename usage of ovrControllerType\_SID to ovrControllerType\_Remote.
10. Rename usage of ovrMirrorTextureDesc::Flags to ovrMirrorTextureDesc::MiscFlags and ovrTextureSwapChainDesc::Flags to ovrTextureSwapChainDesc::MiscFlags.
11. Use ovrMaxLayerCount as the max number of layers. ovrMaxLayerCount was 32 in previous SDK versions but has been reduced.
