---
title: Changes For Release 0.4
---
A number of changes were made to the API since the 0.3.2 Preview release. 

These are summarized as follows:

* Removed the method ovr\_GetDesc. The ovrHmd handle is now a pointer to a ovrHmdDesc struct.
* The sensor interface has been simplified. Your application should now call ovr\_ConfigureTracking at initialization and ovr\_GetTrackingState or ovr\_GetEyePoses to get the head pose.
* ovr\_BeginEyeRender and ovr\_EndEyeRender have been removed. You should now use ovr\_GetEyePoses to determine predicted head pose when rendering each eye. Render poses and ovrTexture info is now passed into ovr\_EndFrame rather than ovr\_EndEyeRender.
* ovrSensorState struct is now ovrTrackingState. The predicted pose Predicted is now named HeadPose. CameraPose and LeveledCameraPose have been added. Raw sensor data can be obtained through RawSensorData.
* ovrSensorDesc struct has been merged into ovrHmdDesc.
* Addition of ovr\_AttachToWindow. This is a platform specific function to specify the application window whose output will be displayed on the HMD. Only used if the ovrHmdCap\_ExtendDesktop flag is false.
* Addition of ovr\_GetVersionString. Returns a string representing the libOVR version. 
There have also been a number of minor changes:

* Renamed ovrSensorCaps struct to ovrTrackingCaps.
* Addition of ovrHmdCaps::ovrHmdCap\_Captured flag. Set to true if the application captured ownership of the HMD.
* Addition of ovrHmdCaps::ovrHmdCap\_ExtendDesktop flag. The display driver is in compatibility mode (read only).
* Addition of ovrHmdCaps::ovrHmdCap\_NoMirrorToWindow flag. Disables mirroring of HMD output to the window. This may improve rendering performance slightly (only if ’Extend-Desktop’ is off).
* Addition of ovrHmdCaps::ovrHmdCap\_DisplayOff flag. Turns off HMD screen and output (only if ’ExtendDesktop’ is off).
* Removed ovrHmdCaps::ovrHmdCap\_LatencyTest flag. Was used to indicate support of pixel reading for continuous latency testing.
* AdditionofovrDistortionCaps::ovrDistortionCap\_Overdriveflag. Overdrivebrightness transitions to reduce artifacts on DK2 displays.
* Addition of ovrStatusBits::ovrStatus\_CameraPoseTracked flag. Indicates that the camera pose is successfully calibrated.
