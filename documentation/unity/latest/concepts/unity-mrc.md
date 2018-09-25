---
title: Unity Mixed Reality Capture
---
This guide describes how to add and configure mixed reality capture support for your Unity application. Mixed reality capture is supported for Rift applications only.

## Introduction

Mixed reality capture places real-world people and objects in VR. It allows live video footage of a Rift user to be composited with the output from a game to create combined video that shows the player in a virtual scene.

![](/images/documentation-unity-latest-concepts-unity-mrc-0.png)  
(Courtesy of Medium and artist Dominic Qwek - <https://www.oculus.com/medium/>)

Live video footage may be captured with a stationary or tracked camera. For more information and complete setup instructions, see the [Mixed Reality Capture Setup Guide](/documentation/pcsdk/latest/concepts/mr-intro/).

Once an application is configured by developers to use mixed reality capture, users can launch applications with the feature enabled and control several relevant settings with external configuration files or command-line parameters. See "Using Mixed Reality Capture" and "External Configuration File" below for more information.

## Preparation

This guide assumes that you have built a functioning Unity VR app. Verify that **Virtual Reality Supported** is selected in **Player Settings** as described in the [Oculus Unity Getting Started Guide](/documentation/unity/latest/concepts/book-unity-gsg/ "This guide describes initial setup, importing the optional Utilities for Unity package, and building Oculus apps using Unity’s first-party support.").

Download and import Oculus Utilities for Unity version 1.18 or later from the [Downloads page](/downloads/). If you have previously imported an earlier version of Utilities for Unity into your project, be sure to remove it from your project before updating by following the steps described in [Importing the Oculus Utilities Package](/documentation/unity/latest/concepts/unity-import/ "Oculus Utilities for Unity is an optional Unity Package that includes scripts, prefabs, and other resources to assist with development.").

You must run the CameraTool prior to launching your mixed reality capture application to configure the external camera and VR Object. See the [Mixed Reality Capture Setup Guide](/documentation/pcsdk/latest/concepts/mr-intro/) for setup information.

Mixed reality capture may be used by any application that includes an instance of OVRManager. Mixed reality capture is disabled by default. To enable it, launch the application using the command line argument -mixedreality, or with external configuration file. For more information, see "Using Mixed Reality" and "External Configuration File" below.

## Compositing the Scene

Mixed reality capture supports three methods for combining application output and tracked video footage: external composition, direct composition, and sandwich composition.

For more polished composition, we recommend using **external composition** mode. In this mode, the application outputs two windows. The MirrorWindow displays the application. The second window displays the foreground content from the video stream on the left against a green background, and displays the background content on the right. The second window is illustrated below:

![](/images/documentation-unity-latest-concepts-unity-mrc-1.png)  
Third-party composition software such as OBS Studio or XSplit is required to clip the green screen and combine the images.

In **direct composition** mode, the application streams camera footage to your scene directly and displays the composited image. Direct composition requires use of a green screen for video capture, and the composited image may exhibit some latency from the video stream. See "Features" below for a discussion of latency correction settings. 

We recommend using direct composition if complicated transparent objects exist between the player and camera.

**Sandwich composition** mode is similar to direct composition mode, but the scene is rendered in three video layers, with the application providing the foreground and background layers, and the camera providing the middle layer. This places greater demands on memory than direct composition (see "Latency Control" below for details), but allows for more powerful latency correction, closer to what can be achieved with third-party composition software. See "Features" below for more information. 

Because they composite the video frame inside of Unity, direct and sandwich composition support more features than external mode, including virtual green screen and dynamic lighting.

Composition Method ComparisonExternal

Direct

Sandwich

Requires video processing software

Yes

No (Casting Only)

No (Casting Only)

Camera Devices

(external software)

USB/ZED camera

USB/ZED camera

Effects/Filters

(external software)

Chroma key

Chroma key

Live preview in game and Editor

No

Yes

Yes

Dynamic Lighting

No/expensive

Yes

Yes

Virtual Green Screen

No

Yes

Yes

Camera Latency Synchronization

Image-Based

Pose-base, Speculator-based

Image-based

Transparency Support

Limited

Yes

Limited

Performance Cost

Low (+ external compositing software cost)

Medium

High

## Using Mixed Reality Capture

Once you’ve built your Unity application with mixed reality capture, launch it with the following parameters to enable the feature:

-mixedreality

Open the mixed reality capture view in the MirrorWindow when app starts.

-directcomposition, -externalcomposition, -sandwichcomposition

When used with -mixedreality, opens the mixed reality view in the specified composition mode.

Most application settings may be controlled with command-line parameters when launching the application. This allows users who have no access to Unity or the project to use and configure mixed reality capture on their systems. 

For convenience, you may wish to create a launch shortcut and append the -mixedreality parameter or other settings. Alternately, you may wish to create a batch file that launches the application with the desired parameters. Or you may provide a configuration file that users can modify. See "External Configuration File" for more information.

If you are running an application in the Editor, check the **Enable Mixed Reality** checkbox while the game is running to switch dynamically to mixed reality capture mode. You may set your application to launch with mixed reality capture enabled in the Editor for debugging purposes only. The setting is automatically disabled when you build your application.

## External Configuration File (mrc.confg)

You may easily override any local Mixed Reality Capture settings by placing a JSON file named **mrc.config** in the application’s data folder. 

To create an mrc.config file, configure your project with the desired settings and launch the application with the -create\_mrc\_config parameter. This will create an mrc.config file in the application’s data folder. You may modify the file as you wish.

Launch Parameter

Description

-create\_mrc\_config

Creates an mrc.config file using the the current MixedRealityCapture settings and places it in the application’s data folder.

-load\_mrc\_config

Launches the application using the MixedRealityCapture settings specified in a mrc.config file in the application’s data folder. These settings will override any local settings.

Most settings in the mrc.config file are the same as the corresponding OVRManager component properties. This table indicates the exceptions:

Setting

Options

compositionMethod

0 = external, 1 = direct, 2 = sandwich

capturingCameraDevice

0 = WebCamera0, 1 = WebCamera1, 2 = ZEDCamera

depthQuality

0 = Low, 1 = Medium, 2 = High

virtualGreenScreenType

0 = Off, 1 = OuterBoundary, 2 = PlayArea

This is a typical mrc.config file for an application set to sandwich composition mode:

{ "enableMixedReality": true, "extraHiddenLayers": { "serializedVersion": "2", "m\_Bits": 0 }, "compositionMethod": 2, "capturingCameraDevice": 2, "flipCameraFrameHorizontally": false, "flipCameraFrameVertically": false, "handPoseStateLatency": 0.0, "sandwichCompositionRenderLatency": 0.1, "sandwichCompositionBufferedFrames": 8, "chromaKeyColor": { "r": 0.0, "g": 1.0, "b": 0.0, "a": 1.0 }, "chromaKeySimilarity": 0.6000000238418579, "chromaKeySmoothRange": 0.029999999329447748, "chromaKeySpillRange": 0.05999999865889549, "useDynamicLighting": false, "depthQuality": 1, "dynamicLightingSmoothFactor": 8.0, "dynamicLightingDepthVariationClampingValue": 0.0010000000474974514, "virtualGreenScreenType": 1, "virtualGreenScreenTopY": 10.0, "virtualGreenScreenBottomY": -10.0, "virtualGreenScreenApplyDepthCulling": false, "virtualGreenScreenDepthTolerance": 0.20000000298023225 }## Features

The following mixed reality properties are available via the OVRManager component. To unhide these settings in the Inspector, select OVRManager and check the **Show Properties** box under Mixed Reality Capture.

Functions and settings for mixed reality capture may be found under OVRManager in our [Unity Scripting Reference](/documentation/unity/latest/concepts/unity-reference-scripting/ "The Unity Scripting Reference contains detailed information about the data structures and files included with the Utilities and Legacy Integration packages.").

![](/images/documentation-unity-latest-concepts-unity-mrc-2.png)  
Note: If they conflict with command-line parameters, these settings will be overridden.Type

Setting

Description

bool

enableMixedReality

Set to true to enable mixed reality capture.

CompositionMethod

compositionMethod

Select External, Direct, or Sandwich.

bool

useHiddenLayerInMixedReality

If true, objects in layers specified by hiddenLayerInMixedReality will be hidden from mixed reality capture.

int

hiddenLayerInMixedReality

Select a layer to hide from mixed reality capture.

LayerMask

extraHiddenLayers

Select any layers which you want to hide from mixed reality capture.

The following features work for direct and sandwich composition.

**Chroma Key**

Chroma key settings allow for fine-tuned control of how the video and application streams are composited. Use these settings to set the reference color of the green screen and control various thresholds at which video pixels are included or excluded from the final frame.

**Dynamic Lighting**

When Dynamic Lighting is enabled, video captured by the physical camera is illuminated in the composted scene by light effects and flashes within the application. For example, a player would briefly be brightly lit during an explosion in the game.

Lighting is applied to video on a flat plane parallel to the camera unless a depth-sensing camera is used (ZED camera), in which case object depth is taken into account.

**Virtual Green Screen**

When enabled, Virtual Green Screen crops video footage that falls outside of the Guardian System Outer Boundary or Play Area configured by the user. The Outer Boundary is the actual perimeter drawn by the user during Touch setup, while the Play Area is a rectangle calculated from the Outer Boundary. Note that the Outer Boundary and Play Area are two-dimensional shapes in the x and z axis. The top and bottom of the y value of the virtual green screen must be specified.

**Latency Control**

When using direct or sandwich composition, there is typically a lag between the camera video and the rendered application. The amount of lag depends on the equipment and configuration of each system, and for best results, must be configured on a case-by-case basis.

In direct composition, users may slow the rendering of tracked controllers relative to the video stream by entering a value for handPoseStateLatency (in milliseconds). The composited scene will then use slightly stale pose data to render controllers in the composited scene.

Sandwich composition supports handPoseStateLatency and two additional values. Use sandwichCompositionRenderLatency to add a specified delay (in milliseconds) to the application-rendered foreground and background content, and sandwichCompositionBufferedFrames to specify the maximum number of frames to store in the buffer for use with this feature. When application FPS is defined, the effective range of sandwichCompositionRenderLatency is clamped to between 0 and sandwichCompositionBufferedFrames / FPS.

The additional GPU memory consumption is approximately sandwichCompositionBufferedFrames * (cameraWidth * cameraHeight) * 9 bytes. Additional CPU memory consumption should be trivial.

The following controls may be configured through OVRManager for preview in the Unity Editor, or configured by launch parameter or external configuration file.

![](/images/documentation-unity-latest-concepts-unity-mrc-3.png)  
TypeSettingDescriptionCameraDevice

capturingCameraDevice

Select the physical camera device used to capture the real world image. 

bool

flipCameraFrameHorizontally

Set to true to flip the camera output horizontally.

bool

flipCameraFrameVertically

Set to true to flip the camera output vertically.

Color

chromaKeyColor

Specify the approximate color of your green screen as compositing reference. The default value is Color.green, which matches a typical general green screen under good lighting conditions.

float

chromaKeySimiliarity

When the distance between pixel color and chromaKeyColor is less than chromaKeySimiliarity, the pixel is hidden. Increase this value if the green screen is partially visible, and reduce this value if the person in the scene partially disappears.

float

chromaKeySmoothRange

Defines a small range of color distance between the pixel and the green screen in which the video frame pixel will be rendered as semi-transparent. Increase this value to make the person image more smooth, and decrease it to sharpen.

float

chromaKeySpillRange

Defines a small range of color distance between the pixel and the green screen in which the video frame pixel will be desaturated. Increase this value to reduce green edges around the person’s image. Decrease it if the person image looks overly desaturated.

bool

useDynamicLighing

Set to true to active Dynamic Lighting. 

DepthQuality

depthQuality

Sets quality level of depth image for dynamic lighting to Low, Medium, or High. Higher values are more smooth and accurate, but more costly for performance. 

float

dynamicLightingSmoothFactor 

Larger values make dynamic lighting effects smoother, but values that are too large make the lighting look flat. 

float

dynamicLightingDepthVariationClampingValue 

Sets the maximum depth variation across edges (smaller values set smoother edges).

VirtualGreen

ScreenType

virtualGreenScreenType 

Options are Off, OuterBoundary, or PlayArea.

floatvirtualGreenScreenTopY 

Sets the top bound of the y-axis of the virtual green screen volume. 

float

virtualGreenScreenBottomY 

Sets the lower bound of the y-axis of the virtual green screen volume. 

bool

virtualGreenScreenApplyDepthCulling 

When using a depth camera such as a ZED camera, set this value to true to use green screen depth culling. 

float

virtualGreenScreenApplyDepthTolerance

The amount to relax depth culling for potential depth measuring errors.

float

handPoseStateLatency 

Adds a delay in seconds (max. 0.5) to the tracked controllers in the composited scene to correct for camera latency. 

The following properties are available in sandwich composition only. Note that all properties in the above table are also available for sandwich composition.

Type

Setting

Description

float

sandwichCompositionRenderLatency 

Adds a delay to the foreground and background image in sandwich composition to accommodate physical camera latency. The maximum duration is a factor of the number of buffered frames allowed by the application, so to correct for high latency, you will need to set a higher value in sandwichCompositionBufferedFrames. 

int

sandwichCompositionBufferedFrames 

Specifies the number of frames buffered in sandwich composition. Higher values consume more memory. 

## Mixed Reality Capture in the Unity Sample Framework

A simple Unity sample with mixed reality capture enabled is included in the Unity Sample Framework in Assets/SampleScenes/MixedRealityCapture/MRCTest. See [Unity Sample Framework](/documentation/unity/latest/concepts/unity-sample-framework/ "The Oculus Unity Sample Framework provides sample scenes and guidelines for common VR-specific features such as hand presence with Oculus Touch, crosshairs, driving, hybrid mono rendering, and video rendering to a 2D textured quad.") for more information.

![](/images/documentation-unity-latest-concepts-unity-mrc-4.png)  
