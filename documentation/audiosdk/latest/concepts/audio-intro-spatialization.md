---
title: 3D Audio Spatialization
---



The previous section discussed how humans localize the sources of sounds in three dimensions. We now invert that and ask, “Can we apply that information to fool people into thinking that a sound is coming from a specific point in space?”

The answer, thankfully, is “yes”, otherwise this would be a pretty short document. A big part of VR audio is **spatialization**: the ability to play a sound as if it is positioned at a specific point in three-dimensional space. Spatialization is a key aspect of presence because it provides powerful cues suggesting the user is in an actual 3D environment, which contributes strongly to a sense of immersion. 

As with localization, there are two key components to spatialization: direction and distance.

## Directional Spatialization with Head-Related Transfer Functions (HRTFs)

We know that sounds are transformed by our body and ear geometry differently depending on the incoming direction. These different effects form the basis of HRTFs, which we use to localize a sound.

### Capturing HRTFs

The most accurate method of HRTF capture is to take an individual, put a couple microphones in their ears (right outside the ear canal), place them in an anechoic chamber (i.e., an anechoic environment), play sounds in the chamber from every direction we care about, and record those sounds from the mics. We can then compare the original sound with the captured sound and compute the HRTF that takes you from one to the other.

We have to do this for both ears, and we have to capture sounds from a sufficient number of discrete directions to build a usable sample set.

But wait — we have only captured HRTFs for a specific person. If our brains are conditioned to interpret the HRTFs of our own bodies, why would that work? Don't we have to go to a lab and capture a personalized HRTF set?

In a perfect world, yes, we'd all have custom HRTFs measured that match our own body and ear geometry precisely, but in reality this isn't practical. While our HRTFs are personal, they are similar enough to each other that a generic reference set is adequate for most situations, especially when combined with head tracking.

Most HRTF-based spatialization implementations use one of a few publicly available data sets, captured either from a range of human test subjects or from a synthetic head model such as the KEMAR.

* [IRCAM Listen Database](http://recherche.ircam.fr/equipes/salles/listen/)
* [MIT KEMAR](http://sound.media.mit.edu/resources/KEMAR.html)
* [CIPIC HRTF Database](https://www.ece.ucdavis.edu/cipic/spatial-sound/hrtf-data/)
* [ARI (Acoustics Research Institute) HRTF Database](https://www.kfs.oeaw.ac.at/index.php?option=com_content&amp;view=article&amp;id=608:ari-hrtf-database&amp;catid=158:resources-items&amp;Itemid=606&amp;lang=en)


Most HRTF databases do not have HRTFs in all directions. For example, there is often a large gap representing the area beneath the subject's head, as it is difficult, if not impossible, to place a speaker one meter directly below an individual's head. Some HRTF databases are sparsely sampled, including HRTFs only every 5 or 15 degrees.

Most implementations either snap to the nearest acquired HRTF (which exhibits audible discontinuities) or use some method of HRTF interpolation. This is an ongoing area of research, but for VR applications on desktops, it is often adequate to find and use a sufficiently-dense data set.

### Applying HRTFs

Given an HRTF set, if we know the direction we want a sound to appear to come from, we can select an appropriate HRTF and apply it to the sound. This is usually done either in the form of a time-domain convolution or an FFT/IFFT pair.

If you don't know what these are, don't worry - those details are only relevant if you are implementing the HRTF system yourself. Our discussion glosses over a lot of the implementation details (e.g., how we store an HRTF, how we use it when processing a sound). For our purposes, what matters is the high-level concept: we are simply filtering an audio signal to make it sound like it's coming from a specific direction.

Since HRTFs take the listener's head geometry into account, it is important to use headphones when performing spatialization. Without headphones, you are effectively applying two HRTFs: the simulated one, and the actual HRTF caused by the geometry of your body.

### Head Tracking

Listeners instinctively use head motion to disambiguate and fix sound in space. If we take this ability away, our capacity to locate sounds in space is diminished, particularly with respect to elevation and front/back. Even ignoring localization, if we are unable to compensate for head motion, then sound reproduction is tenuous at best. When a listener turns their head 45 degrees to the side, we must be able to reflect that in their auditory environment, or the soundscape will ring false.

VR headsets such as the Rift provide the ability to track a listener's head orientation (and, sometimes, position). By providing this information to a sound package, we can project a sound in the listener's space, regardless of their head position.

This assumes that the listener is wearing headphones. It is possible to mimic this with a speaker array, but it is significantly less reliable, more cumbersome, and more difficult to implement, and thus impractical for most VR applications.

## Distance Modeling



HRTFs help us identify a sound's direction, but they do not model our localization of distance. Humans use several factors to infer the distance to a sound source. These can be simulated with varying degrees of accuracy and cost in software:

* **Loudness**, our most reliable cue, is trivial to model with simple attenuation based on distance between the source and the listener.
* **Initial Time Delay** is significantly harder to model, as it requires computing the early reflections for a given set of geometry, along with that geometry's characteristics. This is both computationally expensive and awkward to implement architecturally (specifically, sending world geometry to a lower level API is often complex). Even so, several packages have made attempts at this, ranging from simple “shoebox models” to elaborate full scene geometric modeling.
* **Direct vs. Reverberant Sound** (or, in audio production, the “wet/dry mix”) is a natural byproduct of any system that attempts to accurately model reflections and late reverberations. Unfortunately, such systems tend to be very expensive computationally. With ad hoc models based on artificial reverberators, the mix setting can be adjusted in software, but these are strictly empirical models.
* **Motion Parallax** we get “for free,” because it is a byproduct of the velocity of a sound source.
* **High Frequency Attenuation** due to air absorption is a minor effect, but it is also reasonably easy to model by applying a simple low-pass filter, and by adjusting cutoff frequency and slope. In practice, HF attenuation is not very significant in comparison to the other distance cues.

