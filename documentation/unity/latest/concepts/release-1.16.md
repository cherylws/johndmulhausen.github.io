---
title: 1.16-beta Oculus Utilities for Unity 5 Release Notes
---
## Oculus Utilities for Unity 5 version 1.16.0-beta

## Overview of 1.16-beta

This beta release adds support for mixed reality capture, which allows live video footage of a Rift user to be composited with the output from a game to create combined video that showed the player in a virtual scene. Unity 5.4 is not supported by 1.16-beta, and it introduces known issues regarding VR Compositor Layers - see below for more details.

There is a known black screen issue with Android, and we recommend that you do not use this version for mobile development.

We recommend only updating to this release if you need mixed reality capture support or cylinder VR Compositor Layer support for Rift.

The Oculus integration includes preliminary support for Unity 2017 Beta. If you have any problems or questions, please let us know in our Unity Developer Forum.

## Oculus Integration on the Unity Asset Store

The Oculus Integration, available from the Unity Asset Store [here](https://www.assetstore.unity3d.com/en/#!/content/82022), provides several unityPackages in a single download, including our Utilities for Unity, Oculus Platform SDK Unity plugin, Oculus Avatar SDK Unity Plugin, and the Oculus Native Spatializer Plugin. The Unity Sample Framework is also available from the Asset Store [here](https://www.assetstore.unity3d.com/en/#!/content/82503).

## New Features

* Added support for mixed reality capture (Rift only). For more information, see Unity Mixed Reality Capture. For more information, see [Unity Mixed Reality Capture](/documentation/unity/latest/concepts/unity-mrc/ "This guide describes how to add and configure mixed reality capture support for your Unity application. Mixed reality capture is supported for Rift applications only.").
* Added cylinder layer support to OVROverlay on Rift.
* Added R16G16B16A16\_FP / R11G11B10\_FP support to OVRManager, which can remove banding from dark colors. To enable, use OVRManager.eyeTextureFormat = R11G11B10\_FP. Note: if you need alpha channel in your frame buffer, you must use OVRManager.eyeTextureFormat = R16G16B16A16\_FP.
## Bug Fixes

* Fixed a crash on Windows when another application toggles exclusive full-screen mode.
* Fixed bug with Unity 5.6 where Gear VR would report the wrong field of view for the first frame after launch.
* Fixed pose race condition when OVRCameraRig.useFixedUpdateForTracking is true.
## Known Issues

* Unity 2017
	+  When using the Utilities package, you may encounter the following error when adding scripts to your project: "Assets/OVR/Scripts/OVROverlay.cs(385,20): error CS1501: No overload for method `CreateExternalTexture' takes `6' arguments". As a workaround, open OVROverlay.cs in you script editor and change et = Cubemap.CreateExternalTexture(size.w, size.h, txFormat, mipLevels > 1, isSrgb, externalTex); to et = Cubemap.CreateExternalTexture(size.w, txFormat, mipLevels > 1, externalTex);.
	
* 1.16-beta issues
	+ Due to a black screen issue, we do not recommend using this version for mobile development.
	+ If you are passing a texture with mipmaps to OVROverlay, only the mip level o will be used. You will experience aliasing if your texture is excessively high-resolution. Do not use resolutions above 1024 for now.
	+ Projects using Utilities 1.16-beta only support cubemap VR Compositor Layers in Unity 2017.1 or later.
	
* Mixed reality capture
	+ Recentering a Rift mixed reality capture application will corrupt the camera pose when a static camera was configured with the CameraTool. As a temporary workaround, you may attach a VR Object to your camera (e.g., by using a third Touch), and it will recenter normally.
	
* Unity 5.6 and later: If you have updated your OVRPlugin version from Utilities, you may see a spurious error message when the Editor first launches saying “Multiple plugins with the same name 'ovrplugin'”. Please disregard.
* When using Android SDK Tools 25.3.1 or newer, we recommend using Oculus Utilities 1.15 or newer in combination with Unity 5.4.5p2 or newer, 5.5.3p3 or newer, 5.6.0p3 or newer, or 2017.1.0b5 or newer.
* When Single Pass is enabled, building mobile projects will fail with the error message “Shader error in 'Mobile/Bumped Detail Diffuse'” in certain cases. For more information, see “Known Issues” in [Single Pass Stereo Rendering (Preview, Mobile Only)](/documentation/unity/latest/concepts/unity-single-pass/ "Single Pass stereo rendering is a preview rendering feature for Oculus Go and Gear VR available in Unity 5.6. If your application is CPU-bound or draw call bound, we strongly recommend using Single Pass rendering to improve performance.").
* Two graphics driver issues affect mobile applications with Single Pass enabled using some S8 or S8+ phones with Unity 5.6.0p2-3. They can occur when Standard Shader Quality is set to low, or when you are using tree objects. For more information and workarounds, see “Known Issues” in [Single Pass Stereo Rendering (Preview, Mobile Only)](/documentation/unity/latest/concepts/unity-single-pass/ "Single Pass stereo rendering is a preview rendering feature for Oculus Go and Gear VR available in Unity 5.6. If your application is CPU-bound or draw call bound, we strongly recommend using Single Pass rendering to improve performance.").
* The following versions of Unity require the [Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/en-us/download/details.aspx?id=48145) or Rift builds will fail to run in VR, and the error “Security error. This plugin is invalid!” will be reported in output\_log.txt:
	+ 5.3.6p3-5.3.6p7
	+ 5.4.0f1-5.4.2p1
	+ 5.5.0b1-5.5.0b8
	
* Unity has a known issue such that parenting one VR camera to another will compound tracking twice. As a workaround, make them siblings in the GameObject hierarchy.
* Rift
	+ All Unity versions prior to 5.4.3p3 leak 5MB/s if you have a Canvas in your scene, enable **Run In Background**, and dismount the Rift. You can check OVRManager.hasVrFocus in an Update function to disable your Canvases while the HMD is dismounted.
	+ Transparent VR Compositor Layers do not currently support multiple layers of occlusion.
	
* Gear VR
	+ Gear VR applications built with Unity 5.6.0f2 crash immediately upon launch, and Gear VR applications built with 5.6.0p1 may crash when Multi-View is enabled.
	+ Do not use Utilities 1.11.0 due to a crash when returning to focus from Universal Menu or Quit to Home dialog.
	+ Due to a Unity bug, the Camera pose can be corrupted by scripts in the first frame after being enabled with VR support. As a workaround, use the latest Utilities version or zero out the eye anchor poses when a new OVRCameraRig is spawned and the first frame after usePerEyeAnchors changes.
	+ With Unity 5.3, the world may appear tilted. As a workaround, use the latest Utilities version or disable the virtual reality splash image.
	+ Mobile developers should not use Unity versions 5.3.6p1-2 and 5.4.0p1-2 due to incorrect positional movement of the head.
	+ Unity 5.3.4-5.3.6p3 and Unity 5.4.0b16-Unity 5.4.0p3: Do not set **DSP Buffer Size** to **Best** in Audio Manager in the Inspector for now or you will encounter audio distortion. Set it to **Good** or **Default** instead.
	
* Mobile App Submission to Oculus Store 
	+ All mobile applications using Utilities 1.9 and 1.10 will fail Oculus Store submission due to a bug affecting reserved interaction handling for the Universal Menu. Please remove previously-imported project files as described in [Importing the Oculus Utilities Package](/documentation/unity/latest/concepts/unity-import/ "Oculus Utilities for Unity is an optional Unity Package that includes scripts, prefabs, and other resources to assist with development.") and import the latest Utilities version, and update your Unity editor to a [compatible version](/documentation/unity/latest/concepts/unity-req/ "This guide describes Unity Editor version recommendations and system requirements.") if necessary. 
	
