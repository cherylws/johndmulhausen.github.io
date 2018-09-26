---
title: Audio SDK 1.16 Release Notes
---

This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Audio SDK.

## 1.16.0

## New Features

* Added support for pre-computed visemes to Oculus Lipsync for Unity.
* Viseme engine improved on Rift to generate smoother and more accurate visemes.
* Added Oculus Audio Manager to provide sound FX management that is external to Unity scene files. This has audio workflow benefits as well as providing you with the ability to group sound FX events together for greater flexibility. 


## Bug Fixes

Fixed an issue with ovrLipSyncDll_ProcessFrame where it did not properly analyze the audio signal.

## API Changes

Due to an API change in Unity 2017 beta, the 1.1.5 version of the Oculus ambisonic decoder is obsolete and does not work in Unity 2017 beta 9 or later. The 1.16.0 version of the ambisonic decoder is now the official ambisonic integration.
