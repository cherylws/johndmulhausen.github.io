---
title: Audio SDK 1.0 Release Notes
---
This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Audio SDK.

## 1.0.4

## Overview of Major Changes

The Unity v 5.4.0b16 Editor added a basic version of our Oculus Native Spatializer Plugin for Unity 5 (ONSP). It makes it trivially easy to add basic spatialization (HRTF transforms) to audio point sources in your Unity project. For more information, see [First-Party Audio Spatialization (Beta)](/documentation/audiosdk/latest/concepts/ospnative-unity-fp/) in our Oculus Native Spatializer for Unity guide.

## Bug Fixes

* Fixed bug in which audio sources were silent when attenuation mode was unset.
* Oculus Spatializer for Wwise Plugin
	+ Fixed crash when adding Wwise 2017 spatializer to a Wwise project.
	
## Known Issues

* **Gear VR developers** using Unity 5.3.4 or later, or using Unity 5.4.0b16 and later: Do not set *DSP Buffer Size* to *Best* in *Audio Manager* in the Inspector for now or you will encounter audio distortion. Set it to *Good* or *Default* instead.
## 1.0.3

## New Features

* VST Integration
	+ Added head tracking in DAW.
	+ Added Volume Unit (VU) meter.
	+ Added support for Adobe Audition v 8.1 (Windows and OS X).
	
## API Changes

* Oculus Native Spatializer for Unity 
	+ Log ONSP version number when running test scene.
	+ Redballgreenball demo scene - changed scale of audio parameters (room size and audio source curves) as well as visual geometry to reflect real-world scale.
	
## Bug Fixes

* Fixed incorrect Ambisonics rotation when the listener head rotated.
* Fixed listener rotation for reflections and optimized performance by removing extra silence after reflections.
* Oculus Native Spatializer for Unity
	+ Fixed parameter setting issue in which volume changes and other settings were not set properly.
	+ Fixed volume pop and buzzing anomalies when going in and out of Unity app focus.
	+ Various crash fixes and CPU optimizations.
	
* VST
	+ Fixed scrubbing and loss of early reflections in Adobe Audition and potentially other DAWs.
	
## 1.0.2

## API Changes

* Native Spatializer for Unity: Set void SetParameter(ref AudioSource source) function within ONSPAudioSoure.cs to public. When instantiating a prefab with this component, please be sure to call this function (and pass a reference of the AudioSource component) before calling AudioSource.Play().
* Ambisonics API: Changed to right-hand coordinates to match the rest of the public AudioSDK.
## Bug Fixes

* Fixed bug causing reverb to turn on/off at random. Note that reverb settings in v 1.0.1 plugins may not have been active.
* Reverb is now disabled when per-sound setting to disable reflections is on.
* Fixed rejecting high reflections value from plugins: changed AudioSDK parameter validation to accept reflection coefficients 0-1, and clamp to 0.95.
* Wwise: Fixed for incorrect detection of channel count on sounds sent to OSP bus (previously resulted in n > 1 channel warning message, even though sound is mono).
* Wwise: Temporary fix for sounds using multi-position mode - they now bypass the OSP and display a warning message in profiler log, rather than playing spatialized but unattenuated.
* Unity Native: Fixed reversed z-axis when calculating position of sound relative to listener.
## Known Issues

* High reflection values in small rooms may cause distortion due to volume overload. See parameter documentation in the appropriate OSP guide for more information. 
## 1.0.1

## Overview of Major Changes

This constitutes the first full release of the Oculus Audio SDK.

## New Features

* OSP for FMOD: Added attenuation Range Min. parameter.
* OSP for FMOD: Added support for FMOD Unity Integration 2.0
## API Changes

* Unity Native: Added global scale parameter.
## Bug Fixes

* FMOD: Fixed plugin loading issue for FMOD Unity Integration (Legacy) on OS X.
* Unity Legacy: Microphone input can now be spatialized.
## 1.0.0-beta

## Overview of Major Changes

This constitutes our beta release of Audio SDK 1.0. We have added an additional spatializer plugin for Unity based on their Native Audio Plugin, and are maintaining our original Oculus Spatializer Plugin (OSP) for Unity for legacy development with Unity 4. Developers using Unity 5 should use the Oculus Native Spatializer Plugin.

The priority system has been removed in lieu of middleware- or engine-implemented sound priority. We removed frequency hint as improvements in the core engine made it redundant.

## New Features

* Added Oculus Native Spatializer for Unity.
* Added support for using OSP for FMOD with the FMOD Studio Unity Integration.
* Added support for using OSP for Wwise with the Wwise Unity Integration.
## API Changes

* Removed priority system and frequency hint from all OSPs.
* Added falloff range near/far to Unity Native OSP.
## Bug Fixes

* Wwise: Fixed potential crash bug in spatializer tail processing.
