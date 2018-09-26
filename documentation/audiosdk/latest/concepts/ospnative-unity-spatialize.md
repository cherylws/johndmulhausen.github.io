---
title: Applying Spatialization
---



Attach the helper script ONSPAudioSource.cs, found in Assets/OSPNative/scripts, to an AudioSource. This script accesses the extended parameters required by the Oculus Native Spatializer. Note that all parameters native to an AudioSource are still available, though some values may not be used if spatialization is enabled on the audio source.

In this example, we look at the script attached to the green sphere in our sample RedBallGreenBall:

![](/images/documentationaudiosdklatestconceptsospnative-unity-spatialize-0.jpg)

## OculusSpatializerUserParams Properties

| Spatialization Enabled |                                     If disabled, the attached Audio Source will act as a native audio source without spatialization. This setting is linked to the corresponding parameter in the Audio Source expandable pane (collapsed in the above capture).                                     |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  Reflections Enabled  | Select to enable early reflections for the spatialized audio source. To use early reflections and reverb, you must select this value and add an OculusSpatializerReflection plugin to the channel where you send the AudioSource in the Audio Mixer. See *Audio Mixer Setup* below for more details. |
|          Gain          |                                                                                                          Adds up to 24 dB gain to audio source volume (in db), with 0 equal to unity gain.                                                                                                          |
|   Volumetric Radius   |                                                                  Expands the sound source to encompass a spherical volume up to 1000 meters in radius.For a point source, set the radius to 0 meters. This is the default setting.                                                                  |

## Oculus Attenuation Settings

|    Enabled    | If selected, the audio source will use an internal attenuation falloff curve controlled by the Minimum and Maximum parameters. If deselected, the attenuation falloff will be controlled by the authored Unity Volume curve within the Audio Source Inspector panel.Note: We strongly recommend enabling internal attenuation falloff for a more accurate rendering of spatialization. The internal curves match both the way the direct audio falloff as well as how the early reflections are modeled. For more information, see `Attenuation and Reflections`_ in our Audio SDK Guide.  .. _Attenuation and Reflections: /documentation/audiosdk/latest/concepts/audiosdk-attenuation/ |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Range: Minimum |                                                                                                                                                                                                   Sets the point at which the audio source amplitude starts attenuating, in meters. It also influences the reflection/reverb system, whether or not Oculus attenuation is enabled. Larger values will result in less noticeable attenuation when the listener is near the sound source.                                                                                                                                                                                                   |
| Range: Maximum |                                                                                                                                                                                                           Sets the point at which the audio source amplitude reaches full volume attenuation, in meters. It also influences the reflection/reverb system, whether or not Oculus attenuation is enabled. Larger values allow for loud sounds that can be heard from a distance.                                                                                                                                                                                                           |

## Audio Mixer Setup

Unity 5 includes a flexible mixer architecture for routing audio sources. A mixer allows the audio engineer to add multiple channels, each with their own volume and processing chain, and set an audio source to that channel. For detailed information, see Unity’s [Mixer documentation](http://docs.unity3d.com/Manual/AudioMixer.html). 

## Shared Reflection and Reverb

To allow for the reflection engine to be added within a scene, you must create a mixer channel and add the OculusSpatializerReflection plug-in effect to that channel.

1. Select the *Audio Mixer* tab in your Project View.
2. Select *Add Effect* in the Inspector window.
3. Select *OculusSpatializerReflection*. 
4. Set the *Output* of your attached Audio Source to *Master (SpatializerMixer)*.
5. Set reflection settings to globally affect spatialized voices. 


![](/images/documentationaudiosdklatestconceptsospnative-unity-spatialize-1.jpg)

|          Reflections Engine On          |                                                                          Select to enable the early reflection system. For more information, see `Attenuation and Reflections`_ in our Audio SDK Guide.  .. _Attenuation and Reflections: /documentation/audiosdk/latest/concepts/audiosdk-attenuation/                                                                          |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|            Late Reverberation            |                                                                                                                              Select to enable global reverb, based on room size. Requires reflection engine (Reflections Engine On) to be enabled.                                                                                                                              |
| Room Dimensions: Width / Height / Length |                                                                                                         Sets the dimensions of the room model used to calculate reflections, in meters. The greater the dimensions, the further apart the reflections. Range: 0 - 200 m.                                                                                                         |
|       Wall Reflection Coefficients       |                                                                                   Sets the percentage of sound reflected by each respective wall. At 0, the reflection is fully absorbed. At 1.0, the reflection bounces from the wall without any absorption. Caps at 0.97 to avoid feedback.                                                                                   |
|        Global Scale(1 unit = 1 m)        | The scale of positional values fed into the spatializer must be set to meters. Some applications have different scale values assigned to a unit. For such applications, use this field to adjust the scale for the spatializer. Unity defaults to 1 meter per unit.*Example: for an application with unit set to equal 1 cm, set the Global Scale value to 0.01 (1 cm = 100 m).* |

## RedBallGreenBall Example

![](/images/documentationaudiosdklatestconceptsospnative-unity-spatialize-2.jpg)

To see how this works in RedBallGreenBall, access the Audio Mixer by selecting the **Audio Mixer** tab in your Project View. Then select **Master** under **Groups** as shown below.

![](/images/documentationaudiosdklatestconceptsospnative-unity-spatialize-3.png)

Select the green sphere in your Scene View. Note that the **Output** of the attached Audio Source vocal1 is set to our **Master (SpatializerMixer)**:

![](/images/documentationaudiosdklatestconceptsospnative-unity-spatialize-4.png)

You can now set reflection/reverberation settings to globally affect spatialized voices.
