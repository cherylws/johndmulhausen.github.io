---
title: VRC.PC.Performance.8
---
App must render without visible z-fighting or depth conflict artifacts.

**Required** - Yes

## Additional Details

There must not be any z-fighting flickering amongst coplanar polygons.

## Steps to Test

1. Launch the title.
2. Play through content for at least 45 minutes.
## Expected Result

Objects should render normally. Examples of failure include objects appearing to flicker back and forth, colliding because they think they're at the same depth.

