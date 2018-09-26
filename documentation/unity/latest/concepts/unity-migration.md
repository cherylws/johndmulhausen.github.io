---
title: Migrating to Utilities from the Integration Package
---

Moving to Unity 5.1 is a substantial upgrade for VR development, and we recommend carefully choosing your time frame for making the update. You may encounter problems related to VR performance or otherwise. 

Please let us know about any issues you encounter in the [Oculus Unity Forum](https://forums.oculus.com/viewforum.php?f=37), and keep your eye out for updates.

## Delete Previously-Imported Assets

If you have previously imported a Unity integration package, delete all Oculus Integration content before importing the new Unity package. For detailed instructions, see [Importing the Oculus Utilities Package](/documentation/unity/latest/concepts/unity-import/). 

## Upgrade Procedure

1. Replace any usage of OVRManager.instance.virtualTextureScale or OVRManager.instance.nativeTextureScale with UnityEngine.VR.VRSettings.renderScale. The value of renderScale is equal to nativeTextureScale * virtualTextureScale. If you set renderScale to a value that is less than or equal to any value it has had since the application started, then virtual texture scaling will be used. If you increase it higher, to a new maximum value, then the native scale is increased and the virtual scale is set to 1.
2. Replace any usage of OVRManager.instance.eyeTextureAntiAliasing with UnityEngine.QualitySettings.antiAliasing. Instead of multisampling the back-buffer when VR is enabled, Unity multisamples the eye buffers.
3. Remove any usage of OVRManager.instance.timeWarp and OVRManager.instance.freezeTimeWarp. TimeWarp is always on and cannot be frozen.
4. Do not assume there are Cameras on OVRCameraRig.leftEyeAnchor or rightEyeAnchor. Instead of calling GetComponent&lt;Camera&gt;(), use Camera.main or, for backward compatibility, use OVRCameraRig.leftEyeCamera or rightEyeCamera.
5. Move any scripts, image effects, tags, or references from the Cameras on OVRCameraRig.leftEyeAnchor and rightEyeAnchor to the one on centerEyeAnchor.
6. Remove any usage of OvrCapi.cs. The CAPI C# binding is no longer available. If you need to access CAPI, use UnityEngine.VR.VRDevice.GetNativePtr() to get an ovrHmd pointer and then pass it to a native plugin that uses the Oculus SDK corresponding to your Unity version. For more on which Unity versions correspond to which SDKs, see "Integration Versions" in [Compatibility and Requirements](/documentation/unity/latest/concepts/unity-req/ "This guide describes Unity Editor version recommendations and system requirements."). 


## Importing Utilities Package into Legacy Projects

The legacy Oculus Unity Integration used a separate Camera component on each eye anchor. Oculus Utilities for Unity uses single camera on the center eye anchor. If the Oculus Utilities package is imported into an old project built with the legacy Unity integration, editor scripts will patch up old OVRCameraRig Game Objects and enable PlayerSettings.virtualRealitySupported, so the project should work without further action.
