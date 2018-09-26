---
title: Changes For Release 0.6.0
---

A number of changes were made to the API since the 0.5 release. 

## Overview of Oculus SDK 0.6.0.1

This Oculus SDK 0.6.0.1 release introduces queue ahead. Queue ahead improves CPU and GPU parallelism and increases the amount of time that the GPU has to process frames. For more information, see [Adaptive Queue Ahead](/documentation/pcsdk/latest/concepts/dg-render/#dg-queue-ahead).

## Overview of Oculus SDK 0.6

The Oculus SDK 0.6 release introduces the compositor, a separate process for applying distortion and displaying scenes and other major changes.

There are four major changes to Oculus SDK 0.6:

* The addition of the compositor service and texture sets.
* The addition of layer support.
* Removal of client-based rendering.
* Simplification of the API.


The compositor service moves distortion rendering from the application process to the OVRServer process using texture sets that are shared between the two processes. A texture set is basically a swap chain, with buffers rotated to allow game rendering to proceed while the current frame is distorted and displayed. 

Layer support allows multiple independent application render targets to be independently sent to the HMD. For example, you might render a heads-up display, background, and game space each in their own separate render target. Each render target is a layer, and the layers are combined by the compositor (rather than the application) right before distortion and display. Each layer may have a different size, resolution, and update rate.

The API simplification is a move towards the final API, which primarily removes support for application-based distortion rendering. For more information on each of these, see the Developer Guide for this SDK release. API changes are discussed briefly below. 

## New Features in 0.6.0.1

The following are major new features for the Oculus SDK and runtime:

* Added queue ahead. Queue ahead improves CPU and GPU parallelism and increases the amount of time that the GPU has to process frames. For more information, see [Adaptive Queue Ahead](/documentation/pcsdk/latest/concepts/dg-render/#dg-queue-ahead).
* Added the Debug HUD, which provides useful information while using the HUD. For more information, see [Performance Head-Up Display](/documentation/pcsdk/latest/concepts/dg-hud/ "The Performance Head-Up Display (HUD) enables you or your users to view performance information for applications built with the SDK."). To enable it in OculusWorldDemo, press F11.
* Added two samples:


	+ ORT (Direct Quad)—verifies and demonstrates direct quads.
	+ ORT (Performance HUD)—demonstrates the performance HUD.
	
* Added additional menu options to OculusWorldDemo.


## New Features in 0.6

The following are major new features for the Oculus SDK and runtime:

* Added the compositor service, which improves compatibility and support for simultaneous applications. 
* Added layer support, which increases flexibility and enables developers to tune settings based on the characteristics and requirements of each layer.
* Significantly improved error handling and reporting. 
* Added a suite of new sample projects which demonstrate techniques and the new SDK features. 
* Removed application-side DirectX and OpenGL API shims, which results in improved runtime compatibility and reliability.
* Simplified the API, as described below. 
* Changed Extended mode to use the compositor process. Rendering setup is now identical for extended and direct modes. The application no longer needs to know which mode is being used. 
* Extended mode can now support mirroring, which was previously only supported by Direct mode. 
* Simplified the timing interface and made it more robust by moving to a single function: ovr\_GetFrameTiming.
* Fixed a number of bugs and reliability problems. 


The following are major new features for Unity:

* Disabled eye texture anti-aliasing when using deferred rendering. This fixes the blackscreen issue.
* Eliminated the need for the DirectToRift.exe in Unity 4.6.3p2 and later.
* Removed the hard dependency from the Oculus runtime. Apps now render in mono without tracking when VR isn't present.


## API Changes in 0.6

This release represents a major revision of the API. These changes significantly simplify the API while retaining essential functionality. Changes to the API include:

* Removed support for application-based distortion rendering. Removed functions include ovr\_CreateDistortionMesh, ovr\_GetRenderScaleAndOffset, and so on. If you feel that you require application-based distortion rendering, please contact Oculus Developer Relations. 
* Introduced ovrSwapTextureSets, which are textures shared between the OVRServer process and the application process. Instead of using your own back buffers, applications must render VR scenes and layers to ovrSwapTextureSet textures. Texture sets are created with ovr\_CreateSwapTextureSetD3D11/OpenGL and destroyed with ovr\_DestroySwapTextureSet.
* ovr\_BeginFrame was removed and ovr\_EndFrame was replaced with ovr\_SubmitFrame.
* Added a new layer API. A list of layer pointers is passed into ovr\_SubmitFrame. 
* Improved error reporting, including adding the ovrResult type. Some API functions were changed to return ovrResult. ovr\_GetLastError was replaced with ovr\_GetLastErrorInfo.
* Removed ovr\_InitializeRenderingShim, as it is no longer necessary with the service-based compositor.
* Removed some ovrHmdCaps flags, including ovrHmdCap\_Present, ovrHmdCap\_Available, ovrHmdCap\_Captured, ovrHmdCap\_ExtendDesktop, ovrHmdCap\_NoMirrorToWindow, and ovrHmdCap\_DisplayOff.
* Removed ovrDistortionCaps. Some of this functionality is present in ovrLayerFlags. 
* ovrHmdDesc no longer contains display device information, as the service-based compositor now handles the display device.
* Simplified ovrFrameTiming to only return the DisplayMidpointSeconds prediction timing value. All other timing information is now available through the thread-safe ovr\_GetFrameTiming. The ovr\_BeginFrameTiming and EndFrameTiming functions were removed. 
* Removed the LatencyTest functions (e.g. ovr\_GetLatencyTestResult).
* Removed the PerfLog functions (e.g. ovr\_StartPerfLog), as these are effectively replaced by ovrLogCallback (introduced in SDK 0.5).
* Removed the health-and-safety-warning related functions (e.g. ovr\_GetHSWDisplayState). The HSW functionality is now handled automatically.
* Removed support for automatic HMD mirroring. Applications can now create a mirror texture (e.g. with ovr\_CreateMirrorTextureD3D11 / ovr\_DestroyMirrorTexture) and manually display it in a desktop window instead. This gives developers flexibility to use the application window in a manner that best suits their needs, and removes the OpenGL problem with previous SDKs in which the application back-buffer limited the HMD render size. 
* Added ovrInitParams::ConnectionTimeoutMS, which allows the specification of a timeout for ovr\_Initialize to successfully complete. 
* Removed ovr\_GetHmdPosePerEye and added ovr\_CalcEyePoses.


## Bugs Fixed

The following bugs were fixed since 0.5:

* HmdToEyeViewOffset provided the opposite of the expected result; it now properly returns a vector to each eye's position from the center.
* If both the left and right views are rendered to the same texture, there is less "bleeding" between the two. Apps still need to keep a buffer zone between the two regions to prevent texture filtering from picking up data from the adjacent eye, but the buffer zone is much smaller than before. We recommend about 8 pixels, rather than the previously recommended 100 pixels. Because systems vary, feedback on this matter is appreciated.
* Fixed a crash when switching between Direct and Extended Modes.
* Fixed performance and judder issues in Extended Mode.


## Known Issues

The following are known issues:

* Pre-Kepler NVIDIA GPUs might return "No display attached to compositor" or "SubmitLayers failed" errors, which can result in a black screen for some applications. NVIDIA GTX 600 GPUs and later use the Kepler or Maxwell architectures.
* Some Intel GPUs might return "No display attached to compositor" or "SubmitLayers failed" errors, which can result in a black screen for some applications. 
* Standard RGB (sRGB) is not properly supported.
* Timeout Detection Recovery (TDR) is not properly supported.
* Windows 10 is not yet supported.
* Extended mode does not currently work with AMD GPUs due to issues in the AMD drivers.
* For NVIDIA GPUs, please use driver version 350.12. The latest NVIDIA driver is unstable with the runtime.
* Switching from Extended Mode to Direct Mode while running Oculus World Demo causes sideways rendering.
* Judder with Oculus Room Tiny Open GL examples in Windows 7.
* The Oculus Configuration Utility can crash when the Demo Scene is repeatedly run.
* Application usage of CreateDXGIFactory can result in reduced performance; applications should use CreateDXGIFactory1 instead. Support for CreateDXGIFactory is deprecated in this release and will be removed in a future release.
* For Windows 7 in Extended Mode, any monitors connected to the computer go black when the headset is on and return to normal operation when the headset is removed.
* For Windows 7 in Extended Mode, if the headset is placed above the monitor(s), all displays might go black. The workaround is to place the headset to the right or left of the monitor(s).
* PC SDK applications will crash if the OVR service is not running.


## Migration: Texture Sets and Layers

Prior to Oculus SDK 0.6, the Oculus SDK relied on the game engine to create system textures for eye rendering. To use the SDK, developers stored the API-specific texture pointers into the ovrTexture structure and passed them into ovr_EndFrame for distortion and display on the Rift. After EndFrame returned, a new frame was rendered into the texture, repeating the process Oculus SDK 0.6 changes this in two major ways.

The first is by introducing the concept of ovrSwapTextureSet, a collection of textures that are used in round-robin fashion for rendering. A texture set is basically a swap chain for rendering to the Rift, with buffers rotated to allow the game rendering to proceed while the current frame is distorted and displayed. Unlike textures in earlier SDKs, ovrSwapTextureSet and its internal textures must be created by calling ovr_CreateSwapTextureSetD3D11 or ovr_CreateSwapTextureSetGL. Implementing these functions in the SDK allows us to support synchronization and properly share texture memory with the compositor process. For more details on texture sets, we advise reading the “New Features” section on them.

The second is with the introduction of layers. Instead of a single pair of eye-buffers holding all the visual data in the scene, the application can have multiple layers of different types overlaid on each other. Layers are a large change to the API, and we advise reading the “New Features” section on them for more details. This part of the guide gives only the bare minimum instructions to port an existing single-layer app to the new API.

With the introduction of texture sets and layers, you need to make several changes to how your application handles eye buffer textures in the game engine. 

## Migration: Render Target Creation Code

Previously, the app would have used the API's standard texture creation calls to make render targets for the eye buffers - either one render target for each eye, or a single shared render target with the eyes side-by-side on it. Fundamentally the same process happens, but using the ovr_CreateSwapTextureSet function for your API instead. So the code might have been similar to the following:

```
D3D11_TEXTURE2D_DESC dsDesc;
dsDesc.Width = size.w;
dsDesc.Height = size.h;
dsDesc.MipLevels = 1;
dsDesc.ArraySize = 1;
dsDesc.Format = DXGI_FORMAT_B8G8R8A8_UNORM;
dsDesc.SampleDesc.Count = 1;
dsDesc.BindFlags = D3D11_BIND_SHADER_RESOURCE | D3D11_BIND_RENDER_TARGET;
DIRECTX.Device-&gt;CreateTexture2D(&amp;dsDesc, NULL, &amp;(eye-&gt;Tex));
DIRECTX.Device-&gt;CreateShaderResourceView(Tex, NULL, &amp;(eye-&gt;TexSv));
DIRECTX.Device-&gt;CreateRenderTargetView(Tex, NULL, &amp;(eye-&gt;TexRtv));

```

Instead, the replacement code should be similar to the following:

```
D3D11_TEXTURE2D_DESC dsDesc;
dsDesc.Width = size.w;
dsDesc.Height = size.h;
dsDesc.MipLevels = 1;
dsDesc.ArraySize = 1;
dsDesc.Format = DXGI_FORMAT_B8G8R8A8_UNORM;
dsDesc.SampleDesc.Count = 1;
dsDesc.BindFlags = D3D11_BIND_SHADER_RESOURCE | D3D11_BIND_RENDER_TARGET;
ovr_CreateSwapTextureSetD3D11(session, DIRECTX.Device, &amp;dsDesc, &amp;(eyeBuf-&gt;TextureSet));
for (int i = 0; i &lt; eyeBuf-&gt;TextureSet-&gt;TextureCount; ++i)
{
   ovrD3D11Texture* tex = (ovrD3D11Texture*)&amp;(eyeBuf-&gt;TextureSet-&gt;Textures[i]);
   DIRECTX.Device-&gt;CreateRenderTargetView(tex-&gt;D3D11.pTexture, NULL, &amp;(eyeBuf-&gt;TexRtv[i]));
}
  
```

The application must still create and track the RenderTargetViews on the textures inside the texture sets - the SDK does not do this automatically (not all texture sets need to be rendertargets). The SDK does create ShaderResourceViews for its own use.

Texture sets cannot be multisampled - this is an unfortunate restriction of the way the OS treats these textures. If you wish to use MSAA eyebuffers, you must create the MSAA eyebuffers yourself as before, then create matching non-MSAA texture sets, and have each frame resolve the MSAA eyebuffer target into the respective texture set. See the OculusRoomTiny (MSAA) sample app for more information.

Before shutting down the HMD using ovr_Destroy() and ovr_Shutdown(), make sure to destroy the texture sets using ovr_DestroySwapTextureSet.

## Migration: Scene Rendering

Scene rendering would have previously just rendered to the eyebuffers created above. Now, a texture set is a series of textures, effectively in a swap chain, so a little more work is required. Scene rendering now needs to:

* Increment the value of ovrSwapTextureSet::CurrentIndex, wrapping around to zero if it equals ovrSwapTextureSet::TextureCount. This makes sure the application is rendering to a new texture, not one that is currently being displayed.
* Select the right texture or RenderTargetView in the set with the new ovrSwapTextureSet::CurrentIndex.
* Bind that as a rendertarget and render the scene to it, just like existing code.


So previously, for each eye:

```
 DIRECTX.SetAndClearRenderTarget(pEyeRenderTexture[eye]-&gt;TexRtv, pEyeDepthBuffer[eye]);
 DIRECTX.SetViewport(Recti(eyeRenderViewport[eye]));
   
```

The new code looks more like:

```
 ovrSwapTextureSet *sts = &amp;(pEyeRenderTexture[eye]-&gt;TextureSet);
 sts-&gt;CurrentIndex = (sts-&gt;CurrentIndex + 1) % sts-&gt;TextureCount;
 int texIndex = sts-&gt;CurrentIndex;
 DIRECTX.SetAndClearRenderTarget(pEyeRenderTexture[eye]-&gt;TexRtv[texIndex], pEyeDepthBuffer[eye]);
 DIRECTX.SetViewport(Recti(eyeRenderViewport[eye]));
   
```

## Migration: Frame Submission

The game then submits the frame by calling ovr_SubmitFrame and passing in the texture set inside a layer, which replaces the older ovr_EndFrame function which took two raw ovr*Texture structures. The layer type that matches the previous eye-buffer behavior is the “EyeFov” layer type - that is, an eyebuffer with a supplied FOV, viewport, and pose. Additionally, ovr_SubmitFrame requires a few more pieces of information from the app that are now explicit instead of being implicit. Doing so allows them to dynamically adjusted, and supplied separately for each layer. The new state required is:

* The viewport on the eyebuffer used for rendering each eye. This used to be stored inside the ovrTexture but is now passed in explicitly each frame.
* The field of view (FOV) used for rendering each eye. This used to be set/queried at device creation, but is now passed in explicitly each frame. In this case we still use the default that the SDK recommended, which is now returned in ovrHmdDesc::DefaultEyeFov[]


So previously the code read:

```
ovrD3D11Texture eyeTexture[2];
for (int eye = 0; eye &lt; 2; eye++)
{
   eyeTexture[eye].D3D11.Header.API = ovrRenderAPI_D3D11;
   eyeTexture[eye].D3D11.Header.TextureSize = pEyeRenderTexture[eye]-&gt;Size;
   eyeTexture[eye].D3D11.Header.RenderViewport = eyeRenderViewport[eye];
   eyeTexture[eye].D3D11.pTexture = pEyeRenderTexture[eye]-&gt;Tex;
   eyeTexture[eye].D3D11.pSRView = pEyeRenderTexture[eye]-&gt;TexSv;
}
  ovr_EndFrame(HMD, EyeRenderPose, &amp;eyeTexture[0].Texture);
  
```

This is replaced with the following. 

```
ovrLayerEyeFov ld;
ld.Header.Type = ovrLayerType_EyeFov;
ld.Header.Flags = 0;
for (int eye = 0; eye &lt; 2; eye++)
{
  ld.ColorTexture[eye] = pEyeRenderTexture[eye]-&gt;TextureSet;
  ld.Viewport[eye] = eyeRenderViewport[eye];
  ld.Fov[eye] = HMD-&gt;DefaultEyeFov[eye];
  ld.RenderPose[eye] = EyeRenderPose[eye];
}
ovrLayerHeader* layers = &amp;ld.Header;
ovrResult result = ovr_SubmitFrame(HMD, 0, nullptr, &amp;layers, 1);
```

The slightly odd-looking indirection through the variable “layers” is because this argument to ovr_SubmitFrame would normally be an array of pointers to each of the visible layers. Since there is only one layer in this case, it's not an array of pointers, just a pointer.

## Migration: Other SDK Changes

Before you begin migration, make sure to do the following: 

* #include “OVR\_CAPI\_Util.h” and add OVR\_CAPI\_Util.cpp and OVR\_StereoProjection.cpp to your project so you can use ovr\_CalcEyePoses(..). 
* Allocate textures with ovr\_CreateSwapTextureSetD3D11(..) instead of ID3D11Device::CreateTexture2D(..) and create multiple textures as described above.


In this release, there are significant changes to the game loop. For example, the ovr_BeginFrame function is removed and ovr_EndFrame is replaced by ovr_SubmitFrame . To update your game loop:

1. Replace calls to ovr\_GetEyePoses(..) with ovr\_calcEyePoses(..):

ovrTrackingState state; ovr\_GetEyePoses(m\_hmd, frameIndex, m\_offsets, m\_poses, &amp;state); becomes:

ovrFrameTiming timing = ovr\_GetFrameTiming(m\_hmd, frameIndex); ovrTrackingState state = ovr\_GetTrackingState(m\_hmd, timing.DisplayMidpointSeconds); ovr\_CalcEyePoses(state.HeadPose.ThePose, m\_offsets, poses); 
2. Replace calls to ovr\_ConfigureRendering(..) with ovr\_GetRenderDesc(..) as described above:

ovrBool success = ovr\_ConfigureRendering(m\_hmd, &amp;apiConfig, distortionCaps, m\_fov, desc); becomes:

for (int i = 0; i &lt; ovrEye\_Count; ++i) desc[i] = ovr\_GetRenderDesc(m\_hmd, (ovrEyeType)i, m\_fov[i]); 
3. Swap the target texture each frame. Instead of rendering to the same texture or pair of textures each frame, you need to advance to the next texture in the ovrSwapTextureSet:

sts-&gt;CurrentIndex = (sts-&gt;CurrentIndex + 1) % sts-&gt;TextureCount; camera-&gt;SetRenderTarget(((ovrD3D11Texture&amp;)sts-&gt;Textures[ts-&gt;CurrentIndex]).D3D11.pTexture); 
4. Remove calls to ovr\_BeginFrame(..).
5. Replace calls to ovr\_EndFrame(..) with ovr\_SubmitFrame(..):

ovr\_EndFrame(m\_hmd, poses, textures); becomes:

ovrViewScaleDesc viewScaleDesc; viewScaleDesc.HmdSpaceToWorldScaleInMeters = 1.0f; ovrLayerEyeFov ld; ld.Header.Type = ovrLayerType\_EyeFov; ld.Header.Flags = 0; for (int eye = 0; eye &lt; 2; eye++) { viewScaleDesc.HmdToEyeViewOffset[eye] = m\_offsets[eye]; ld.ColorTexture[eye] = m\_texture[eye]; ld.Viewport[eye] = m\_viewport[eye]; ld.Fov[eye] = m\_fov[eye]; ld.RenderPose[eye] = m\_poses[eye]; } ovrLayerHeader* layers = &amp;ld.Header; ovr\_SubmitFrame(m\_hmd, frameIndex, &amp;viewScaleDesc, &amp;layers, 1); 


Please refer to OculusRoomTiny source code for an example of how ovrTextureSets can be used to submit frames in the updated game loop.

 ovr_SubmtiFrame on success can return a couple different values. ovrSuccess means distortion completed successfully and was displayed to the HMD. ovrSuccess_NotVisible means the frame submission succeeded but that what was rendered was not visible on the HMD because another VR app has focus. In this case the application should skip rendering and resubmit the same frame until submit frame returns ovrSuccess rather than ovrSuccess_NotVisible. 

The 0.6 simplifies the PC SDK, so you can remove a lot of functions that are no longer needed. To remove functions: 

1. Remove calls to ovr\_AttachToWindow(..).
2. Remove calls to ovr\_DismissHSWDisplay(..).
3. Remove calls to ovr\_GetHSWDisplayState(..).
4. Remove all references to ovrTextureHeader::RenderViewport and use your own per-texture ovrRecti viewports.


Now that you have finished updating your code, you are ready to test the results. To test the results:

1. With the HMD in a resting state, images produced by 0.6 should match ones produced by 0.5.
2. When wearing the HMD, head motion should feel just as responsive as before, even when you twitch your head side-to-side and up-and-down.
3. Use the DK2 latency tester to confirm your render timing has not changed.

