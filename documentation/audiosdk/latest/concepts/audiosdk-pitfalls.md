---
title: Pitfalls and Workarounds
---

Spatialization and room effects greatly contribute to realism, but they come at a cost.

## Performance

Spatialization incurs a performance hit for each additional sound that must be placed in the 3D sound field. This cost varies, depending on the platform. For example, on a high end PC, it may be reasonable to spatialize 50+ sounds, while you may only be able to spatialize one or two sounds on a mobile device.

Some sounds may not benefit from spatialization even if placed in 3D in the world. For example, very low rumbles or drones offer poor directionality and could be played as standard stereo sounds with some panning and attenuation.

## Audible Artifacts

As a 3D sound moves through space, different HRTFs and attenuation functions may become active, potentially introducing discontinuities at audio buffer boundaries. These discontinuities will often manifest as clicks, pops or ripples. They may be masked to some extent by reducing the speed of traveling sounds and by ensuring that your sounds have broad spectral content.

## Latency

While latency affects all aspects of VR, it is often viewed as a graphical issue. However, audio latency can be disruptive and immersion-breaking as well. Depending on the speed of the host system and the underlying audio layer, the latency from buffer submission to audible output may be as short as 2 ms in high performance PCs using high end, low-latency audio interfaces, or, in the worst case, as long as hundreds of milliseconds.

High system latency becomes an issue as the relative speed between an audio source and the listener's head increases. In a relatively static scene with a slow moving viewer, audio latency is harder to detect. 

## Compatibility between VR and Non-VR Games

Few developers have the luxury of targeting VR headsets exclusively, and must support traditional, non-VR games using external speakers and without the benefit of positional tracking. Weighing quality versus compatibility can be difficult and incur development time.
