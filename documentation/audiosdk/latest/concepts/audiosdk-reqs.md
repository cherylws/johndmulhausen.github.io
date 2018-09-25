---
title: Requirements
---
## Head Tracking

By tracking the listener's head position and orientation, we can achieve accurate 3D sound spatialization. As the listener moves or rotates their head, they perceive the sound as remaining at a fixed location in the virtual world.

Developers may pass Oculus PC SDK ovrPosef structures to the Oculus Audio SDK for head tracking support. Alternatively, they can pass listener-space sound positions and no pose information for the same effect.

## Headphones

The Oculus Audio SDK assumes that the end user is wearing headphones, which provide better isolation, privacy, portability, and spatialization than free-field speaker systems. When combined with head tracking and spatialization technology, headphones deliver an immersive sense of presence. For more on the advantages and disadvantages of headphones for virtual reality, please refer to [Listening Devices](/documentation/audiosdk/latest/concepts/audio-intro-devices/) in *Introduction to Audio for Virtual Reality*.

