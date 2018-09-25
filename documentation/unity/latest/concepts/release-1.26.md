---
title: 1.26 Oculus Utilities for Unity Release Notes
---
## New Features

* N/A
## Integration Changes

* N/A
## Bug Fixes

* Fixed bug where app would revert from floor-level to eye-level tracking when exiting and re-entering VR mode.
* Refactored Rift underlay support to use depth testing instead of alpha when available.
* Fixed race condition causing back button not to bring up system UI on mobile devices.
* Increased minimum Android SDK requirement from 19 to 21.
* Fixed depth fighting issues with OVRScreenFade.
* Fixed brightness issues with OVROverlay.
* Fixed texture layout used by OVROverlay when created at runtime.
* Moved all assets from Assets/OVR to Assets/Oculus/VR to integrate cleanly with other Oculus SDKs.
* Fixed inconsistent input mappings in OVRInputModule.
* Made scripts fail more gracefully when OVRPlugin is not present.
* Fixed inconsistent behavior when upgrading OVRPlugin.
* OVRLint now prompts to enable trilinear filtering and mipmapping on the VR splash image.
* Optimized OVROverlay texture bandwidth usage when texture data isn't changing.
* Fixed bug causing head velocity and acceleration to always be 0.
* Fixed OVROverlay flicker when loading a scene.
## Known Issues

* Unity 2018.1 Rift looks over dark under "Single Pass" stereo rendering method
* If you experience long UI stalls or poor performance with the Unity Editor when targeting Oculus Rift on Windows 10, please run Windows Update to ensure that you have the latest version of Windows 10.
* Unity 5 5.6.3p2 - 5.6.4p1, Unity 2017.1 - 2017.1.2p1, 2017.2.0f3 - 2017.2.0p2:
	+ The Unity engine uses projection matrix calculations that are at variance with the Oculus SDK, causing VR scenes to have the wrong parallax, which may cause discomfort.
	
* All Unity versions with Oculus runtime 1.17+ and Windows 10 + Creators Update
	+  This combination results in spurious WM\_DEVICECHANGE reports in the Editor, even in non-VR projects. Many users will notice no impact, but users connected to certain USB devices may find the Editor becomes non-responsive and needs to be terminated from Task Manager. To mitigate, please update to the Beta runtime available on our Public Test channel. We are currently working with Unity and Microsoft on a permanent solution.
	
* Cubemap VR compositor layers currently do not work in mobile applications, or in Rift applications using Unity versions earlier than 2017.1.
* Adaptive Resolution currently works only with Unity 2017.1.1p1 and later, you might experience some slightly pixel shaking when resolution is changing, this is a known issue, we are working with Unity to resolve it.
* Unity 5.6 and later: If you have updated your OVRPlugin version from Utilities, you may see a spurious error message when the Editor first launches saying “Multiple plugins with the same name 'ovrplugin'”. Please disregard.
* Unity has a known issue such that parenting one VR camera to another will compound tracking twice. As a workaround, make them siblings in the GameObject hierarchy.
* Rift
	+ All Unity versions prior to 5.4.3p3 leak 5MB/s if you have a Canvas in your scene, enable **Run In Background**, and dismount the Rift. You can check OVRManager.hasVrFocus in an Update function to disable your Canvases while the HMD is dismounted.
	+ Transparent VR Compositor Layers do not currently support multiple layers of occlusion.
	+ The following versions of Unity require the [Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/en-us/download/details.aspx?id=48145) or Rift builds will fail to run in VR, and the error “Security error. This plugin is invalid!” will be reported in output\_log.txt:
		- 5.3.6p3-5.3.6p7
		- 5.4.0f1-5.4.2p1
		- 5.5.0b1-5.5.0b8
		
	
* Mobile
	+ When building a mobile app using one of the Unity versions listed below, you'll need to export a Gradle project and modify the SigningConfig in the build.gradle file to include v1SigningEnabled=true, v2SigningEnabled=false. The affected versions are:
		- all 2017.3 versions
		- all 2017.4 versions below 2017.4.2f1
		- all 2018.1 versions below 2018.1.0b12
		- and all 2018.2 a types
		
	+ 5.4.6p2 and 2017.3: A Unity issue may cause mobile builds to fail with the error "Failed to Repackage Resources" due to the erroneous insertion of the keyword density into the Android manifest. Until this is fixed in the engine, as a workaround you can install Android Build Tools v.24 or later. Note that Build Tools v24 requires JDK 1.8 or later.
	+ Mobile developers should not use Unity versions 5.3.6p1-2 and 5.4.0p1-2 due to incorrect positional movement of the head.
	+ Unity 5.3.4-5.3.6p3 and Unity 5.4.0b16-Unity 5.4.0p3: Do not set **DSP Buffer Size** to **Best** in Audio Manager in the Inspector for now or you will encounter audio distortion. Set it to **Good** or **Default** instead.
	+ Gear VR applications built with Unity 5.6.0f2 crash immediately upon launch, and Gear VR applications built with 5.6.0p1 may crash when Multi-View is enabled.
	+ A known bug in Unity causes a deterioration of performance in mobile applications when the back button is used to enter the Universal Menu, and then to return to the application. It particularly affects applications that use multi-threading or which use high CPU utilization, and S7 (Europe) and S8 (global) phones. This bug is fixed in 5.6.4p2, 2017.1.2p4 , 2017.3.0b9 , 2017.2.0p3.
	+ Do not use Utilities 1.11.0 due to a crash when returning to focus from Universal Menu or Quit to Home dialog.
	
* Single-Pass Stereo Rendering
	+ When Single Pass is enabled, building mobile projects will fail with the error message “Shader error in 'Mobile/Bumped Detail Diffuse'” in certain cases. For more information, see “Known Issues” in [Single Pass Stereo Rendering (Preview, Mobile Only)](/documentation/unity/latest/concepts/unity-single-pass/ "Single Pass stereo rendering is a preview rendering feature for Oculus Go and Gear VR available in Unity 5.6. If your application is CPU-bound or draw call bound, we strongly recommend using Single Pass rendering to improve performance.").
	+ Two graphics driver issues affect mobile applications with Single Pass enabled using some S8 or S8+ phones with Unity 5.6.0p2-3. They can occur when Standard Shader Quality is set to low, or when you are using tree objects. For more information and workarounds, see “Known Issues” in [Single Pass Stereo Rendering (Preview, Mobile Only)](/documentation/unity/latest/concepts/unity-single-pass/ "Single Pass stereo rendering is a preview rendering feature for Oculus Go and Gear VR available in Unity 5.6. If your application is CPU-bound or draw call bound, we strongly recommend using Single Pass rendering to improve performance.").
	
* Mixed Reality Capture
	+ ZED Camera users should upgrade their SDK version to 2.3.1. All previous versions are not compatible.
	
