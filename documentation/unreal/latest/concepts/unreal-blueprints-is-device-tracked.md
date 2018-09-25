---
title: Is Device Tracked
---
Determines whether or not a device (such as a controller) is being tracked by the sensors. 

## Overview

This blueprint determines whether or not a device (such as a controller) is being tracked by the sensors. You pass an argument, such as the Left Hand controller, and this Blueprint returns a boolean that is True if that device is being tracked by the sensors, and False otherwise. For example, if you are using Go and have associated the controller with the right hand, then calling this blueprint with the Right Hand argument will return True, but calling it with the Left Hand argument will return False. ## Blueprint

![](/images/documentation-unreal-latest-concepts-unreal-blueprints-is-device-tracked-0.png)  
## Arguments

* No Devices: Specifies that no devices should be checked to see if they are currently being tracked by the sensors. 
* HMD: Checks to see if the head position is being tracked by the sensors.
* Left Hand: Checks to see if the position of the controller associated with the left hand is being tracked by the sensors.
* Right Hand: Checks to see if the position of the controller associated with the right hand is being tracked by the sensors.
* All Hands: Checks to see if the position of any controller is being tracked by the sensors, regardless of whether that controller is associated with the left hand or right hand. So, if only one controller is being tracked, this Blueprint will return True. If two controllers are being tracked, this Blueprint will return True.
* Device Object Zero: Checks to see if a camera is being tracked by the sensors. An external camera is used by the mixed reality feature. In this scenario, the user attaches a Touch Controller to the camera, and the sensors then track the camera by tracking the Touch Controller. 
* All Devices: Checks to see if all available devices are being tracked by the sensors.
## Output

* Return Value: A boolean that is True if the specified device is being tracked by the sensors, and is False otherwise.
