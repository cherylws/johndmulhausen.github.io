---
title: Exploring Oculus Lipsync with the Sample Scene
---

To get started, we recommend opening the supplied demonstration scene LipSync_Demo, located under Assets/Oculus/LipSync/Scenes. This scene provides an introduction to Oculus Lipsync resources and examples of how the library works.

## Using the LipSync_Demo scene

![](/images/documentationaudiosdklatestconceptsaudio-ovrlipsync-sample-0.png "Lipsync demo scene")

 You can switch models between a geometry morph target and a texture flip target, and also switch between microphone and our provided sample audio clip using the following controls: 

|                     Key                     |                                                      Control                                                      |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
|                      1                      |                                     Select Morph target, Mic input (default).                                     |
|                      2                      |                                      Select Texture Flip target, Mic input.                                      |
|                      3                      |                                         Select Morph target, Audio Clip.                                         |
|                      4                      |                                      Select Texture Flip target, Audio Clip.                                      |
|                      5                      |                                     Select Morph target, Precomputed Visemes.                                     |
|                      6                      |                                 Select Texture Flip target, Precomputed Visemes.                                 |
|                      L                      | Toggle loopback on/off to hear your voice with the mic input. Use headphones to avoid feedback. (default is off). |
|                      D                      |                                  Toggle debug display to show predicted visemes                                  |
|                &lt;left arrow&gt;                |                                             Rotate scene object left                                             |
|                ` (backtick)                |                           Add 100% activation to "sil" viseme on geometry morph target                           |
| Tab through \ (QWERTY row of a US keyboard) |                     Add 100% activation to "PP" through "ou" visemes on geometry morph target                     |
|                &lt;right arrow&gt;                |                                             Rotate scene object right                                             |

|             Action             |                                                                                                                                              Control                                                                                                                                              |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|           Swipe Down           |                                                                                                                                 Decrease microphone gain (1-15).                                                                                                                                 |
|            Swipe Up            |                                                                                                                                 Increase microphone gain (1-15).                                                                                                                                 |
| Swipe Forward / Swipe Backward | Cycle forward/backward through targets:1. Morph target - mic input 2. Flipbook target - mic input 3. Morph target - audio clip input 4. Flipbook target - audio clip input 5. Morph target - pregenerated visemes 6. Flipbook target - pregenerated visemes Audio clip input plays automatically. |
|           Single Tap           |                                                                                                                 Toggle mic loopback on/off to hear your voice with the mic input.                                                                                                                 |

## To preview the scene in the Unity Editor Game View:

1. Import and launch LipSync\_Demo as described above.
2. Play the LipSync\_Demo scene in the Unity Editor Game View.


![](/images/documentationaudiosdklatestconceptsaudio-ovrlipsync-sample-1.png "Lip sync demo scene in Game view")

## To preview the scene with a Rift:

1. Import and launch LipSync\_Demo as described above.
2. In *Build Settings*, verify that the *PC, Mac &amp; Linux Standalone* option is selected under *Platform*.
3. In *Player Settings*, select *Virtual Reality Supported*.
4. Preview the scene normally in the Unity Game View.


## To preview the scene in Gear VR:

1. Be sure you are able to build and run projects on your Samsung phone (Debug Mode enabled, adb installed, etc.) See the Mobile SDK Setup Guide for more information.
2. Import and launch LipSync\_Demo as described above.
3. In *Build Settings*:
	1. Select *Android* under *Platform*.
	2. Select *Add Current*s*Scenes in Build*.
	3. Set *Texture Compression* to *ASTC* (recommended).
	
4. In *Player Settings*:
	1. Select *Virtual Reality Supported*.
	2. Specify the *Bundle Identifier*.
	
5. Copy your osig to &lt;unity-project&gt;/Assets/Plugins/Android/assets.
6. Build and run your project.

