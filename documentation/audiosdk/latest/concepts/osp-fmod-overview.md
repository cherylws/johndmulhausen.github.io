---
title: Overview
---
The Oculus Spatializer Plugin (OSP) is an add-on plugin for FMOD Studio for Windows and Mac OS X that allows monophonic sound sources to be properly spatialized in 3D relative to the user's head location. This plugin requires FMOD Studio version 1.08.16 or later. 

This integration guide outlines how to install and use the OSP in both FMOD Studio and the end-user application.

## General OSP Limitations

1. CPU usage increases when early reflections are turned on, and increases proportionately as room dimensions become larger.
## Adding the OSP to your project in FMOD Studio 1.07.00 and later

Download the **Oculus Spatializer FMOD** package from the [Audio Packages](/downloads/audio/) page.

Windows:

1. Navigate to the folder AudioSDK\Plugins\FMOD\x64.
2. Add the 64-bit version of OculusSpatializerFMOD.dll to Program Files\FMOD SoundSystem\FMOD Studio <version>\plugins.
macOS

1. Ctrl-click (right-click) on FMOD Studio.app and select *Show Package Contents*.
2. Copy libOculusSpatializerFMOD.dylib from AudioSDK/Plugins/FMOD/mcub to FMOD Studio.app/Contents/Plugins.
## Adding the OSP to your project in earlier versions of FMOD

Windows:

1. Navigate to the folder AudioSDK\Plugins\FMOD\Win32.
2. Copy the 32-bit OculusSpatializerFMOD.dll into the *Plugins* directory in your FMOD Studio project directory. (Create this directory if it does not already exist.)
macOS

1. Navigate to the folder AudioSDK/Plugins/FMOD/macub.
2. Copy libOculusSpatializerFMOD.dylib into the *Plugins* directory in your FMOD Studio project directory. (Create this directory if it does not already exist.).
