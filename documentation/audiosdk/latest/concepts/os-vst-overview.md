---
title: Overview
---
The Oculus Spatializer VST plugin for professional Digital Audio Workstations (DAWs) lets you spatialize monophonic sound sources in 3D relative to the user's head location and preview the soundscape. You can also record the mix to an ambisonic stream for later use. 

The VST plugin incorporates the same spatialization algorithms found in our other plugin formats (Wwise, FMOD, and Unity). These other formats are typically used to generate real-time spatialization within virtual environments. For the audio designer, the VST plugin comes in handy for setting up mixes within your favorite DAW, and for previewing what the mix sounds like prior to being spatialized in virtual reality.

## Version Compatibility

This VST has been tested with various DAWs on Windows 7 and 8.1 (32-bit and 64-bit) and Mac OS X 10.8.5+. For more information, please see [DAW-Specific Notes](/documentation/audiosdk/latest/concepts/os-vst-daw/ "This section discusses DAW-specific caveats and issues for the Oculus Spatializer Plugin.").

## General OSP Limitations

1. CPU usage increases when early reflections are turned on, and increases proportionately as room dimensions become larger.
## Limitations Specific to VST

* All parameters are assigned to MIDI controllers. However, most parameter ranges fall outside of the current MIDI mapping range of 0.0 - 1.0. Range settings for each parameter will be resolved in a future release of the plugin. 
* Please see [DAW-Specific Notes](/documentation/audiosdk/latest/concepts/os-vst-daw/ "This section discusses DAW-specific caveats and issues for the Oculus Spatializer Plugin.") for information about each DAW tested with the spatializer.
* You must set your DAW sample rate to be at 44.1 kHz or 48 kHz for optimal fidelity. Note that values below 16 kHz or above 48 kHz will result in no sound.
## Installation

Download the **Oculus Spatializer DAW Mac** or **Oculus Spatializer DAW Win** package from the [Audio Packages](/downloads/audio/) page.

Copy the relevant VST files to your system or to your DAW's VST installation directory.

## PC

On Windows, some DAWs require you to specify custom locations for 32-bit and 64-bit VST plugins. If you have not already setup custom locations for your VST folders, we recommend using the following:

64-bit

C:\Program Files\Steinberg\VSTPlugins

32-bit

C:\Program Files (x86)\Steinberg\VSTPlugins

## Mac

In OS X, VST plugins must be installed to either the global or user Library folder.

Global

/Library/Audio/Plug-Ins/VST

User

~/Library/Audio/Plug-Ins/VST

