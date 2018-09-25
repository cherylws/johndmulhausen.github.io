---
title: 1.14 Oculus Utilities for Unity 5 Release Notes
---
## Oculus Utilities for Unity 5 version 1.14.0

This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Utilities for Unity 5. For information on first-party changes to Unity VR support for Oculus, see the Unity Release Notes for the appropriate version. You will find a scripting reference for the included C# scripts in our [Unity Reference Content](/documentation/unity/latest/concepts/book-unity-reference/).

## OVRPlugin Now Included with Utilities

All Unity Editor versions ship with a bundled version of the Oculus OVRPlugin that provides built-in Rift and Gear VR support.

Beginning with this release, the Utilities package will also include the latest version of OVRPlugin, allowing us to provide the latest features as quickly as possible.

When you import Utilities for Unity into a Unity project, if the OVRPlugin version included with the Utilities is later than the version built into your editor, a pop-up dialog will give you the option to update it. We always recommend using the latest available OVRPlugin version.

If you install OVRPlugin from the Utilities package and later wish to roll back to the version included with the Editor for any reason, you may easily do so by selecting **Tools > Oculus > Disable OVR Utilities Plugin**.

For more information, please see “OVRPlugin” in [Oculus Utilities for Unity](/documentation/unity/latest/concepts/unity-utilities-overview/#unity-utilities-overview "This section provides an overview of the Utilities package, including its directory structure, the supplied prefabs, and several key C# scripts.").

Note: The update feature is currently not supported on OS X/macOS.## New Features

* Added OVRPlugin auto-updating (see above).
* Added support for preview Single Pass stereo rendering to Unity 5.6 (mobile only), which can provide a significant reduction to CPU overhead. When enabled, objects are rendered to the left buffer and then duplicated with minor adjustment to the right buffer, rather than drawing them in two separate passes. For more information, see [Single Pass Stereo Rendering (Preview, Mobile Only)](/documentation/unity/latest/concepts/unity-single-pass/ "Single Pass stereo rendering is a preview rendering feature for Oculus Go and Gear VR available in Unity 5.6. If your application is CPU-bound or draw call bound, we strongly recommend using Single Pass rendering to improve performance.").
* Performance Auditing Tool improvements. See [Performance Auditing Tool (OVRLint)](/documentation/unity/latest/concepts/unity-perf/#unity-perf-auditing "The performance auditing tool may be used to verify that your Rift or mobile VR project configuration and settings are consistent with our recommendations.") for more information.
	+ Now allows fixes to be applied to multiple instances of the same issue at once.
	+ Click on any reported object with a problem to highlight the relevant object in your scene.
	
## API Changes

* Added OVRInput.RecenterController() to OVRIniput to recenter Gear VR Controller. 
## Known Issues

* Unity 5.6 and later: If you have updated your OVRPlugin version from Utilities, you may see a spurious error message when the Editor first launches saying “Multiple plugins with the same name 'ovrplugin'”. Please disregard.
* Gear VR applications built with Unity 5.6.0f2 crash immediately upon launch, and Gear VR applications built with 5.6.0p1 may crash when Multi-View is enabled.
* Unity 5.6 and later: If you have updated your OVRPlugin version from Utilities, you may see a spurious error message when the Editor first launches saying “Multiple plugins with the same name 'ovrplugin'”. Please disregard. 
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
	