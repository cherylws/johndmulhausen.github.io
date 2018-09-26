---
title: Audio SDK 1.1 Release Notes
---

This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Audio SDK.

## 1.1.5

## New Features

* Added near-field rendering for more realistic spatialization of sound sources closer than 1 meter.
* Added volumetric rendering to sound sources to support sound emanating from a spherical volume instead of a point-source. Set to 0m to render a point-source.
* Added new virtual speaker mode to decode ambisonics as an array of eight point-sourced and spatialized speakers, each located at the vertex of a cube located around the listener.
* In Wwise, the 3D position editor can now be used to preview spatialization.
* VST Plugin
	+ Added a recording mode to render the spatialized soundscape to an AmbiX .wav file.
	+ Added mouse support to the 2D view to move sound sources around.
	+ Moved several options from the About dialog box to the Config dialog box.
	+ You can now label a sound source for easy identification as well as change its color from the Config dialog box.
	
* Added beta ambisonic playback support for Unity version 2017.1 beta.


## Bug Fixes

* Fixed an issue that could corrupt shared data when running DAWS on a multi-core computer system.
* Fixed an issue that could create spurious error messages in Steinberg Nuendo.


## 1.1.4

## Bug Fixes

* Fixed issue causing spatializer to sometimes fail to initialize and output silence. This issue affected all middleware/engines and platforms.


## 1.1.3

The 1.1.3 release includes bug fixes for the FMOD and Wwise plugins.

Our FMOD spatializer plugin now requires on FMOD Studio version 1.08.16 or later.

## Bug Fixes

* FMOD 
	+ Fixed incorrect listener position, which sometimes caused â€œglitchy" sound.
	+ Added workaround for FMOD issue with not releasing DSP instances. This would sometimes cause sound to drop out.
	
* WWISE 
	+ Fixed issue with Shared Attenuation Range parameters not being written to sound banks correctly.
	


## 1.1.2

The 1.1.2 release includes minor bug fixes and logging changes.

## New Features

* Added more detailed error log messages for setting Shared Reverb Range parameters.


## Bug Fixes

* FMOD
	+ Fixed inverse solving of listener coordinates. 
	+ Increased "inside head" zone where sound is placed in front of listener. Sounds closer than 1 cm to the center of the head are placed in front to prevent glitches where sound jumps from side to side due to floating point error (exhibited in FMOD plugin reverse solving listener coordinates).
	+ Fixed incorrect audio output from OSP when FMOD Studio project is set to surround output (i.e., 5.1) rather than stereo.
	+ Fixed Shared Reverb Min/Max range parameter values not being set correctly.
	


## 1.1.1

The 1.1.1 release adds an updated version of the Oculus Native Spatializer Plugin for Unity and minor bug fixes.

## Bug Fixes

* Unity ONSP: Version 1.0.4 of the Unity ONSP was inadvertently included with release 1.1.0. Audio SDK 1.1.1 includes the latest plugin.
* Wwise: SDK now always sets Min/Max attachment parameter values. This allows reflection values to be modified even if we are using Wwise to author direct curve.
* AAX and VST for DAWs: Visualizer now only updates listener position when HMD is mounted/worn. 


## 1.1.0

## Overview of Major Changes

The 1.1 release includes major improvements to the Audio SDK and some big new features, including Ambisonics support, shared reverb, and attenuation controls. It also includes tweaks to the HRTF to flatten frequency response and improve spatialization. The VST and AAX plugins now feature 3D Audio Visualizers allowing users to visualize and manipulate sound parameters within VR.

We have discontinued the Legacy Audio Spatializer for Unity 4. If you still need that plugin, it is still available with Audio SDK v1.0.4 on the [Downloads page](/downloads/) page - select the Audio category and version 1.0.4 to download.

The Oculus Spatializer for FMOD has been renamed OculusSpatializerFMOD.dll, and the Oculus Spatializer for Wwise has been renamed the OculusSpatializerWwise.dll.

## New Features

* Wwise and FMOD: Added Ambisonics spatialization support using spherical harmonic-based rendering to provide accurate reproduction of Ambisonics. For more information, see the *Oculus Ambisonics* section of the [Supported Features](/documentation/audiosdk/latest/concepts/audiosdk-features/#audiosdk-features-supported "This section describes supported features.") section of our Audio SDK Guide.
* Added shared reverb to FMOD, Wwise, and Unity plugins, moving all reverb processing to a single effect for more efficient processing.
* Added Attenuation Range min/max, providing control over internal attenuation model used for early reflections. This allows better distance simulation, as the authored curve can match the internal curve, meaning reflections fall off naturally.
* AAX and VST: added 3D Audio Visualizer with HMD interface, allowing users to visualize and manipulate sound parameters within VR using Oculus Touch or Xbox controllers. For more information, see [3D Visualizer](/documentation/audiosdk/latest/concepts/os-aax-visualizer/ "This guide describes how to install and use the Oculus Spatializer AAX plugin with the Oculus Rift.") (AAX) and [3D Visualizer](/documentation/audiosdk/latest/concepts/os-vst-visualizer/ "This guide describes how to install and use the Oculus Spatializer VST plugin with the Oculus Rift.") (VST).
* Added visual representation of Room Model to Unity Native plugin.


## API Changes

* Moved all FMOD global settings to Oculus Spatial Reverb effect.
* Oculus Spatializer for FMOD has been renamed OculusSpatializerFMOD.dll.
* Oculus Spatializer for Wwise has been renamed the OculusSpatializerWwise.dll.
* Renamed several parameters for consistency across plugins.
* Removed OculusFMODSpatializerSettings.h from FMOD Plugin. All values are now available through the Oculus Spatializer.
* Deprecated OvrFMODGlobalSettings.cs from FMOD Plugin.
* Added Bypass Spatializer option to Wwise Plugin.
* Renamed Disable Reflections to Enable Reflections in FMOD, Wwise, and Unity plugins, inverted logic.
* Removed Legacy Audio Spatializer for Unity 4.


## Known Issues

* Unity ONSP: Version 1.0.4 of the Unity ONSP was inadvertently included in this release. Version 1.1.x will be released soon. 
* FMOD Studio 1.8.xx: Putting the Oculus Ambisonics on the event master track does not provide optimal results. FMOD interprets the 4 channel ambisonics as quadraphonic and automatically up-mixes to 5.1 at the track output. To work around this issue:
	+ Put the Oculus Ambisonics effect on the audio track so it has 4 channel input, **OR**
	+ Set the project to 5.1 speaker mode and manually convert the 4 channel B-Format to 5.1 by leave channels 3 (center) and 4 (LFE) silent to prevent automatic upmix.
	
* **Gear VR developers** using Unity 5.3.4 or later, or using Unity 5.4.0b16 and later: Do not set *DSP Buffer Size* to *Best* in *Audio Manager* in the Inspector for now or you will encounter audio distortion. Set it to *Good* or *Default* instead.

