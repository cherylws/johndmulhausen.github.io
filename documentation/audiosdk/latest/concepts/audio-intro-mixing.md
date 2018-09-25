---
title: Mixing Scenes for Virtual Reality
---
As with sound design, mixing a scene for VR is an art as well as a science, and the following recommendations may include caveats.

## Creative Control

Realism is not necessarily the end goal! Keep this in mind at all times. As with lighting in computer environments, what is consistent and/or “correct” may not be aesthetically desirable. Audio teams must be careful not to back themselves into a corner by enforcing rigid notions of correctness on a VR experience.

This is especially true when considering issues such as dynamic range, attenuation curves, and direct time of arrival.

## Accurate 3D Positioning of Sources

Sounds must now be placed carefully in the 3D sound field. In the past a general approximation of location was often sufficient since positioning was accomplished strictly through panning and attenuation. The default location for an object might be its hips or where its feet met the ground plane, and if a sound is played from those locations it will be jarring with spatialization, e.g. “crotch steps” or “foot voices”.

## Directional Sources

The Oculus Audio SDK does not support directional sound sources (speakers, human voice, car horns, et cetera). However, higher level SDKs often model these using angle-based attenuation that controls the tightness of the direction. This directional attenuation should occur before the spatialization effect.

## Area Sources

The Oculus Audio SDK does not support area sound sources such as waterfalls, rivers, crowds, and so on.

## Doppler Effect

The Doppler effect is the apparent change of a sound's pitch as its source approaches or recedes. VR experiences can emulate this by altering the playback based on the relative speed of a sound source and the listener, however it is very easy to introduce artifacts inadvertently in the process.

The Oculus Audio SDK does not have native support for the Doppler effect, though some high-level SDKs do.

## Sound Transport Time

In the real world, sound takes time to travel, so there is often a noticeable delay between seeing and hearing something. For example, you would see the muzzle flash from a rifle fired at you 100 meters away roughly 330 ms before you would hear it. Modeling propagation time incurs some additional complexity and may paradoxically make things seem less realistic, as we are conditioned by popular media to believe that loud distance actions are immediately audible.

The Oculus Audio SDK supports time-of-arrival.

## Non-Spatialized Audio

Not all sounds need to be spatialized. Plenty of sounds are static or head relative, such as:

* User interface elements, such as button clicks, bleeps, transitions, and other cues
* Background music
* Narration
* Body sounds, such as breathing or heart beats
Such sounds should be segregated during authoring as they will probably be stereo, and during mixing so they are not inadvertently pushed through the 3D positional audio pipeline.

## Performance

Spatialization incurs a performance hit for each additional sound that must be placed in the 3D sound field. This cost varies, depending on the platform. For example, on a high end PC, it may be reasonable to spatialize 50+ sounds, while you may only be able to spatialize one or two sounds on a mobile device.

Some sounds may not benefit from spatialization even if placed in 3D in the world. For example, very low rumbles or drones offer poor directionality and could be played as standard stereo sounds with some panning and attenuation.

## Ambiance

Aural immersion with traditional non-VR games was often impossible since many gamers or PC users relied on low-quality desktop speakers, home theaters with poor environmental isolation, or gaming headsets optimized for voice chat.

With headphones, positional tracking, and full visual immersion, it is now more important than ever that sound designers focus on the user's audio experience.

This means:

* Properly spatialized sound sources
* Appropriate soundscapes that are neither too dense nor too sparse
* Avoidance of user fatigue
* Suitable volume levels comfortable for long-term listening
* Room and environmental effects
## Audible Artifacts

As a 3D sound moves through space, different HRTFs and attenuation functions may become active, potentially introducing discontinuities at audio buffer boundaries. These discontinuities will often manifest as clicks, pops or ripples. They may be masked to some extent by reducing the speed of traveling sounds and by ensuring that your sounds have broad spectral content.

## Latency

While latency affects all aspects of VR, it is often viewed as a graphical issue. However, audio latency can be disruptive and immersion-breaking as well. Depending on the speed of the host system and the underlying audio layer, the latency from buffer submission to audible output may be as short as 2 ms in high performance PCs using high end, low-latency audio interfaces, or, in the worst case, as long as hundreds of milliseconds.

High system latency becomes an issue as the relative speed between an audio source and the listener's head increases. In a relatively static scene with a slow moving viewer, audio latency is harder to detect. 

## Effects

Effects such as filtering, equalization, distortion, flanging, and so on can be an important part of the virtual reality experience. For example, a low pass filter can emulate the sound of swimming underwater, where high frequencies lose energy much more quickly than in air, or distortion may be used to simulate disorientation.

