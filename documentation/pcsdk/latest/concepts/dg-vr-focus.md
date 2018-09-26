---
title: VR Focus Management
---

 When you submit your application to Oculus, you provide the application and metadata necessary to list it in the Oculus Store and launch it from Oculus Home. 

Once launched from Oculus Home, you need to write a loop that polls for session status. ovr_GetSessionStatus returns a struct with the following booleans:

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

If ShouldRecenter is true, the application should call ovr_RecenterTrackingOrigin or ovr_SpecifyTrackingOrigin and be prepared for future tracking positions to be based on a different origin. 

Some applications may have reason to ignore the request or to implement it via an internal mechanism other than via ovr_RecenterTrackingOrigin. In such cases the application can call ovr_ClearShouldRecenterFlag to cause the recenter request to be cleared.

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

## Managing an Unavailable Headset

 When a user removes the headset or if your application does not have VR focus, HmdMounted or IsVisible returns false. Pause the application until they return true.

When your application loses VR focus, it automatically stops receiving input. If your application does not use the Oculus input API, it will need to ignore any received input.

## Managing Loss of Windows Focus

When your application loses Windows focus, the Oculus Remote, Xbox controller, and Touch controllers will continue to work normally. However, the application will lose control of the mouse and keyboard.

If your application loses Windows focus and maintains VR focus (IsVisible), continue to process input and allow the application to run normally. If the keyboard or mouse is needed to continue, prompt the user to remove the headset and use Alt-Tab to regain Windows focus.

## Managing Dashboards and Application Focus

With the introduction of Dash, your application should now indicate whether or not it is it is prepared to respond to ovrSessionStatus focus states, including ovrSessionStatus::HasInputFocus. For more information, please see [unresolvable-reference.xml](unresolvable-reference)

## Code Sample

```
  
bool shouldQuit = false;

void RunApplication()
{
    ovrResult result = ovr_Initialize();

    if (OVR_SUCCESS(result))
    {
        ovrSession session;
        ovrGraphicsLuid luid;
        result = ovr_Create(&amp;session, &amp;luid);
        result = ovr_WaitToBeginFrame(session, 0);
        result = ovr_BeginFrame(session, 0);

        if (OVR_SUCCESS(result))
        {
            ovrSessionStatus ss;

            &lt;create graphics device with luid&gt;
            &lt;create render target via ovr_CreateTextureSwapChain&gt;
       
            while (!shouldQuit)
            {
                &lt;get next frame pose, e.g. via ovr_GetEyePoses&gt;
                &lt;render frame&gt;

                result = ovr_EndFrame(...);

                if (result == ovrSuccess_NotVisible)
                {
                    &lt;turn off audio output&gt;
                    do { // Wait until we regain visibility or should quit
                        &lt;sleep&gt;
                        result = ovr_GetSessionStatus(session, &amp;ss);
                        if (ss.ShouldQuit)
                            shouldQuit = true;
                    } while (OVR_SUCCESS(result) &amp;&amp; !ss.IsVisible &amp;&amp; !shouldQuit);
                    &lt;possibly re-enable audio&gt;
                }
                else if (result == ovrError_DisplayLost)
                {
                    // We can either immediately quit or do the following:
                    &lt;destroy render target and graphics device&gt;
                    ovr_Destroy(session);

                    do { // Spin while trying to recreate session.
                        result = ovr_Create(&amp;session, &amp;luid);
                    } while (OVR_FAILURE(result) &amp;&amp; !shouldQuit);

                    if (OVR_SUCCESS(result))
                    {
                        &lt;recreate graphics device with luid&gt;
                        &lt;recreate render target via ovr_CreateTextureSwapChain&gt;
                    }
                }
                else if (OVR_FAILURE(result))
                {
                    shouldQuit = true;
                }

                ovr_GetSessionStatus(session, &amp;ss);
                if (ss.ShouldQuit)
                    shouldQuit = true;
                if (ss.ShouldRecenter)
                {
                    ovr_RecenterTrackingOrigin(session); // or ovr_ClearShouldRecenterFlag(session) to ignore the request.
                    &lt;do anything else needed to handle this&gt;
                }
            }

            &lt;destroy render target via ovr_DestroyTextureSwapChain&gt;
            &lt;destroy graphics device&gt;

            ovr_Destroy(session);
        }

        ovr_Shutdown();
    }
}
  
  
 
```
