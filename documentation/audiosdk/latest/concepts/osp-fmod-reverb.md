---
title: Oculus Spatial Reverb
---



Requires FMOD Studio 1.08 and later.

Place the Oculus Spatial Reverb effect before the Fader on the Master Bus channel. These parameters will affect all sounds in the project using the Oculus Spatializer Plugin.

1. From the main menu, select Window &gt; Mixer. ![](/images/documentationaudiosdklatestconceptsosp-fmod-reverb-0.jpg)


2. In the space before the Fader, right-click (Cmd+click on Mac) and select *Add Effect* &gt; *Plug-in Effects* &gt; *Oculus Spatial Reverb*.


This effect contains parameters that directly control the reverb as well as global settings that are shared across all instances of the spatializer.

## Parameters

![](/images/documentationaudiosdklatestconceptsosp-fmod-reverb-1.png)

|                 Refl. Engine                 | This global setting enables/disables the reflection engine (room model) for all sound sources, including early reflections and late reverberation. For more information, see `Attenuation and Reflections`_ in our Audio SDK Guide.  .. _Attenuation and Reflections: /documentation/audiosdk/latest/concepts/audiosdk-attenuation/ |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                    Reverb                    |                                                                                                                     Enables the shared reverb output from the Oculus Spatial Reverb effect, based on room size.                                                                                                                     |
|                  Bypass All                  |                                                                      This global setting bypasses processing in all instances of the Oculus Spatializer, Oculus Ambisonics, and the Oculus Spatial Reverb effects in the project. May be used for A/B testing.                                                                      |
|                 Global Scale                 |                                                                              Specifies a scaling factor to convert game units to meters. For example, if the game units are described in feet, the Global Scale would be 0.3048. Default value is 1.0.                                                                              |
|         Room Width / Height / Length         |                                                                                                                Global settings that control the dimensions of the room model used for early reflections and reverb.                                                                                                                |
| Refl. Left / Right / Up / Down / Front / Back |                                                                                                         Global settings that control the reflectivity of the walls of the room model used for early reflections and reverb.                                                                                                         |
|                 Range Min/Max                 |                                                                                                                                    Controls the attenuation calculations for the spatial reverb.                                                                                                                                    |
