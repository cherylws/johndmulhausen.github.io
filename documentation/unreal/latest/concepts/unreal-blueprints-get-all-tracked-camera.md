---
title: Get All Tracked Cameras
---
Retrieves an array of all calibrated and tracked cameras, which were calibrated through the camera tool.

## Overview

This is a mixed reality function. It is only available in versions of the Oculus Unreal integration that you obtain directly from Oculus (not from Epic). 

This Blueprint retrieves an array of variables of type FTrackedCamera, where each entry in the array represents a camera in the physical world. These are the cameras that are setup to capture video streams which are then played within the virtual world, in order to create a form of mixed reality.

## Blueprint

![](/images/documentation-unreal-latest-concepts-unreal-blueprints-get-all-tracked-camera-0.png)  
## Arguments

* Calibrated Only: Specifies to return only calibrated cameras or all cameras (regardless of calibration status). 
## Output

* Tracked Cameras: An array of variables of type FTrackedCamera, where each FTrackedCamera represents a camera in the physical world: FTrackedCamera() : Index(-1) , Name(TEXT("Unknown")) , FieldOfView(90.0f) , SizeX(1280) , SizeY(720) , AttachedTrackedDevice(ETrackedDeviceType::None) , CalibratedRotation(EForceInit::ForceInitToZero) , CalibratedOffset(EForceInit::ForceInitToZero) , UserRotation(EForceInit::ForceInitToZero) , UserOffset(EForceInit::ForceInitToZero)
