---
title: VR Focus Management
---
 When you submit your application to Oculus, you provide the application and metadata necessary to list it in the Oculus Store and launch it from Oculus Home. 

Once launched from Oculus Home, you need to write a loop that polls for session status. ovr\_GetSessionStatus returns a struct with the following booleans:

* ShouldQuit—True if the application should initiate shutdown.
* HmdPresent—True if an HMD is present. 
* DisplayLost—True if the HMD was unplugged or the display driver was manually disabled or encountered a TDR.
* HmdMounted—True if the HMD is on the user's head.
* IsVisible—True if the game or experience has VR focus and is visible in the HMD.
* ShouldRecenter—True if the application should call ovr\_RecenterTrackingOrigin. This is triggered when the user initiates recentering through the Universal Menu.
## Managing When a User Quits

If ShouldQuit is true, save the application state and shut down or shut down without saving the application state. The user will automatically return to Oculus Home. 

Depending on the type of application, you can prompt the user to start where he or she left off the next time it is opened (e.g., a multi-level game) or you can just start from the beginning of the experience (e.g., a passive video). If this is a multiplayer game, you might want to quit locally without ending the game.

## Managing When a User Requests Recentering

If ShouldRecenter is true, the application should call ovr\_RecenterTrackingOrigin or ovr\_SpecifyTrackingOrigin and be prepared for future tracking positions to be based on a different origin. 

Some applications may have reason to ignore the request or to implement it via an internal mechanism other than via ovr\_RecenterTrackingOrigin. In such cases the application can call ovr\_ClearShouldRecenterFlag to cause the recenter request to be cleared.

## Managing an Unplugged Headset

If DisplayLost is true:

1. Pause the application, including audio.
2. Display a prompt on the monitor that says that the headset was unplugged. 
3. Destroy any TextureSwapChains or mirror textures.
4. Call ovrDestroy.
5. Poll ovrSessionStatus::HmdPresent until true. 
6. Call ovrCreate to recreate the session.
7. Recreate any TextureSwapChains or mirror textures.
8. Resume the application.
If ovrDetect doesn’t isn’t returned as true after a specified amount of time, act as though ShouldQuit returned true. If the user takes no action after a specified amount of time, choose a default action (save the session or close without saving) and close the application. 

Note: For multiplayer games, you might want to follow the same process without pausing the game.## Managing an Unavailable Headset

 When a user removes the headset or if your application does not have VR focus, HmdMounted or IsVisible returns false. Pause the application until they return true.

When your application loses VR focus, it automatically stops receiving input. If your application does not use the Oculus input API, it will need to ignore any received input.

Note: For multiplayer games, you might want the game to continue without pausing.## Managing Loss of Windows Focus

When your application loses Windows focus, the Oculus Remote, Xbox controller, and Touch controllers will continue to work normally. However, the application will lose control of the mouse and keyboard.

If your application loses Windows focus and maintains VR focus (IsVisible), continue to process input and allow the application to run normally. If the keyboard or mouse is needed to continue, prompt the user to remove the headset and use Alt-Tab to regain Windows focus.

## Managing Dashboards and Application Focus

With the introduction of Dash, your application should now indicate whether or not it is it is prepared to respond to ovrSessionStatus focus states, including ovrSessionStatus::HasInputFocus. For more information, please see [unresolvable-reference.xml](unresolvable-reference)

## Code Sample

 bool shouldQuit = false; void RunApplication() { ovrResult result = ovr\_Initialize(); if (OVR\_SUCCESS(result)) { ovrSession session; ovrGraphicsLuid luid; result = ovr\_Create(&session, &luid); result = ovr\_WaitToBeginFrame(session, 0); result = ovr\_BeginFrame(session, 0); if (OVR\_SUCCESS(result)) { ovrSessionStatus ss; <create graphics device with luid> <create render target via ovr\_CreateTextureSwapChain> while (!shouldQuit) { <get next frame pose, e.g. via ovr\_GetEyePoses> <render frame> result = ovr\_EndFrame(...); if (result == ovrSuccess\_NotVisible) { <turn off audio output> do { // Wait until we regain visibility or should quit <sleep> result = ovr\_GetSessionStatus(session, &ss); if (ss.ShouldQuit) shouldQuit = true; } while (OVR\_SUCCESS(result) && !ss.IsVisible && !shouldQuit); <possibly re-enable audio> } else if (result == ovrError\_DisplayLost) { // We can either immediately quit or do the following: <destroy render target and graphics device> ovr\_Destroy(session); do { // Spin while trying to recreate session. result = ovr\_Create(&session, &luid); } while (OVR\_FAILURE(result) && !shouldQuit); if (OVR\_SUCCESS(result)) { <recreate graphics device with luid> <recreate render target via ovr\_CreateTextureSwapChain> } } else if (OVR\_FAILURE(result)) { shouldQuit = true; } ovr\_GetSessionStatus(session, &ss); if (ss.ShouldQuit) shouldQuit = true; if (ss.ShouldRecenter) { ovr\_RecenterTrackingOrigin(session); // or ovr\_ClearShouldRecenterFlag(session) to ignore the request. <do anything else needed to handle this> } } <destroy render target via ovr\_DestroyTextureSwapChain> <destroy graphics device> ovr\_Destroy(session); } ovr\_Shutdown(); } } 