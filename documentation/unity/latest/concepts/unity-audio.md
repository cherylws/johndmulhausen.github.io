---
title: Unity Audio
---

This guide describes guidelines and resources for creating a compelling VR audio experience in Unity.

If you’re unfamiliar with Unity’s audio handling, we recommend starting with the [Unity Audio guide](http://docs.unity3d.com/Manual/Audio.html).

## General Best Practices

* Do not use more than 16 audio sources. 
* Avoid using Decompress on Load for audio clips.
* Do not use ONSP reflections for mobile applications. 
* Disable Preload Audio Data for all individual audio clips.


## Unity Audio and Rift

Audio input and output automatically use the Rift microphone and headphones unless configured to use the Windows default audio device by the user in the Oculus app. Events OVRManager.AudioOutChanged and AudioInChanged occur when audio devices change, making audio playback impossible without a restart.

For instructions on using Unity and Wwise with the Rift, see [Rift Audio](/documentation/pcsdk/latest/concepts/dg-vr-audio/) in the PC SDK Developer Guide.

## The Oculus Audio SDK and Audio Spatialization

The Oculus Audio SDK provides free, easy-to-use spatializer plugins for engines and middleware including Unity. Our spatialization features support both Rift and mobile development.

Our ability to localize audio sources in three-dimensional space is a fundamental part of how we experience sound. Spatialization is the process of modifying sounds to make them localizable, so they seem to originate from distinct locations relative to the listener. It is a key part of creating presence in virtual reality games and applications.

For a detailed discussion of audio spatialization and virtual reality audio, we recommend reviewing our [Introduction to Virtual Reality Audio](/documentation/audiosdk/latest/concepts/book-audio-intro/) guide. 

**Oculus Native Spatializer Plugin for Unity (ONSP)**

The Oculus Native Spatializer Plugin (ONSP) is an plugin for Unity that allows monophonic sound sources to be spatialized in 3D relative to the user's head location.

The ONSP is built on Unity’s Native Audio Plugin, which removes redundant spatialization logic and provides a first-party HRTF. 

The ONSP Audio SDK also supports early reflections and late reverberations using a simple 'shoebox model,' consisting of a virtual room centered around the listener's head, with four parallel walls, a floor, and a ceiling at varying distances, each with its own distinct reflection coefficient.

The ONSP is available with the Audio SDK Plugins package from our [Downloads page](/downloads/). To learn more about it, see our [Oculus Audio SDK Guide](/documentation/audiosdk/latest/concepts/book-audiosdk/) and our [Oculus Native Spatializer for Unity Guide](/documentation/audiosdk/latest/concepts/book-ospnative-unity/). 

## Built-in audio spatialization

Unity versions 5.4.1p1 and later include a basic version of our ONSP built into the editor, which includes HRTF spatialization, but not early reflections and late reverberations. This makes it trivially easy to add basic spatialization to audio point sources in your Unity project. 

For more information, see [VR Audio Spatializers](https://docs.unity3d.com/Manual/VRAudioSpatializer.html) in the Unity Manual, or [First-Party Audio Spatialization (Beta)](/documentation/audiosdk/latest/concepts/ospnative-unity-fp/) in our Oculus Native Spatializer for Unity guide.
