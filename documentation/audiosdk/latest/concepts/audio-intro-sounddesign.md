---
title: Sound Design for Spatialization
---

Now that we've established how humans place sounds in the world and, more importantly, how we can fool people into thinking that a sound is coming from a particular point in space, we need to examine how we must change our approach to sound design to support spatialization.

## Mono

Most spatialization techniques model sound sources as infinitely small **point sources**; that is, sound is treated as if it were coming from a single point in space as opposed to a large area, or a pair of discrete speakers. As a result, sounds should be authored as monophonic (single channel) sources.

## Avoid Sine Waves

Pure tones such as sine waves lack harmonics or overtones, which presents several issues:

* Pure tones do not commonly occur in the real world, so they often sound unnatural. This does not mean you should avoid them entirely, since many VR experiences are abstract, but it is worth keeping in mind.
* HRTFs work by filtering frequency content, and since pure tones lack that content, they are difficult to spatialize with HRTFs
* Any glitches or discontinuities in the HRTF process will be more audible since there is no additional frequency content to mask the artifacts. A moving sine wave will often bring out the worst in a spatialization implementation.


## Use Wide Spectrum Sources

For the same reasons that pure tones are poor for spatialization, broad spectrum sounds work well by providing lots of frequencies for the HRTF to work with. They also help mask audible glitches that result from dynamic changes to HRTFs, pan, and attenuation. In addition to a broad spectrum of frequencies, ensure that there is significant frequency content above 1500 Hz, since this is used heavily by humans for sound localization.

Low frequency sounds are difficult for humans to locate - this is why home theater systems use a monophonic subwoofer channel. If a sound is predominantly low frequency (rumbles, drones, shakes, et cetera), then you can avoid the overhead of spatialization and use pan/attenuation instead.

## Avoid Real-time Format Conversions

Converting from one audio format to another can be costly and introduce latency, so sounds should be delivered in the same output format (sampling rate and bit depth) as the target device. For most PCs, this will be 16-bit, 44.1 kHz PCM, but some platforms may have different output formats (e.g. 16-bit, 48 kHz on Gear VR).

Spatialized sounds are monophonic and should thus be authored as a single channel to avoid stereo-to-mono merging at run-time (which can introduce phase and volume artifacts).

If your title ships with non-native format audio assets, consider converting to native format at installation or load time to avoid a hit at run-time.
