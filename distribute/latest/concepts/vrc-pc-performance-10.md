---
title: VRC.PC.Performance.10
---
The app must not synchronize animation or physics to an assumed 90Hz frame rate.

**Required** - Yes

## Additional Details

Animations and physics synced to a fixed frame rate go out of sync when your app drops frames or when Asynchronous SpaceWarp is active.

## Steps to Test

1. Observe animation.
2. Use the [Oculus Debug Tool](/documentation/pcsdk/latest/concepts/dg-debug-tool/) to select Force 45 fps, ASW disabled.
3. Observe animation.
## Expected Result

Animations should continue to play at normal speed.

