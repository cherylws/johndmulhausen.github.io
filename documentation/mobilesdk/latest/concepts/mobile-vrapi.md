---
title: VrApi
---





## Lifecycle and Rendering

Multiple Android activities that live in the same address space can cooperatively use the VrApi. However, only one activity can be in "VR mode" at a time. The following explains when an activity is expected to enter/leave VR mode.

### Android Activity lifecycle

An Android Activity can only be in VR mode while the activity is in the resumed state. The following shows how VR mode fits into the Android Activity lifecycle.

```
     1.  VrActivity::onCreate() &lt;---------+
     2.  VrActivity::onStart()  &lt;-------+ |
     3.  VrActivity::onResume() &lt;---+   | |
     4.  vrapi_EnterVrMode()        |   | |
     5.  vrapi_LeaveVrMode()        |   | |
     6.  VrActivity::onPause() -----+   | |
     7.  VrActivity::onStop() ----------+ |
     8.  VrActivity::onDestroy() ---------+     
```

### Android Surface lifecycle

An Android Activity can only be in VR mode while there is a valid Android Surface. The following shows how VR mode fits into the Android Surface lifecycle.

```
     1.  VrActivity::surfaceCreated() &lt;----+
     2.  VrActivity::surfaceChanged()      |
     3.  vrapi_EnterVrMode()               |
     4.  vrapi_LeaveVrMode()               |
     5.  VrActivity::surfaceDestroyed() ---+
```

Note that the lifecycle of a surface is not necessarily tightly coupled with the lifecycle of an activity. These two lifecycles may interleave in complex ways. Usually `surfaceCreated()` is called after `onResume()` and `surfaceDestroyed()` is called between `onPause()` and `onDestroy()`. However, this is not guaranteed and, for instance, `surfaceDestroyed()` may be called after `onDestroy()` or even before `onPause()`.

An Android Activity is only in the resumed state with a valid Android Surface between `surfaceChanged()` or `onResume()`, whichever comes last, and `surfaceDestroyed()` or `onPause()`, whichever comes first. In other words, a VR application will typically enter VR mode from `surfaceChanged()` or `onResume()`, whichever comes last, and leave VR mode from `surfaceDestroyed()` or `onPause()`, whichever comes first.

### Android VR lifecycle

This is a high-level overview of the rendering pipeline used by VrApi. For more information, see VrApi\Include\VrApi.h.

1. Initialize the API.
2. Create an EGLContext for the application.
3. Get the suggested resolution to create eye texture swap chains with vrapi\_GetSystemPropertyInt( &amp;java, VRAPI\_SYS\_PROP\_SUGGESTED\_EYE\_TEXTURE\_WIDTH ).
4. Allocate a texture swap chain for each eye with the application's EGLContext current.
5. Android Activity/Surface lifecycle loop.
	1. Acquire ANativeWindow from Android Surface.
	2. Enter VR mode once the Android Activity is in the resumed state with a valid ANativeWindow.
	3. Set the tracking transform to use (eye level by default).
	4. Frame loop, possibly running on another thread.
	5. Get the HMD pose, predicted for the middle of the time period during which the new eye images will be displayed. The number of frames predicted ahead depends on the pipeline depth of the engine and the synthesis rate. The better the prediction, the less black will be pulled in at the edges.
	6. Advance the simulation based on the predicted display time.
	7. Render eye images and setup ovrSubmitFrameDesc using ovrTracking2.
	8. Render to textureId using the ViewMatrix and ProjectionMatrix from ovrTracking2. Insert fence using eglCreateSyncKHR.
	9. Submit the frame with vrapi\_SubmitFrame2.
	10. Must leave VR mode when the Android Activity is paused or the Android Surface is destroyed or changed.
	11. Destroy the texture swap chains. Make sure to delete the swapchains before the application's EGLContext is destroyed.
	
6. Shut down the API.


### Integration

The API is designed to work with an Android Activity using a plain Android SurfaceView, where the Activity lifecycle and the Surface lifecycle are managed completely in native code by sending the lifecycle events (onResume, onPause, surfaceChanged etc.) to native code.

The API does not work with an Android Activity using a GLSurfaceView. The GLSurfaceView class manages the window surface and EGLSurface and the implementation of GLSurfaceView may unbind the EGLSurface before `onPause()` gets called. As such, there is no way to leave VR mode before the EGLSurface disappears. Another problem with GLSurfaceView is that it creates the EGLContext using `eglChooseConfig()`. The Android EGL code pushes in multisample flags in `eglChooseConfig()` if the user has selected the "force 4x MSAA" option in settings. Using a multisampled front buffer is completely wasted for TimeWarp rendering.

Alternately, an Android NativeActivity can be used to avoid manually handling all the lifecycle events. However, it is important to select the EGLConfig manually without using `eglChooseConfig()` to make sure the front buffer is not multisampled.

The vrapi_GetSystemProperty* functions can be called at any time from any thread. This allows an application to setup its renderer, possibly running on a separate thread, before entering VR mode.

On Android, an application cannot just allocate a new window/frontbuffer and render to it. Android allocates and manages the window/frontbuffer and (after the fact) notifies the application of the state of affairs through lifecycle events (surfaceCreated / surfaceChanged / surfaceDestroyed). The application (or 3rd party engine) typically handles these events. Since the VrApi cannot just allocate a new window/frontbuffer, and the VrApi does not handle the lifecycle events, the VrApi somehow has to take over ownership of the Android surface from the application. To allow this, the application can explicitly pass the EGLDisplay, EGLContext EGLSurface or ANativeWindow to `vrapi_EnterVrMode()`, where the EGLSurface is the surface created from the ANativeWindow. The EGLContext is used to match the version and config for the context used by the background time warp thread. This EGLContext, and no other context can be current on the EGLSurface.

If, however, the application does not explicitly pass in these objects, then `vrapi_EnterVrMode()`**must** be called from a thread with an OpenGL ES context current on the Android window surface. The context of the calling thread is then used to match the version and config for the context used by the background TimeWarp thread. The TimeWarp will also hijack the Android window surface from the context that is current on the calling thread. On return, the context from the calling thread will be current on an invisible pbuffer, because the time warp takes ownership of the Android window surface. Note that this requires the config used by the calling thread to have an EGL_SURFACE_TYPE with EGL_PBUFFER_BIT.

Before getting sensor input, the application also needs to know when the images that are going to be synthesized will be displayed, because the sensor input needs to be predicted ahead for that time. As it turns out, it is not trivial to get an accurate predicted display time. Therefore the calculation of this predicted display time is part of the VrApi. An accurate predicted display time can only really be calculated once the rendering loop is up and running and submitting frames regularly. In other words, before getting sensor input, the application needs an accurate predicted display time, which in return requires the renderer to be up and running. As such, it makes sense that sensor input is not available until `vrapi_EnterVrMode()` has been called. However, once the application is in VR mode, it can call `vrapi_GetPredictedDisplayTime()` and `vrapi_GetPredictedTracking()` at any time from any thread.

### How Eye Images are Synchronized

The VrApi allows for one frame of overlap which is essential on tiled mobile GPUs. Because there is one frame of overlap, the eye images have typically not completed rendering by the time they are submitted to `vrapi_SubmitFrame()`. To allow the time warp to check whether the eye images have completed rendering, the application can explicitly pass in a sync object (CompletionFence) for each eye image through `vrapi_SubmitFrame()`, or in the case of `vrapi_SubmitFrame2`, one `CompletionFence` is specified for the whole frame via the `ovrSubmitFrameDescription` structure. Note that these sync objects must be EGLSyncKHR because the VrApi still supports OpenGL ES 2.0.

If, however, the application does not explicitly pass in sync objects, then `vrapi_SubmitFrame()`**must** be called from the thread with the OpenGL ES context that was used for rendering, which allows `vrapi_SubmitFrame()` to add a sync object to the current context and check if rendering has completed.

Note that even if no OpenGL ES objects are explicitly passed through the VrApi, `vrapi_EnterVrMode()` and `vrapi_SubmitFrame()` can still be called from different threads. `vrapi_EnterVrMode()` needs to be called from a thread with an OpenGL ES context that is current on the Android window surface. This does not need to be the same context that is also used for rendering. `vrapi_SubmitFrame()` needs to be called from the thread with the OpenGL ES context that was used to render the eye images. If this is a different context than the context used to enter VR mode, then for stereoscopic rendering this context *never* needs to be current on the Android window surface.

Eye images are passed to `vrapi_SubmitFrame()` as "texture swap chains" (ovrTextureSwapChain). These texture swap chains are allocated through `vrapi_CreateTextureSwapChain()`. This is important to allow these textures to be allocated in special system memory. When using a static eye image, the texture swap chain does not need to be buffered and the chain only needs to hold a single texture. When the eye images are dynamically updated, the texture swap chain needs to be buffered. When the texture swap chain is passed to `vrapi_SubmitFrame()`, the application also passes in the chain index to the most recently updated texture.

## Frame Timing

It is critical in VR that we never show the user a stale frame.

`vrapi_SubmitFrame()` controls the synthesis rate through an application specified specified frame parameter, `SwapInterval`. It also determines the point where the calling thread gets released, currently the halfway point of the predicted display refresh cycle.

`vrapi_SubmitFrame()` only returns when both these conditions are met:

* the previous eye images have been consumed by the asynchronous time warp (ATW) thread
* at least the specified minimum number of V-syncs have passed since the last call to vrapi\_SubmitFrame().


The ATW thread consumes new eye images and updates the V-sync counter halfway through a display refresh cycle. This is the first time ATW can start updating the first eye, covering the first half of the display. As a result, `vrapi_SubmitFrame()` returns and releases the calling thread at the halfway point of the display refresh cycle.

Once `vrapi_SubmitFrame()` returns, synthesis has a full display refresh cycle to generate new eye images up to the next midway point. At the next halfway point, the time warp has half a display refresh cycle (up to V-sync) to update the first eye. The time warp then effectively waits for V-sync and then has another half a display refresh cycle (up to the next-next halfway point) to update the second eye. The asynchronous time warp uses a high priority GPU context and will eat away cycles from synthesis, so synthesis does not have a full display refresh cycle worth of actual GPU cycles. However, the asynchronous time warp tends to be very fast, leaving most of the GPU time for synthesis.

Instead of just using the latest sensor sampling, synthesis uses predicted sensor input for the middle of the time period during which the new eye images will be displayed. This predicted time is calculated using `vrapi_GetPredictedDisplayTime()`. The number of frames predicted ahead depends on the pipeline depth, the extra latency mode, and the minimum number of V-syncs in between eye image rendering. Less than half a display refresh cycle before each eye image will be displayed, ATW will get new predicted sensor input using the very latest sensor sampling. ATW then corrects the eye images using this new sensor input. In other words, ATW always correct the eye images even if the predicted sensor input for synthesis is not perfect. However, the better the prediction for synthesis, the less black will be pulled in at the edges by the asynchronous time warp.

The application can improve the prediction by fetching the latest predicted sensor input right before rendering each eye, and passing a, possibly different, sensor state for each eye to `vrapi_SubmitFrame()`. However, it is very important that both eyes use a sensor state that is predicted for the exact same display time, so both eyes can be displayed at the same time without causing intra frame motion judder. While the predicted orientation can be updated for each eye, the position must remain the same for both eyes, or the position would seem to judder "backwards in time" if a frame is dropped.

Ideally the eye images are only displayed for the `SwapInterval` display refresh cycles that are centered about the eye image predicted display time. In other words, a set of eye images is first displayed at **Predicted Display Time** - (`SwapInterval` / 2) display refresh cycles. The eye images should never be shown before this time because that can cause intra frame motion judder. Ideally the eye images are also not shown after **Predicted Display Time** + (`SwapInterval` / 2) display refresh cycles, but this may happen if synthesis fails to produce new eye images in time.

## Latency Examples





### Diagram Legend



![](/images/documentationmobilesdklatestconceptsmobile-vrapi-0.png)



### SwapInterval = 1, ExtraLatencyMode = off

* Expected single-threaded simulation latency is 33 milliseconds
* ATW reduces this to 8-16 milliseconds.




![](/images/documentationmobilesdklatestconceptsmobile-vrapi-1.png)



### SwapInterval = 1, ExtraLatencyMode = on

* Expected single-threaded simulation latency is 49 milliseconds.
* ATW reduces this to 8-16 milliseconds.




![](/images/documentationmobilesdklatestconceptsmobile-vrapi-2.png)



### SwapInterval = 2, ExtraLatencyMode = off

* Expected single-threaded simulation latency is 58 milliseconds.
* ATW reduces this to 8-16 milliseconds.




![](/images/documentationmobilesdklatestconceptsmobile-vrapi-3.png)



### SwapInterval = 2, ExtraLatencyMode = on

* Expected single-threaded simulation latency is 91 milliseconds.
* ATW reduces this to 8-16 milliseconds.




![](/images/documentationmobilesdklatestconceptsmobile-vrapi-4.png)


