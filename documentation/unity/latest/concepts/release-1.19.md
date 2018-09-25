---
title: 1.19 Oculus Utilities for Unity Release Notes
---
## Oculus Utilities for Unity version 1.19.0

2017.1 and 2017.2 are officially supported, and we recommend developers update to these versions when convenient. Our support for 2017.3 is currently in beta, and we do not recommend shipping applications using it at this time. 

## Dash Support

At Oculus Connect 4 we announced Rift Core 2.0, which includes substantial changes to Oculus Home and will replace our Universal Menu with Oculus Dash. We plan to make it available with the 1.21 runtime in early December.

Dash re-implements Universal Menu as a VR compositor layer. Have a look at our Blog announcement and watch the Dash video to get a sense of how it works.

We have added new application lifecycle support to our 1.18 integration in preparation for Dash. When Dash draws a menu overlay, the new Has Input Focus flag will return false, indicating that the application should pause and mute and the tracked controllers and hands be hidden from the scene, as Dash provides its own UI in the foreground. Depending on the application, additional action may also be warranted when input focus is lost (e.g., during a multi-player combat game, you may wish to freeze the player’s avatar and make it temporarily invulnerable to other players).

For more information, see [Application Lifecycle Handling](/documentation/unity/latest/concepts/unity-lifecycle/ "This guide describes the process to handle the lifecycle for applications built in Unity."). See the Input Focus sample in the Unity Sample Framework for an example of a typical implementation.

Additional information about supporting Dash will be available soon.

## API Changes

* Removed OVRManager.hasSystemOverlayPresent. All Dash lifecycle state information may now be queries with OVRManager.hasInputFocus.
## Bug Fixes

* Fixed VR compositor layer cubemap support on Rift only in Unity versions 2017.1 and later.
* Fixed Oculus integration 1.18 bug causing Occlusion Mesh to be rendered incorrectly. The lower side was blocked instead of the upper side, causing the Editor mirror window to show a black border on the top.
* Fixed VR Compositor Overlay bug affecting Utilities 1.18.x, causing mobile applications using gamma space lighting to be too dark. Rift applications and mobile apps using linear lighting were unaffected.
## Known Issues

* Do not use Utilities 1.16.0-beta. If you are using that version, please update to 1.18.
* Adaptive Resolution currently works only with Unity 2017.1.1p1 and later.
* Cubemap VR compositor layers currently do not work in mobile applications, or in Rift applications using Unity versions earlier than 2017.1.
* Unity 5.6 and later: If you have updated your OVRPlugin version from Utilities, you may see a spurious error message when the Editor first launches saying “Multiple plugins with the same name 'ovrplugin'”. Please disregard.
* Unity has a known issue such that parenting one VR camera to another will compound tracking twice. As a workaround, make them siblings in the GameObject hierarchy.
* Rift
	+ All Unity versions prior to 5.4.3p3 leak 5MB/s if you have a Canvas in your scene, enable **Run In Background**, and dismount the Rift. You can check OVRManager.hasVrFocus in an Update function to disable your Canvases while the HMD is dismounted.
	+ Transparent VR Compositor Layers do not currently support multiple layers of occlusion.
	
* The following versions of Unity require the [Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/en-us/download/details.aspx?id=48145) or Rift builds will fail to run in VR, and the error “Security error. This plugin is invalid!” will be reported in output\_log.txt:
	+ 5.3.6p3-5.3.6p7
	+ 5.4.0f1-5.4.2p1
	+ 5.5.0b1-5.5.0b8
	
* Mobile
	+ Do not use Utilities 1.11.0 due to a crash when returning to focus from Universal Menu or Quit to Home dialog. 
	+ Due to a Unity bug, the Camera pose can be corrupted by scripts in the first frame after being enabled with VR support. As a workaround, use the latest Utilities version or zero out the eye anchor poses when a new OVRCameraRig is spawned and the first frame after usePerEyeAnchors changes.
	+ Mobile developers should not use Unity versions 5.3.6p1-2 and 5.4.0p1-2 due to incorrect positional movement of the head.
	+ Unity 5.3.4-5.3.6p3 and Unity 5.4.0b16-Unity 5.4.0p3: Do not set **DSP Buffer Size** to **Best** in Audio Manager in the Inspector for now or you will encounter audio distortion. Set it to **Good** or **Default** instead.
	
* Mobile applications built with Unity 5.6.0f2 crash immediately upon launch, and mobile applications built with 5.6.0p1 may crash when Multi-View is enabled.
* Single-Pass Stereo Rendering
	+ When Single Pass is enabled, building mobile projects will fail with the error message “Shader error in 'Mobile/Bumped Detail Diffuse'” in certain cases. For more information, see “Known Issues” in [Single Pass Stereo Rendering (Preview, Mobile Only)](/documentation/unity/latest/concepts/unity-single-pass/ "Single Pass stereo rendering is a preview rendering feature for Oculus Go and Gear VR available in Unity 5.6. If your application is CPU-bound or draw call bound, we strongly recommend using Single Pass rendering to improve performance.").
	+ Two graphics driver issues affect mobile applications with Single Pass enabled using some S8 or S8+ phones with Unity 5.6.0p2-3. They can occur when Standard Shader Quality is set to low, or when you are using tree objects. For more information and workarounds, see “Known Issues” in [Single Pass Stereo Rendering (Preview, Mobile Only)](/documentation/unity/latest/concepts/unity-single-pass/ "Single Pass stereo rendering is a preview rendering feature for Oculus Go and Gear VR available in Unity 5.6. If your application is CPU-bound or draw call bound, we strongly recommend using Single Pass rendering to improve performance.").
	
