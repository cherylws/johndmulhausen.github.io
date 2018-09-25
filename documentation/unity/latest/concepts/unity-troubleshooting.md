---
title: Troubleshooting and Known Issues
---
This section outlines some currently known issues with the Oculus Unity Integration and the Oculus Utilities for Unity.

## Rift

**The app does not launch as a VR app.**

Verify that you have installed the Oculus app and completed setup as described in [Preparing for Rift Development](/documentation/unity/latest/concepts/unity-pcprep/ "Unity 5 or later offers built-in Rift support. The Oculus SDK is not required.").

Verify that you have selected **Virtual Reality Supported** in **Player Settings**.

are using a compatible runtime - see [Compatibility and Requirements](/documentation/unity/latest/concepts/unity-req/ "This guide describes Unity Editor version recommendations and system requirements.") for more details.

Verify that the HMD is plugged in and working normally. 

Verify that you have not selected D3D 9 or Windows GL as the renderer (Legacy Integration only).

## Mobile

**The app does not launch as a VR app.**

Verify that you selected **Virtual Reality Supported** in **Player Settings** before building your APK. 

**Applications fail to launch on Gear VR with error message "thread priority security exception make sure the apk is signed”.**

You must sign your application with an Oculus Signature File (osig). See "Sign your App with an Oculus Signature File" in [Preparing for Mobile Development](/documentation/unity/latest/concepts/unity-mobileprep/ "To prepare for Unity mobile development for Oculus Go and Samsung Gear VR, you must set up the Unity Editor for Android development and install the Android SDK. The Oculus Mobile SDK is not required.") for instructions.

## General Issues

**Unity 5 hangs while importing assets from SDKExamples.**

Unity 5 is known to import ETC2-compressed assets very slowly.

**Receiving OVRPlugin console errors after importing a new version of Utilities.**

Be sure to delete any previously-imported Utilities packages from your Unity project before importing a new version. If you are receiving errors and have not done so, delete the relevant folders in your project and re-import Utilities. For more information, please see [Importing the Oculus Utilities Package](/documentation/unity/latest/concepts/unity-import/ "Oculus Utilities for Unity is an optional Unity Package that includes scripts, prefabs, and other resources to assist with development.").

 table, th, td { border: 1px solid black; } th { text-align: center;} td, th { padding: 5px;} ### Version-Specific Known Issues

This section details known issues with specific versions of Unity.

**Unity Version**

**Known Issues**

2018.2

2017.4

2017.3

All Unity 2018.2 versions

All Unity 2017.4.1 versions

All Unity 2017.3 versions

* (Mobile) You'll need to either switch the AndroidBuildSystem to internal or export a Gradle project and modify the SigningConfig in the build.gradle file to include v1SigningEnabled=true, v2SigningEnabled=false. 
2017.2

Unity versions 2017.2.0f3-2017.2.0p2

* The Unity engine uses projection matrix calculations that are at variance with the Oculus SDK, causing VR scenes to have the wrong parallax, which may cause discomfort.
2017.1

Unity versions 2017.1-2017.1.2p1

* The Unity engine uses projection matrix calculations that are at variance with the Oculus SDK, causing VR scenes to have the wrong parallax, which may cause discomfort.
Unity 2017.1.0f2 and later

* When using Adaptive Resolution, you might experience some slightly pixel shaking when resolution is changing, this is a known issue, we are working with Unity to resolve it.
5.6

Unity versions 5.6 and later

* If you have updated your OVRPlugin version from Utilities, you may see a spurious error message when the Editor first launches saying “Multiple plugins with the same name 'ovrplugin'”. Please disregard.
Unity 5.6.0f2 and Unity 5.6.0p1

* Gear VR applications built with these versions crash immediately upon launch. 
Unity versions 5.6.0p2-5.6.0p3

* Two graphics driver issues affect mobile applications with Single Pass Stereo rendering enabled using some S8 or S8+ phones. They can occur when Standard Shader Quality is set to low, or when you are using tree objects. For more information and workarounds, see “Known Issues” in the Single Pass Stereo Rendering section of [Advanced Rendering Features.](/documentation/unity/latest/concepts/unity-rendering/)
Unity 5 5.6.3p2-5.6.4p1

* The Unity engine uses projection matrix calculations that are at variance with the Oculus SDK, causing VR scenes to have the wrong parallax, which may cause discomfort.
  
  
### General Unity Known Issues

This section details known issues with Unity that are not tied to a specific version. Issues are grouped by most closely related subject.

**Subject**

**Known Issues**

Unity

* Unity has a known issue such that parenting one VR camera to another will compound tracking twice. As a workaround, make them siblings in the GameObject hierarchy.
Windows 10

* If you experience long UI stalls or poor performance with the Unity Editor when targeting Rift on Windows 10, please run Windows Update to ensure that you have the latest version of Windows 10.
* All Unity versions with Oculus runtime 1.17+ and Windows 10 + Creators Update: This combination results in spurious WM\_DEVICECHANGE reports in the Editor, even in non-VR projects. Many users will notice no impact, but users connected to certain USB devices may find the Editor becomes non-responsive and needs to be terminated from Task Manager. To mitigate, please update to the Beta runtime available on our Public Test channel. We are currently working with Unity and Microsoft on a permanent solution.
Rift

* Guardian System API: ovr\_SetBoundaryLookAndFeel currently does not take effect if the HMD is not worn when the call is made (e.g., on Start).
* Transparent VR Compositor Layers do not currently support multiple layers of occlusion.
* For Mixed Reality Capture, ZED Camera users should upgrade their SDK version to 2.3.1 or later. Previous versions are not compatible.
Mobile

* A known bug in Unity causes a deterioration of performance in mobile applications when the back button is used to enter the Universal Menu and then to return to the application. It particularly affects applications that use multi-threading or which have high CPU utilization, and S7 (Europe) and S8 (global) phones. This bug is fixed in Unity versions 2017.3.0b9 , 2017.2.0p3, 2017.1.2p4, and 5.6.4p2.
* Do not use Utilities 1.11.0 due to a crash when returning to focus from Universal Menu or Quit to Home dialog.
* When Single Pass Stereo rendering is enabled, building projects will fail with the error message “Shader error in 'Mobile/Bumped Detail Diffuse'” in certain cases. For more information, see “Known Issues” in the Single Pass Stereo Rendering section of [Advanced Rendering Features](/documentation/unity/latest/concepts/unity-rendering/).
* (Gear VR) Flickering or left/right eye mismatching can occur when you have an input attribute value pass through to a pixel shader directly on Mali GPUs such as those in Samsung phones (used in Gear VR HMDs). This is because the ARM driver specifically targets such "volatile" data and tries to optimize for it, inadvertently creating the issue. A workaround is to try to use a modified version of the original value in some way. For example, instead of passing input value a directly through to shader value b, set b = a + 0.0001; which will prevent the driver from treating b differently.
  
  
## Contact Information

Questions?

Visit our developer support forums at [https://developer.oculus.com](/).

Our Support Center can be accessed at [https://support.oculus.com](https://support.oculus.com/).

