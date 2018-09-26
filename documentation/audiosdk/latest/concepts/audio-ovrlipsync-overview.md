---
title: Overview
---

This guide describes how to install and use the Oculus Lipsync Unity integration.

The Oculus Lipsync Unity integration is a tool used to sync avatar lip movements to speech sounds. Oculus Lipsync analyzes an audio input stream from a microphone input or an audio file, and either offline or in real-time predicts a set of values (called visemes) which may be used to animate the lips of an avatar.

A **viseme** is a gesture or expression of the lips and face that corresponds to a particular speech sound. The term is used, for example, when discussing lip reading, where it is analogous to the concept of a phoneme, and is a basic visual unit of intelligibility. In computer animation, visemes may be used to animate avatars so that they look like they are speaking.

Oculus Lipsync uses a repertoire of visemes to modify avatars based on a specified audio input stream. Each viseme targets a specified geometry morph target in an avatar to influence the amount that target will be expressed on the model. Thus, with Oculus Lipsync we can generate realistic lip movement in sync with what is being spoken or heard. This enhances the visual cues that one can use when populating an application with avatars, be they controlled by a user, or Non-playable Characters (NPCs).

Our system maps to 15 separate viseme targets: sil, PP, FF, TH, DD, kk, CH, SS, nn, RR, aa, E, ih, oh, and ou. The visemes describe the face expression produced when uttering the corresponding speech sound. For example the viseme sil corresponds to a silent/neutral expression, PP corresponds to pronouncing the first syllable in “popcorn,” FF the first syllable of “fish,” and so forth. 

These targets have been selected to give the maximum range of lip movement, and are agnostic to language. For more information on these 15 visemes and how they were selected, please read the following documentation: [Viseme MPEG-4 Standard](http://www.visagetechnologies.com/uploads/2012/08/MPEG-4FBAOverview.pdf). We have also produced a set of reference images which we believe are easier to work from here: [Viseme Reference Images](/documentation/audiosdk/latest/concepts/audio-ovrlipsync-viseme-reference/). 
