---
title: Overview
---
This document introduces fundamental concepts in audio development for virtual reality (VR) with an emphasis on key factors that deserve development attention. 

We hope to establish that audio is crucial for creating a persuasive VR experience. Because of the key role that audio cues play in our cognitive perception of existing in space, any effort that development teams devote to getting it right will pay off in spades, as it will contribute powerfully to the user's sense of immersion. This is as true for small- or mid-sized teams as it is for design houses â€” perhaps even more so.

Audio has been a crucial part of the computer and video gaming experience since the advent of the first coin-op games, which filled arcades with bleeps, bloops, and digital explosions. Over time, the state of computer audio has steadily improved, from simple wave generators (SID, 1983) to FM synthesis (AdLib, 1987), evolving on to 8-bit mono samples (Amiga OCS, 1985; SoundBlaster, 1989) and 16-bit stereo samples (SoundBlaster Pro), culminating in today's 5.1 surround sound systems on modern gaming consoles (Xbox, 2001).

Since the development of 5.1 surround, little has changed. The fundamental technology of playing waveforms over speakers is the same, and the game playing environment is still primarily the living room or den with a large television and speakers.

Virtual reality, however, is changing all this. Instead of a large environment with speakers, virtual reality brings the experience in close to the player via a head-mounted display (HMD) and headphones. The ability to track the user's head orientation and position significantly empowers audio technology.

Until now, the emphasis has typically been placed on the visual aspects of virtual reality (resolution, latency, tracking), but audio must now catch up in order to provide the greatest sense of presence possible.

This document discusses the challenges, opportunities, and solutions related to audio in VR, and how some of the techniques learned in traditional game development must be revisited and modified for VR. It is not intended to be a rigorous scientific study of the nature of acoustics, hearing and human auditory perception. Its intended audience includes anyone with an interest in audio and VR, including sound designers, artists, and programmers.

If you are interested in learning about these details in greater depth, we recommend searching the Web for the following terms:

* Head-Related Impulse Response
* Head-Related Transfer Function
* Sound Localization
