---
title: How to Use the Oculus Spatializer in Wwise
---



1. Launch Wwise.
2. To add OSP to a bus, create a new audio bus and place it under one of the master buses. ![](/images/documentationaudiosdklatestconceptsosp-wwise-usage-0.png)

Note: Mixer bus plugins may not be added to master buses.
3. Click on the newly-created bus and then click on the *Mixer Plug-in* tab in the *Audio Bus Property Editor*. Select the *&gt;&gt;*, find the *Oculus Spatializer* selection, and add a *Default (Custom)* preset: ![](/images/documentationaudiosdklatestconceptsosp-wwise-usage-1.png)

Note: If the *Mixer Plug-in* tab is not visible, click the "+" tab and verify that mixer plugins are enabled (check box is selected) for buses. ![](/images/documentationaudiosdklatestconceptsosp-wwise-usage-2.png)


4. Under the *Mixer Plug-in* tab, click on the "â€¦" button at the right-hand side of the property window. This will open up the *Effect Editor* (global properties) for OSP: ![](/images/documentationaudiosdklatestconceptsosp-wwise-usage-3.jpg)




## Global Properties

The following properties are found within the OSP effect editor:

|        Bypass  Use native panning        |                                                                                                                                           Disables spatialization. All sounds routed through this bus receive Wwise native 2D panning.                                                                                                                                           |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|              Gain (+/-24db)              |                                                                   Sets a global gain to all spatialized sounds. Because the spatializer attenuates the overall volume, it is important to adjust this value so spatialized sounds play at the same volume level as non-spatialized (or native panning) sounds.                                                                   |
|        Global Scale(1 unit = 1 m)        | The scale of positional values fed into the spatializer must be set to meters. Some applications have different scale values assigned to a unit. For such applications, use this field to adjust the scale for the spatializer. Unity defaults to 1 meter per unit.*Example: for an application with unit set to equal 1 cm, set the Global Scale value to 0.01 (1 cm = 100 m).* |
|           Reflections Engine On           |                                                                                                                                        Enables early reflections. This greatly enhances the spatialization effect, but incurs a CPU hit.                                                                                                                                        |
|            Late Reverberation            |                           If this field is set, a fixed reverberation calculated from the early reflection room size and reflection values will be mixed into the output (see below). This can help diffuse the output and give a more natural sounding spatialization effect. Reflections Engine On must be enabled for reverberations to be applied.                           |
| Shared Reverb Attenuation Range Min / Max |                                                                             Controls the attenuation calculations for the spatial reverb. For more information, see `Attenuation and Reflections`_.  .. _Attenuation and Reflections: /documentation/audiosdk/latest/concepts/audiosdk-attenuation/                                                                             |
|           Reflections Range Max           |                                                                            Range of the attenuation curve for reflections. This is the distance at which the reflections go silent, so it should roughly match the attenuation curve in Wwise. For more information, see Attenuation and Reflections.                                                                            |
|  Room Dimensions Width / Height / Length  |                                                                                                  Sets the dimensions of the room model used to calculate reflections. The greater the dimensions, the further apart the reflections. Value range is 1-200 meters for each axis.                                                                                                  |
|       Wall Reflection Coefficients       |                                                    Sets the percentage of sound reflected by walls for each wall specified for a room (Left/Right,Forward/Backward, Up/Down). At 0, the reflection is fully absorbed. At 1.0, the reflection bounces from the wall without any absorption. Capped at 0.97 to avoid feedback.                                                    |

### Notes and Best Practices

Up to 64 sounds running through the bus are spatialized. Subsequent sounds use Wwise native 2D panning until the spatialized sound slots are free to be reused.

All global properties may be set to an RTPC, for real-time control within the user application.

In the main menu, set your audio output configuration to a 2.1 or 2 Stereo Channel Configuration (Speakers or Headphones). The spatializer will not work on higher channel configurations.

Note that the room model used to calculate reflections follows the listener's position and rotates with the listener's orientation. Future implementation of early reflections will allow for the listener to freely walk around a static room.

When using early reflections, be sure to set non-cubical room dimensions. A perfectly cubical room may create reinforcing echoes that can cause sounds to be poorly spatialized. The room size should roughly match the size of the room in the game so the audio reinforces the visuals. The shoebox model works best when simulating rooms. For large spaces and outdoor areas, it should be complemented with a separate reverb. 

**IMPORTANT**: When early reflections are enabled, you must ensure that the room size is set to be large enough to contain the sound. If a sound goes outside the room size (relative to the listener's position), early reflections will not be heard.

## Sound Properties



For a sound to be spatialized, you must ensure that sounds are set to use the bus to which you added OSP:

![](/images/documentationaudiosdklatestconceptsosp-wwise-usage-4.png)

Ensure that your sound positioning is set to 3D:

![](/images/documentationaudiosdklatestconceptsosp-wwise-usage-5.png)

Upon setting the sound to the OSP bus, a **Mixer plug-in** tab will show up on the sounds Sound Property Editor:

### Parameters

![](/images/documentationaudiosdklatestconceptsosp-wwise-usage-6.jpg)

The following properties are applied per sound source. 

|       Bypass Spatializer       |                                                                                                                                                                                                                          Disables spatialization. Individual voices / actor-mixer channels may skip spatialization processing and go directly to native Wwise panning.                                                                                                                                                                                                                          |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      Reflections Enabled      |                                                                                                                                                                                                                                                Enables early reflections. This greatly enhances the spatialization effect, but incurs a CPU hit.                                                                                                                                                                                                                                                |
|   Oculus Attenuation Enabled   |                                                                                                                                                                                                                               If selected, the audio source will use an internal amplitude attenuation falloff curve controlled by the Range Min/Max parameters.                                                                                                                                                                                                                               |
|     Attenuation Range Min     |                                                                                                                                                                                                          Sets the distance at which the audio source amplitude starts attenuating, in meters. It also influences the reflection/reverb system, even if Oculus attenuation is disabled.                                                                                                                                                                                                          |
|     Attenuation Range Max     |                                                                                                                                                                                                   Sets the distance at which the audio source amplitude reaches full volume attenuation, in meters. It also influences the reflection/reverb system, even if Oculus attenuation is disabled.                                                                                                                                                                                                   |
|       Volumetric Radius       |                                                                                                                                                                                                                    Expands the sound source from a point source to a spherical volume. The radius of the sphere is defined in meters. For a point source, use a value of 0.                                                                                                                                                                                                                    |
|    Treat Sound As Ambisonic    |                                                                                      Treats sound as ambisonic instead of applying spatialization. Recommended for ambient or environmental sounds, that is, any sound not produced by a visible actor in the scene. Note: Attached sound must be in AmbiX format. Please see *Ambisonics* in `Supported Features`_ for more information.  .. _Supported Features: /documentation/audiosdk/latest/concepts/audiosdk-features/#audiosdk-features-supported                                                                                      |
| Ambisonic Virtual Speaker Mode | Decodes ambisonics as an array of eight point-sourced and spatialized speakers, each located at the vertex of a cube located around the listener.If the check box is not selected, ambisonics are decoded by OculusAmbi, our novel spherical harmonic decoder.OculusAmbi has a flatter frequency response, has less smearing, uses less compute resources, and externalizes audio better than virtual speakers. However, some comb filtering may become audible in broadband content such as wind and rushing water sounds. For broadband content, we recommend using the virtual speaker mode. |

### Notes and Best Practices

Currently, only mono (1-channel) and stereo (2-channel) sounds are spatialized. Any sounds with a higher channel count will not be spatialized.

A stereo sound will be collapsed down to a monophonic sound by having both channels mixed into a single channel and attenuated. Keep in mind that by collapsing the stereo sound to a mono sound, phasing anomalies with the audio spectrum may occur. It is highly recommended that the input sound is authored as a mono sound.

Spatialized sounds will not be able to use stereo spread to make a sound encompass the listener as it gets closer (this a common practice for current spatialization techniques).
