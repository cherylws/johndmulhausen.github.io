---
title: VRC.PC.Performance.2
---
App must display graphics in the headset at 90 frames per second on Nvidia 970 GPU running Windows 7.

**Required** - Yes

## Additional Details

It is acceptable for performance to drop below 90 if you have a compositor layer/TimeWarp layer/loading screen.

## Steps to Test

1. Launch the Oculus Debug Tool and open the [Lost Frame Capture](/documentation/pcsdk/latest/concepts/dg-performance-lostframes/) window.
2. Launch the title and click the Record button on the Lost Frame Capture window.
3. Put on the HMD and play through content for at least 45 minutes.
4. Stop recording and examine the capture result for frame rate and dropped frames.
## Expected Result

App runs at 90 FPS with no significant framerate drops (momentary drops are ok).

