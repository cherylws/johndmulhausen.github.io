---
title: Listening Devices
---



Traditionally, high quality audio reproduction has been the domain of multi-speaker systems, often accompanied by one or more subwoofers. However, with the rise of online gaming and voice chat, many players have transitioned to headsets (headphones with integrated microphones).

For modern VR, especially with head tracking and user movement, speaker arrays are an evolutionary dead end. Headphone audio will be the standard for VR into the future, as it provides better isolation, privacy, portability, and spatialization.

## Headphones

Headphones offer several significant advantages over free-field speaker systems for virtual reality audio:

* **Acoustic isolation** from the listener's environment enhance realism and immersion.
* **Head tracking** is greatly simplified.
* **HRTFs** are more accurate since they don't suffer from the “doubling down” of HRTF effects (sounds modified from the simulated HRTF, and again by the listener's actual body geometry).
* **Access to controls** while wearing an HMD is far simpler when those controls are physically attached to the listener.
* **Microphones** are ideally placed and subject to much less echo/feedback.


![](/images/documentationaudiosdklatestconceptsaudio-intro-devices-0.png)

Headphones are available in a variety of types with various trade-offs:

## Closed Back Headphones

As a general rule of thumb, closed back headphones offer the most isolation and bass response. However, the closed construction may lead to discomfort (due to heat and weight), and they tend to offer less accurate reproduction due to internal resonance. Also, if placed on or over the ear, they cause the pinnae to impact sound reproduction slightly.

![](/images/documentationaudiosdklatestconceptsaudio-intro-devices-1.png)

While acoustic isolation can help with immersion, it cuts listeners off from their environment so they may be unable to hear others entering the room, cell phone ringing, doorbell, et cetera. Whether that is a good thing or not is up to the individual.

## Open Back Headphones

Open back headphones are generally more accurate and comfortable than closed-back headphones, but they do not isolate listeners from the exterior environment, and broadcast to the surrounding environment as well. These are suitable for quiet areas devoted to a VR experience, possibly in conjunction with a subwoofer.

![](/images/documentationaudiosdklatestconceptsaudio-intro-devices-2.png)

As with closed back headphones, when placed on or over the ear, open back headphones allow the pinnae to impact sound reproduction slightly.

## Earbuds

Earbuds (such as those that ship with cell phones or portable music players) are cheap, lightweight, and very portable, though they typically lack bass. Some models, such as Apple EarPods, have surprisingly good frequency response, albeit with a steady roll off of bass frequencies. These are mostly ignored for spatialization.

Most earbuds are poor at isolation.

![](/images/documentationaudiosdklatestconceptsaudio-intro-devices-3.png)

## In-Ear Monitors

In-ear monitors offer superior isolation from your environment, are very lightweight, and have excellent frequency response over the entire range. They remove the effects of the listener's pinnae from sound (unlike on-ear headphones). They have the downside of requiring insertion into the ear canal, which eliminates the effects of the ear canal from sound reproduction entirely (since most HRTFs are captured with microphones right outside the ear canal).

![](/images/documentationaudiosdklatestconceptsaudio-intro-devices-4.png)

## Impulse Responses

Headphones, like all transducers, impart their own characteristics on signals, and since HRTFs are frequency sensitive, removing the headphone character from the signal will usually be beneficial. This can be accomplished by deconvolving the output signal with the headphone's impulse response.

## External Speaker Systems

Until recently, the most common way to provide sound immersion was to surround the listener with speakers, such as a Dolby 5.1 or 7.1 speaker configuration. While partially effective for a fixed and narrow sitting position, speaker array systems suffer from key drawbacks:

* **Imprecise imaging** due to panning over large portions of the listening area.
* **No elevation cues**, sounds only appear in a 360 degree circle around the listener.
* Assumption of **immobile listener**; in particular, no head tracking.
* **Room effects** such as reverberation and reflections impact the reproduced sound.
* **Poor isolation** means that outside sounds can intrude on the VR experience.


It is doubtful that multi-speaker configurations will be common or effective for home VR applications, though they may be viable for dedicated commercial installations.

## Bluetooth

Bluetooth has become a popular communication method of wireless audio broadcast. Unfortunately, modern Bluetooth implementations often incur significant latency, sometimes as high as 500 milliseconds. As a result, Bluetooth technology is not recommended for audio output.
