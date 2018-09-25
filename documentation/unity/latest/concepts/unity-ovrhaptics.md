---
title: OVRHaptics for Oculus Touch
---
This guide reviews OVRHaptics and OVRHapticsClip, two C# scripts that programmatically control haptics feedback for Touch. 

## Haptics Clips

Haptics clips specify the data used to control haptic vibrations in Touch controllers.

Vibrations are specified by an array of bytes or “samples,” which specify vibration strength from 0-255. This data can be sent to the left and right touch controllers independently, which process the amplitudes at a sample rate of 320 Hz. The duration of vibration is determined by the number of bytes sent to the devices.

Haptics clips may be created in different ways, depending on your needs. For example, you may manually create a clip with a pre-allocated fixed size buffer, and then write in bytes procedurally. This allows you to generate vibrations on a frame-by-frame basis.

The OVRHaptics class is used to produce the actual vibrations. It defines a LeftChannel and a RightChannel. You can also access these channels through the aliased Channels property, where Channels[0] maps to LeftChannel, and Channels[1] maps to RightChannel. This alias is useful when using a variable for the channel index in a script that can be associated with either hand..

Once you have selected a haptics channel, you may perform four operations with the following OVRHapticsChannel member functions:

* Queue(OVRHapticsClip clip): Queues up a clip.
* Preempt(OVRHapticsClip clip): Removes any previously existing clips already in the queue, and queues up the provided clip; useful for per-frame scenarios.
* Mix(OVRHapticsClip clip): Performs a simple sum and clip mix of the provided clip with any existing clips already in the queue. Can be useful to play multiple clips simultaneously. For example, firing a shotgun in a scene while a dinosaur is stomping by.
* Clear(): Removes all pending clips in the queue and stops haptics for the current channel.
See our [Developer Reference](/documentation/game-engines/latest/concepts/book-unity-reference/) for API documentation and details on the relevant classes and members.

## Generating Haptics Clips from AudioClips

The OVRHapticsClip(AudioClip audioClip, int channel = 0) constructor allows applications to read in a audio clip and generate haptics clips that correspond in strength to the audio clip’s amplitude (i.e., volume). You may use monophonic audio clips, or access the left or right channel of a stereo audio clip with the optional channel parameter (default 0 = left stereo/mono, 1 = right stereo). See the [Unity Scripting Reference](/documentation/unity/latest/concepts/unity-reference-scripting/ "The Unity Scripting Reference contains detailed information about the data structures and files included with the Utilities and Legacy Integration packages.") for more information.

OVRHapticsClip reads in an audio clip, downsamples the audio data to a sequence of bytes with the expected sample rate and amplitude range, and feeds that data into the clip’s internal amplitude buffer.

We generally recommend AudioClip-generated haptics clips for static sound effects such as gunshots or music that do not vary at runtime. However, you may wish to write your own code to pipe the audio output of an audio source in realtime to a OVRHapticsClip, allowing you near-realtime conversion of audio into corresponding haptics data.

## Best Practices

The Rift must be worn in order for haptics to work, as the Oculus runtime only allows the currently-focused VR app to receive Touch haptics. 

It is important to keep your sample pipeline at around the right size. Assuming a haptic frequency of 320 Hz and an application frame rate of 90 Hz, we recommend targeting a buffer size of around 10 clips per frame. This allows you to play 3-4 haptics clips per frame, while preserving a buffer zone to account for any asynchronous interruptions. The more bytes you queue, the safer you are from interruptions, but you add additional latency before newly queued vibrations will be played.

Note: For use with Oculus Touch only.