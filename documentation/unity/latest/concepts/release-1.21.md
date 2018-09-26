---
title: 1.21 Oculus Utilities for Unity Release Notes
---



## Oculus Utilities for Unity version 1.21.0

For version compatibility information, see [Compatibility and Version Requirements](/documentation/unity/latest/concepts/unity-req/).

## Unity 5.x Support

With this release we have deprecated support for Unity 5.4.x and 5.5.x. For developers using Unity 5.6,x, we strongly recommend using version 5.6.4p2, which features several significant performance improvements.

Note that 5.6.4p2 has the following known issues:

* Adaptive Resolution is not working.
* A Unity issue may cause mobile builds to fail with the error "Failed to Repackage Resources" due to the erroneous insertion of the keyword density into the Android manifest. Until this is fixed in the engine, as a workaround you can install Android Build Tools v.24 or later. Note that Build Tools v24 requires JDK 1.8 or later. For more information, see [this entry](https://issuetracker.unity3d.com/issues/android-build-fails-with-failed-to-repackage-resources-error-when-api-level-23-or-lower-is-used) in Unityâ€™s Issue Tracker.


We recommend that all developers update to Unity 2017 or later.

## Oculus Dash Support

Rift Core 2.0 introduces substantial changes to Oculus Home and replaces the Universal Menu with Oculus Dash. We plan to roll it out to Rift users with the 1.22 runtime in early 2018.

We recommend adding Dash support to your application to provide the best possible user experience. Developers who would like to add Dash support before it rolls out in early 2018 can test it using Oculus runtime 1.21, which includes preview support. Runtime 1.21 is now available through our opt-in Public Test Channel (PTC).

Note that Dash support is **enabled by default** in Unity 2017.3b11 and later, in versions 2017.3f1-2, and in Unity Dash custom builds. It is off by default in all other versions, and we plan to disable it by default in 2017.3f3 and later.

For more information, please see [Oculus Dash in Unity](/documentation/unity/latest/concepts/unity-dash/).

## New Features

* Added Equirectangular support to VR Compositor Layers (mobile only).


## Bug Fixes

* Unity 2017.2: Fixed issue causing OVRInput.GetDown() to return incorrect values. 


## Known Issues

* Do not use Utilities 1.16.0-beta. If you are using that version, please update to a later version.
* Unity 5.6 versions 5.6.3p2 and later, and Unity 2017.1 versions 2017.1.0p3 and later:
	+ The Unity engine uses projection matrix calculations that are at variance with the Oculus SDK, causing VR scenes to have the wrong parallax, which may cause discomfort. Note that object size in affected scenes is not quite correct, and take this into consideration when thinking about design. We are working with Unity to fix this as soon as possible.
	
* Unity Utilities 1.18 includes a VR Compositor Overlay bug which causes mobile applications using gamma space lighting to be too dark. This bug is fixed in 1.19.0.
* All Unity versions with Oculus runtime 1.17+ and Windows 10 + Creators Update
	+  This combination results in spurious WM\_DEVICECHANGE reports in the Editor, even in non-VR projects. Many users will notice no impact, but users connected to certain USB devices may find the Editor becomes non-responsive and needs to be terminated from Task Manager. To mitigate, please update to the Beta runtime available on our Public Test channel. We are currently working with Unity and Microsoft on a permanent solution.
	
* Cubemap VR compositor layers currently do not work in mobile applications, or in Rift applications using Unity versions earlier than 2017.1.
* Adaptive Resolution currently works only with Unity 2017.1.1f2 and later.
* Unity 5.6 and later: If you have updated your OVRPlugin version from Utilities, you may see a spurious error message when the Editor first launches saying “Multiple plugins with the same name 'ovrplugin'”. Please disregard.
* Unity has a known issue such that parenting one VR camera to another will compound tracking twice. As a workaround, make them siblings in the GameObject hierarchy.
* Rift
	+ All Unity versions prior to 5.4.3p3 leak 5MB/s if you have a Canvas in your scene, enable **Run In Background**, and dismount the Rift. You can check OVRManager.hasVrFocus in an Update function to disable your Canvases while the HMD is dismounted.
	+ Transparent VR Compositor Layers do not currently support multiple layers of occlusion.
	+ The following versions of Unity require the [Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/en-us/download/details.aspx?id=48145) or Rift builds will fail to run in VR, and the error “Security error. This plugin is invalid!” will be reported in output\_log.txt:
		- 5.3.6p3-5.3.6p7
		- 5.4.0f1-5.4.2p1
		- 5.5.0b1-5.5.0b8
		
	
* Gear VR
	+ 5.4.6p2 and 2017.3: A Unity issue may cause mobile builds to fail with the error "Failed to Repackage Resources" due to the erroneous insertion of the keyword density into the Android manifest. Until this is fixed in the engine, as a workaround you can install Android Build Tools v.24 or later. Note that Build Tools v24 requires JDK 1.8 or later.
	+ Unity 2017.2/OVRPlugin 1.18.1: GetActiveController switches to gamepad following Gear VR Controller button release. With OVRPlugin 1.21 or later, this is only expected to occur if the user has a gamepad and Gear VR Controller connected at the same time.
	+ Mobile developers should not use Unity versions 5.3.6p1-2 and 5.4.0p1-2 due to incorrect positional movement of the head.
	+ Unity 5.3.4-5.3.6p3 and Unity 5.4.0b16-Unity 5.4.0p3: Do not set **DSP Buffer Size** to **Best** in Audio Manager in the Inspector for now or you will encounter audio distortion. Set it to **Good** or **Default** instead.
	+ Gear VR applications built with Unity 5.6.0f2 crash immediately upon launch, and Gear VR applications built with 5.6.0p1 may crash when Multi-View is enabled.
	+ A known bug in Unity 2017.x causes a deterioration of performance in mobile applications when the back button is used to enter the Universal Menu, and then to return to the application. It particularly affects applications that use multi-threading or which use high CPU utilization, and S7 (Europe) and S8 (global) phones. 
	+ Do not use Utilities 1.11.0 due to a crash when returning to focus from Universal Menu or Quit to Home dialog.
	
* Single-Pass Stereo Rendering
	+ When Single Pass is enabled, building mobile projects will fail with the error message “Shader error in 'Mobile/Bumped Detail Diffuse'” in certain cases. For more information, see “Known Issues” in [Single Pass Stereo Rendering (Preview, Mobile Only)](/documentation/unity/latest/concepts/unity-single-pass/ "Single Pass stereo rendering is a preview rendering feature for Oculus Go and Gear VR available in Unity 5.6. If your application is CPU-bound or draw call bound, we strongly recommend using Single Pass rendering to improve performance.").
	+ Two graphics driver issues affect mobile applications with Single Pass enabled using some S8 or S8+ phones with Unity 5.6.0p2-3. They can occur when Standard Shader Quality is set to low, or when you are using tree objects. For more information and workarounds, see “Known Issues” in [Single Pass Stereo Rendering (Preview, Mobile Only)](/documentation/unity/latest/concepts/unity-single-pass/ "Single Pass stereo rendering is a preview rendering feature for Oculus Go and Gear VR available in Unity 5.6. If your application is CPU-bound or draw call bound, we strongly recommend using Single Pass rendering to improve performance.").
	

