---
title: Features
---

This section describes the features supported by the Oculus Audio SDK. 

## Supported Features

This section describes supported features. 

### Spatialization

Spatialization is the process of transforming monophonic sound sources to make them sound as though they originate from a specific desired direction. The Oculus Audio SDK uses **head-related transfer functions (HRTFs)** to provide audio spatialization through the C/C++ SDK and plugins.

### Volumetric Sources

### Near-field Rendering

Sound sources in close proximity to a listener's head have properties that make some aspects of their spatialization independent of their distance. Our near-field rendering automatically approximates the effects of acoustic diffraction to create a more realistic representation of audio sources closer than 1 meter.

### Environmental Modeling

HRTFs provide strong directional cues, but without room effects, they often sound dry and lifeless. Some environmental cues (for example, early reflections and late reverberation) are also important in providing strong cues about the distance to a sound source.

The Audio SDK supports early reflections and late reverberations using a simple 'shoebox model,' consisting of a virtual room centered around the listener's head, with four parallel walls, a floor, and a ceiling at varying distances, each with its own distinct reflection coefficient.

### Oculus Ambisonics

Ambisonics is a multichannel audio format that represents a 3D sound field. It can be thought of as a skybox for audio with the listener at the center. It is a computationally- efficient way to play a pre-rendered or live-recorded scene. The trade-off is that ambisonic sounds offer less spatial clarity and display more smearing than point-source HRTF-processed point source sounds. We recommend using ambisonics for non-diegetic sounds, such as like music and ambiance.

Oculus has developed a novel method for the binaural rendering of ambisonics based on spherical harmonics that reduces the smearing, has better frequency response, and produces better externalization compared with the common virtual speaker- based methods. The Audio SDK supports first-order ambisonics in the AmbiX (ACN/SN3D) format.

Oculus offers an Ambisonics Starter Pack as a convenience for developers (available on our [Download page](/downloads/)). It includes several AmbiX WAV files licensed for use under Creative Commons. The files represent ambient soundscapes, including parks, natural environments with running water, indoor ventilation, rain, urban ambient sounds, and driving noises. 

## Unsupported Features

There are other aspects of a high quality audio experience, however these are often more appropriately implemented by the application programmer or a higher level engine.

### Occlusion

Sounds interact with a user's environment in many ways. Objects and walls may obstruct, reflect, or propagate a sound through the virtual world. The Oculus SDK only supports direct reflections and does not factor in the virtual world geometry. This problem needs to be solved at a higher level than the Oculus Audio SDK due to the requirements of scanning and referencing world geometry.

### Doppler Effect

The **Doppler effect** is the perceived change in pitch that occurs when a sound source is moving at a rapid rate towards or away from a listener, such as the pitch change that is perceived when a car whooshes by. It is often emulated in middleware with a simple change in playback rate by the sound engine.

### Creative Effects

Effects such as equalization, distortion, flanging, and so on can be used to great effect in a virtual reality experience. For example, a low pass filter can emulate the sound of swimming underwater, where high frequencies lose energy much faster than in air, distortion may be used to simulate disorientation, a narrow bandpass equalizer can give a 'radio' effect on sound sources, and so on.

The Oculus Audio SDK does not provide these effects. Typically, these would be applied by a higher level middleware package either before or after the Audio SDK, depending on the desired outcome. For example, a low-pass filter might be applied to the master stereo buffers to simulate swimming underwater, but a distortion effect may be applied pre-spatialization for a broken radio effect in a game.

### Area and directional Sound Sources

The Oculus Audio SDK supports **monophonic point sources**. When a sound is specified, it is assumed that the waveform data represents the sound as audible to the listener. It is up to the caller to attenuate the incoming sound to reflect speaker directional attenuation (e.g. someone speaking while facing away from the listener) and area sources such as waterfalls or rivers.
