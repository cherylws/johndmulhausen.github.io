---
title: Get Pose
---
Returns the orientation and position (if available) for the headset.

## Overview

This blueprint returns the current orientation and position for the headset. 

## Blueprint

![](/images/documentation-unreal-latest-concepts-unreal-blueprints-get-pose-0.png)  
## Arguments

* Use Orientation for Player Camera: Set this to True to specify that the orientation should be used to update orientation of the camera manually.
* Use Position for Player Camera: Set this to True if the position is going to be used to update position of the camera manually. 
* Position Scale: The 3D scale factor that will be applied to the position values before they are returned.
## Output

* Device Rotation: The device's current rotation. 
* Device Position: The device's current position, in its own tracking space. If positional tracking is not available, this value will be a zero vector.
* Neck Position: The estimated neck position, calculated using the NeckToEye vector from the User Profile. This value is expressed in the same coordinate space as Device Position. 
