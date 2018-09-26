---
title: VRC.Mobile.Performance.2
---

The app displays graphics without judder.

**Required** - Yes

## Additional Details

Asynchronous Timewarp can help with minor rotational judder, but your application still needs to be at 60 FPS most of the time.

## Steps to Test

1. Play through several levels of the application.
2. Observe the graphics throughout for choppiness or smearing.


## Expected Result

Application should not experience extended periods of framerate below the target framerate. On Gear, the target framerate is 60 FPS. On Oculus Go, the target may be either 60 or 72 FPS. Exceptions include when there's a black screen or during loading scenes.
