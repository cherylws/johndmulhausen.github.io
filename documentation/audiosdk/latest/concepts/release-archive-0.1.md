---
title: Audio SDK 0.10 Release Notes
---
This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Audio SDK.

## 0.10.2

## Overview of Major Changes

The Oculus Audio SDK consists of a set of plugins for popular middleware and engines; the Oculus Spatializer VST plugin for content authors; and documentation to assist developers that want to incorporate realistic spatialized audio in their VR-enabled applications and games.

Currently the Oculus Audio SDK supports Mac, Windows, and mobile platforms, and provides integrations with:

* FMOD (Windows, Mac and mobile)
* Audiokinetic Wwise (Windows)
* Unity 4.6 and later (Windows, Mac, and mobile)
The optional OVRAudio C/C++ SDK is available to qualified developers by contacting developer support directly.

## New Features

* Unity Plugin
	+ Works with Unity 4 Free.
	+ Defaults to 'slow' audio path for reliability.
	
* Wwise plugin
	+ Removed dependency on VS2013 CRTL.
	
* FMOD plugin
	+ Significant crash bug/reliability improvements.
	+ Added Mac support.
	+ Removed dependency on VS2013 CRTL.
	
* VST
	+ Finalized user interface.
	+ Now available for Mac.
	
* OVRAudio (internal only)
	+ Changed from bool returns to error code returns.
	+ Added debug output.
	+ Added 16 kHz support.
	+ Removed Bass Boost option.
	
## API Changes

* OVRAudio (internal only)
	+ Added ovrAudio\_SetAudioSourcePropertyf().
	+ Added ovrAudio\_SetUserConfig().
	
## Bug Fixes

* Unity plugin
	+ Removed AndroidManifest, which was causing conflicts with user's existing manifests.
	+ Fixed various bugs.
	
* Wwise plugin
	+ Fixed various crash bugs.
	
## Known Issues

* This is still a preview release, so expect a lot of bugs and other minor issues!
