---
title: Notes and Best Practices
---
![](/images/documentation-audiosdk-latest-concepts-osp-fmod-notes-0.png)  
Up to 64 sounds running through the bus may be spatialized.

Make sure that your Project Output Format is set to *stereo* in FMOD Studio (*Edit → Preferences → Format → Stereo*).

Note that the room model used to calculate reflections follows the listener's position and rotates with the listener's orientation. Future implementation of early reflections will allow for the listener to freely walk around a static room.

When using early reflections, be sure to set non-cubical room dimensions. A perfectly cubical room may create reinforcing echoes that can cause sounds to be poorly spatialized. The room size should roughly match the size of the room in the game so the audio reinforces the visuals. The shoebox model works best when simulating rooms. For large spaces and outdoor areas, it should be complimented with a separate reverb. 

## Parameters

Sound Properties

Prefer mono sounds and/or set the master track input format to mono (by right-clicking on the metering bars on the left side). ![](/images/documentation-audiosdk-latest-concepts-osp-fmod-notes-1.png)  
Attenuation

Enables the internal distance attenuation model. If attenuation is disabled, you can create a custom attenuation curve using a volume automation on a distance parameter.

Range Max

Maximum range for distance attenuation and reflections. Note that this affects reflection modeling even if Attenuation is disabled.

Range Max

Maximum range for distance attenuation and reflections. Note that this affects reflection modeling even if Attenuation is disabled.

Volumetric Radius

Specifies the radius to be associated with the sound source, if you want the sound to seem to emanate from a volume of space, rather than from a point source.

Sound sources can be given a radius which will make them sound volumetric. This will spread the sound out, so that as the source approaches the listener, and then completely envelops the listener, the sound will be spread out over a volume of space. This is especially useful for larger objects, which will otherwise sound very small when they are close to the listener. For more information, please see the blog articles [https://developer.oculus.com/blog/volumetric-sounds/](/blog/volumetric-sounds/).

Enable Reflections

If set to true, this sound instance will calculate reflections. Reflections take up extra CPU, so disabling can be a good way to reduce the overall audio CPU cost. Reflections will only be applied if the Reflection Engine is enabled on the Oculus Spatial Reverb effect.

For more information, see [Attenuation and Reflections](/documentation/audiosdk/latest/concepts/audiosdk-attenuation/ "Attenuation is key component of game audio, but 3D spatialization with reflections complicates the topic.") in our Audio SDK Guide.

