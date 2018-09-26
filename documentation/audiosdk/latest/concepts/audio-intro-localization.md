---
title: Localization and the Human Auditory System
---



Human beings have two ears, but are able to locate sound sources in three dimensions. This should not be possible — if someone played a stereo recording and asked you to determine if the sound came from above or below the microphones, you could not tell. If you can't do it from a recording, how can you do it in reality?

Humans rely on psychoacoustics and inference to localize sounds in 3 dimensions, including factors such as timing, phase, level, and spectral modifications.

This section summarizes how humans localize sound. Later, we will apply that knowledge to solve the spatialization problem, and learn how developers can use a monophonic sound and transform its signal so that it sounds like it comes from a specific point in space.

## Directional Localization

In this section, we will look at the cues humans use to determine the direction to a sound source. The two key components of localization are direction and distance.

### Lateral

Laterally localizing a sound is the simplest type of localization, as one would expect. When a sound is closer to the left, the left ear hears it before the right ear hears it, and it sounds louder. The closer to parity, the more centered the sound, generally speaking.

There are, however, some interesting details. First, we may primarily localize a sound based on the delay between the sound's arrival in both ears, or **interaural time difference** (**ITD**); or, we may primarily localize a sound based on the difference in the sound's volume level in both ears, or the **interaural level difference** (**ILD**). The localization technique we rely upon depends heavily on the frequency content of the signal.

Sounds below a certain frequency (anywhere from 500 to 800 Hz, depending on the source) are difficult to distinguish based on level differences. However, sounds in this frequency range have half wavelengths greater than the dimensions of a typical human head, allowing us to rely on timing information (or **phase**) between the ears without confusion.

At the other extreme, sounds with frequencies above approximately 1500 Hz have half wavelengths smaller than the typical head. Phase information is therefore no longer reliable for localizing the sound. At these frequencies, we rely on level differences caused by **head shadowing**, or the sound attenuation that results from our heads obstructing the far ear (see figure below).

![](/images/documentationaudiosdklatestconceptsaudio-intro-localization-0.png)

We also key on the difference in time of the signal's onset. When a sound is played, which ear hears it first is a big part of determining its location. However, this only helps us localize short sounds with transients as opposed to continuous sounds.

There is a transitional zone between ~800 Hz and ~1500 Hz in which both level differences and time differences are used for localization.

### Front/Back/Elevation

Front versus back localization is significantly more difficult than lateral localization. We cannot rely on time differences, since interaural time and/or level differences may be zero for a sound in front of or behind the listener.

In the following figure, we can see how sounds at locations **A** and **B** would be indistinguishable from each other since they are the same distance from both ears, giving identical level and time differences.

![](/images/documentationaudiosdklatestconceptsaudio-intro-localization-1.png)

Humans rely on **spectral modifications** of sounds caused by the head and body to resolve this ambiguity. These spectral modifications are filters and reflections of sound caused by the shape and size of the head, neck, shoulders, torso, and especially, by the outer ears (or **pinnae**). Because sounds originating from different directions interact with the geometry of our bodies differently, our brains use spectral modification to infer the direction of origin. For example, sounds approaching from the front produce resonances created by the interior of our pinnae, while sounds from the back are shadowed by our pinnae. Similarly, sounds from above may reflect off our shoulders, while sounds from below are shadowed by our torso and shoulders.

These reflections and shadowing effects combine to create a **direction-selective filter**.

### Head-Related Transfer Functions (HRTFs)

A direction-selection filter can be encoded as a **head-related transfer function** (HRTF). The HRTF is the cornerstone for most modern 3D sound spatialization techniques. How we measure and create an HRTF is described in more detail elsewhere in this document.

### Head Motion

HRTFs by themselves may not be enough to localize a sound precisely, so we often rely on head motion to assist with localization. Simply turning our heads changes difficult front/back ambiguity problems into lateral localization problems that we are better equipped to solve.

In the following figure, sounds at **A** and **B** are indistinguishable from each other based on level or time differences, since they are identical. By turning her head slightly, the listener alters the time and level differences between ears, helping to disambiguate the location of the sound. **D1** is closer than **D2**, which is a cue to the listener that the sound is to now closer to the left, and therefore behind her.

![](/images/documentationaudiosdklatestconceptsaudio-intro-localization-2.png)

Likewise, cocking our heads can help disambiguate objects vertically. In the following figure, the listener cocks her head, which results in **D1** shortening and **D2** lengthening. This helps the listener determine that the sound originated above her head instead of below it.

![](/images/documentationaudiosdklatestconceptsaudio-intro-localization-3.png)

## Distance Localization



ILD, ITD and HRTFs help us determine the direction to a sound source, but they give relatively sparse cues for determining the distance to a sound. We use a combination of the following factors to determine distance:

* Loudness
* Initial time delay
* Ratio of direct sound to reverberant sound
* Motion parallax
* High-frequency attenuation


#### Loudness

Loudness is the most obvious distance cue, but it can be misleading. If we lack a frame of reference, we can't judge how much the sound has diminished in volume from its source, and thus estimate a distance. Fortunately, we are familiar with many of the sound sources that we encounter daily, such as musical instruments, human voice, animals, vehicles, and so on, so we can predict these distances reasonably well.

For synthetic or unfamiliar sound sources, we have no such frame of reference, and we must rely on other cues or relative volume changes to predict if a sound is approaching or receding.

#### Initial Time Delay

**Initial time delay** describes the interval between the direct sound and its first reflection. The longer this gap, the closer we assume that we are to the sound source.

![](/images/documentationaudiosdklatestconceptsaudio-intro-localization-4.png)

Anechoic (echoless) or open environments such as deserts may not generate appreciable reflections, which makes estimating distances more difficult.

#### Ratio of Direct Sound to Reverberation

In a reverberant environment there is a long, diffuse sound tail consisting of all the late echoes interacting with each other, bouncing off surfaces, and slowly fading away. The more we hear of a direct sound in comparison to the late reverberations, the closer we assume it is.

This property has been used by audio engineers for decades to move a musical instrument or vocalist “to the front” or “to the back” of a song by adjusting the “wet/dry mix” of an artificial reverb.

#### Motion Parallax

Motion parallax (the apparent movement of a sound source through space) indicates distance because nearby sounds typically exhibit a greater degree of parallax than far-away sounds. For example, a nearby insect can traverse from the left to the right side of your head very quickly, but a distant airplane may take many seconds to do the same. As a consequence, if a sound source travels quickly relative to a stationary perspective, we tend to perceive that sound as coming from nearby. 

#### High-Frequency Attenuation

High frequencies attenuate faster than low frequencies, so over long distances we can infer a bit about distance based on how attenuated those high frequencies are. This is often a little overstated in the literature, because sounds must travel hundreds or thousands of feet before high frequencies are noticeably attenuated (i.e., well above 10 kHz). This is also affected by atmospheric conditions, such as temperature and humidity.
