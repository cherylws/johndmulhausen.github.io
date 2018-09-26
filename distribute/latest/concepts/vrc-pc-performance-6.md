---
title: VRC.PC.Performance.6
---

App displays graphics without significant systemic judder.

**Required** - Yes

## Additional Details

Asynchronous TimeWarp can help with minor rotational judder, but your application still needs to be at 90 FPS most of the time. You should disable Asynchronous SpaceWarp for performance testing because it can mask brief performance drops.

## Steps to Test

1. Launch the Oculus Debug Tool and open the [Lost Frame Capture](https://developer.oculus.com/documentation/pcsdk/latest/concepts/dg-performance-lostframes/) window.
2. Launch the title and click the Record button on the Lost Frame Capture window.
3. Put on the HMD and play through content for at least 45 minutes.
4. Stop recording and examine the capture result for frame rate and dropped frames.


## Expected Result

App runs at 90 FPS with no significant framerate drops (momentary drops are ok).
