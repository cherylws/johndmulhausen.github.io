---
title: Application Lifecycle Handling
---
This guide describes the process to handle the lifecycle for applications built in Unity.

## Input Focus

With Dash we introduced the concept of input focus, or whether the user is focused on your app, or elsewhere. Adding Dash support to your app means correctly handling the times when your app is running, but the user's focus is elsewhere. 

To check if your app has focus input, query OVRManager.hasInputFocus every frame. If your app has focus hasInputFocus will return true. If the user's focus is elsewhere, like when the user opens the Dash menu or removes their HMD, hasInputFocus will return false.

In single-player apps or experiences, you can pause the app, mute audio playback, and stop rendering any tracked controllers/hands present in the scene (Dash will use a separate set of hands).

Multiplayer experiences may wish to handle the loss of input focus differently. You're required to hide the hands and ignore any input while the app does not have focus input, but you may wish to continue audio playback and the match in the background. 

For more information, see HasInputFocus under OVRManager in our [Unity Scripting Reference](/documentation/unity/latest/concepts/unity-reference-scripting/ "The Unity Scripting Reference contains detailed information about the data structures and files included with the Utilities and Legacy Integration packages.").

See the Input Focus sample in the [Unity Sample Framework](/documentation/unity/latest/concepts/unity-sample-framework/ "The Oculus Unity Sample Framework provides sample scenes and guidelines for common VR-specific features such as hand presence with Oculus Touch, crosshairs, driving, hybrid mono rendering, and video rendering to a 2D textured quad.") for an example of a typical implementation and the [Oculus Dash in Unity](/documentation/unity/latest/concepts/unity-dash/ "This guide describes how to add Oculus Dash support to Unity applications.") guide for other information you should know about being focus aware. 

## VR Focus

Similar to Input Focus, the runtime will also tell you if your app has VR Focus, or if any part of your app is visible to the user.

Your app could lose VR focus for a number of reasons, the most common is if the user exits to Home or switches to another app. To check if your app has VR input, query OVRManager.hasVRFocus every frame. OVRManager.hasVrFocus() will return false when you app is no longer visible.

When you lose VR focus the user can no longer see your app. You should stop submitting frames, drop audio, and stop tracking input. You may also wish to save the game state so you can return the user to where they left off in your app.

For more information, see HasVRFocus under OVRManager in our [Unity Scripting Reference](/documentation/unity/latest/concepts/unity-reference-scripting/ "The Unity Scripting Reference contains detailed information about the data structures and files included with the Utilities and Legacy Integration packages.").

