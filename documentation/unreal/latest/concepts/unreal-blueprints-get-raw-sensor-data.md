---
title: Get Raw Sensor Data
---

Reports raw sensor data from the headset. 

## Overview

This blueprint reports raw sensor data from the headset, such as its angular acceleration or linear velocity. If the headset does not support a sensor data reading, then that result will return as zero.

## Blueprint

![](/images/documentationunreallatestconceptsunreal-blueprints-get-raw-sensor-data-0.png)

## Arguments

* No Devices: Specifies that sensor data should be not be returned for any devices that are currently being tracked by the sensors. 
* HMD: Specifies that sensor data should be returned for the HMD that is being tracked by the sensors.
* Left Hand: Specifies that sensor data should be returned for the controller associated with the left hand is being tracked by the sensors.
* Right Hand: Specifies that sensor data should be returned for the controller associated with the right hand is being tracked by the sensors.
* All Hands: Specifies that sensor data should be returned for the controller that is being tracked by the sensors, regardless of whether that controller is associated with the left hand or right hand. So, if only one controller is being tracked, this Blueprint will return True. If two controllers are being tracked, this Blueprint will return True.
* DeviceObject Zero: Specifies that sensor data should be returned for the camera is being tracked by the sensors. An external camera is used by the mixed reality feature. In this scenario, the user attaches a Touch Controller to the camera, and the sensors then track the camera by tracking the Touch Controller. 
* All Devices: Specifies that sensor data should be returned for all available devices are being tracked by the sensors.


## Output

* Angular Acceleration: Angular acceleration in radians per second per second.
* Linear Acceleration: Acceleration in meters per second per second.
* Angular Velocity: Angular velocity in radians per second.
* Linear Velocity: Velocity in meters per second.
* Time in Seconds: Time when the reported Inertial Measurement Unit (IMU) reading took place, in seconds.

