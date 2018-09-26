---
title: Attenuation and Reflections
---

Attenuation is key component of game audio, but 3D spatialization with reflections complicates the topic.

Accurate reflections are the most important feature in simulating distance, and to provide correct distance cues it is critical to have a natural balance between the direct path and reflections. We must consider the attenuation of all reflection paths reflected by the room model. 

For a sound source close to the listener, the sound’s reflections are barely audible, and the sound is dominated by the direct signal. A sound that is further away has more reverberant content, and reflections are typically almost as loud as the direct signal.

This creates a challenge when using authored curves. If they do not match the internal curve, they will create conflicting distance cues. Consider the situation where the authored curve is more gradual than the internal curve - as the sound moves away from the listener, the reflections falls off faster and results in an apparently-distant sound with no audible reflections. That is the opposite of what is expected.

The best way to achieve accurate distance cues is to use the Oculus Attenuation model, as it will guarantee that the reflections and direct signal are correctly balanced. If you do need to use authored curves, we recommend that you set the attenuation range min/max to match the authored curve as closely as possible.
