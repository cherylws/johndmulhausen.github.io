---
title: Oculus Dash
---
This section introduces Oculus Dash for the PC-SDK.

Oculus Dash rolls up all of Rift’s menus and UI into a central hub that is instantly accessible from anywhere within the VR experience. Dash runs as an overlay inside your current VR experience, so you’ll be able to quickly switch from one application to the next, open your library, connect with friends, and even use the rest of your PC without any extra steps. Not only does this make VR more intuitive and convenient, it also lets you multitask like never before—a huge plus for creators and developers who use VR while they work.

For general information about Dash, please see the Dash announcement: [Introducing Rift Core 2.0—Our Biggest Software Update Yet!](https://www.oculus.com/blog/introducing-rift-core/). Also see the "Introducing Oculus Dash" video in our [Welcome to Rift Core 2.0](https://www.oculus.com/blog/welcome-to-rift-core-beta-now-available/) blog post to get a sense of how Dash works. 

**Getting Ready for Dash**

You need to ensure that your computer (tower or laptop) is prepped to deliver the best possible experience. We put together a few pointers to help you get started:

* **Windows 10 Recommended:** Rift Core 2.0, which underlies Dash, pushes the boundaries of VR computing. Dash's multitasking, window pinning, and Oculus Desktop features are resource-heavy system tasks that we have introduced while still maintaining current performance standards. Oculus Desktop requires Windows 10. You can still use Windows 7 and Windows 8 and enjoy the core functionality of Rift Core 2.0, including the new Dash system menu and Oculus Home. However, you won’t be able to use features like Oculus Desktop for virtual computing, and Dash won't be able to run as an overlay on top of your currently running VR application. 
* **Update Your GPU Drivers:** We worked with both AMD and NVIDIA to integrate Dash support at the driver level. You'll need the latest drivers from NVIDIA and AMD to run Dash. [Click here](https://support.oculus.com/326247701060681/) for more information on GPU specs.
* **Touch-First Design:** We redesigned the core Rift experience to be truly Touch-native, offering you all the benefits of hand presence in [an intuitive, easy-to-use interface](https://www.youtube.com/watch?v=SvP_RI_S-bw). Although many features will continue to work with the Xbox controller, some new functionality—such as customizing your Home— requires Touch. Put simply, if you want to take full advantage of all the features in Rift Core 2.0, use Touch.
![](/images/documentation-pcsdk-latest-concepts-dg-dash-0.png)  
Oculus Dash User Interface**Using Dash**

We recommend adding Dash support to your application to provide the best possible user experience. The experience will vary, depending upon whether or not your application provides Dash support: 

* If the application includes Dash support, when the application pauses the Dash menu UI will be drawn over the paused application. 
* If the application does not include Dash support, when the application pauses the user will be presented with the Dash menu UI in an empty room, similar to the way the Universal Menu was displayed with earlier Oculus runtimes. 
When the Dash UI is active, the runtime will render tracked controllers in the scene to interact with the menu. Your application should pause, mute, and hide any tracked controllers it renders in the scene, so there will not be a duplicate pair of hands. 

When you implement support for Dash, you need to consider three areas:

* Input Focus Handling
* Depth Buffer Support
* Declaring an Application is Input Focus Aware
**Input Focus Handling**

When the Dash UI is active, the running application loses input focus and the ovrSessionStatus::HasInputFocus flag will return false. In this state, the runtime renders tracked controllers in the scene to interact with the menu.

When HasInputFocus is false, your application should pause all activity, mute audio playback, hide any tracked controllers in the scene so there will not be a duplicate pair of hands, and hide any near field objects (within about one meter of the user). Depending on the application, additional action may also be warranted when input focus is lost. For example, during a multiplayer combat game, you may wish to indicate that the player is unavailable and take any other appropriate action.

The VR Compositor may use up to 3 ms of additional rendering time during each frame cycle while HasInputFocus is False. Because of this, it is a good idea to switch your application into a lower performance mode, if possible, as long as HasInputFocusis False. Wait until HasInputFocus becomes True again before reverting this action. This approach is not required, and Oculus does not enforce performance VRC requirements during the time that the Dash UI is active.

Note that HasInputFocus returns false under any other conditions in which the application loses input focus, such as when the HMD is removed from the head.

You can check the HasInputFocus flag with the following code:

 ovrSessionStatus sessionStatus = {}; ovr\_GetSessionStatus(Session, &sessionStatus); if (!sessionStatus.HasInputFocus) {/*Handle situation where your app has lost input focus*/}This code should be executed once during every frame render cycle.

**Depth Buffer Support**

If you are rendering of lot of geometry near the user, it may cause uncomfortable visual disparities when a Dash panel renders on top of geometry that is closer to the player than the Dash panel. To avoid that disparity, you can submit depth with your eye buffers. This will allow Dash to draw an x-ray effect that prevents this discomfort. For this reason, and for future improvements, we recommend submitting depth data with your eye buffers. However, if you are unable to do this, it is still better to support Dash (and live with the disparity) than to not support Dash. 

To submit depth data, use ovrLayerType\_EyeFovDepth, as shown in the example code below. This code was derived from the OculusRoomTiny DX11 code sample (located under <sdk\_folder>\OculusSDK\Samples\OculusRoomTiny\OculusRoomTiny (DX11)\Projects\Windows\VS2015):

// Initialize our single full screen Fov layer. ovrLayerEyeFovDepth ld = {}; ld.Header.Type = ovrLayerType\_EyeFovDepth; ld.Header.Flags = 0; for (int eye = 0; eye < 2; ++eye) { ld.ColorTexture[eye] = pEyeRenderTexture[eye]->TextureChain; ld.DepthTexture[eye] = pEyeRenderTexture[eye]->DepthTextureChain; ld.Viewport[eye] = eyeRenderViewport[eye]; ld.Fov[eye] = hmdDesc.DefaultEyeFov[eye]; ld.RenderPose[eye] = EyeRenderPose[eye]; ld.SensorSampleTime = sensorSampleTime; ld.ProjectionDesc = posTimewarpProjectionDesc[eye]; } ovrLayerHeader* layers = &ld.Header; result = ovr\_SubmitFrame(session, frameIndex, nullptr, &layers, 1); // exit the rendering loop if submit returns an error, will retry on ovrError\_DisplayLost if (!OVR\_SUCCESS(result)) goto Done; frameIndex++; }**Declaring an Application is Input Focus Aware**

Your application should indicate whether or not it is it is prepared to respond to ovrSessionStatus focus states, including HasInputFocus. If your application is prepared to handle the loss of focus, as described under **Input Focus Handling** (above), then set the ovrInit\_FocusAware flag to True, and otherwise set ovrInit\_FocusAware to False.

The following code sample shows how to set ovrInit\_FocusAware. This code was derived from the OculusRoomTiny DX11 code sample (located under <sdk\_folder>\OculusSDK\Samples\OculusRoomTiny\OculusRoomTiny (DX11)\Projects\Windows\VS2015):

int WINAPI WinMain(HINSTANCE hinst, HINSTANCE, LPSTR, int) { // Initializes LibOVR and the Rift ovrInitParams initParams = { ovrInit\_RequestVersion | ovrInit\_FocusAware, OVR\_MINOR\_VERSION, NULL, 0, 0 }; ovrResult result = ovr\_Initialize(&initParams); VALIDATE(OVR\_SUCCESS(result), "Failed to initialize libOVR."); VALIDATE(DIRECTX.InitWindow(hinst, L"Oculus Room Tiny (DX11)"), "Failed to open window."); DIRECTX.Run(MainLoop); ovr\_Shutdown(); return(0); }