---
title: "Oculus Rift:  Mixed Reality Capture"
---

This guide describes how to add and configure mixed reality capture support for your Unreal application. Mixed reality capture is supported for Rift applications only.

## Introduction

Mixed reality capture places real-world people and objects in VR. It allows live video footage of a Rift user to be composited with the output from a game to create combined video that shows the player in a virtual scene.

![](/images/documentationunreallatestconceptsunreal-mrc-0.png)

(Courtesy of Medium and artist Dominic Qwek - [https://www.oculus.com/medium/](https://www.oculus.com/medium/))

Live video footage may be captured with a stationary or tracked camera. For more information and complete setup instructions, see the [Mixed Reality Capture Setup Guide](/documentation/pcsdk/latest/concepts/mr-intro/).

Once configured to use mixed reality capture, applications can be launched with the feature enabled by running them with the appropriate parameter - see "Command-line Parameter Reference" below for more information. 

Once an application is configured by developers to use mixed reality capture, users can launch applications with the feature enabled and control several relevant settings with settings controlled by Engine.ini or command-line parameters. See “[Oculus.Settings.MixedReality] in Engine.ini” below for more information.

Mixed Reality Capture is available in Unreal versions that use Oculus OVRPlugin 1.16 or later available through the Oculus GitHub repository. For more information, see [Unreal/Oculus SDK Version Compatibility](/documentation/unreal/latest/concepts/unreal-engine/).

## Compositing the Scene

Mixed reality capture supports two methods for combining application output and video footage: direct composition and external composition.

In **direct composition** mode, your mixed reality capture application streams the real-world footage from your camera to your scene directly, and displays the composited image in the application itself. Direct composition mode requires the use of a green screen for video capture, and the composited image may exhibit some latency from the video stream. We currently recommend using it for proof-of-concept, troubleshooting, and hobby use.

For more polished composition, we recommend using **external composition** mode. In this mode, the application outputs two windows. The MirrorWindow displays the application, as shown below. The second window displays the foreground content from the video stream on the left against a green background, and it displays the background content on the right.

![](/images/documentationunreallatestconceptsunreal-mrc-1.png)

In external composition mode, third-party composition software such as OBS Studio or XSplit is required to clip the green screen, combine the images, and compensate for camera latency.

For more information on how to composite a scene, see the [Mixed Reality Capture Setup Guide](/documentation/pcsdk/latest/concepts/mr-intro/).

## Preparation

You must run the CameraTool prior to launching your mixed reality capture application to configure the external camera and VR Object. See the [Mixed Reality Capture Setup Guide](/documentation/pcsdk/latest/concepts/mr-intro/) for setup information.

## Create Simple VR Application (Optional)

If you wish to experiment with this feature but do not have a VR application prepared, create a basic application with the following steps.

1. Create a new project with the Virtual Reality Blueprint template.
2. Open the MotionControllerMap in **Content &gt; VirtualRealityBP &gt; Maps**.
3. Configure the Virtual Reality Blueprint for mixed reality capture.
	1. (Optional) To be able to use a Touch controller as an input device with the Virtual Reality Blueprint, open the Project Settings menu, select **Engine - Input** and expand **Action Mappings**. Modify the settings as shown below.![](/images/documentationunreallatestconceptsunreal-mrc-2.png)
	
	
	2. (Optional) **Open Edit Preference** in the **General - Miscellaneous** panel and uncheck **Use Less CPU when in Background**. This prevents applications with mixed reality capture enabled from entering a low-FPS mode when switching to the composition software.
	3. The MotionControllerPawn Blueprint contains a bug which sets the Tracking Origin to "Eye Level" incorrectly. Add a link between "Default" and "Set Tracking Origin (Floor Level) as shown:
	


![](/images/documentationunreallatestconceptsunreal-mrc-3.png)

## Add Mixed Reality Capture Support

To enable mixed reality capture, you will add a camera actor to your map, and set it as the origin for your tracking space (optional). See the "Blueprint Reference" below for detailed information on the various components and settings.

![](/images/documentationunreallatestconceptsunreal-mrc-4.png)

1. In the Level editor:
	1. Add an instance of "Oculus MR Casting Camera Actor" to the map, which will be used in mixed reality capture. The composition parameters for this view may be set in the **Oculus MR** section of the OculusMR\_CastingCameraActor instance.
	![](/images/documentationunreallatestconceptsunreal-mrc-5.png)


2. In the Level Blueprint editor:
	1. Set VRPawn’s VROrigin (or the tracking origin component in your map) as the OculusMR\_CastingCameraActor1’s TrackingReferenceComponent. If you plan to use the first PlayerController’s position as the tracking reference, you may skip this step. See "Blueprint Reference" below for more information.
	2. Bind the OculusMR\_CastingCameraActor1 to the first TrackedCamera, which was configured with the CameraTool. The final Blueprint should looks like this:
	![](/images/documentationunreallatestconceptsunreal-mrc-6.png)


3. (Optional) Check the **Casting Auto Start** checkbox in the **Oculus MR** section of OculusMR\_CastingCameraActor1 to configure the engine to automatically open the Casting Window on launch. This option is useful for debugging.


To check that everything is working properly, launch the map in VR Preview mode and verify that the Casting Window opens with the mixed reality capture content.

## Sample Scene

A trivial sample map with mixed reality capture enabled is available in the private Oculus Unreal GitHub repository (access instructions [here](/documentation/unreal/latest/concepts/unreal-engine/)) in Samples/Oculus/MixedRealitySample.

## [Oculus.Settings.MixedReality] in Engine.ini

You may override any local Mixed Reality Capture settings by specifying launch settings in the [Oculus.Settings.MixedReality] section in your Engine.ini file.

To easily write Mixed Reality Capture settings to Engine.ini, configure your project with the desired settings and launch the application with the `-save_mxr_settings` parameter. This will create an [Oculus.Settings.MixedReality] section with the current configuration settings in **Saved/Config/Windows/Engine.ini**. Any user may edit the Engine.ini file to change these settings later.

To launch an application using the settings specified in Engine.ini, use the launch parameter -load_mxr_settings.

## Launch Commands

Once you package the sample scene, you may launch it with these parameters.

You may set your application to launch with mixed reality capture enabled in Blueprints for debugging purposes only. The Blueprint setting `bCastingAutoStart` is automatically disabled when you build your package.

```
// launch in direct composition mode
MixedRealitySample.exe -vr -mxr_open_direct_composition 	

// launch in direct composition mode with MirrorWindow projection
MixedRealitySample.exe -vr -mxr_open_direct_composition -mxr_project_to_mirror_window 

// launch in MultiView mode
MixedRealitySample.exe -vr -mxr_open_multiview 

// launch in MultiView with MirrorWindow projection
MixedRealitySample.exe -vr -mxr_open_multiview -mxr_project_to_mirror_window
   
// launch using settings in [Oculus.Settings.MixedReality] section in Engine.ini (overrides local settings)
-load_mxr_settings
   
// Save current settings to [Oculus.Settings.MixedReality] section in Engine.ini.
-save_mxr_settings
```

## Mixed Reality Capture Features

The following features work for direct composition.

Chroma Key

Chroma key settings allow for fine-tuned control of how the video and application streams are composited. Use these settings to set the reference color of the green screen and control various thresholds at which video pixels are included or excluded from the final frame.

Dynamic Lighting

When Dynamic Lighting is enabled, video captured by the physical camera is illuminated in the composted scene by light effects and flashes within the application. For example, a player would briefly be brightly lit during an explosion in the game.

Lighting is applied to video on a flat plane parallel to the camera unless a depth-sensing camera is used (ZED camera), in which case pixel depth is used to generate a per-pixel normal which is used in the lighting process.

Virtual Green Screen

When enabled, Virtual Green Screen crops video footage that falls outside of the Guardian System Outer Boundary or Play Area configured by the user. The Outer Boundary is the actual perimeter drawn by the user during Touch setup, while the Play Area is a rectangle calculated from the Outer Boundary. Note that the Outer Boundary and Play Area are two-dimensional shapes in the x and z axis. Note that the Outer Boundary and Play Area are two-dimensional shapes in the x and z axis, and the virtual green screen is a 3D volume whose caps are set at +/- 10 meters by default.

## Blueprint Reference

## AOculusMR_CastingCameraActor

Properties

|                  Property                  |                                                                                                                                                                                 Description                                                                                                                                                                                 |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|             bCastingAutoStart             |                                              Starts mixed reality capture casting automatically when the level starts. This option is for debugging only, and will be automatically disabled when the game is launched as a standalone package. Use launch commands to launch applications with mixed reality capture enabled.                                              |
|           bProjectToMirrorWindow           | Set to true to cast to the MirrorWindow. This can simplify window switching, especially on a single-monitor configuration. By default the scene is casted to a standalone window, which offers the most precision in the composition.When set to true, the bProjectToMirrorWindow is automatically minimized on startup, as the content is now casting to the MirrorWindow. |
|             CompositionMethod             |                                                                                        MultiView (default): The casting window includes the background and foreground view for external composition.DirectComposition: The game scene is composited with the camera frame directly.                                                                                        |
|             ClippingReference             |                       Specifies the distance from the camera to the mixed reality capture casting background/foreground boundary. Set to CR_TrackingReference to use the distance to the Tracking Reference (recommended for stationary experiences). Set to CR_Head to use the distance to the HMD (default, recommended for roomscale experiences).                       |
|               TrackedCamera               |                                                                                                                                                     Information about the tracked camera which this object is bound to.                                                                                                                                                     |
|         TrackingReferenceComponent         |                                                                         (optional) If the application uses a VROrigin component to set the tracking space origin, specify that component here. Otherwise the system will use the location of the first PlayerController as the tracking reference.                                                                         |
|          bFollowTrackingReference          |                                                                                                                                        If true the casting camera will automatically follow the movement of the tracking reference.                                                                                                                                        |
|        bUseTrackedCameraResolution        |                                                                                                                                  If true the casting viewports will use the same resolution as the camera used in the calibration process.                                                                                                                                  |
|                WidthPerView                |                                                                                                                     When bUseTrackedCameraResolution is false, sets the width of each casting viewport (foreground, background, or direct composited).                                                                                                                     |
|               HeightPerView               |                                                                                                                     When bUseTrackedCameraResolution is false, sets the height of each casting viewport (foreground, background, or direct composited).                                                                                                                     |
|              CapturingCamera              |                                                                                        When CompositionMethod is set to DirectComposition, indicates which physical camera device provides the video frame for compositing. Options are Web Camera 0, Web Camera 1, and ZED camera.                                                                                        |
|               CastingLatency               |                                                                                         When CompositionMethod is set to MultiView, sets the latency of the casting output. This setting may be used to help sync with the camera latency in the external composition application.                                                                                         |
|            HandPoseStateLatency            |                                                                                                                            Adds a delay in seconds (max. 0.5) to the tracked controllers in the composited scene to correct for camera latency.                                                                                                                            |
|               ChromaKeyColor               |                                                                                         Specify the approximate color of your green screen as compositing reference. The default value is Color.green, which matches a typical general green screen under good lighting conditions.                                                                                         |
|            ChromaKeySimilarity            |                                                            When the distance between pixel color and chromaKeyColor is less than chromaKeySimiliarity, the pixel is hidden. Increase this value if the green screen is partially visible, and reduce this value if the person in the scene partially disappears.                                                            |
|            ChromaKeySmoothRange            |                                                                  Defines a small range of color distance between the pixel and the green screen in which the video frame pixel will be rendered as semi-transparent. Increase this value to make the person image more smooth, and decrease it to sharpen                                                                  |
|            ChromaKeySplitRange            |                                                      Defines a small range of color distance between the pixel and the green screen in which the video frame pixel will be desaturated. Increase this value to reduce green edges around the persons image. Decrease it if the person image looks overly desaturated.                                                      |
|           VirtualGreenScreenType           |                                                                                                                                                                Options are Off, OuterBoundary, or PlayArea.                                                                                                                                                                |
|             UseDynamicLighting             |                                                                                                                                                                   Set to true to active Dynamic Lighting.                                                                                                                                                                   |
|                DepthQuality                |                                                                                                        Sets quality level of depth image for dynamic lighting to Low, Medium, or High. Higher values are more smooth and accurate, but more costly for performance.                                                                                                        |
|      DynamicLightingDepthSmoothFactor      |                                                                                                                              Larger values make dynamic lighting effects smoother, but values that are too large make the lighting look flat.                                                                                                                              |
| DynamicLightingDepthVariationClampingValue |                                                                                                                                             Sets the maximum depth variation across edges (smaller values set smoother edges).                                                                                                                                             |

Methods

|               Method               |                                                                                                                                  Description                                                                                                                                  |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BindToTrackedCameraIndexIfAvailable | Binds the casting camera to the calibrated external camera. If there is no calibrated external camera, the TrackedCamera parameters must be set up to match CastingCameraActor placement. It provides an easy way to directly place a stationary casting camera in the level. |
|   RequestTrackedCameraCalibration   |                                                               When bFollowTrackingReference is false, manually call this method to move the casting camera to follow the tracking reference (i.e., the player).                                                               |
|          OpenCastingWindow          |                                                                                                                           Opens the casting window.                                                                                                                           |
|         CloseCastingWindow         |                                                                                                                          Closes the casting window.                                                                                                                          |
|         ToggleCastingWindow         |                                                                                                                          Toggles the casting window.                                                                                                                          |
|       HasCastingWindowOpened       |                                                                                                             Checks if the casting window has already been opened.                                                                                                             |

## FTrackedCamera

Properties

|               Property               |                                                                              Description                                                                              |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                Index                |             &gt;=0: the index of the external camera.-1: Do not bind to any external camera (i.e., set up to match the manual CastingCameraActor placement).             |
|                 Name                 |                                                          The external camera name set through the CameraTool.                                                          |
|             FieldOfView             |                                                                      Horizontal FOV, in degrees.                                                                      |
|             SizeX, SizeY             |                                                                    Resolution of the camera frame.                                                                    |
|        AttachedTrackedDevice        |      The tracking node the external camera is bound to:* None: stationary camera * HMD, LTouch, RTouch: HMD or left/right Touch * DeviceObjectZero: The VR object      |
| CalibratedRotation, CalibratedOffset |             The relative pose of the camera to the attached tracking device.Equals the absolute pose in the tracking space if AttachedTrackedDevice==None.             |
|       UserRotation. UserOffset       | (optional) Provide user pose to fine tune the relative camera pose at the run-time.Use to match the manual CastingCameraActor placement in the level when Index == -1. |

## UOculusMRFunctionLibrary

Methods

|       Method       |                                      Description                                      |
|---------------------|----------------------------------------------------------------------------------------|
| GetAllTrackedCamera | Retrieve an array of all tracked cameras which were calibrated through the CameraTool. |

## Command-line Parameter Reference

|           Parameter           |                                                         Description                                                         |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------|
|           -mxr_open           |                             Automatically open the casting window in the preset composition mode                             |
|      -mxr_open_multiview      |                             Automatically open the casting window in MultiView composition mode.                             |
| -mxr_open_direct_composition |                               Automatically open the casting window in DirectCompositon mode.                               |
| -mxr_project_to_mirror_window |                                       Project the casting output to the MirrorWindow.                                       |
|      -save_mxr_settings      | Create an [Oculus.Settings.MixedReality] section with the current configuration settings in Saved/Config/Windows/Engine.ini. |
|      -load_mxr_settings      |       Load mixed reality settings from the [Oculus.Settings.MixedReality] section in Saved/Config/Windows/Engine.ini.       |

## Console commands

|               Command               |                                                                                                                           Description                                                                                                                           |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      mr.AutoOpenCasting [0|1|2]      |                                                                                          Automatically open the casting window: 0=Off; 1=MultiView; 2=DirectComposition                                                                                          |
|     mr.ChromaTorelanceA &lt;float&gt;     |        [Green-screen removal] When CompositionMethod is set to DirectComposition, sets how heavily to weight non-green values in a pixel. For example, if the character image looks too transparent, you may increase this value to make it more opaque.        |
|     mr.ChromaTorelanceB &lt;float&gt;     |                           [Green-screen removal] When CompositionMethod is set to DirectComposition, sets how heavily to weight the green value. If mid-range greens dont appear to be cut out, increasing B or decreasing A may help.                           |
|       mr.ChromaShadows &lt;float&gt;       |                                              [Green-screen removal] When CompositionMethod is set to DirectComposition, the shadow threshold helps mitigate shadow casting issues by eliminating very dark pixels.                                              |
|     mr.ChromaAlphaCutoff &lt;float&gt;     |                               [Green-screen removal] When CompositionMethod is DirectComposition, alpha cutoff is evaluated after chroma-key evaluation and before the bleed test to fully discard pixels with a low alpha value.                               |
|      mr.CastingLantency &lt;float&gt;      |                                                                                                              The casting latency in MultiView mode.                                                                                                              |
|    mr.ProjectToMirrorWindow [0|1]    |                                                                                                         Project the casting output to the MirrorWindow.                                                                                                         |
|    mr.ProjectToMirrorWindow [0|1]    |                Set to 1 to cast to the MirrorWindow. This can simplify window switching, especially on a single-monitor configuration. By default the scene is casted to a standalone window, which offers the most precision in the composition.                |
|    mr.MixedReality_Override [0|1]    |                                                                                                             Use the Mixed Reality console variables.                                                                                                             |
|   mr.MixedReality_ChromaKeyColor_R   |                                                                                                                        Chroma Key Color R                                                                                                                        |
|   mr.MixedReality_ChromaKeyColor_G   |                                                                                                                        Chroma Key Color G                                                                                                                        |
|   mr.MixedReality_ChromaKeyColor_B   |                                                                                                                        Chroma Key Color B                                                                                                                        |
| mr.MixedReality_ChromaKeySimilarity |      When the distance between pixel color and chromaKeyColor is less than chromaKeySimiliarity, the pixel is hidden. Increase this value if the green screen is partially visible, and reduce this value if the person in the scene partially disappears.      |
| mr.MixedReality_ChromaKeySmoothRange |            Defines a small range of color distance between the pixel and the green screen in which the video frame pixel will be rendered as semi-transparent. Increase this value to make the person image more smooth, and decrease it to sharpen.            |
| mr.MixedReality_ChromaKeySpillRange | Defines a small range of color distance between the pixel and the green screen in which the video frame pixel will be desaturated. Increase this value to reduce green edges around the persons image. Decrease it if the person image looks overly desaturated. |
|      mr.CastingLantency &lt;float&gt;      |                                                                                                             The casting latency in Multi-View mode.                                                                                                             |
