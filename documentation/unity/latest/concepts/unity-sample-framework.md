---
title: Unity Sample Framework
---
The Oculus Unity Sample Framework provides sample scenes and guidelines for common VR-specific features such as hand presence with Oculus Touch, crosshairs, driving, hybrid mono rendering, and video rendering to a 2D textured quad.

The Unity Sample Framework can guide developers in producing reliable, comfortable applications and avoiding common mistakes. The assets and scripts included with the Sample Framework may be reused in your applications per the terms of our [SDK 3.4.1 license](/licenses/sdk-3.4.1/). Note that some folders of the Sample Framework include a more permissive BSD license - this license supersedes the SDK 3.4.1 license in folders in which it occurs. See LICENSE.txt in the relevant folders for additional details.

The Unity Sample Framework is available as a Unity Package for developers who wish to examine how the sample scenes were implemented, and as binaries for Rift, Oculus Go, and Gear VR for developers to explore the sample scenes entirely in VR.

The Sample Framework Unity Package is available from our Downloads Center and from the Unity Asset Store [here](https://www.assetstore.unity3d.com/en/#!/content/82503). The Rift executable and mobile application are available from the Oculus Store in the Gallery section.

![](/images/documentation-unity-latest-concepts-unity-sample-framework-0.png)  
Sample Framework UI SceneThe Unity Sample Framework works on all currently-supported versions of Unity. Please check [Compatibility and Requirements](/documentation/unity/latest/concepts/unity-req/ "This guide describes Unity Editor version recommendations and system requirements.") for supported versions.

## Sample Scenes

In the Unity project, the following scenes are found in /Assets/SampleScenes:

Scene

Directory

Concept Illustrated

Multiple Cameras

Cameras/

Switching between cameras in a scene. 

Crosshairs

First Person/

Using crosshairs to aim a weapon in VR and different configuration options. 

Mirror

First Person/

A simple mirror effect.

Outdoor Motion

First Person/

Basic forms of movement, and the effects a variety of design choices may have on comfort. 

Scale

First Person/

How various scale factors interact. 

Stairs

First Person/

Factors affecting comfort in first-person stairs movement. 

Teleport

First Person/Locomotion/

A teleportation locomotion scene that reduces the risk of discomfort.

TeleportAvatar

First Person/Locomotion2/

A teleportation scene that supports switching between any combination of teleports and linear motion at run time.

Guardian Boundary System

Guardian Boundary System/

Illustrates use of OVRBoundary API to interact with Guardian System Outer Boundary and Play Area.

AvatarWithGrab

Hands/

Uses the Unity Avatar SDK and the scripts OVRGrabber and OVRGrabbable to illustrate hands presence with Touch. Pick up and throw blocks from a table using the Touch grip buttons. This sample requires importing the Oculus Avatar SDK. 

CustomControllers

Hands/

A simple sample displaying tracked Touch models in a scene.

CustomHands

Hands/

Uses low-resolution custom hand models and the scripts OVRGrabber and OVRGrabbable to illustrate hands presence with Touch. Pick up and throw blocks from a table using the Touch grip buttons. May be used as a reference for implementing your own hand models.

Distance Grab

Hands/

Illustrates selecting and grabbing distant objects with hand models using Touch. For more information, see Distance Grab Sample on our Developer Blog. 

Input Tester

Input/

This scene assists with testing input devices, displaying axis values in real time. 

Keyboard

Input/

A virtual keyboard.

Input Focus

Input Focus/

Illustrates typical handling for loss of Input Focus, such as when a Dash overlay is present. The application is paused, muted, and tracked controllers are hidden.

MRCTest

MixedRealityCapture/

A simple scene with mixed reality capture enabled.

Splash Screen

OVRHarness/Scenes/Loading.unity*

Splash screen modal that supports custom images and content. 

Movie Player

Rendering/

Video rendering to a 2D textured quad using the Android Media Surface Plugin. Source for the plugin ships with the Mobile SDK in \VrAppSupport\MediaSurfacePlugin.

Surface Detail

Rendering/

Different ways to create surface detail with normal, specular, parallax, and displacement mapping. 

OverlayUIDemo

UI/

Demonstrates creating a UI with a VR Compositor Layer to improve image quality and anti-aliasing. Includes a quad overlay for , and a quad and a cylinder overlay for mobile. 

Pointers

UI/

How UI elements can be embedded in a scene and interact with different gaze controllers. 

Pointers - Gaze Click

UI/

An extension of the Pointers scene, with gaze selection. 

Tracking Volume

UI/

Different ways to indicate the user is about to leave the position tracking volume. 

Note: * The Splash Screen sample is found in a different location from the other samples listed in this table.## A Note on Comfort

These samples are intended to be tools for exploring design ideas in VR, and should not necessarily be construed as design recommendations. The Sample Framework allows you to set some parameters to values that will reliably cause discomfort in most users - they are available precisely to give developers an opportunity to find out how much is too much.

It is as important to play test your game on a range of players throughout development to ensure your game is a comfortable experience. We have provided in-game warnings to alert you to potentially uncomfortable scenes.

## Downloading and Installation

To download the Oculus Sample Framework Unity Project, visit our [Downloads Center](/downloads/unity/). The Sample Framework application may be downloaded for free from the Gallery Apps section of the Oculus Store. 

To run the PC Binary

Note: You will need to enable running applications from unknown sources in the Oculus app settings. Launch the Oculus app, and in the “gear” pull-down menu in the upper right, select **Settings** > **General** and toggle **Unknown Sources** on to allow. You may wish to disable this setting after use for security reasons.1. Download the Unity Sample Framework PC Binary.
2. Unzip the contents.
3. Run the OculusSampleFramework.exe. Note that it must be run from a directory location that also includes the OculusSampleFramework\_Data folder.
To open the project in Unity Editor:

1. Verify that you have installed the latest-recommended version of Unity 5 or later (see [Compatibility and Requirements](/documentation/unity/latest/concepts/unity-req/ "This guide describes Unity Editor version recommendations and system requirements.") for up-to-date information).
2. Download the Unity Sample Framework Project from our [Downloads Center](/downloads/unity/).
3. Launch the Unity Editor and create a new project.
4. Import the Unity Sample Framework Unity Package by selecting **Assets > Import Package > Custom Package…** and selecting the Unity Sample Framework.
## Building the Unity Project

This is only necessary if you want to experiment with the project, as application binaries are provided by Oculus for free download.

To build the Unity Project for Rift:

Note: You will need to enable running applications from unknown sources in the Oculus app settings. Launch the Oculus app, select **Settings** > **General**, and toggle **Unknown Sources** on to allow. You may wish to disable this setting after use for security reasons.1. Open the Sample Framework project as described above.
2. From the Editor menu bar, select **OVR** > **Samples Build Config** > **Configure Build**.
3. Build and run the project normally.
To build the Unity Project for Mobile:

1. Open the Sample Framework project as described above.
2. From Editor menu bar, select **OVR** > **Samples Build Config** > **Configure Gear VR Build**.
3. Ensure the project contains an Oculus signature file and that you have an Android keystore configured. See [Application Signing](/documentation/mobilesdk/latest/concepts/mobile-submission-sig-file/) in our Mobile SDK documentation for more details.
4. Sample Framework Android builds use a custom manifest and are not visible from Applications, and cannot be launched from Oculus Home or the Android Application Launcher. To launch: 
	1. Install the APK to your phone.
	2. Open **Settings** > **Applications** > **Application Manager** > **Gear VR Service**.
	3. Select **Storage**.
	4. Select **Manage Storage**.
	5. Toggle **Add icon to app list to On**.
	6. Close **Settings**.
	7. Open **Apps**.
	8. Select **Gear VR Service**.
	9. Select **Oculus Sample Framework** to launch.
	
## Exploring the Sample Framework in VR

Sample scenes are browsed and controlled with a simple UI which provides in-app explanatory notes. Parameter controls allow users to adjust settings, providing an immediate, direct experience of the impact of different design decisions. The Sample Framework control panel itself is an example of in-VR control and navigation, and may be used as a model for your own applications.

We have provided a Windows executable for use with the Oculus or DK2. A mobile app may be downloaded for free from the Gallery Apps section of the Oculus Store. These applications are simply builds of the Unity project.

**Navigation**

Launch the Sample Framework on Rift, Oculus Go, or Gear VR to load the startup scene. You will see the **Inspector**, a three-pane interface providing controls for scene settings, documentation, and navigation controls for browsing to other scenes. Making selections on the top-level menu on the left panel changes the content of the other two panels. The center panel is a contextual menu, and the right panel displays notes and instructions for the current scene.

![](/images/documentation-unity-latest-concepts-unity-sample-framework-1.png)  
Sample Framework Controls in VRInspector navigation is primarily gaze-controlled, supplemented by a mouse and keyboard, a gamepad (PC or Gear VR), or the Gear VR touchpad.

To launch a scene from the center panel, you may select and click the scene with a mouse, gaze at the scene name and press the A button on a gamepad, or tap the Gear VR touchpad.

Some scenes are grouped into folders (displayed as buttons). When browsing from a folder, select the “..” button to navigate one level up in the scene hierarchy.

**Scrolling**

Some panels support vertical scrolling. Several methods of scrolling are supported in order to illustrate some of the available options for implementing this feature. The following methods are supported:

1. Gaze at the bottom or top of the panel.
2. Gaze over the panel and swipe up or down on the Gear VR touch pad.
3. Position the mouse pointer over the panel and use the mouse scroll wheel.
4. Click and drag the panel using the mouse pointer. 
5. Click and drag by using the gaze pointer and “clicking” with the Gear VR touch pad, the gamepad A button, or your space bar.
6. Gaze over the panel and scroll with the right thumbstick.
