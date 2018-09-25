---
title: Overview
---
The Oculus Spatializer AAX plugin is an add-on plugin for Avidâ€™s Pro Tools audio production platform. 

This plugin allows for monophonic sound sources to be properly spatialized in 3D relative to the user's head location. 

The AAX plugin incorporates the same spatialization algorithms found in our other plugin formats (e.g., Wwise, Unity). These other formats are typically used to generate real-time spatialization within virtual environments. For the audio designer, the AAX plugin is useful for setting up mixes within the Pro Tools DAW (Digital Audio Workstation) and for hearing what the mix will sound like prior to being spatialized in virtual reality.

## Version Compatibility

The AAX plugin has been tested in Pro Tools 11 (64-bit) on Windows 7 and 8, and OS X 10.10+.

## General OSP Limitations

1. CPU usage increases when early reflections are turned on, and increases proportionately as room dimensions become larger.
## Limitations Specific to AAX

* All parameters are assigned to MIDI controllers. However, most parameter ranges fall outside of the current MIDI mapping range of 0.0 - 1.0. Range settings for each parameter will be resolved in a future release of the plugin. 
* You must set the Pro Tools sample rate to be at 44.1 kHz or 48 kHz for optimal fidelity. Note that values below 16 kHz or above 48 kHz will result in no sound.
## Installation

Download the **Oculus Spatializer DAW Mac** or **Oculus Spatializer DAW Win** package from the [Audio Packages](/downloads/audio/) page.

Copy Oculus Spatializer.aaxplugin to the Avid Pro Tools Plug-Ins folder.

On a Mac:

Macintosh HD/Library/Application Support/Avid/Audio/Plug-Ins On a PC:

C:\Program Files\Common Files\Avid\Audio\Plug-Ins