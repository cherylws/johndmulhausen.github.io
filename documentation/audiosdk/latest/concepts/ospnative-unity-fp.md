---
title: First-Party Audio Spatialization (Beta)
---
Unity v5.4.0b16 and later include a basic version of our Oculus Native Spatializer Plugin (ONSP) that makes it easy to apply basic spatialization (HRTF transforms) to audio point sources in your Unity project. For full functionality, you must import our standalone plugin into your project.

To activate the Unity built-in Oculus spatializer:

1. Open your project in the Unity Editor.
2. Select *Edit > Project Settings > Audio*.
3. In the Inspector, select *OculusSpatializer* in the *Spatializer Plugin* selection box.
4. Set *Default Speaker Mode* to *Stereo*.
![](/images/documentation-audiosdk-latest-concepts-ospnative-unity-fp-0.png)  
HRTF transforms will be applied to any point sources as if you had imported the native plugin. For the full functionality, you must download and import the standalone ONSP - see the next section for details.

## Using the Standalone Oculus Native Spatializer Plugin

The standalone plugin provides configurable room reflections, ambisonic decoding, and various other audio settings in addition to the HRTF spatialization you get with the built-in Oculus spatializer. You can switch to the standalone plugin even if you previously activated Unityâ€™s built-in Oculus spatializer in Unity.

To import the standalone ONSP, see [Requirements and Setup](/documentation/audiosdk/latest/concepts/ospnative-unity-req-setup/). After importing the standalone ONSP, its settings and effects override any other settings previously made with the built-in spatializer.

![](/images/documentation-audiosdk-latest-concepts-ospnative-unity-fp-1.png)  
You must set the AudioManager settings as follows:

1. Set *Default Speaker Mode* to *Stereo*.
2. Set *Spatializer Plugin* to *OculusSpatializer*.
3. Set *Ambisonic Decoder Plugin* to *OculusSpatializer*.
4. If developing for Gear VR, set *DSP Buffer Size* to *Good* or *Default* to avoid audio distortion.
