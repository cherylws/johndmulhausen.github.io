---
title: DAW-Specific Notes
---
This section discusses DAW-specific caveats and issues for the Oculus Spatializer Plugin.

The Oculus Spatializer DAW plugin is a full stereo effect (Left/Right in, Left/Right out). It will only process the incoming Left channel and allow you to move this monophonic signal through 3D space. Some DAWs will work properly when assigning a stereo effect to a monophonic channel, while others will require workarounds.

Up to 64 sounds running through the bus may be spatialized.

DAWWindowsOS XAdditional NotesAbleton Live 9.1.7Yes  Adobe Audition 8.1YesYes PreSonus Studio One 2.6.5Partial Mono track not supported. Use a stereo track; the plugin will collapse channels to mono automatically. You may also send the mono track to the plugin as a send/return effect instead of as an insert effect.Reaper 6.5Yes Multicore usage must be turned off when rendering out an ambisonic stream. This can be set by navigating to: Options > Preferences > Buffering

and setting Audio reading/processing threads to 0.

Steinberg Nuendo 6.5 / Steinberg Cubase 8Partial Placing a stereo insert effect onto a mono track is not supported. Solution 1) Place your mono sound on a stereo track, with the OSP as an insert effect. Solution 2) Convert your mono source into a stereo source. Currently, the left channel of the source will be affected; there is no right channel selection or stereo to mono collapse feature in the plugin. Solution 3) Use a stereo send from a mono source.