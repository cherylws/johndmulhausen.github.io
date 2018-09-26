---
title: Blueprints Reference
---

This section serves as a reference guide for the Blueprints in the Online Subsystem Oculus library. 

To access these Blueprints, you must enable the **Online Subsystem Oculus** in **Edit &gt; Plugin &gt; Online Platform.**

**User and Account Blueprints**

* **[Get Device Name](/documentation/unreal/latest/concepts/unreal-blueprints-get-device-name/)**  
Returns the current device's name.
* **[Get User Profile](/documentation/unreal/latest/concepts/unreal-blueprints-get-user-profile/)**  
 Returns current user profile.


**Splash Screen Blueprints**

* **[Add Loading Splash Screen](/documentation/unreal/latest/concepts/unreal-blueprints-add-loading-splash-screen/)**  
Adds a splash screen with parameters to the application.
* **[Clear Loading Splash Screens](/documentation/unreal/latest/concepts/unreal-blueprints-clear-loading-splash-screen/)**  
Removes all splash screens from the application. 
* **[Enable Auto-Loading Splash Screen](/documentation/unreal/latest/concepts/unreal-blueprints-enable-auto-loading-splash-screen/)**  
Enables/disables the splash screen to be automatically shown when loading a new level. 


**Position and Orientation Blueprints**

* **[Enable Orientation Tracking](/documentation/unreal/latest/concepts/unreal-blueprints-enable-orientation-tracking/)**  
Enables or disables orientation tracking.
* **[Enable Position Tracking](/documentation/unreal/latest/concepts/unreal-blueprints-enable-position-tracking/)**  
Enables or disables positional tracking.
* **[Get Base Rotation and Base Offset in Meters](/documentation/unreal/latest/concepts/unreal-blueprints-get-base-rotation-and-base-offset-in-meters/)**  
Returns the current rotation and position of the headset, with respect to the base rotation and position, expressed in meters.
* **[Get Pose](/documentation/unreal/latest/concepts/unreal-blueprints-get-pose/)**  
Returns the orientation and position (if available) for the headset.
* **[Get Raw Sensor Data](/documentation/unreal/latest/concepts/unreal-blueprints-get-raw-sensor-data/)**  
Reports raw sensor data from the headset. 
* **[Is Device Tracked](/documentation/unreal/latest/concepts/unreal-blueprints-is-device-tracked/)**  
Determines whether or not a device (such as a controller) is being tracked by the sensors. 
* **[Set Base Rotation and Base Offset in Meters](/documentation/unreal/latest/concepts/unreal-blueprints-set-base-rotation-and-base-offset-in-meters/)**  
Specifies the current rotation and position of the headset, with respect to the base rotation and position, expressed in apparent meters.
* **[Set Reorient HMD On Controller Recenter](/documentation/unreal/latest/concepts/unreal-blueprints-set-reorient-hmd-on-controller-recenter/)**  
Sets the HMD recenter behavior.


**Guardian Blueprints**

* **[Get Guardian Dimensions](/documentation/unreal/latest/concepts/unreal-blueprints-get-guardian-dimensions/)**  
Returns the dimensions of the Outer Boundary or the Play Area, expressed in UE4 units.
* **[Get Guardian Points](/documentation/unreal/latest/concepts/unreal-blueprints-get-guardian-points/)**  
Returns the points, in UE4 world space, that define the Outer Boundary or the Play Area.
* **[Get Node Guardian Intersection](/documentation/unreal/latest/concepts/unreal-blueprints-get-node-guardian-intersection/)**  
Returns the intersection result between a tracked device (HMD or Controller) and the Guardian boundary.
* **[Get Play Area Transform](/documentation/unreal/latest/concepts/unreal-blueprints-get-play-area-transform/)**  
Returns the transform of the Play Area rectangle, defining it's position, rotation, and scale to apply a unit cube to match it with the Play Area.
* **[Get Point Guardian Intersection](/documentation/unreal/latest/concepts/unreal-blueprints-get-point-guardian-intersection/)**  
Returns the intersection result between the Oculus Guardian boundary and a specified UE4 coordinate.
* **[Is Guardian Displayed](/documentation/unreal/latest/concepts/unreal-blueprints-is-guardian-displayed/)**  
Returns a boolean result that indicates whether or not the Outer Boundary Guardian is being displayed.
* **[Set Guardian Visibility](/documentation/unreal/latest/concepts/unreal-blueprints-set-guardian-visibility/)**  
Specifies whether or not the runtime should render the Guardian.


**Dash Blueprints**

* **[Has Input Focus](/documentation/unreal/latest/concepts/unreal-blueprints-has-input-focus/)**  
Determines whether or not the application has input focus.
* **[Has System Overlay Present - DEPRECATED](/documentation/unreal/latest/concepts/unreal-blueprints-has-system-overlay-present/)**  



**Mixed Reality Blueprints**

* **[Get All Tracked Cameras](/documentation/unreal/latest/concepts/unreal-blueprints-get-all-tracked-camera/)**  
Retrieves an array of all calibrated and tracked cameras, which were calibrated through the camera tool.


**Performance Optimization Blueprints**

* **[Get Available Display Frequencies](/documentation/unreal/latest/concepts/unreal-blueprints-get-available-display-frequencies/)**  
Returns the display frequencies that are available with the current headset. 
* **[Get Current Display Frequency](/documentation/unreal/latest/concepts/unreal-blueprints-get-current-display-frequency/)**  
Returns the current display frequency for the connected HMD.
* **[Get GPU Frame Time](/documentation/unreal/latest/concepts/unreal-blueprints-get-gpu-frame-time/)**  
Returns the amount of time that the GPU spent rendering the most recent frame.
* **[Get GPU Utilization](/documentation/unreal/latest/concepts/unreal-blueprints-get-gpu-utilization/)**  
Returns the CPU utilization availability and value.
* **[Get Tiled Multires Level](/documentation/unreal/latest/concepts/unreal-blueprints-get-tiled-multires-level/)**  
 Returns the current multi-resolution level, which applies to fixed foveated rendering.
* **[Set CPU and GPU Levels](/documentation/unreal/latest/concepts/unreal-blueprints-set-cpu-and-gpu-levels/)**  
Sets the clock rates for the CPU and GPU on mobile devices.
* **[Set Display Frequency](/documentation/unreal/latest/concepts/unreal-blueprints-set-display-frequency/)**  
Sets the display frequency (frame rate) for Oculus Go to either 60 Hz or 72 Hz.
* **[Set Tiled Multires Level](/documentation/unreal/latest/concepts/unreal-blueprints-set-tiled-multires-level/)**  
Sets the multi-resolution level for fixed foveated rendering.

