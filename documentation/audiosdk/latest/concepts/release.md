---
title: Audio SDK 1.29 Release Notes
---
This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Audio SDK.

## 1.29.0

## New Features

* **Wwise Version Support**: 
	+ Wwise 2015 support has been DEPRECATED.
	+ Wwise 2016 support remains the same.
	+ Wwise 2017.2 is now supported, in addition to Wwise 2017.1 (which was previously supported). Separate builds are provided for 2017.1 and 2017.2. If you are using Wwise 2017.x, you must match it with the correct build.
	+ Wwise 2018.1 support has been added.
	
* **Decoupling of early reflections and late reverb**: Early reflections have now been decoupled from late reverb. Previously, reverb could only be turned on if reflections were on. Now, you can use any possible combination of reflections and reverb. This allows for room modeling on lower-spec platforms (including Oculus Go) where much of the time spent in the modeling phase is in the early reflections. The reverb portion results in a more-or-less a fixed CPU hit, so turning that on and disabling early reflections can help to keep the CPU budget in check. 
## Bug Fixes

*  There are not bug fixes in this release.
## API Changes

* There are no breaking API changes in this release.
