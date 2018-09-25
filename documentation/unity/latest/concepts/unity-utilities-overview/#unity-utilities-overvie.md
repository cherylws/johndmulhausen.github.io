---
title: Oculus Utilities for Unity
---
This section provides an overview of the Utilities package, including its directory structure, the supplied prefabs, and several key C# scripts.

The Utilities package is available from our [Unity Downloads](/downloads/unity/) page, and as part of the Oculus Integration available from the Unity Asset Store [here](https://www.assetstore.unity3d.com/en/#!/content/82022).

## OVR Utilities Plugin (OVRPlugin)

The OVR Utilities Plugin (OVRPlugin) provides Rift and Mobile support to the Unity Editor.

All Unity versions 5.1 and later ship with a bundled version of OVRPlugin that provides built-in support for Rift, Oculus Go, and Samsung Gear VR.

Utilities versions 1.14 and later include the latest version of OVRPlugin. When you import Oculus Utilities for Unity into a project, if the OVRPlugin version included with the Utilities package is **later** than the version built into your Editor, a pop-up dialog will give you the option to automatically update it. Note that your project is updated, not your Editor - you may work with different projects using different versions of OVRPlugin with the same Editor. However, we always recommend using the latest available OVRPlugin version.

If you decline to update OVRPlugin during the import process, you may update it later by selecting **Tools > Oculus > Update OVR Utilities Plugin**.

If you update OVRPlugin using the Utilities package and later wish to roll back to the version included with the Editor for any reason, you may easily do so by selecting **Tools > Oculus > Disable OVR Utilities Plugin**.

The update feature is currently not supported on OS X/macOS.

Note: The latest OVRPlugin version number may be a version or two behind the Utilities version number.In Unity apps targeting API levels lower than 23, certain basic permissions, such as INTERNET, are requested in a user-facing UI when the apps are run. For this reason, it is highly recommended that apps target API levels 23 and later because these permissions are automatically granted without prompting the user. The OVRPlugin API is for internal use only, unsupported, and its behavior may change at any time without warning. Do not use it.## Utilities for Unity Contents

This guide offers a high-level description of contents of the Utilities package. 

### OVR

The contents of the OVR folder in OculusUtilities.unitypackage are uniquely named and should be safe to import into an existing project.

The OVR directory contains the following subdirectories:

Editor

Scripts that add functionality to the Unity Editor and enhance several C# component scripts.

Materials

Materials used for graphical components within the Utilities package, such as the main GUI display.

Meshes

Meshes required by some OVR scripts, such as the TrackerBounds.

Prefabs

The main Unity prefabs used to provide the VR support for a Unity scene: OVRCameraRig and OVRPlayerController. 

Scenes

Sample scenes illustrating common concepts. 

Scripts

C# files used to tie the VR framework and Unity components together. Many of these scripts work together within the various Prefabs.

Textures

Image assets required by some script components.

Note: We strongly recommend that developers not directly modify the included OVR scripts.### Plugins

The Plugins folder contains the OVRGamepad.dll, which enables scripts to communicate with the Xbox gamepad on Windows (both 32 and 64-bit versions).

This folder also contains the plugin for Mac OS: OVRGamepad.bundle.

## Prefabs

This section gives a general overview of the Prefabs provided by the Utilities package including OVRCameraRig, which provides an interface to OVRManager, and OVRPlayerController. 

Utilities for Unity provides prefabs in Assets/OVR/Prefabs:

* OVRCameraRig
* OVRPlayerController
* OVRCubemapCaptureProbe
To use, simply drag and drop one of the prefabs into your scene.

### OVRCameraRig

OVRCameraRig is a custom VR camera that may be used to replace the regular Unity Camera in a scene. Drag an OVRCameraRig into your scene and you will be able to start viewing the scene. 

The primary benefit to using OVRCameraRig is that it provides access to OVRManager, which provides the main interface to the VR hardware. If you do not need such access, a standard Unity camera may be easily configured to add basic VR support; see [Unity VR Support](/documentation/unity/latest/concepts/book-unity-dg/ "Welcome to the Oculus Unity Developer Guide.") for more information. 

Note: Make sure to turn off any other Camera in the scene to ensure that OVRCameraRig is the only one being used.![](/images/documentation-unity-latest-concepts-unity-utilities-overview-unity-utilities-overview-0.png)  
OVRCameraRig and OVRManagerOVRCameraRig contains one Unity camera, the pose of which is controlled by head tracking; two “anchor” Game Objects for the left and right eyes; and one “tracking space” Game Object that allows you to fine-tune the relationship between the head tracking reference frame and your world. The rig is meant to be attached to a moving object, such as a character walking around, a car, a gun turret, et cetera. This replaces the conventional Camera.

The following scripts (components) are attached to the OVRCameraRig prefab:

* OVRCameraRig.cs
* OVRManager.cs
Learn more about the OVRCameraRig and OVRManager components in [Unity Components](/documentation/unity/latest/concepts/unity-utilities-overview/#unity-components "This section gives a general overview of the Components provided by the Utilities package.").

### OVRPlayerController

The OVRPlayerController is the easiest way to start navigating a virtual environment. It is basically an OVRCameraRig prefab attached to a simple character controller. It includes a physics capsule, a movement system, a simple menu system with stereo rendering of text fields, and a cross-hair component.

To use, drag the player controller into an environment and begin moving around using a gamepad, or a keyboard and mouse.

Note: Make sure that collision detection is active in the environment.One script (Components) is attached to the OVRPlayerController prefab:

* OVRPlayerController.cs
![](/images/documentation-unity-latest-concepts-unity-utilities-overview-unity-utilities-overview-1.png)  
OVRPlayerController### OVRCubemapCaptureProbe

This prefab allows you to capture a static 360 screenshot of your application while it is running, either at a specified time after launch, when a specified key is pressed, or when the static function OVRCubemapCapture.TriggerCubemapCapture is called. For more information on this function, see our Unity Developer Reference.

OVRCubemapCaptureProbe is based on OVR Screenshot (see [Cubemap Screenshots](/documentation/unity/latest/concepts/unity-cubemap/ "The OVR Screenshot Wizard allows you to easily export a 360 screenshot in cubemap format.") for more information).

Screenshots are taken from the perspective of your scene camera. They are written to a specified directory and may be either JPEG or PNG. File type is specified by the file extension entered in the Path Name field; default is PNG. Resolution is configurable. 

**Basic Use**

Drag OVRCubemapCaptureProbe into the scene and set the parameters as desired in the Inspector view.

![](/images/documentation-unity-latest-concepts-unity-utilities-overview-unity-utilities-overview-2.png)  
**Parameters**

Auto Trigger After Launch

Select to enable capture after a delay specified in Auto Trigger Delay. Otherwise capture is triggered by the keypress specified in Triggered by Key.

Auto Trigger Delay

Specify delay after application launch before cubemap is taken. (requires Auto Trigger After Launch selected).

Triggered By Key

Specifies key to trigger image capture (requires Auto Trigger After Launch not selected).

Path Name

Specifies directory, file name, and file type (JPEG or PNG) for screen capture.

Windows default path: C:\Users\$username\AppData\LocalLow\Sample\$yourAppName\OVR\_ScreenShot306\

Android default path: /storage/emulated/0/Android/data/com.unity3d.$yourAppName/files/OVR\_ScreenShot360/

Default file type: PNG. 

Cubemap Size

Specify size (2048 x 2048 is default, and is the resolution required for preview cubemaps submitted to the Oculus Store). 

## Unity Components

This section gives a general overview of the Components provided by the Utilities package.

### OVRCameraRig

OVRCameraRig is a Component that controls stereo rendering and head tracking. It maintains three child "anchor" Transforms at the poses of the left and right eyes, as well as a virtual "center" eye that is halfway between them.

This Component is the main interface between Unity and the cameras. It is attached to a prefab that makes it easy to add comfortable VR support to a scene.

**Important**: All camera control should be done through this component. You should understand this script when implementing your own camera control mechanism.

### Mobile and Rift Public Members

Updated Anchors

Allows clients to filter the poses set by tracking. Used to modify or ignore positional tracking.

### Game Object Structure

TrackingSpace

A Game Object that defines the reference frame used by tracking. You can move this relative to the OVRCameraRig for use cases in which the rig needs to respond to tracker input. For example, OVRPlayerController changes the position and rotation of TrackingSpace to make the character controller follow the yaw of the current head pose.

### OVRManager

OVRManager is the main interface to the VR hardware. It is a singleton that exposes the Oculus SDK to Unity, and includes helper functions that use the stored Oculus variables to help configure camera behavior.

This component is added to the OVRCameraRig prefab. It can be part of any application object. However, it should only be declared once, because it includes public members that allow for changing certain values in the Unity Inspector. If OVRManager is present in your scene, VR will be automatically enabled.

OVRManager.cs contains the following public members:

Queue Ahead (Deprecated)

When enabled, distortion rendering work is submitted a quarter-frame early to avoid pipeline stalls and increase CPU-GPU parallelism.

Use Recommended MSAA Level

When enabled, Unity will use the optimal antialiasing level for quality/performance on the current hardware.

Enable Adaptive Resolution (Rift only)

Enable to configure app resolution to scale down as GPU exceeds 85% utilization, and to scale up as it falls below 85% (range 0.5 - 2.0; 1 = normal density). Requires Unity 5.4 or later.

To minimize the perceived artifacts from changing resolution, there is a two-second minimum delay between every resolution change.

Min Render Scale (Rift only)

Sets minimum bound for Adaptive Resolution (default = 0.7).

Max Render Scale (Rift only)

Sets maximum bound for Adaptive Resolution (default = 1.0).

Enable Mixed Reality (Rift only)

Enables mixed reality capture. See [Unity Mixed Reality Capture](/documentation/unity/latest/concepts/unity-mrc/ "This guide describes how to add and configure mixed reality capture support for your Unity application. Mixed reality capture is supported for Rift applications only.") for more information.

Use Direct Composition (Rift only)

Opens mixed reality capture view in direct composition mode. Deselect to set to external composition mode.

Green Screen Color Tolerance A (Rift only)

Sets how heavily to weigh non-green values in a pixel for mixed reality capture. (direct composition only)

Green Screen Color Tolerance B (Rift only)

Sets how heavily to weigh green values in a pixel for mixed reality capture. (direct composition only)

Green Screen Color Alpha Cutoff (Rift only)

Alpha cutoff is evaluated after the chroma-key evaluation and before the bleed test to take pixels with a low alpha value and fully discard them. (For mixed reality capture, direct composition only.)

Green Screen Color Shadows (Rift only)

Shadow threshold reduces dark pixels to mitigate the shadow casting issues. (For mixed reality capture, direct composition only.)

Tracking Origin Type

Set to Eye Level to track the position and orientation y-axis relative to the HMD’s position. Set to Floor Level to track position and orientation relative to the floor, based on the user’s standing height as specified in the Oculus Configuration Utility. Default is Eye Level.

Use Position Tracking

Disables the IR tracker and causes head position to be inferred from the current rotation using the head model. 

Use IPD in Position Tracking

If enabled, the distance between the user's eyes will affect the position of each OVRCameraRig's cameras.

Reset Tracker On Load

When disabled, subsequent scene loads will not reset the tracker. This will keep the tracker orientation the same from scene to scene, as well as keep magnetometer settings intact.

### Floating-point format eye buffers

Rift only. Requires Unity 5.6.1p1 or later and Utilities 1.15 or later.

8-bit sRGB framebuffers work well for non-VR apps. However, due to the light-locked nature of VR, when sRGB buffers are used in VR apps, the user’s eyes can adjust to the dark, allowing them to detect subtle differences in dark areas of the scene, including color banding artifacts.

You may use OVRManager to submit floating-point format eye buffers to the Oculus runtime, which helps eliminate color banding in dark areas that might have been visible with 8-bit sRGB eye buffers.

OVRManager supports two floating point formats:

* R11G11B10\_FP: this format has same bandwidth cost with regular 8 bits sRGB framebuffer, so there should be no extra performance cost for regular rendering. This format should be good enough for most applications to remove color banding. However, as the name indicates, there is no alpha channel for this format, so if your application requires destination alpha blending or needs to sample the frame buffer alpha channel, you might prefer R16G16B16A16\_FP
* R16G16B16A16\_FP: this format has full alpha channel with 16-bit floating point precision, which should be compatible with your application even if it requires framebuffer alpha channel. The bandwidth cost is 2x of 8 bit sRGB format.
To enable this feature, add OVRManager.eyeTextureFormat = R11G11B10\_FP or OVRManager.eyeTextureFormat= R16G16B16A16\_FP into your Unity initialization script.

Note: The new eye texture format only works under Linear color space. If you need alpha channel in your frame buffer, you must use OVRManager.eyeTextureFormat = R16G16B16A16\_FP.### Helper Classes

In addition to the above components, your scripts can always access the HMD state via static members of OVRManager. For detailed information, see our [Unity Scripting Reference](/documentation/unity/latest/concepts/unity-reference-scripting/ "The Unity Scripting Reference contains detailed information about the data structures and files included with the Utilities and Legacy Integration packages.").

OVRDisplay

Provides the pose and rendering state of the HMD.

OVRTracker

Provides the pose, frustum, and tracking status of the infrared tracking sensor.

### Rift Recentering

OVRManager.display.RecenterPose() recenters the head pose and the tracked controller pose, if present (see [OVRInput](/documentation/unity/latest/concepts/unity-ovrinput/#unity-ovrinput "OVRInput exposes a unified input API for multiple controller types.") for more information on tracking controllers).

If Tracking Origin Type is set to Floor Level, OVRManager.display.RecenterPose() resets the x-, y-, and z-axis position to origin. If it is set to Eye Level, the x-, y-, and z-axis are all reset to origin, with the y-value corresponding to the height calibration performed with the Oculus Configuration Utility. In both cases, the y rotation is reset to 0, but the x and z rotation are unchanged to maintain a consistent ground plane.

Recenter requests are passed to the Oculus C API. For a more detailed description of what happens subsequently, please see [VR Focus Management](/documentation/pcsdk/latest/concepts/dg-vr-focus/) in our PC SDK Developer Guide.

### Utilities

OVRPlayerController

OVRPlayerController implements a basic first-person controller for the VR framework. It is attached to the OVRPlayerController prefab, which has an OVRCameraRig attached to it.

The controller will interact properly with a Unity scene, provided that the scene has collision detection assigned to it.

OVRPlayerController contains a few variables attached to sliders that change the physics properties of the controller. This includes Acceleration (how fast the player will increase speed), Dampening (how fast a player will decrease speed when movement input is not activated), Back and Side Dampen (how much to reduce side and back Acceleration), Rotation Amount (the amount in degrees per frame to rotate the user in the Y axis) and Gravity Modifier (how fast to accelerate player down when in the air). When HMD Rotates Y is set, the actual Y rotation of the cameras will set the Y rotation value of the parent transform that it is attached to.

The OVRPlayerController prefab has an empty Game Object attached to it called ForwardDirection. This Game Object contains the matrix which motor control bases it direction on. This Game Object should also house the body geometry which will be seen by the player.

OVRGridCube

OVRGridCube is a helper class that shows a grid of cubes when activated. Its main purpose is to be used as a way to know where the ideal center of location is for the user's eye position. This is especially useful when positional tracking is activated. The cubes will change color to red when positional data is available, and will remain blue if position tracking is not available, or change back to blue if vision is lost.

### Game Object Structure

ForwardDirection

An empty Game Object attached to the OVRPlayerController prefab containing the matrix upon which motor control bases its direction. This Game Object should also house the body geometry which will be seen by the player.

See TrackingSpace in “OVRCameraRig” for more information

For more information on OVRInput, see [OVRInput](/documentation/unity/latest/concepts/unity-ovrinput/#unity-ovrinput "OVRInput exposes a unified input API for multiple controller types.").

## Oculus Scripts and Scenes

The Utilities package includes scripts to assist with development and a handful of trivial scenes. 

A handful of rudimentary sample scenes are provided in Assets/OVR/Scenes. They illustrate simple implementations of basic components and may be useful for verifying that VR functionality is working properly. For much more detailed samples including scripts and assets that you may re-use in your own applications, see [Unity Sample Framework](/documentation/unity/latest/concepts/unity-sample-framework/ "The Oculus Unity Sample Framework provides sample scenes and guidelines for common VR-specific features such as hand presence with Oculus Touch, crosshairs, driving, hybrid mono rendering, and video rendering to a 2D textured quad.").

Trivial

An empty scene with one cube and a plain Unity camera. If this scene fails to render normally, Unity’s VR support is not working.

Cubes

A 3D array of cubes and an OVRCameraRig from the Utilities package.

Room

A cubic room formed from six cubes enclosing an OVRPlayerController. Includes the scripts OVRGrabber and OVRGrabbable, enabling users to pick up cubes with Touch controllers.

Scripts for assisting with mobile development are located in Assets/OVR/Scripts/. Scripts included in the folder that are not intended for developers to use are omitted from this list. 

OVRBoundary

Exposes an API for interacting with the Oculus Guardian System. For more information, see [OVRBoundary Guardian System API](/documentation/unity/latest/concepts/unity-ovrboundary/ "OVRBoundary exposes an API for interacting with the Rift Guardian System for Touch."). 

OVRGrabber

Allows grabbing and throwing of objects with the OVRGrabbable component on them using Oculus Touch. Requires OVRGrabbable to use.

OVRGrabbable

Attach to objects to allow them to be grabbed and thrown with the Oculus Touch. Requires OVRGrabber to use.

OVRHaptics

Programmatically controls haptic feedback to Touch controllers. For more information, see [OVRHaptics for Oculus Touch](/documentation/unity/latest/concepts/unity-ovrhaptics/ "This guide reviews OVRHaptics and OVRHapticsClip, two C# scripts that programmatically control haptics feedback for Touch.").

OVRHapticsClip

Programmatically controls haptic feedback to Touch controllers. For more information, see [OVRHaptics for Oculus Touch](/documentation/unity/latest/concepts/unity-ovrhaptics/ "This guide reviews OVRHaptics and OVRHapticsClip, two C# scripts that programmatically control haptics feedback for Touch.").

OVRInput

Exposes a unified input API for multiple controller types. For more information, see [OVRInput](/documentation/unity/latest/concepts/unity-ovrinput/#unity-ovrinput "OVRInput exposes a unified input API for multiple controller types.").

OVROverlay.cs

Add to a Game Object to render as a VR Compositor Layer instead by drawing it into the eye buffer. For more information, see [VR Compositor Layers](/documentation/unity/latest/concepts/unity-ovroverlay/ "OVROverlay is a script in OVR/Scripts that allows you to render Game Objects as VR Compositor Layers instead of drawing them to the eye buffer.")

OVRPlatformMenu.cs

Helper component for detecting Back Key long-press to bring-up the Universal Menu and Back Key short-press to bring up the Confirm-Quit to Home Menu. Additionally implements a Wait Timer for displaying Long Press Time. For more information on interface guidelines and requirements, please review *Interface Guidelines* and *Universal Menu* in the [Mobile SDK documentation](/documentation/mobilesdk/latest/).

OVRTouchpad.cs

Interface class to a touchpad.

Simple scripts for assisting with mobile development are located in Assets/OVR/Scripts/Util. Scripts included in the folder that are not intended for developers to use are omitted from this list.

OVRChromaticAberration.cs

Drop-in component for toggling chromatic aberration correction on and off for Android.

OVRDebugGraph.cs

Drop-in component for toggling the TimeWarp debug graph on and off. Information regarding the TimeWarp Debug Graph may be found in the **TimeWarp technical note** in the [Mobile SDK documentation](/documentation/#filter=mobile).

OVRModeParms.cs

Example code for de-clocking your application to reduce power and thermal load as well as how to query the current power level state.

OVRMonoscopic.cs

Drop-in component for toggling Monoscopic rendering on and off for Android.

OVRResetOrientation.cs

Drop-in component for resetting the camera orientation.

OVRWaitCursor.cs

Helper component for auto-rotating a wait cursor.

See our [Oculus Utilities for Unity Reference Manual](/documentation/game-engines/latest/concepts/book-unity-reference/) for a more detailed look at these and other C# scripts. Undocumented scripts may be considered internal, and should generally never be modified.

