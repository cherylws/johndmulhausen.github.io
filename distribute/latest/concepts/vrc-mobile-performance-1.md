---
title: VRC.Mobile.Performance.1
---

The app displays graphics in the headset at 60 frames per second.

**Required** - Yes

## Additional Details

For information on performance debugging and best practices, see [ Squeezing Performance out of your Unity Gear VR Game Part 1 ](/blog/squeezing-performance-out-of-your-unity-gear-vr-game) and [ Part 2 ](/blog/squeezing-performance-out-of-your-unity-gear-vr-game-continued).

## Steps to Test

1. Use the app for the length of the content or 45 minutes, whichever is shorter.
2. Launch the [OVR Metrics](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-ovrmetricstool/) tool and select the log file for your app.
3. Observe the FPS graph.


## Expected Result

Application should not experience extended periods of framerate below 60 FPS. Exceptions include when there's a black screen or during loading scenes.
