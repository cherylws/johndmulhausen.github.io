---
title: 1.x Release Notes
---



The Oculus Remote Monitor client connects to mobile VR applications running on remote devices to capture, store, and display streamed-in data for performance evaluation and testing.

The Oculus Remote Monitor works with any Oculus mobile application built with Unity, Unreal Engine, or Native development tools.

For more information and usage instructions, please see the [Oculus Remote Monitor](/documentation/mobilesdk/latest/concepts/mobile-remote-monitor/#mobile-remote-monitor) page.

## Oculus Remote Monitor for PC and OS X 1.12

New Features

* OVRMonitor's new lost frame capture will now show a screenshot of any frames dropped during the capture session and information about the app performance at the time the frame was lost.


## Oculus Remote Monitor for PC and OS X 1.7

New Features

* Added a high-level Performance Overview. It plots a graphical summary of the VrAPI messages and error conditions against the timeline. Double-click any spot in the overview to open the Profiler Data and zoom in to that precise point in the timeline.


## Oculus Remote Monitor for PC and OS X 1.0.3

New Features

* CPU Scheduler events are now available on Galaxy S7.
* Added memory Allocation tracking. Every malloc/free can now be charted in the profiler view.
* Added Head Tracking graph.


Bug Fixes

* Fixed corrupt data streams that would happen on slow networks.
* Improved profiler view performance.
* Fixed miscellaneous bugs.


## Oculus Remote Monitor for PC and OS X 1.0.0

This is the initial stand-alone release. Release notes for earlier versions may be found in the [Mobile SDK Release Notes](/documentation/mobilesdk/latest/concepts/release-archive/).

New Features

* VR Developer Mode is no longer required if you have System Activities 1.0.2 or greater and an app built with Oculus Mobile SDK 1.0 or greater.
* Added experimental layer texel density and complexity visualizers (supported by apps built with Oculus Mobile SDK 1.0 or later).
* Improved network stability on Windows.
* Now available as a separate downloadable package from the full Mobile SDK download.

