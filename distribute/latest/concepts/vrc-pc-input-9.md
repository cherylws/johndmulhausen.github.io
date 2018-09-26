---
title: VRC.PC.Input.9
---

If an app is “focus aware,” it must continue rendering while Dash is up, but hide any user hands or controllers and ignore all input.

**Required** - Yes

## Additional Details

Focus aware support is not required. If not enabled, users will see the Universal Menu instead. Information about handling focus aware is available in the [Unity](/documentation/unity/latest/concepts/unity-lifecycle/), [Unreal](/documentation/unreal/latest/concepts/unreal-lifecycle/), and [PC](/documentation/pcsdk/latest/concepts/dg-vr-focus/) guides. 

## Steps to Test

1. Press the Oculus menu button on the controller.
2. Observe: if Dash appears on top of the currently running and rendering app, it is configured to be focus aware. If you see a gray room with menu items directly in front of your face, the app is not focus aware and other VRCs related to the Universal Menu will apply.
3. Observe the app rendering.
4. Move the Touch controllers around, click buttons


## Expected Result

User should only be able to interact with Dash overlay elements while the app continues to render in the background. To avoid duplicate interactions, in-app hand or controller movement should not render while Dash is up. If the app has pause functionality (users can pause, or the app pauses in menus, or it pauses when the HMD is off) then it should pause while Dash is up.
