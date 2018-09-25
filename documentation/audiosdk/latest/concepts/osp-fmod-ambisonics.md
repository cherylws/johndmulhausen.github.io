---
title: Ambisonics in FMOD
---
The Oculus FMOD OSP supports Oculus Ambisonics in the AmbiX (ACN/SN3D) format.

To apply Oculus Ambisonics to a sound file, select *Add Effect > Plug-in Effects > Oculus Ambisonics*.

![](/images/documentation-audiosdk-latest-concepts-osp-fmod-ambisonics-0.png)  
Ambisonics are not officially supported by FMOD Studio 1.8, but its flexible bus architecture and multi-channel audio support allows ambisonics to work. However, there are two quirks to watch out for:

## Head Tracking Only Works with an Oculus Effect on the Master Track

There is no head tracking if you don't have any Oculus effects on the master track. For example, if you are creating a sound scene composed solely of Oculus Ambisonics effects on audio tracks, the audio will not be spatialized as you turn or move your head. This limitation is because FMOD only propagates the 3D positional data to effects that are on the master track.

The workaround is to add the Oculus Spatializer effect to the master track even if you only play silence on that track. This works because positional data is shared between all the Oculus effects. The Oculus Spatializer effect on the master track will get the FMOD positional data and then share it with the other Oculus effects on the audio tracks.

## Avoid putting the Oculus Ambisonic Effect on the Master Track.

If you put a 4-channel ambisonic sound file on an audio track and the Oculus Ambisonics effect on the master track, it will not sound right. FMOD upmixes 4-channel ambisonic sound files to 5.1 at the output of the audio track. This mixes the channels together in a way that interferes with the sound field. 

There are two ways to work around this:

* Add the Oculus Ambisonics effect to the same Audio Track as the sound file.

Notice in the screenshot below that the meters on the “In” at the left side of the track shows 4 channels. This is the best approach if you wish to play back a single ambisonic sound or loop.

![](/images/documentation-audiosdk-latest-concepts-osp-fmod-ambisonics-1.png)  

* Convert your 4-channel ambisonics sound files to pseudo 5.1 files by converting them to 6 channels.

Insert two silent channels between the ambisonics channel, so the third and fourth channels are silent, as shown below. This prevents FMOD from upmixing and passes through six channels to the Oculus Ambisonics, which knows to interpret that as ambisonic.

This approach works well if you are playing back several ambisonic sounds in one event and want to mix them together before spatializing. The most common use case for this is an interactive music mix using ambisonics.

![](/images/documentation-audiosdk-latest-concepts-osp-fmod-ambisonics-2.png)  
Note: You will have to make your project speaker mode 5.1 instead of stereo to make this work.
For more information on Oculus Ambisonics, see the *Oculus Ambisonics* section of the [Supported Features](/documentation/audiosdk/latest/concepts/audiosdk-features/#audiosdk-features-supported "This section describes supported features.") section of our Audio SDK Guide.

