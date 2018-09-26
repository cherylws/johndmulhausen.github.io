---
title: Overview
---

This guide describes how to install and use the Oculus Native Spatializer plugin in Unity 5.2+ and in end-user applications.

The Oculus Native Spatializer Plugin (ONSP) is an add-on plugin for Unity that allows monophonic sound sources to be spatialized in 3D relative to the user's head location. 

The Native Oculus Spatializer is built on Unity’s [Native Audio Plugin](http://docs.unity3d.com/Manual/AudioMixerNativeAudioPlugin.html), which removes redundant spatialization logic and provides a first-party HRTF. 

Our ability to localize audio sources in three-dimensional space is a fundamental part of how we experience sound. **Spatialization** is the process of modifying sounds to make them localizable, so they seem to originate from distinct locations relative to the listener. It is a key part of creating a sense of presence in virtual reality games and applications.

For a detailed discussion of audio spatialization and virtual reality audio, we recommend reviewing our [Introduction to Virtual Reality Audio](/documentation/audiosdk/latest/concepts/book-audio-intro/) guide before using the Oculus Native Spatializer. If you’re unfamiliar with Unity’s audio handling, be sure to review the [Unity Audio guide](http://docs.unity3d.com/Manual/Audio.html).

## General OSP Limitations

1. CPU usage increases when early reflections are turned on, and increases proportionately as room dimensions become larger.

