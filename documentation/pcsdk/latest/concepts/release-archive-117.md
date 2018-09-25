---
title: Changes in Version 1.17.x
---
## New Features for 1.17.x

* In the Oculus PC SDK, prior to version 1.17, eye poses only had three degrees-of-freedom (DOF), i.e. only translation. Eye poses were specified in the HmdToEyeOffsetvector provided by the ovr\_GetRenderDesc function. Starting with version 1.17, HmdToEyeOffset has been renamed to HmdToEyePose using the type ovrPosef which contains a Position and Orientation, effectively giving eye poses six degrees-of-freedom. This means that each eye’s render frustum can now be rotated away from the HMD’s orientation, in addition to being translated by the SDK. Because of this, the eye frustums’ axes are no longer guaranteed to be parallel to each other or to the HMD’s orientation axes. This generalization provides greater freedom to the SDK in defining the HMD geometry. But it also means that, as a VR app developer, you need to be more careful about your previous assumptions, especially when it comes to rendering.
## API Changes

* Promoted data member HmdToEyeOffset, which was previously found in the structs ovrEyeRenderDesc and ovrViewScaleDesc, from ovrVector3f to ovrPosef and renamed the data member to HmdToEyePose in both occurrences.
* While this API change does not affect VR apps compiled against PC-SDK versions prior to 1.17, VR apps that are upgraded to 1.17 or later will need to update any usages of HmdToEyeOffset accordingly. HmdToEyePose is used in the following functions: 
	+ ovr\_GetRenderDesc
	+ ovr\_SubmitFrame
	+ ovr\_GetEyePoses
	+ ovr\_CalcEyePoses
	
* For more info about this and related pointers, refer to the PC-SDK documentation section “Working with HMD Eye Poses”.
## Known SDK Issues

The following are known issues:

* Recentering a mixed reality capture application will corrupt the camera pose when using a static camera. As a temporary workaround, attach a VR Object to your camera (e.g., by using a third Touch), and it will recenter normally.
* If you encounter intermittent tracking issues, remove the batteries from any Engineering Sample Oculus Remotes that you paired with your headset and contact Developer Relations for replacement remotes.
* If you bypass the shim and communicate with the DLL directly, without specifying a version to ovr\_Initialize, the DLL has no way of knowing the SDK version with which the application was built. This can result in unpredictable or erratic behavior which might cause the application to crash.
* If you are running your application from the Unity Editor and you press the controller's home button to return to Oculus Home, you will be prompted to close the application. If you select OK, Unity might remain in a state where it is running, but will never get focus. To work around this, restart Unity.
