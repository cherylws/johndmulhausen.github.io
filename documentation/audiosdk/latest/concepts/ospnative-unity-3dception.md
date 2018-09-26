---
title: Migrating from TBE 3DCeption to Oculus Spatialization
---

This guide describes how to migrate a Unity project from the Two Big Ears 3Dception spatializer to Unity's built-in Oculus Spatializer or the Oculus Native Spatializer Plugin (ONSP) that ships with the Oculus Audio SDK, using the Two Big Ears 3Dception_Example.unity scene found in the latest Non-Commercial 3Dception 1.2.4 package as an example.

## Preparation

Be sure to use the latest supported version of Unity. For up-to-date version recommendations, see the [Compatibility and Requirements](/documentation/unity/latest/concepts/unity-req/) section of our Unity Developer Guide.

Before attempting migration, open the 3DCeption_Example.unity scene in the 3Dception NonComm package and verify that the scene works as expected by running it and moving the player controller around. We recommend using headphones for this step.

## Basic Migration using Unity's Built-In Oculus Spatializer

This section describes how to provide easy, basic spatialization to your Unity project using the basic spatializer included in some Unity versions. For more information, see [First-Party Audio Spatialization (Beta)](/documentation/audiosdk/latest/concepts/ospnative-unity-fp/).

Even if you intend to install the ONSP, we recommend going through this step first.

In the Unity editor, go to **Edit** &gt; **Project Settings** &gt; **Audio** and change **Spatializer Plugin** from 3Dception to OculusSpatializer provided by Unity (no need to install the Oculus integration yet).

There are two Game Objects within the Unity hierarchy with attached audio sources: one is under Robot, and the other is under AudioSource2. For both of these Game Objects:

1. Remove the *TBE\_SourceControl* component.
2. In the AudioSource component, ensure that *Spatialize* is enabled.
3. In the AudioSource component, ensure that *SpatialBlend* is set fully to the right (to the value 1, 3D).


In the AudioSource 3D Sound Settings, ensure that Doppler Level is set to 0. 

Now, run the scene to hear the spatialization take effect. Note the following limitations:

* The spatialization is direct-only, as the default Unity/Oculus spatializer provider does not provide room/reflection properties.
* Attenuation falloff defaults to using authored Unity volume curves. The built-in Oculus spatializer does not expose the ability to use the Oculus attenuation mode


These limitations can be addressed by installing the ONSP (see next step). 

Overall signal gain may be attenuated when using the Oculus spatializer due to differences in spatialization algorithms. Gain can be easily adjusted by running sounds through a native Unity channel. For a quick guide to the native Unity audio mixer, see Unity's [Audio Mixer and Audio Mixer Groups](https://unity3d.com/learn/tutorials/modules/beginner/5-pre-order-beta/audiomixer-and-audiomixer-groups?playlist=17096) tutorial.

If you are satisfied with the spatialization provided by the built-in Oculus spatializer, proceed to the **Final Clean-Up** section at the bottom of this guide. Otherwise, continue to the next section.

## Advanced Migration using the Oculus Native Spatializer Plugin (ONSP)

This section describes how to add additional features and control by importing the Oculus Native Spatialization Plugin to your project. The ONSP is available for download from our [Downloads page](/downloads/).

Begin by reviewing the rest of our [Oculus Native Spatializer for Unity](/documentation/audiosdk/latest/concepts/book-ospnative-unity/) Developer Guide and following the included installation instructions. Once installed, Unity will use the latest spatializer plugin found in Assets/Plugins, overriding the built-in Oculus spatializer described above.

We recommend trying the example scene RedBallGreenBall to become familiar with the plugin features.

Add the ONSPAudioSource component found in OSPNative/scripts/ to the Robot and AudioSource2 Game Objects. This will add additional parameters on the AudioSource, including:

* Overall gain control
* Oculus attenuation (instead of native Unity curves)
* Min / max falloff range setting
* The ability to enable/disable reflections.


You may now switch between 3Dception provider and OculusSpatializer and adjust the values within the ONSPAudioSource component until they reasonably match 3Dception.

Another plugin will be exposed which can be added to a native Unity mixer channel. This plugin exposes the reflection engine, which will allow sounds to be treated with early reflections and reverberation.

If you are satisfied with the spatialization provided by the ONSP and do not need additional control, proceed to the **Final Clean-Up** section at the bottom of this guide. Otherwise, continue to the next section.

## Reflection Zones and Scene Morphing

This section describes the following optional steps for advanced users who have installed the ONSP: 

* How to add the OculusSpatializerReflection plugin to an audio mixer channel,
* How to route sounds to that channel, and
* How to set up snapshots which can be triggered by room volumes with the same settings as the 3Dception demo.


To begin, be sure to review the Audio Mixer Setup section in the [Applying Spatialization](/documentation/audiosdk/latest/concepts/ospnative-unity-spatialize/) page of our ONSP guide.

Unity's native audio mixer includes a **snapshot** feature which may be used to change mixer plugin parameters. For more information on how snapshots work, see Unity's [Audio Mixer Snapshots](https://unity3d.com/learn/tutorials/topics/audio/audio-mixer-snapshots) tutorial.

The Oculus Spatializer integration includes the ONSPReflectionZone.cs helper script. You may add it to a Game Object with a Box Collider, which manages calling any snapshots set up within the audio mixer. See the ONSP sample scene RedBallGreenBall for an example application.

To replace 3Dception reverb zones, first ensure that a Box Collider is on the Game Objects and verify that it is set to **Is Trigger**. Add ONSPReflectionZone.cs to the Game Object. Then open the audio mixer and create snapshots that describe the zone's reflection/reverb characteristics. Note that you can add transition times when triggering snapshots, which will help smooth the transitions from one zone to the next.

Finally, assign the snapshot to the ONSPReflectionZone component. When the AudioListener enters that new zone, the snapshot will set the new Reflection/Reverb parameters.

Experimentation is key when setting up zones with different snapshots. However, transitioning from TBE reverb zones to this new system should not be difficult, and it provides an effective way to model your reflection/reverb space.

## Final Clean-UP

Remove all Game Object and Components (scripts) left over from the 3DCeption integration:

1. Delete **3Dception Global** Game Object in the main Hierarchy.
2. Delete the **TBE\_Room\_Properties** component on the **TBE\_Room\_1/2** Game Objects.
3. Delete TBE\_3DCeption folder in the /Assets folder.


## Contact

If you have any questions about this procedure, please visit our [Audio Developer Forum](https://forums.oculus.com/community/categories/audio-development).
