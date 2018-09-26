---
title: Exploring Oculus Native Spatializer with the Sample Scene
---

To get started, we recommend opening the supplied demonstration scene RedBallGreenBall, which provides a simple introduction to OSNP resources and examples of how what the spatializer sounds like. 

![](/images/documentationaudiosdklatestconceptsospnative-unity-scene-0.jpg)

This simple scene includes a red ball and a green ball, which illustrate different spatializer settings. A looping electronic music track is attached to the red ball, and a short human voice sequence is attached to the green ball. The room model used to calculate reflections and reverb is visualized in the scene around the listener.

Launch the scene in the Unity Game View, navigate with the arrow keys, and control the camera orientation with your mouse to quickly hear the spatialization effects.

To import and open RedBallGreenBall:

1. Create a new Unity project.
2. Import the OculusNativeSpatializer.unitypackage.
3. When the *Importing Package* dialog opens, leave all assets selected and click *Import*.
4. Enable the Spatializer as described in [Download and Setup](/documentation/audiosdk/latest/concepts/ospnative-unity-req-setup/)
5. Open RedBallGreenBall in /Assets/scenes. 


To preview the scene with a Rift:

1. Import and launch RedBallGreenBall as described above.
2. In *Build Settings*, verify that the *PC, Mac and Linux Standalone* option is selected under *Platform*.
3. In *Player Settings*, select *Virtual Reality Supported*. 
4. Preview the scene normally in the Unity Game View. 


To preview the scene in Gear VR (requires gamepad):

1. Be sure you are able to build and run projects on your Samsung phone (Debug Mode enabled, adb installed, etc.). See the [Mobile SDK Getting Started Guide](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/book-intro/) for more information. 
2. Follow the setup steps at the top of this section. 
3. In *Build* Settings 
	1. Select *Android* under *Platform*.
	2. Select *Add Current* to *Scenes in Build*.
	
4. In *Player Settings*, select *Virtual Reality Supported*.
5. Copy your osig to &lt;unity-project&gt;/Assets/Plugins/Android/assets.
6. Build and run your project. 
7. Navigate the scene with a compatible gamepad.

