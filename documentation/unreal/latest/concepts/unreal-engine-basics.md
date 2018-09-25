---
title: Unreal Engine Basics
---
This guide reviews the basics for developing Oculus applications in Unreal.

## Overview

The easiest way to get started with Oculus development in Unreal is to experiment with the HMD support provided by default as a Player Start. If Unreal detects an Oculus Rift runtime **(e.g., the Oculus application is installed)**, it will automatically provide orientation and positional tracking and stereoscopic rendering for any game. Standalone PC executables will automatically display in Oculus Rift when run in full-screen mode, if a Rift is detected on your system. **If Unreal detects an Oculus Go or Gear VR runtime, it will automatically provide orientation and stereoscopic rendering for any game**.

You may build a project normally and preview it in the Engine by selecting the VR Preview mode in the Play button pulldown options.

To preview a level in the Rift while editing with the engine, select the dropdown arrow near the Play button and select VR Preview.

![](/images/documentation-unreal-latest-concepts-unreal-engine-basics-0.png)  
To play a scene in the Rift with a standalone PC game, simply maximize the game window and it will be mirrored to the Rift display.

Note: While Unreal is running, you will not be able to access Oculus Home by putting on the headset.## Adding a VR Camera

Using the default camera set to VR Preview is a good way to get a quick sense of VR development with minimal overhead, but for actual development, we recommend adding a camera to a Pawn. By default, the camera is locked to the HMD. You can verify this by selecting the camera in Viewport and looking at the **Lock to Hmd** checkbox in the **Details** tab.

![](/images/documentation-unreal-latest-concepts-unreal-engine-basics-1.png)  
Placing a camera in the scene allows you to control the orientation of the camera view when the game loads, so that you can control the exact perspective that will be visible to the user. This is not possible with the Play Start described above.

Note: Game-related actions should be performed on the Pawn to which the camera was added, not directly on the camera itself.An additional benefit to using a Camera attached to a Pawn is that you can attach meshes and they will update their position following the HMD view with very little latency. This is generally the best way to add head-locked elements such as cockpit details. Note that we generally discourage head-locked UI elements, but it can be an attractive feature when used carefully. 

## HMD Pose Tracking Origin

The HMD pose is reported relative to a tracking origin, which may be set to two values in your HeadMountedDisplay settings:

Eye Level

The initial pose of the HMD when the camera activates.

Floor Level

The origin set by the user during Rift calibration, typically near the center of their playable area. Unlike eye-level, the floor-level origin's position is on the floor, at Y = 0.

When you recenter the tracking origin, the behavior is different for eye and floor level.

Eye level moves the origin's position (X, Y, and Z) and the yaw (Y rotation) to match the current head pose. Pitch and roll (X and Z rotation) are not modified because that would make the application's virtual horizon mismatch the real-world horizon, disorienting the user.

Floor level moves the origin's X and Z position, but leaves the Y position alone to keep it consistent with the real-world floor. Rotation is handled the same way as eye level.

For more information, see:

* [Tracking](/design/latest/concepts/bp-orientation-tracking/) in our Intro to VR
* [IHeadMountedDisplay](https://docs.unrealengine.com/latest/INT/API/Runtime/HeadMountedDisplay/IHeadMountedDisplay/index.html) in the Unreal API Guide
## VR Template

Unreal Engine v4.13 and later include a Virtual Reality Blueprint project template which may be selected when creating a New Project.

![](/images/documentation-unreal-latest-concepts-unreal-engine-basics-2.png)  
VR Template contains two maps, accessible through the Content Browser in **Content** > **VirtualRealityBP** > **Maps**.

The HMD Locomotion Map is a simple level that demonstrates teleportation. Set your travel destination with the blue gaze-controlled circle. Once the teleport target is set, press the spacebar or gamepad button to teleport. You may optionally control the orientation you will be facing on arrival with the gamepad primary joystick.

![](/images/documentation-unreal-latest-concepts-unreal-engine-basics-3.png)  
The Motion Controller Map also demonstrates teleportation control, in this case using tracked Touch controllers. Point in the direction youâ€™d like to travel with the Touch controller and control the destination orientation with your gaze. Then press the A-button to teleport.

![](/images/documentation-unreal-latest-concepts-unreal-engine-basics-4.png)  
Use the trigger buttons to pick up and manipulate the small blue blocks in the level.

![](/images/documentation-unreal-latest-concepts-unreal-engine-basics-5.png)  
