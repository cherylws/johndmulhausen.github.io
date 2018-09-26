---
title: Overview
---

The Audio SDK Profiler provides real-time statistics and metrics to track audio performance in apps that use Oculus Spatializer plugins.

The profiler collects analytics from an analytics server embedded within every Oculus Spatializer plugin (OSP). You can profile audio performance in both VR and non-VR applications, either running locally or remotely.

## Limitations

* Analytics are only available for Unity, Wwise, FMOD, and Native OSP versions 1.18 or later. 
* Remote profiling requires both nodes to be in the same subnet of the local area network.
* Profiling mobile or Gear VR apps requires a Wi-Fi connection.
* Port 2121 is the default port for the OSP server. To change the port, you must edit your OSP settings and then rebuild. See &lt;/documentation/audiosdk/latest/concepts/audio-profiler-setup/#activatingprofiling&gt;.

