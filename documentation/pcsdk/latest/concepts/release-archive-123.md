---
title: Changes in Version 1.23.x
---



## New Features for 1.23.x

* **VRC Validator GUI:** The Virtual Reality Check (VRC) Validator utility runs automated tests to determine if your Rift app is ready for Oculus Store technical review. The VRC Validator now provides an easy-to-use GUI interface (in addition to the command-line interface that has been available in previous releases). The GUI interface can be launched from the Oculus Debug Tool. For more information, see &lt;https://developer.oculus.com/documentation/pcsdk/latest/concepts/dg-vrcvalidator/&gt;.


## API Changes

* There are no breaking API changes in this release.
* The following error codes were added: OVR\_ErrorCode.h: ovrError\_DisplayLimitReached = -6009, /// There was a problem initializing the external camera for capture ovrError\_ExternalCameraInitializedFailed = -1019, /// There was a problem capturing external camera frames ovrError\_ExternalCameraCaptureFailed = -1020, /// The external camera friendly name list and the external camera name list /// are not the fixed size(OVR\_MAX\_EXTERNAL\_CAMERA\_NAME\_BUFFER\_SIZE). ovrError\_ExternalCameraNameListsBufferSize = -1021, /// The external camera friendly name list is not the same size as /// the external camera name list. ovrError\_ExternalCameraNameListsMistmatch = -1022, /// The external camera property has not been sent to OVRServer /// when the user tries to open the camera. ovrError\_ExternalCameraNotCalibrated = -1023, /// The external camera name is larger than OVR\_EXTERNAL\_CAMERA\_NAME\_SIZE-1 ovrError\_ExternalCameraNameWrongSize = -1024,


## Known SDK Issues

* The sample project, LibOVR.vcxproj, cannot be used with Visual Studio 2010 and 2012. If you compile this project with those Visual Studio versions, it will not load. A fix for this issue is expected in the 1.23 PC-SDK release. 
* There's a bug affecting the Guardian System API by which color set operations to the visualized grid don't work if they are called while the HMD is not being worn.

