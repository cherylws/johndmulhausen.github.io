---
title: Changes For Release 0.7.0
---
A number of changes were made to the API since the 0.6 release. 

## Overview of Oculus SDK 0.7

The most significant change is the addition of the Direct Driver Mode and the removal of Extended Mode.

Direct Driver Mode uses features of NVIDIA Gameworks VR or AMD LiquidVR to render directly to the HMD. If the installed GPU does not support NVIDIA Gameworks VR or AMD LiquidVR, it uses Oculus Direct Mode. 

The removal of the legacy Extended Mode means that users can no longer manage the Oculus Rift as an extended monitor, which will affect some games. Additionally, Standalone Mode (which uses the Oculus Rift as the only display device) is no longer supported.

## Runtime Changes

This release represents significant changes to the runtime. Changes include:

* The runtime now supports Direct Driver Mode. Direct Driver Mode requires the latest GPU drivers:


	+ [NVIDIA Driver Version 355.83 or later](https://developer.nvidia.com/oculus-07-sdk-driver-support)
	+ [AMD Catalyst Display Driver Version 15.200.1062.1005 or later](http://support.amd.com/en-us/kb-articles/Pages/Oculus07SDK-Driver.aspx)
	
* The SDK now uses sRGB-aware rendering instead of making assumptions. Unless you update your code, rendered scenes will appear brighter than before. For more information, see [Migrating to SDK 1.27](/documentation/pcsdk/latest/concepts/release-migration/).
* Applications built against SDKs prior to 0.6 will not work with the 0.7 runtime. Developers should recompile their applications using the 0.7 SDK.
* Preliminary support for Windows 10, which requires Direct Driver Mode. If you are using Windows 10, make sure to get the recommended drivers.
* Extended Mode is no longer supported. This means that users can no longer manage the Oculus Rift as an extended monitor, which will affect some games built against SDKs prior to 0.6.
* Standalone Mode (which uses the Oculus Rift as the only display device) is no longer supported.
* The runtime no longer supports the 32-bit versions of Windows. Although you will need to use a 64-bit version to operate the runtime, 32-bit applications will still work properly.
## API Changes

This release represents a major revision of the API. Changes to the API include:

* The SDK now uses sRGB-aware rendering instead of making assumptions. Unless you update your code, rendered scenes will appear brighter than before. For more information, see [Migrating to SDK 1.27](/documentation/pcsdk/latest/concepts/release-migration/).
* Converted ovrHmd\_XXX function names to ovr\_XXX. This is for improved internal consistency and consistency with mobile.
* Changed ovrHmd from a struct pointer to an opaque pointer and left ovrHmdDesc as a separate struct.
* Removed ovrHmd\_ResetFrameTiming from the public interface, as it is no longer relevant since SDK v0.6.0 and does not appear to be in use.
* Removed ovrHmdDesc::EyeRenderOrder as it is no longer relevant.
* Changed ovrHmdDesc::ProductName and ovrHmdDesc::Manufacturer from pointers to arrays.
* Renamed ovrHmdDesc::HmdCaps to ovrHmdDesc::AvailableHmdCaps to provide available capabilities and added DefaultHmdCaps to provide the default capabilities.
* Added ovrHmdDesc::DefaultHmdCaps to convey the default caps to the user. This enables applications to support future HMDs correctly by default and allows applications to OR in caps as needed.
* Renamed ovrHmdDesc::TrackingCaps to ovrHmdDesc::AvailableTrackingCaps to provide available tracking capabilities and added DefaultTrackingCaps to provide default tracking capabilities.
* Added ovrHmdDesc::DefaultTrackingCaps to convey the default caps to the user. This enables applications to support future HMDs correctly by default and allows applications to OR in caps as needed.
* Added ovrHmdDesc::DisplayRefreshRate, which represents the nominal refresh rate of the newly created HMD.
* Removed the index parameter of ovrHmd\_Create (ovr\_Create) as we currently support a single HMD.
* Added the LUID parameter to ovrResult returned by ovrHmd\_Create (ovr\_Create).
* Added the ovrError\_DisplayLost (6000) error return value to ovr\_SubmitFrame.
* Removed ovrRenderAPIType::ovrRenderAPI\_D3D9\_Obsolete and ovrRenderAPIType::ovrRenderAPI\_D3D10\_Obsolete.
* Removed ovrHmdCaps::ovrHmdCap\_LowPersistence and made it enabled by default. This fixes a bug in which an application that didn't call ovrHmd\_SetEnabledCaps inherited the settings of the previous application instead of the default settings. 
* Removed ovrHmdCaps::ovrHmdCap\_DynamicPrediction and made it enabled by default on HMDs that support it (DK2 and later).
* Removed ovrInitFlags::ovrInit\_ForceNoDebug.
* Made ovrLogCallback take a userData parameter, so application-specific context can be conveyed by the SDK user.
* Renamed ovrHmd\_ResetOnlyBackOfHeadTrackingForConnectConf to ovr\_ResetBackOfHeadTracking.
* Added ovr\_ResetMulticameraTracking to reset the location of the headset.
* Removed ovr\_WaitTillTime, as it has been deprecated for a while and implements an undesirable spin wait.
* ovrHmd\_Detect was removed. You can now use ovr\_GetHmdDesc(nullptr) instead.
* ovrHmd\_CreateDebug was removed. To enable a virtual HMD when a physical one isn't present, use RiftConfigUtil utility. 
* ovr\_CreateSwapTextureSetD3D11 now takes an additional flags parameter.
## Known Issues

The following are known issues:

* Previously, a user could unplug the Oculus Rift and plug it back in without affecting the running app. With 0.7, the app won't continue to work unless the app recreates the shared textures.
* OpenGL-based applications can judder if the application is configured to sync to the monitor's refresh rate instead of the refresh rate of the headset. To work around this, set the NVIDIA Vertical Sync control panel option to Use the 3D Application Setting or set the AMD control panel Wait for Vertical Refresh option to disabled.
* If you receive the error message “HMD powered off, check HDMI connection” in the Oculus Configuration Utility with your headset and sensor correctly plugged in, make sure to update all of your system drivers (graphics, USB, and so on).
* The mirror window might be blank and the headset might not work after installing the 0.7 runtime and the NVIDIA 355.83 driver (or later). To fix this issue, restart your computer with the headset plugged in. You should only have to do this once.
## Migration: General Changes

1. Change ovrHmd\_XXX function references to ovr\_XXX.
2. ovr\_Create now returns an out LUID. Use the LUID to select the IDXGIAdapter on which the ID3D11Device is created.
3. Update ovr\_Create (ovrHmd\_Create) to no longer pass the index parameter as the SDK supports a single HMD.
4. Update your code to handle the ovrError\_DisplayLost (6000) error from ovr\_SubmitFrame.
5. If needed, update your code to get the HMD specifications from ovrHmdDesc. The ovrSessionstruct pointer was changed to an opaque pointer; ovrHmdDesc is now a separate struct.
6. To get information about the available capabilities of the HMD, read ovrHmdDesc::AvailableHmdCaps instead of ovrHmdDesc::HmdCaps. Applications do not need to call ovr\_SetEnabledCaps; the default caps reported by ovrHmdDesc::DefaultHmdCaps work fine.
7. To get information about the tracking capabilities of the HMD, read ovrHmdDesc::AvailableTrackingCaps instead of ovrHmdDesc::TrackingCaps. To get the default tracking capabilities, read ovrHmdDesc::DefaultTrackingCaps.
8. Do not enable ovrHmdCaps::ovrHmdCap\_LowPersistence and ovrHmdCaps::ovrHmdCap\_DynamicPrediction as they are now internal and enabled by default.
9. Remove any calls to ovr\_WaitTillTime.
## Migration: Compositor and sRGB/Gamma Correctness

Prior to Oculus SDK 0.7, the Oculus compositor treated all eye texture formats as sRGB color textures, even when marked otherwise. As a result, when applications provided sRGB-correct textures (e.g. DXGI\_FORMAT\_R8G8B8A8\_UNORM\_SRGB and GL\_SRGB8\_ALPHA8), the results would look wrong. The compositor now requires all provided textures to be labelled with correct sRGB format. If an application uses an eye texture format such as DXGI\_FORMAT\_R8G8B8A8\_UNORM, this will cause the results in the HMD display to look too bright even though the mirror texture visible on the desktop window might look normal.

There are a few ways to address this, but we will describe two of them. The first ensures that the application and Oculus compositor correctly manage sRGB. The second is for existing applications that want to make the fewest rendering changes.

Note: Oculus strongly recommends that you don't simply apply pow(2.2) in the shader that writes into an 8-bit eye texture. While the results in the final HMD output might look right initially, there will be significant luminance-banding issues that only show up under subtle visual situations.The recommended method requires you to render in an sRGB-correct fashion, and then set the texture format accordingly. For D3D11, most applications use DXGI\_FORMAT\_R8G8B8A8\_UNORM\_SRGB instead of DXGI\_FORMAT\_R8G8B8A8\_UNORM. For OpenGL, the correct format is GL\_SRGB8\_ALPHA8, but you have to make sure that the application calls glEnable(GL\_FRAMEBUFFER\_SRGB). 

In some cases, making an existing application sRGB-correct might not be straightforward. There are some implications, including sRGB-correct diffuse texture sampling, linear-space and energy-conserving shading, and GPU-accelerated gamma read/write technology that are available in any modern GPU. We expect some applications that are gamma-correct do not rely on GPU read/write conversions and have opted to handle the conversions via shader math such as applying pow(2.2) and its inverse. This approach requires some finesse which is explained in the second method.

Although not recommended, the least resistance method allows the application to keep its rendering as-is while only modifying the calls to ovr\_CreateSwapTextureSetD3D11() for D3D11 rendering or modifying the GL context state for OpenGL rendering. 

Since each render API requires different approaches, a detailed explanation is provided in the function declarations of both ovr\_CreateSwapTextureSetD3D11() and ovr\_CreateSwapTextureSetGL() in OVR\_CAPI\_D3D.h and OVR\_CAPI\_GL.h respectively. For this purpose and other potential uses, we introduced a ovrSwapTextureSetD3D11\_Typeless flag for D3D11 that allows the application to create DXGI-specific typeless textures that can have a ShaderResourceView that does not have to be the same as the RenderTargetView. Keep in mind that this also applies as a mirror texture creation flag. For OpenGL, the application can simply drop the glEnable(GL\_FRAMEBUFFER\_SRGB) while still creating a swap texture set with the format GL\_SRGB8\_ALPHA8.

For more information, refer to the "Swap Texture Set Initialization" section and the code samples provided in the SDK.

