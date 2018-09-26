---
title: A Detailed Look at the Unity Integration
---

This section examines the Unity integration, including the directory structure of the integration, the Unity prefabs are described, and several key C# scripts.

## Contents



### OVR

The contents of the OVR folder in OculusUnityIntegration.unitypackage are uniquely named and should be safe to import into an existing project.

The OVR directory contains the following subdirectories:

|  Editor  |                            Contains scripts that add functionality to the Unity Editor, and enhance several C# component scripts.                            |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Materials |                        Contains materials that are used for graphical components within the integration, such as the main GUI display.                        |
| Moonlight | Contains classes designed for mobile development. Holds sub-folders with mobile equivalents of all top-level folders (Editor, Materials, Prefabs, et cetera). |
|  Prefabs  |               Contains the main Unity prefabs that are used to provide the VR support for a Unity scene: OVRCameraRig and OVRPlayerController.               |
| Resources |                       Contains prefabs and other objects that are required and instantiated by some OVR scripts, such as the main GUI.                       |
|  Scenes  |                                                                    Contains sample scenes.                                                                    |
|  Scripts  |  Contains the C# files that are used to tie the VR framework and Unity components together. Many of these scripts work together within the various Prefabs.  |
|  Shaders  |                                              Contains various Cg shaders required by some of the OVR components.                                              |
| Textures |                                           Contains image assets that are required by some of the script components.                                           |

### Plugins

The Plugins folder contains vrapi.so and the OculusPlugin.dll, which enables the VR framework to communicate with Unity on Windows (both 32 and 64-bit versions).

This folder also contains the plugins for other platforms: OculusPlugin.bundle for MacOS; and Android/libOculusPlugin.so, vrlib.jar, and AndroidManifest.xml for Android.

## Prefabs



The current integration for adding VR support into Unity applications is based on two prefabs that may be added into a scene:

* OVRCameraRig
* OVRPlayerController


To use, simply drag and drop one of the prefabs into your scene.

### OVRCameraRig

OVRCameraRig replaces the regular Unity Camera within a scene. You can drag an OVRCameraRig into your scene and you will be able to start viewing the scene with the Gear VR and Rift.

![](/images/documentationunitylatestconceptsunity-integration-overview-0.png)

OVRCameraRig contains two Unity cameras, one for each eye. It is meant to be attached to a moving object (such as a character walking around, a car, a gun turret, etc.) This replaces the conventional Camera.

The following scripts (components) are attached to the OVRCameraRig prefab:

* OVRCameraRig.cs
* OVRManager.cs


### OVRPlayerController

The OVRPlayerController is the easiest way to start navigating a virtual environment. It is basically an OVRCameraRig prefab attached to a simple character controller. It includes a physics capsule, a movement system, a simple menu system with stereo rendering of text fields, and a cross-hair component.

To use, drag the player controller into an environment and begin moving around using a gamepad, or a keyboard and mouse. 

Two scripts (components) are attached to the OVRPlayerController prefab:

* OVRPlayerController.cs
* OVRGamepadController.cs


![](/images/documentationunitylatestconceptsunity-integration-overview-1.png)

## Unity Components

This section gives a general overview of the Components provided by the legacy integration.

### OVRCameraRig

OVRCameraRig is a component that controls stereo rendering and head tracking. It maintains three child "anchor" Transforms at the poses of the left and right eyes, as well as a virtual "center" eye that is halfway between them.

This component is the main interface between Unity and the cameras. This is attached to a prefab that makes it easy to add comfortable VR support to a scene.

**Important**: All camera control should be done through this component. You should understand this script when implementing your own camera control mechanism.

### Mobile and PC Public Members

| Updated Anchors | Allows clients to filter the poses set by tracking. Used to modify or ignore positional tracking. |
|-----------------|---------------------------------------------------------------------------------------------------|

### GameObject Structure

| TrackingSpace | A GameObject that defines the reference frame used by tracking. You can move this relative to the OVRCameraRig for use cases in which the rig needs to respond to tracker input. For example, OVRPlayerController changes the position and rotation of TrackingSpace to make the character controller follow the yaw of the current head pose. |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### OVRManager

OVRManager is the main interface to the VR hardware. It is a singleton that exposes the Oculus SDK to Unity, and includes helper functions that use the stored Oculus variables to help configure camera behavior.

This component is added to the OVRCameraRig prefab. It can be part of any application object. However, it should only be declared once, because there are public members that allow for changing certain values in the Unity inspector.

OVRManager.cs contains the following public members:

|        Monoscopic        | If true, rendering will try to optimize for a single viewpoint rather than rendering once for each eye. Not supported on all platforms. |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
|    Eye Texture Format    |       Sets the format of the eye RenderTextures. Normally you should use Default or DefaultHDR for high-dynamic range rendering.       |
|    Eye Texture Depth    |             Sets the depth precision of the eye RenderTextures. May fix z-fighting artifacts at the expense of performance.             |
| Eye Texture Antialiasing |                                       Sets the level of antialiasing for the eye RenderTextures.                                       |

|      Native Texture Scale      | Each camera in the camera controller creates a RenderTexture that is the ideal size for obtaining the sharpest pixel density (a 1-to-1 pixel size in the center of the screen post lens distortion). This field can be used to permanently scale the cameras' render targets to any multiple ideal pixel fidelity, which gives you control over the trade-off between performance and quality. |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      Virtual Texture Scale      |                                                                                                         This field can be used to dynamically scale the cameras render target to values lower than the ideal pixel fidelity, which can help reduce GPU usage at run-time if necessary.                                                                                                         |
|      Use Position Tracking      |                                                                                     Disables the IR tracker and causes head position to be inferred from the current rotation using the head model. To fully ignore tracking or otherwise modify tracking behavior, see OVRCameraRig.UpdatedAnchors above                                                                                     |
|        Mirror to Display        |                                                       When enabled, the undistorted rendered output appears on your desktop in addition to the Rift. If disabled, you may add your own scripts next to OVRCameraRig and set that GameObject's Camera component to render whatever you like. Disabling may slightly improve performance.                                                       |
|    Time Warp (desktop only)    |                                                                       Time warp is a technique that adjusts the on-screen position of rendered images based on the latest tracking pose at the time the user will see it. Enabling this will force vertical-sync and make other timing adjustments to minimize latency.                                                                       |
| Freeze Time Warp (desktop only) |                                                                                                                                              If enabled, this illustrates the effect of time warp by temporarily freezing the rendered eye pose.                                                                                                                                              |
|      Reset Tracker On Load      |                                                                                      This value defaults to True. When turned off, subsequent scene loads will not reset the tracker. This will keep the tracker orientation the same from scene to scene, as well as keep magnetometer settings intact.                                                                                      |

### Helper Classes

In addition to the above components, your scripts can always access the HMD state via static members of OVRManager.

| OVRDisplay |                Provides the pose and rendering state of the HMD.                |
|------------|----------------------------------------------------------------------------------|
| OVRTracker | Provides the pose, frustum, and tracking status of the infrared tracking sensor. |

### OVRCommon

| OVRCommon | OVRCommon is a collection of reusable static functions. |
|-----------|---------------------------------------------------------|

### Utilities

The following classes are optional. We provide them to help you make the most of virtual reality, depending on the needs of your application.

| OVRPlayerController | OVRPlayerController implements a basic first-person controller for the VR framework. It is attached to the OVRPlayerController prefab, which has an OVRCameraRig attached to it.The controller will interact properly with a Unity scene, provided that the scene has collision detection assigned to it.OVRPlayerController contains a few variables attached to sliders that change the physics properties of the controller. This includes Acceleration (how fast the player will increase speed), Dampening (how fast a player will decrease speed when movement input is not activated), Back and Side Dampen (how much to reduce side and back Acceleration), Rotation Amount (the amount in degrees per frame to rotate the user in the Y axis) and Gravity Modifier (how fast to accelerate player down when in the air). When HMD Rotates Y is set, the actual Y rotation of the cameras will set the Y rotation value of the parent transform that it is attached to.The OVRPlayerController prefab has an empty GameObject attached to it called ForwardDirection. This GameObject contains the matrix which motor control bases it direction on. This GameObject should also house the body geometry which will be seen by the player. |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OVRGamepadController |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  OVRGamepadController is an interface class to a gamepad controller.On Windows systems, the gamepad must be XInput-compliant.**Note**: currently native XInput-compliant gamepads are not supported on Mac OS. Please use the conventional Unity input methods for gamepad input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|     OVRCrosshair     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        OVRCrosshair is a helper class that renders and controls an on-screen cross-hair. It is currently used by the OVRMainMenu component.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|        OVRGUI        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    OVRGUI is a helper class that encapsulates basic rendering of text in either 2D or 3D. The 2D version of the code will be deprecated in favor of rendering to a 3D element (currently used in OVRMainMenu).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|     OVRGridCube     |                                                                                                                                                                                                                                                                                                                                                                                                      OVRGridCube is a helper class that shows a grid of cubes when activated. Its main purpose is to be used as a way to know where the ideal center of location is for the user's eye position. This is especially useful when positional tracking is activated. The cubes will change color to red when positional data is available, and will remain blue if position tracking is not available, or change back to blue if vision is lost.                                                                                                                                                                                                                                                                                                                                                                                                      |
|   OVRTrackerBounds   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Warns players when the HMD moves outside the trackable range.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### GameObject Structure

| ForwardDirection | An empty GameObject attached to the OVRPlayerController prefab containing the matrix upon which motor control bases its direction. This GameObject should also house the body geometry which will be seen by the player.See TrackingSpace in OVRCameraRig for more information |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

For more information on OVRInput, see [OVRInput](/documentation/unity/latest/concepts/unity-integration-ovrinput/#unity-integration-ovrinput).

## Oculus Mobile SDKExamples

The Mobile SDK includes sample applications to illustrate implementation of common functionality such as a first-person scene and crosshairs. 

To import SDKExamples into Unity, begin by creating a new, empty project. Then select **Assets** &gt; **Import Package** &gt; **Custom Package...** and select SDKExamples.unityPackage to import the assets into your project. Alternately, you can locate the SDKExamples.unityPackage and double-click to launch, which will have the same effect.

 Once imported, replace your Unity project's ProjectSettings folder with the ProjectSettings folder included with SDKExamples.

You will find the following sample scenes located in Assets/Scenes:

|    Cubes    |               A 3D array of cubes and an OVRCameraRig.               |
|-------------|----------------------------------------------------------------------|
| Multicamera |            An example of switching cameras in one scene.            |
|    Room    | A cubic room formed from six cubes enclosing an OVRPlayerController. |

The example scripts are located in Assets/OVR/Moonlight/:

| OVRChromaticAberration.cs |                                                                                                                                                                                               Drop-in component for toggling chromatic aberration correction on and off for Android.                                                                                                                                                                                               |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      OVRCrosshair.cs      |                                                                                                                                                                                                             A component that adds a stereoscopic crosshair to a scene.                                                                                                                                                                                                             |
|     OVRDebugGraph.cs     |                                                                                                                                                                                               Drop-in component for toggling the TimeWarp debug graph, which is no longer available.                                                                                                                                                                                               |
| OVRDebugHeadController.cs |                                                                                                                                                         A simple behavior that can be attached to the parent of the CameraRig to provide movement via the gamepad, useful for testing applications in Unity without an HMD.                                                                                                                                                         |
|    OVRInputControl.cs    |                                                                                                                                                                                                                       Cross-platform wrapper for Unity Input.                                                                                                                                                                                                                       |
|      OVRModeParms.cs      |                                                                                                                                                                        Example code for de-clocking your application to reduce power and thermal load as well as how to query the current power level state.                                                                                                                                                                        |
|     OVRMonoscopic.cs     |                                                                                                                                                                                                     Drop-in component for toggling Monoscopic rendering on and off for Android.                                                                                                                                                                                                     |
|       OVROverlay.cs       |                                                                                                                                                                         Add to an object with a Quad mesh filter to have the quad rendered as a TimeWarp overlay instead by drawing it into the eye buffer.                                                                                                                                                                         |
|    OVRPlatformMenu.cs    | Helper component for detecting Back Key long-press to bring-up the Universal Menu and Back Key short-press to bring up the Confirm-Quit to Home Menu. Additionally implements a Wait Timer for displaying Long Press Time. For more information on interface guidelines and requirements, please review *Interface Guidelines* and *Universal Menu* in the `Mobile SDK documentation`_.  .. _Mobile SDK documentation: https://developer.oculus.com/documentation/mobilesdk/latest/ |
|  OVRResetOrientation.cs  |                                                                                                                                                                                                               Drop-in component for resetting the camera orientation.                                                                                                                                                                                                               |
|    OVRTimeWarpUtils.cs    |                                                                                                                                                                            Demonstrates the interface calls for setting important configs, including min vsyncs, enable tw debug graph, and enable cac.                                                                                                                                                                            |
|      OVRTouchpad.cs      |                                                                                                                                                                                                                           Interface class to a touchpad.                                                                                                                                                                                                                           |
|    OVRVolumeControl.cs    |                                                                                                                                                                                                          An on-screen display that shows the current system audio volume.                                                                                                                                                                                                          |
|     OVRWaitCursor.cs     |                                                                                                                                                                                                                  Helper component for auto-rotating a wait cursor.                                                                                                                                                                                                                  |

See our [Oculus Utilities for Unity Reference Manual](/documentation/game-engines/latest/concepts/book-unity-reference/) for a more detailed look at these and other C# scripts. Undocumented scripts may be considered internal, and should generally never be modified. 
