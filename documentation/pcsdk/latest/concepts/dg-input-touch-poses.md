---
title: Hand Tracking
---

The constellation sensor used to track the head position of the Oculus Rift also tracks the hand poses of the Oculus Touch controllers.

For installations that have the Oculus Rift and Oculus Touch controllers, there will be at least two constellation sensors to improve tracking accuracy and help with occlusion issues.

The SDK uses the same ovrPoseStatef struct as the headset, which includes six degrees of freedom (6DoF) and tracking data (orientation, position, and their first and second derivatives).

Here’s an example of how to get tracking input:

```
ovrTrackingState trackState = ovr_GetTrackingState(session, displayMidpointSeconds, ovrTrue);
ovrPosef         handPoses[2];
ovrInputState    inputState;

```

In this code sample, we call ovr_GetTrackingState to get predicted poses. Hand controller poses are reported in the same coordinate frame as the headset and can be used for rendering hands or objects in the 3D world. An example of this is provided in the Oculus World Demo.
