---
title: Initialization and Sensor Enumeration
---
This example initializes LibOVR and requests information about the available HMD.

Review the following code:

 // Include the OculusVR SDK #include <OVR\_CAPI.h> void Application() { ovrResult result = ovr\_Initialize(nullptr); if (OVR\_FAILURE(result)) return; ovrSession session; ovrGraphicsLuid luid; result = ovr\_Create(&session, &luid); if (OVR\_FAILURE(result)) { ovr\_Shutdown(); return; } ovrHmdDesc desc = ovr\_GetHmdDesc(session); ovrSizei resolution = desc.Resolution; ovr\_Destroy(session); ovr\_Shutdown(); } As you can see, ovr\_Initialize is called before any other API functions and ovr\_Shutdown is called to shut down the library before you exit the program. In between these function calls, you are free to create HMD objects, access tracking state, and perform application rendering.

In this example, ovr\_Create(&session &luid) creates the HMD. Use the LUID returned by ovr\_Create() to select the IDXGIAdapter on which your ID3D11Device or ID3D12Device is created. Finally, ovr\_Destroy must be called to clear the HMD before shutting down the library.

You can use ovr\_GetHmdDesc() to get a description of the HMD.

If no Rift is plugged in, ovr\_Create(&session, &luid) returns a failed ovrResult unless a virtual HMD is enabled through RiftConfigUtil. Although the virtual HMD will not provide any sensor input, it can be useful for debugging Rift-compatible rendering code and for general development without a physical device.

The description of an HMD (ovrHmdDesc) handle can be retrieved by calling ovr\_GetHmdDesc(session). The following table describes the fields:

FieldTypeDescriptionTypeovrHmdTypeType of the HMD, such as ovr\_DK2 or ovr\_DK2 .ProductNamechar[]Name of the product as a string.Manufacturerchar[]Name of the manufacturer.VendorIdshortVendor ID reported by the headset USB device.ProductIdshortProduct ID reported by the headset USB device.SerialNumberchar[]Serial number string reported by the headset USB device.FirmwareMajorshortThe major version of the sensor firmware.FirmwareMinorshortThe minor version of the sensor firmware.AvailableHmdCapsunsigned intCapability bits described by ovrHmdCaps which the HMD currently supports.DefaultHmdCapsunsigned intDefault capability bits described by ovrHmdCaps for the current HMD.AvailableTrackingCapsunsigned intCapability bits described by ovrTrackingCaps which the HMD currently supports.DefaultTrackingCapsunsigned intDefault capability bits described by ovrTrackingCaps for the current HMD.DefaultEyeFovovrFovPort[]Recommended optical field of view for each eye.MaxEyeFovovrFovPort[]Maximum optical field of view that can be practically rendered for each eye.ResolutionovrSizeiResolution of the full HMD screen (both eyes) in pixels.DisplayRefreshRatefloatNominal refresh rate of the HMD in cycles per second at the time of HMD creation.The description of a sensor (ovrTrackerDesc) handle can be retrieved by calling ovr\_GetTrackerDesc(sensor). The following table describes the fields:

FieldTypeDescriptionFrustumHFovInRadiansfloatThe horizontal FOV of the position sensor frustum.FrustumVFovInRadians floatThe vertical FOV of the position sensor frustum.FrustumNearZInMetersfloatThe distance from the position sensor to the near frustum bounds.FrustumNearZInMetersfloatThe distance from the position sensor to the far frustum bounds.## Head Tracking and Sensors

The Oculus Rift hardware contains a number of micro-electrical-mechanical (MEMS) sensors including a gyroscope, accelerometer, and magnetometer. 

There is also a sensor to track headset position. The information from each of these sensors is combined through the sensor fusion process to determine the motion of the user’s head in the real world and synchronize the user’s view in real-time.

Once the ovrSession is created, you can poll sensor fusion for head position and orientation by calling ovr\_GetTrackingState. These calls are demonstrated by the following code:

// Query the HMD for ts current tracking state. ovrTrackingState ts = ovr\_GetTrackingState(session, ovr\_GetTimeInSeconds(), ovrTrue); if (ts.StatusFlags & (ovrStatus\_OrientationTracked | ovrStatus\_PositionTracked)) { ovrPosef pose = ts.HeadPose.ThePose; ... } This example initializes the sensors with orientation, yaw correction, and position tracking capabilities. If the sensor is not available during the time of the call, but is plugged in later, the sensor is automatically enabled by the SDK.

After the sensors are initialized, the sensor state is obtained by calling ovr\_GetTrackingState. This state includes the predicted head pose and the current tracking state of the HMD as described by StatusFlags. This state can change at runtime based on the available devices and user behavior. For example, the ovrStatus\_PositionTracked flag is only reported when HeadPose includes the absolute positional tracking data from the sensor.

The reported ovrPoseStatef includes full six degrees of freedom (6DoF) head tracking data including orientation, position, and their first and second derivatives. The pose value is reported for a specified absolute point in time using prediction, typically corresponding to the time in the future that this frame’s image will be displayed on screen. To facilitate prediction, ovr\_GetTrackingState takes absolute time, in seconds, as a second argument. The current value of absolute time can be obtained by calling ovr\_GetTimeInSeconds. If the time passed into ovr\_GetTrackingState is the current time or earlier, the tracking state returned will be based on the latest sensor readings with no prediction. In a production application, however, you should use the real-time computed value returned by GetPredictedDisplayTime. Prediction is covered in more detail in the section on Frame Timing.

As already discussed, the reported pose includes a 3D position vector and an orientation quaternion. The orientation is reported as a rotation in a right-handed coordinate system, as illustrated in the following figure. 

![](/images/documentation-pcsdk-latest-concepts-dg-sensor-dg-sensor-0.png)  
Rift Coordinate SystemThe x-z plane is aligned with the ground regardless of camera orientation.

As seen from the diagram, the coordinate system uses the following axis definitions:

* Y is positive in the up direction.
* X is positive to the right.
* Z is positive heading backwards.
Rotation is maintained as a unit quaternion, but can also be reported in yaw-pitch-roll form. Positive rotation is counter-clockwise (CCW, direction of the rotation arrows in the diagram) when looking in the negative direction of each axis, and the component rotations are:

* Pitch is rotation around X, positive when pitching up.
* Yaw is rotation around Y, positive when turning left.
* Roll is rotation around Z, positive when tilting to the left in the XY plane.
The simplest way to extract yaw-pitch-roll from ovrPose is to use the C++ OVR Math helper classes that are included with the library. The following example uses direct conversion to assign ovrPosef to the equivalent C‍++ Posef class. You can then use the Quatf::GetEulerAngles<> to extract the Euler angles in the desired axis rotation order.

All simple C math types provided by OVR such as ovrVector3f and ovrQuatf have corresponding C++ types that provide constructors and operators for convenience. These types can be used interchangeably.

If an application uses a left-handed coordinate system, it can use the ovrPosef\_FlipHandedness function to switch any right-handed ovrPosef provided by ovr\_GetTrackingState, ovr\_GetEyePoses, or ovr\_CalcEyePoses functions to be left-handed. Be aware that the RenderPose and QuadPoseCenterrequested for the ovrLayers must still use the right-handed coordinate system.

### Position Tracking

The frustum is defined by the horizontal and vertical FOV, and the distance to the front and back frustum planes.

Approximate values for these parameters can be accessed through the ovrTrackerDesc struct as follows:

ovrSession session; ovrGraphicsLuid luid; if(OVR\_SUCCESS(ovr\_Create(&session, &luid))) { // Extract tracking frustum parameters. float frustomHorizontalFOV = session->CameraFrustumHFovInRadians; ... The following figure shows the tracking sensor and a representation of the resulting tracking frustum. 

![](/images/documentation-pcsdk-latest-concepts-dg-sensor-dg-sensor-1.png)  
Tracking Sensor and Tracking FrustumThe relevant parameters and typical values are list below:

FieldTypeTypical ValueFrustumHFovInRadiansfloat1.292 radians (74 degrees)FrustumVFovInRadiansfloat0.942 radians (54 degrees)FrustumNearZInMetersfloat0.4mFrustumFarZInMetersfloat2.5mThese parameters provide application developers with a visual representation of the tracking frustum. The previous figure also shows the default tracking origin and associated coordinate system. 

Note: Although the sensor axis (and hence the tracking frustum) are shown tilted downwards slightly, the tracking coordinate system is always oriented horizontally such that the axes are parallel to the ground. By default, the tracking origin is located one meter away from the sensor in the direction of the optical axis but with the same height as the sensor. The default origin orientation is level with the ground with the negative axis pointing towards the sensor. In other words, a headset yaw angle of zero corresponds to the user looking towards the sensor. 

This can be modified using the API call ovr\_RecenterTrackingOrigin, which resets the tracking origin to the headset’s current location and sets the yaw origin to the current headset yaw value. Additionally, it can be manually specified to any location using the API call ovr\_SpecifyTrackingOrigin.

There are two types of tracking origins: floor-level and eye-level. Floor-level is recommended for room scale, when the user stands, and when the user is interacting with objects on the floor (although telekinesis/force grab/gaze grab is a better option for picking up objects). For most other experiences, especially when the user is seated, eye-level is preferred. To get the current origin, use ovr\_GetTrackingOriginType. To set the origin, use ovr\_SetTrackingOriginType.

Note: The tracking origin is set on a per application basis; switching focus between different VR apps also switches the tracking origin. The head pose is returned by calling ovr\_GetTrackingState. The returned ovrTrackingState struct contains several items relevant to position tracking:

* HeadPose—includes both head position and orientation.
* Pose—the pose of the sensor relative to the tracking origin.
* CalibratedOrigin—the pose of the origin previously calibrated by the user and stored in the profile reported in the new recentered tracking origin space. This value can change when the application calls ovr\_RecenterTrackingOrigin, though it refers to the same location in real-world space. Otherwise it will remain as an identity pose. Different tracking origin types will report different CalibrateOrigin poses, as the calibration origin refers to a fixed position in real-world space but the two tracking origin types refer to different y levels.
The StatusFlags variable contains the following status bits relating to position tracking:

* ovrStatus\_PositionTracked—flag that is set only when the headset is being actively tracked.
There are several conditions that may cause position tracking to be interrupted and for the flag to become zero:

* The headset moved wholly or partially outside the tracking frustum. 
* The headset adopts an orientation that is not easily trackable with the current hardware (for example facing directly away from the sensor). 
* The exterior of the headset is partially or fully occluded from the sensor’s point of view (for example by hair or hands). 
* The velocity of the headset exceeds the expected range. 
Following an interruption, assuming the conditions above are no longer present, tracking normally resumes quickly and the ovrStatus\_PositionTracked flag is set. 

If you want to get the pose and leveled pose of a sensor, call ovr\_GetTrackerPose. The returned ovrTrackerPose struct contains the following:

* Pose—the pose of the sensor relative to the tracking origin.
* LeveledPose— the pose of the sensor relative to the tracking origin but with roll and pitch zeroed out. You can use this as a reference point to render real-world objects in the correct place.
### User Input Integration

To provide the most comfortable, intuitive, and usable interface for the player, head tracking should be integrated with an existing control scheme for most applications.

For example, in a first person shooter (FPS) game, the player generally moves forward, backward, left, and right using the left joystick, and looks left, right, up, and down using the right joystick. When using the Rift, the player can now look left, right, up, and down, using their head. However, players should not be required to frequently turn their heads 180 degrees since this creates a bad user experience. Generally, they need a way to reorient themselves so that they are always comfortable (the same way in which we turn our bodies if we want to look behind ourselves for more than a brief glance).

To summarize, developers should carefully consider their control schemes and how to integrate head-tracking when designing applications for VR. The OculusRoomTiny application provides a source code sample that shows how to integrate Oculus head tracking with the aforementioned standard FPS control scheme.

For more information about good and bad practices, refer to the *Oculus Best Practices Guide*.

## Health and Safety Warning

All applications that use the Oculus Rift periodically display a health and safety warning.

This warning appears for a short amount of time when the user wears the Rift; it can be dismissed by pressing a key or gazing at the acknowledgement. After the screen is dismissed, it shouldn't display for at least 30 minutes.

