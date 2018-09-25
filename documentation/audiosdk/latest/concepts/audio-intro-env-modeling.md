---
title: Environmental Modeling
---
 HRTFs in conjunction with attenuation provide an anechoic model of three dimensional sound, which exhibits strong directional cues but tends to sound dry and artificial due to lacking room ambiance. To compensate for this, we can add environmental modeling to mimic the acoustic effects of nearby geometry.

## Reverberation and Reflections

As sounds travel through space, they reflect off of surfaces, creating a series of echoes. The initial distinct echoes (*early reflections*) help us determine the direction and distance to a sound. As these echoes propagate, diminish, and interact they create a *late reverberation tail*, which contributes to our sense of space.

![](/images/documentation-audiosdk-latest-concepts-audio-intro-env-modeling-0.png)  
 We can model reverberation and reflection using several different methods. **Shoebox Model**

Some 3D positional implementations layer simple “shoebox room” modeling on top of their HRTF implementation. These consist of specifying the distance and reflectivity of six parallel walls (i.e., the “shoebox”) and sometimes the listener's position and orientation within that room as well. With that basic model, you can simulate early reflections from walls and late reverberation characteristics.

While far from perfect, it's much better than artificial or no reverberation.

![](/images/documentation-audiosdk-latest-concepts-audio-intro-env-modeling-1.png)  
**Artificial Reverberations**

Since modeling physical walls and late reverberations can quickly become computationally expensive, reverberation is often introduced via artificial, ad hoc methods such as those used in digital reverb units of the 80s and 90s. While less computationally intensive than physical models, they may also sound unrealistic, depending on the algorithm and implementation — especially since they are unable to take the listener's orientation into account.

**Sampled Impulse Response Reverberation**

Convolution reverb samples the *impulse response* from a specific real-world location such as a recording studio, stadium, or lecture hall. It can then be applied to a signal later, resulting in a signal that sounds as if it were played back in that location. This can produce some phenomenally lifelike sounds, but there are some drawbacks. Sampled impulse responses rarely match in-game synthetic environments; they represent a fixed listener position and orientation; they are monophonic; they are difficult to transition between different areas.

Even with these limitations, they still provide high-quality results in many situations.

## World Geometry and Acoustics

The “shoebox model” attempts to provide a simplified representation of an environment's geometry. It assumes no occlusion, equal frequency absorption on all surfaces, and six parallel walls at a fixed distance from the listener's head. Needless to say, this is a heavy simplification for the sake of performance, and as VR environments become more complex and dynamic, it may not scale properly

Some solutions exist today to simulate diffraction and complex environmental geometry, but support is not widespread and performance implications are still significant.

## Environmental Transitions

Modeling a specific area is complex, but still relatively straightforward. Irrespective of choice of model, however, there is a problem of audible discontinuities or artifacts when transitioning between areas. Some systems require flushing and restarting the entire reverberator, and other systems introduce artifacts as parameters are changed in real-time.

## Presence and Immersion

By creating audio that is on par with high quality VR visuals, developers immerse the user in a true virtual world, giving them a sense of presence.

Audio immersion is maximized when the listener is located inside the scene, as opposed to viewing it from afar. For example, a 3D chess game in which the player looks down at a virtual board offers less compelling spatialization opportunities than a game in which the player stands on the play field. By the same token, an audioscape in which moving elements whiz past the listener's head with auditory verisimilitude is far more compelling than one in which audio cues cut the listener off from the action by communicating that they're outside of the field of activity.

![](/images/documentation-audiosdk-latest-concepts-audio-intro-env-modeling-2.png)  
![](/images/documentation-audiosdk-latest-concepts-audio-intro-env-modeling-3.png)  
Note: It should be noted that while the pursuit of realism is laudable, it is also optional, as we want developers and sound designers to maintain creative control over the output.