---
title: Overview
---
The Oculus Spatializer Plugin (OSP) is an add-on plugin for the Audiokinetic Wwise tool set that allows monophonic sound sources to be spatialized in 3D relative to the user's head location. This integration guide describes how to install and use OSP in both the Wwise application and the end-user application.

## Version Compatibility

Download the **Oculus Spatializer Wwise** package from the [Audio Packages](/downloads/audio/) page.

## Download Package Contents

The download package contains the following folders:

* Wwise2016 Files for Wwise 2016.x, tested against Wwise 2016.1 on Windows and MacOS. 
	+ Android - library file to add to Android apps.
	+ Include - header file and sample code to integrate Wwise into a Windows app.
	+ Mac - library file to add to macOS apps.
	+ Win32 - library file for macOS Wwise Authoring Tool and 32-bit Windows Wwise Authoring tool and apps.
	+ x64 - library file for 64-bit Windows Wwise Authoring Tooland apps.
	
* Wwise2017 - Files for Wwise 2017.x, tested against Wwise 2017.1 and 2017.2 on Windows. 
	+ Include - header file and sample code to integrate Wwise into a Windows app.
	+ Win32 - library file for 32-bit Windows Wwise Authoring Tool and apps.
	+ x64 - library file for 64-bit Windows Wwise Authoring Tool and apps.
	
The Include folder contains OculusSpatializer.h, which is used to integrate Wwise into a Windows app. It contains important registration values that the app must use to register OSP within Wwise. The header file also includes (commented out) source code that shows how to register the plugin with the Wwise run-time.

## General OSP Limitations

1. CPU usage increases when early reflections are turned on, and increases proportionately as room dimensions become larger.
## Limitations Specific to Wwise Integration

* The plugin may only be added to one bus. If you add the plugin to a second bus, you may experience some unwanted noise on the audio output.
