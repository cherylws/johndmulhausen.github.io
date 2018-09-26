---
title: Troubleshooting and Known Issues
---

This section outlines some currently known issues with the Oculus Unity Integration and the Oculus Utilities for Unity.

## Rift

**The app does not launch as a VR app.**

Verify that you have installed the Oculus app and completed setup as described in [Preparing for Rift Development](/documentation/unity/latest/concepts/unity-pcprep/).

Verify that you have selected **Virtual Reality Supported** in **Player Settings**.

are using a compatible runtime - see [Compatibility and Requirements](/documentation/unity/latest/concepts/unity-req/) for more details.

Verify that the HMD is plugged in and working normally. 

Verify that you have not selected D3D 9 or Windows GL as the renderer (Legacy Integration only).

## Mobile

**The app does not launch as a VR app.**

Verify that you selected **Virtual Reality Supported** in **Player Settings** before building your APK. 

**Applications fail to launch on Gear VR with error message "thread priority security exception make sure the apk is signed”.**

You must sign your application with an Oculus Signature File (osig). See "Sign your App with an Oculus Signature File" in [Preparing for Mobile Development](/documentation/unity/latest/concepts/unity-mobileprep/) for instructions.

## General Issues

**Unity 5 hangs while importing assets from SDKExamples.**

Unity 5 is known to import ETC2-compressed assets very slowly.

**Receiving OVRPlugin console errors after importing a new version of Utilities.**

Be sure to delete any previously-imported Utilities packages from your Unity project before importing a new version. If you are receiving errors and have not done so, delete the relevant folders in your project and re-import Utilities. For more information, please see [Importing the Oculus Utilities Package](/documentation/unity/latest/concepts/unity-import/).

## Contact Information

Questions?

Visit our developer support forums at [https://developer.oculus.com](/).

Our Support Center can be accessed at [https://support.oculus.com](https://support.oculus.com/).
