---
title: VRC.PC.Performance.9
---

The app should render head-locked UI elements in a compositor layer to avoid judder if the app misses frames or runs with Asynchronous SpaceWarp.

**Required** - Yes

## Additional Details

VR compositor layers update independent of the app frame rate. See [VR Compositor Layers](/documentation/unity/latest/concepts/unity-ovroverlay/).

## Steps to Test

1. Use [Oculus Debug Tool](https://developer.oculus.com/documentation/pcsdk/latest/concepts/dg-debug-tool/) to disable Asynchronous SpaceWarp (ASW).
2. Look for judder in headlocked elements.


## Expected Result

Objects should look just as smooth as if the app is running at 90 FPS.
