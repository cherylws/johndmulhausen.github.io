---
title: Unity Social Starter Example
---

The Social Starter example scene demonstrates using Oculus Avatars together with other Oculus Platform features such as invites, peer-to-peer networking, and VoIP.

This scene depicts a virtual room into which you can invite your friends who are also running the scene. As your friends join your room, the scene sets up a VoIP connection to transmit voice packets and a peer-to-peer connection to transmit avatar packets.

## Requirements

This scene requires the following Unity packages:

* Oculus Unity Utilities
* Oculus Avatar SDK
* Oculus Platform SDK


Because this scene uses Oculus Platform features, you must paste an Oculus App ID in both the Oculus Platform and the Oculus Avatars settings. For more information, see [Using Unity Features](/documentation/avatarsdk/latest/concepts/legacy-avatars-sdk-unity/#avatars-sdk-unity).

## Demonstrating the Social Features

In the middle of the room is a sphere. The sphere is white if you are in an online room or black if the room creation fails for any reason. The floor is blue if you are the owner of the room, green if you have joined someone else's room.

Things you can do:

* To send an invitation, press **X** on your Touch controller or **Back** on your Gear VR controller.
* To view the scene from a different camera, press **Y** on your Touch or click the trackpad on your Gear VR controller.
* To move and turn your avatar around the room, use the thumbsticks on your Touch or the trackpad on your Gear VR controller.
* To turn off the help text, click the thumbstick on your left Touch or pull the trigger on your Gear VR controller.

