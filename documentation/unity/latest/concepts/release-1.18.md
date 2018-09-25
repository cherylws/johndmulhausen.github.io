---
title: 1.18 Oculus Utilities for Unity Release Notes
---
## Oculus Utilities for Unity version 1.18.1

Bug Fixes

* Fixed bug causing VR Compositor Layers to persist after changing scenes in a multi-scene game.
## Oculus Utilities for Unity version 1.18.0

Unity versions 5.1 and later provide built-in VR support for Rift, Oculus Go, and Samsung Gear VR. The optional Utilities unitypackage includes prefabs, C# scripts, sample scenes, and more to assist with development. For more information, see our Oculus Unity Developer Guide.

The Utilities package includes the most recent version of the Oculus OVRPlugin that is also included in the Unity Editor. When you import the Utilities package into a project, if the OVRPlugin included with Utilities is greater than the version in your Editor, a pop-up dialog will give you the option to update it. We recommend always using the latest-available OVRPlugin version.

Note: The latest OVRPlugin version number may be a version or two behind the Utilities version number.For information on which versions of the Unity Editor are compatible with which versions of Utilities for Unity, please see Compatibility and Version Requirements.

Be sure to review our Downloads page for other useful tools to assist development, such as the Unity Sample Framework. For more information on Oculus resources for Unity developers, please see Other Oculus Resources for Unity Developers.

The Oculus Integration, available through the Unity Asset Store, provides several unityPackages in a single download, including our Utilities for Unity, Oculus Platform SDK Unity plugin, Oculus Avatar SDK Unity Plugin, Oculus Native Spatializer Plugin, and the Unity Sample Framework.

## Unity 2017

2017.1 is officially supported, and we recommend developers update to this version when convenient. Our support for 2017.2 is currently in beta, and we do not recommend shipping applications using it at this time. Our support for 2017.3 is in alpha and may be unstable. See the “Unity 2017” section of “Known Issues” below for more information.

## Stereo Shader Reprojection

In our Developer Blog article [Introducing Stereo Shader Reprojection for Unity](/blog/introducing-stereo-shading-reprojection-for-unity/), we describe a new technique to optimize VR rendering by reprojecting rendered pixels from one eye to the other eye, and then filling in the gaps with an additional rendering pass. In pixel shader heavy scenarios, this technique can save 20% GPU cost per frame or more.

## New Features

* Mixed Reality Capture - see [Unity Mixed Reality Capture](/documentation/unity/latest/concepts/unity-mrc/ "This guide describes how to add and configure mixed reality capture support for your Unity application. Mixed reality capture is supported for Rift applications only.") for more information.
	+ Added sandwich composition mode, which is similar to direct composition in that camera and application content are composited by Unity. However, in sandwich composition, three distinct video layers are preserved - foreground and background content from the application, and a middle camera layer. This mode places greater demands on memory than Direct Composition, but allows for finer latency correction.
	+ Added latency correction controls for direct and sandwich Composition.
	+ Added Chroma Key options for direct and sandwich composition, replacing the previous green screen control parameters.
	+ Removed green screen tolerance, alpha cutoff, and color shadows settings.
	+ Added support for configuration by JSON file.
	+ Added a dynamic lighting option, which illuminate video content with application lights and flashes (e.g., the interpolated person in the scene is illuminated by explosions).
	+ Added ZED camera support, which provides depth information that can be used to present more realistic dynamic lighting in direct or sandwich composition.
	+ Added Virtual Green Screen, which confines interpolated camera stream content to an area defined by Guardian System configuration.
	+ Added selective layer hiding and capture camera selection options.
	
* OVRManager
	+ Added input focus and system overlay support. When input focus or system overlay status changes, applications may implement appropriate handling, such as pausing and muting applications when a system overlay is present, and hiding tracked controllers when input focus is lost. For an illustration of typical use, see the Input Focus System Overlay sample in our Unity Sample Framework. For additional documentation, see OVRManager in our [Unity Scripting Reference](/documentation/unity/latest/concepts/unity-reference-scripting/ "The Unity Scripting Reference contains detailed information about the data structures and files included with the Utilities and Legacy Integration packages.").
	
## Bug Fixes

* Fixed Gear VR black screen issue affecting Utilities 1.16.0-beta.
* Fixed “Mobile/Bumped detail diffuse” shader error when using Single-Pass Stereo Rendering with some Unity versions.
* Fixed quad layer failure to render with Unity 5.4 and 5.6.
* Fixed issue limiting mipmap textures passed to OVROverlay to mip level 0.
## Known Issues

* Unity 2017
	+ APKs built with Unity 2017 versions earlier than 2017.1.0p5 fail submission to the Oculus Store, which does not accept APK Signature Scheme V2.
	
* Do not use Utilities 1.16.0-beta. If you are using that version, please update to 1.18.
* VR Compositor Overlays will remain viewable after switching scenes in multi-scene applications unless all OVROverlay instances are explicitly disabled. Fixed in 1.18.1.
* Adaptive Resolution currently works only with Unity 2017.1.1p1 and later.
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
* There is a known Unity bug causing a deterioration of performance in mobile applications when the back button is used to enter the Universal Menu, and then to return to the application. It particularly affects applications that use multi-threading or which use high CPU utilization, and S7 (Europe) and S8 (global) phones. 
* Single-Pass Stereo Rendering
	+ When Single Pass is enabled, building mobile projects will fail with the error message “Shader error in 'Mobile/Bumped Detail Diffuse'” in certain cases. For more information, see “Known Issues” in [Single Pass Stereo Rendering (Preview, Mobile Only)](/documentation/unity/latest/concepts/unity-single-pass/ "Single Pass stereo rendering is a preview rendering feature for Oculus Go and Gear VR available in Unity 5.6. If your application is CPU-bound or draw call bound, we strongly recommend using Single Pass rendering to improve performance.").
	+ Two graphics driver issues affect mobile applications with Single Pass enabled using some S8 or S8+ phones with Unity 5.6.0p2-3. They can occur when Standard Shader Quality is set to low, or when you are using tree objects. For more information and workarounds, see “Known Issues” in [Single Pass Stereo Rendering (Preview, Mobile Only)](/documentation/unity/latest/concepts/unity-single-pass/ "Single Pass stereo rendering is a preview rendering feature for Oculus Go and Gear VR available in Unity 5.6. If your application is CPU-bound or draw call bound, we strongly recommend using Single Pass rendering to improve performance.").
	
