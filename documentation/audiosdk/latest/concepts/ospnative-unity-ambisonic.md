---
title: Playing Ambisonic Audio in Unity 2017.1 (Beta)
---

The Oculus Spatializer supports playing AmbiX format ambisonic audio in Unity 2017.1. This is a beta feature.

For Unity 2017.1, the Oculus Spatializer supports ambisonic audio, letting you attach 4-channel AmbiX format audio clips to game objects. Rotating either the headset (the AudioListener) or the audio source itself affects the ambisonic orientation.

You can smooth the cross-fading between multiple ambient ambisonic audio sources in your scene by customizing the Volume Rolloff curve for each audio source.

## Adding Ambisonic Audio to a Scene

To add ambisonic audio to a scene in Unity 2017.1 beta:

1. Import the OculusNativeSpatializer Unity package into your project.


2. Select OculusSpatializer for the ambisonic plugin in AudioManager:


	1. Click **Edit &gt; Project Settings &gt; Audio**.
	
	
	2. In the **Inspector** window, locate the **AudioManager** options.
	
	
	3. From **Ambisonic Decoder Plugin**, select **OculusSpatializer**.
	
	Note: If OculusSpatializer is not available as an option, it is likely because Unity is using its built-in OculusSpatializer plugin instead of the newer version you imported into your project. To resolve this issue in Unity 2017.1, save your project and restart Unity.![](/images/documentationaudiosdklatestconceptsospnative-unity-ambisonic-0.png)
	
	
	
3. Add the AmbiX format ambisonic audio file to your project:


	1. Copy the audio file to your Unity assets.
	
	
	2. In the **Project** window, select your audio file asset.
	
	
	3. In the **Inspector** window, select the **Ambisonic** check box and then click **Apply**.
	
	![](/images/documentationaudiosdklatestconceptsospnative-unity-ambisonic-1.png)
	
	
	
4. Create a **GameObject** to attach the sound to.


5. Add the **ONSP Ambisonics Native** script component to your GameObject.


6. Add an **Audio Source** component to your GameObject and configure it for your ambisonic audio file:


	1. In the **AudioClip** field, select your ambisonic audio file.
	
	
	2. In the **Output** field, select **SpatializerMixer &gt; Master**.
	
	![](/images/documentationaudiosdklatestconceptsospnative-unity-ambisonic-2.png)
	
	
	


## ONSP Ambisonics Native Options

| Use Virtual Speakers | Decodes ambisonics as an array of eight point-sourced and spatialized speakers, each located at the vertex of a cube located around the listener.If the check box is not selected, ambisonics are decoded by OculusAmbi, our novel spherical harmonic decoder.OculusAmbi has a flatter frequency response, has less smearing, uses less compute resources, and externalizes audio better than virtual speakers. However, some comb filtering may become audible in broadband content such as wind and rushing water sounds.For broadband content, we recommend using the virtual speaker mode. |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Ambisonic Sample Scene: YellowBall

For a quick demonstration of the Oculus beta support for ambisonic sound sources, open the YellowBall scene included in the OculusSpatializerNative package. Move the left Stick on your controller to move closer to and farther from the audio source. The volume rolls off according to its attenuation curve. Turning your head left and right changes the ambisonic orientation accordingly.

Before you click **Play** in Unity, be sure that:

* In **Edit &gt; Project Settings &gt; Player**, **Virtual Reality Supported** is selected.


* In **Edit &gt; Project Settings &gt; Audio**, **Spatializer Plugin** and **Ambisonic Decoder Plugin** are set to **OculusSpatializer**.

Note: If OculusSpatializer is not available as an option, it is likely because Unity is using its built-in OculusSpatializer plugin instead of the newer version you imported into your project. To resolve this issue in Unity 2017.1, save your project and restart Unity.


![](/images/documentationaudiosdklatestconceptsospnative-unity-ambisonic-3.png)
