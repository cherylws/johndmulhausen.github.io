---
title: Get Base Rotation and Base Offset in Meters
---

Returns the current rotation and position of the headset, with respect to the base rotation and position, expressed in apparent meters.

## Overview

The base offset is the translational difference between the current position of the headset and the base position, that was most recently set by using [Set Base Rotation and Base Offset in Meters](/documentation/unreal/latest/concepts/unreal-blueprints-set-base-rotation-and-base-offset-in-meters/). It is expressed as a vector that translates the headset position into the (0,0,0) point, in meters. The axes of the vector are the same as for Unreal: X is forward, Y is right, Z is up.

Similarly, the base rotation offset is the rotational difference between the current rotation of the headset and the base rotation, that was most recently set by using [Set Base Rotation and Base Offset in Meters](/documentation/unreal/latest/concepts/unreal-blueprints-set-base-rotation-and-base-offset-in-meters/). It is expressed as an FRotator object with properties Pitch, Roll, and Yaw.

When the user recenters the headset from the original center of the tracking space, the base offset is the delta from the center of the tracking space to the new center of the game space (or "world space"). 

This blueprint expresses its values in meters. In each UE4 world, you can define the scale factor of the world, which scales everything in the world consistently. By default, the scale factor is 100, which means values are expressed in centimeters instead of meters. But you can use any scale factor you wish, for example when loading splash screens. 

## Blueprint

![](/images/documentationunreallatestconceptsunreal-blueprints-get-base-rotation-and-base-offset-in-meters-0.png)

## Arguments

* No arguments.


## Output

* Out Rotation: The rotational difference between the current rotation of the headset and the base rotation, that was most recently set by using [Set Base Rotation and Base Offset in Meters](/documentation/unreal/latest/concepts/unreal-blueprints-set-base-rotation-and-base-offset-in-meters/ "Specifies the current rotation and position of the headset, with respect to the base rotation and position, expressed in apparent meters."). It is expressed as an FRotator construct with properties Pitch, Roll, and Yaw.
* Out Base Offset in Meters: The translational difference between the current position of the headset and the base position, that was most recently set by using [Set Base Rotation and Base Offset in Meters](/documentation/unreal/latest/concepts/unreal-blueprints-set-base-rotation-and-base-offset-in-meters/ "Specifies the current rotation and position of the headset, with respect to the base rotation and position, expressed in apparent meters."). It is expressed as an FVector construct that translates the headset position into the (0,0,0) point, in meters.

