---
title: Advanced Rendering Configuration
---
By default, the SDK generates configuration values that optimize for rendering quality. 

It also provides a degree of flexibility. For example, you can make changes when creating render target textures. 

This section discusses changes you can make when choosing between rendering quality and performance, or if the engine you are using imposes constraints.

## Coping with Graphics API or Hardware Render Target Granularity

The SDK is designed with the assumption that you want to use your video memory as carefully as possible and that you can create exactly the right render target size for your needs. 

However, real video cards and real graphics APIs have size limitations (all have a maximum size; some also have a minimum size). They might also have granularity restrictions, for example, only being able to create render targets that are a multiple of 32 pixels in size or having a limit on possible aspect ratios. As an application developer, you can also impose extra restrictions to avoid using too much graphics memory. 

In addition to the above, the size of the actual render target surface in memory might not necessarily be the same size as the portion that is rendered to. The latter may be slightly smaller. However, since it is specified as a viewport, it typically does not have any granularity restrictions. When you bind the render target as a texture, however, it is the full surface that is used, and so the UV coordinates must be corrected for the difference between the size of the rendering and the size of the surface it is on. The API will do this for you, but you need to tell it the relevant information. 

The following code shows a two-stage approach for settings render target resolution. The code first calls ovr\_GetFovTextureSize to compute the ideal size of the render target. Next, the graphics library is called to create a render target of the desired resolution. In general, due to idiosyncrasies of the platform and hardware, the resulting texture size might be different from that requested.

 // Get recommended left and right eye render target sizes. Sizei recommenedTex0Size = ovr\_GetFovTextureSize(session, ovrEye\_Left, session->DefaultEyeFov[0], pixelsPerDisplayPixel); Sizei recommenedTex1Size = ovr\_GetFovTextureSize(session, ovrEye\_Right, session->DefaultEyeFov[1], pixelsPerDisplayPixel); // Determine dimensions to fit into a single render target. Sizei renderTargetSize; renderTargetSize.w = recommenedTex0Size.w + recommenedTex1Size.w; renderTargetSize.h = max ( recommenedTex0Size.h, recommenedTex1Size.h ); // Create texture. pRendertargetTexture = pRender->CreateTexture(renderTargetSize.w, renderTargetSize.h); // The actual RT size may be different due to HW limits. renderTargetSize.w = pRendertargetTexture->GetWidth(); renderTargetSize.h = pRendertargetTexture->GetHeight(); // Initialize eye rendering information. // The viewport sizes are re-computed in case RenderTargetSize changed due to HW limitations. ovrFovPort eyeFov[2] = { session->DefaultEyeFov[0], session->DefaultEyeFov[1] }; EyeRenderViewport[0].Pos = Vector2i(0,0); EyeRenderViewport[0].Size = Sizei(renderTargetSize.w / 2, renderTargetSize.h); EyeRenderViewport[1].Pos = Vector2i((renderTargetSize.w + 1) / 2, 0); EyeRenderViewport[1].Size = EyeRenderViewport[0].Size; This data is passed into ovr\_EndFrame as part of the layer description.

You are free to choose the render target texture size and left and right eye viewports as you like, provided that you specify these values when calling ovr\_EndFrame using the ovrTexture. However, using ovr\_GetFovTextureSize will ensure that you allocate the optimum size for the particular HMD in use. The following sections describe how to modify the default configurations to make quality and performance trade-offs. You should also note that the API supports using different render targets for each eye if that is required by your engine (although using a single render target is likely to perform better since it will reduce context switches). OculusWorldDemo allows you to toggle between using a single combined render target versus separate ones for each eye, by navigating to the settings menu (press the Tab key) and selecting the Share RenderTarget option.

## Forcing a Symmetrical Field of View

Typically the API will return an FOV for each eye that is not symmetrical, meaning the left edge is not the same distance from the center as the right edge.

This is because humans, as well as the Rift, have a wider FOV when looking outwards. When you look inwards, your nose is in the way. We are also better at looking down than we are at looking up. For similar reasons, the Rift’s view is not symmetrical. It is controlled by the shape of the lens, various bits of plastic, and the edges of the screen. The exact details depend on the shape of your face, your IPD, and where precisely you place the Rift on your face; all of this is set up in the configuration tool and stored in the user profile. All of this means that almost nobody has all four edges of their FOV set to the same angle, so the frustum produced will be off-center. In addition, most people will not have the same fields of view for both their eyes. They will be close, but rarely identical.

As an example, on our first generation DK1 headset, the author’s left eye has the following FOV: 

* 53.6 degrees up
* 58.9 degrees down
* 50.3 degrees inwards (towards the nose)
* 58.7 degrees outwards (away from the nose) 
In the code and documentation, these are referred to as ‘half angles’ because traditionally a FOV is expressed as the total edge-to-edge angle. In this example, the total horizontal FOV is 50.3+58.7 = 109.0 degrees, and the total vertical FOV is 53.6+58.9 = 112.5 degrees. 

The recommended and maximum fields of view can be accessed from the HMD as shown below: 

ovrFovPort defaultLeftFOV = session->DefaultEyeFov[ovrEye\_Left]; ovrFovPort maxLeftFOV = session->MaxEyeFov[ovrEye\_Left]; DefaultEyeFov refers to the recommended FOV values based on the current user’s profile settings (IPD, eye relief etc). MaxEyeFov refers to the maximum FOV that the headset can possibly display, regardless of profile settings.

The default values provide a good user experience with no unnecessary additional GPU load. If your application does not consume significant GPU resources, you might want to use the maximum FOV settings to reduce reliance on the accuracy of the profile settings. You might provide a slider in the application control panel that enables users to choose interpolated FOV settings between the default and the maximum. But, if your application is heavy on GPU usage, you might want to reduce the FOV below the default values as described in [Improving Performance by Decreasing Field of View](/documentation/pcsdk/latest/concepts/dg-render-advanced/#dg_render_advanced_fov_decrease "In addition to reducing the number of pixels in the intermediate render target, you can increase performance by decreasing the FOV that the pixels are stretched across.").

The FOV angles for up, down, left, and right (expressed as the tangents of the half-angles), is the most convenient form to set up culling or portal boundaries in your graphics engine. The FOV values are also used to determine the projection matrix used during left and right eye scene rendering. We provide an API utility function ovrMatrix4f\_Projection for this purpose: 

ovrFovPort fov; // Determine fov. ... ovrMatrix4f projMatrix = ovrMatrix4f\_Projection(fov, znear, zfar, 0); It is common for the top and bottom edges of the FOV to not be the same as the left and right edges when viewing a PC monitor. This is commonly called the ‘aspect ratio’ of the display, and very few displays are square. However, some graphics engines do not support off-center frustums. To be compatible with these engines, you will need to modify the FOV values reported by the ovrHmdDesc struct. In general, it is better to grow the edges than to shrink them. This will put a little more strain on the graphics engine, but will give the user the full immersive experience, even if they won’t be able to see some of the pixels being rendered. 

Some graphics engines require that you express symmetrical horizontal and vertical fields of view, and some need an even less direct method such as a horizontal FOV and an aspect ratio. Some also object to having frequent changes of FOV, and may insist that both eyes be set to the same. The following is a an example of code for handling this restrictive case: 

 ovrFovPort fovLeft = session->DefaultEyeFov[ovrEye\_Left]; ovrFovPort fovRight = session->DefaultEyeFov[ovrEye\_Right]; ovrFovPort fovMax = FovPort::Max(fovLeft, fovRight); float combinedTanHalfFovHorizontal = max ( fovMax.LeftTan, fovMax.RightTan ); float combinedTanHalfFovVertical = max ( fovMax.UpTan, fovMax.DownTan ); ovrFovPort fovBoth; fovBoth.LeftTan = fovBoth.RightTan = combinedTanHalfFovHorizontal; fovBoth.UpTan = fovBoth.DownTan = combinedTanHalfFovVertical; // Create render target. Sizei recommenedTex0Size = ovr\_GetFovTextureSize(session, ovrEye\_Left, fovBoth, pixelsPerDisplayPixel); Sizei recommenedTex1Size = ovr\_GetFovTextureSize(session, ovrEye\_Right, fovBoth, pixelsPerDisplayPixel); ... // Initialize rendering info. ovrFovPort eyeFov[2]; eyeFov[0] = fovBoth; eyeFov[1] = fovBoth; ... // Compute the parameters to feed to the rendering engine. // In this case we are assuming it wants a horizontal FOV and an aspect ratio. float horizontalFullFovInRadians = 2.0f * atanf ( combinedTanHalfFovHorizontal ); float aspectRatio = combinedTanHalfFovHorizontal / combinedTanHalfFovVertical; GraphicsEngineSetFovAndAspect ( horizontalFullFovInRadians, aspectRatio ); ... Note: You will need to determine FOV before creating the render targets, since FOV affects the size of the recommended render target required for a given quality. ## Improving Performance by Decreasing Pixel Density

The DK1 has a resolution of 1280x800 pixels, split between the two eyes. However, because of the wide FOV of the Rift and the way perspective projection works, the size of the intermediate render target required to match the native resolution in the center of the display is significantly higher. 

For example, to achieve a 1:1 pixel mapping in the center of the screen for the author’s field-of-view settings on a DK1 requires a much larger render target that is 2000x1056 pixels in size. 

Even if modern graphics cards can render this resolution at the required 60Hz, future HMDs might have significantly higher resolutions. For virtual reality, dropping below 60Hz provides a terrible user experience; it is always better to decrease the resolution to maintain framerate. This is similar to a user having a high resolution 2560x1600 monitor. Very few 3D applications can run at this native resolution at full speed, so most allow the user to select a lower resolution to which the monitor upscales to the fill the screen. 

You can use the same strategy on the HMD. That is, run it at a lower video resolution and let the hardware upscale for you. However, this introduces two steps of filtering: one by the distortion processing and one by the video upscaler. Unfortunately, this double filtering introduces significant artifacts. It is usually more effective to leave the video mode at the native resolution, but limit the size of the intermediate render target. This gives a similar increase in performance, but preserves more detail. 

One way to resolve this is to allow the user to adjust the resolution through a resolution selector. However, the actual resolution of the render target depends on the user’s configuration, rather than a standard hardware setting This means that the ‘native’ resolution is different for different people. Additionally, presenting resolutions higher than the physical hardware resolution might confuse some users. They might not understand that selecting 1280x800 is a significant drop in quality, even though this is the resolution reported by the hardware. 

A better option is to modify the pixelsPerDisplayPixel value that is passed to the ovr\_GetFovTextureSize function. This could also be based on a slider presented in the applications render settings. This determines the relative size of render target pixels as they map to pixels at the center of the display surface. For example, a value of 0.5 would reduce the render target size from 2000x1056 to 1000x528 pixels, which might allow mid-range PC graphics cards to maintain 60Hz. 

float pixelsPerDisplayPixel = GetPixelsPerDisplayFromApplicationSettings(); Sizei recommenedTexSize = ovr\_GetFovTextureSize(session, ovrEye\_Left, fovLeft, pixelsPerDisplayPixel); Although you can set the parameter to a value larger than 1.0 to produce a higher-resolution intermediate render target, Oculus hasn't observed any useful increase in quality and it has a high performance cost. 

OculusWorldDemo allows you to experiment with changing the render target pixel density. Navigate to the settings menu (press the Tab key) and select Pixel Density. Press the up and down arrow keys to adjust the pixel density at the center of the eye projection. A value of 1.0 sets the render target pixel density to the display surface 1:1 at this point on the display. A value of 0.5 means sets the density of the render target pixels to half of the display surface. Additionally, you can select Dynamic Res Scaling which will cause the pixel density to automatically adjust between 0 to 1. 

## Improving Performance by Decreasing Field of View

In addition to reducing the number of pixels in the intermediate render target, you can increase performance by decreasing the FOV that the pixels are stretched across. 

Depending on the reduction, this can result in tunnel vision which decreases the sense of immersion. Nevertheless, reducing the FOV increases performance in two ways. The most obvious is fill rate. For a fixed pixel density on the retina, a lower FOV has fewer pixels. Because of the properties of projective math, the outermost edges of the FOV are the most expensive in terms of numbers of pixels. The second reason is that there are fewer objects visible in each frame which implies less animation, fewer state changes, and fewer draw calls.

Reducing the FOV set by the player is a very painful choice to make. One of the key experiences of virtual reality is being immersed in the simulated world, and a large part of that is the wide FOV. Losing that aspect is not a thing we would ever recommend happily. However, if you have already sacrificed as much resolution as you can, and the application is still not running at 60Hz on the user’s machine, this is an option of last resort.

We recommend giving players a Maximum FOV slider that defines the four edges of each eye’s FOV.

ovrFovPort defaultFovLeft = session->DefaultEyeFov[ovrEye\_Left]; ovrFovPort defaultFovRight = session->DefaultEyeFov[ovrEye\_Right]; float maxFovAngle = ...get value from game settings panel...; float maxTanHalfFovAngle = tanf ( DegreeToRad ( 0.5f * maxFovAngle ) ); ovrFovPort newFovLeft = FovPort::Min(defaultFovLeft, FovPort(maxTanHalfFovAngle)); ovrFovPort newFovRight = FovPort::Min(defaultFovRight, FovPort(maxTanHalfFovAngle)); // Create render target. Sizei recommenedTex0Size = ovr\_GetFovTextureSize(session, ovrEye\_Left newFovLeft, pixelsPerDisplayPixel); Sizei recommenedTex1Size = ovr\_GetFovTextureSize(session, ovrEye\_Right, newFovRight, pixelsPerDisplayPixel); ... // Initialize rendering info. ovrFovPort eyeFov[2]; eyeFov[0] = newFovLeft; eyeFov[1] = newFovRight; ... // Determine projection matrices. ovrMatrix4f projMatrixLeft = ovrMatrix4f\_Projection(newFovLeft, znear, zfar, 0); ovrMatrix4f projMatrixRight = ovrMatrix4f\_Projection(newFovRight, znear, zfar, 0); It might be interesting to experiment with non-square fields of view. For example, clamping the up and down ranges significantly (e.g. 70 degrees FOV) while retaining the full horizontal FOV for a ‘Cinemascope’ feel. 

OculusWorldDemo allows you to experiment with reducing the FOV below the defaults. Navigate to the settings menu (press the Tab key) and select the “Max FOV” value. Pressing the up and down arrows to change the maximum angle in degrees.

## Improving Performance by Rendering in Mono

A significant cost of stereo rendering is rendering two views, one for each eye.

For some applications, the stereoscopic aspect may not be particularly important and a monocular view might be acceptable in return for some performance. In other cases, some users may get eye strain from a stereo view and wish to switch to a monocular one. However, they still wish to wear the HMD as it gives them a high FOV and head-tracking. 

OculusWorldDemo allows the user to toggle mono render mode by pressing the F7 key. 

To render in mono, your code should have the following changes:

*  Set the FOV to the maximum symmetrical FOV based on both eyes.
* Call ovhHmd\_GetFovTextureSize with this FOV to determine the recommended render target size.
* Configure both eyes to use the same render target and the same viewport when calling ovr\_EndFrame.
* Render the scene once to the shared render target.
This merges the FOV of the left and right eyes into a single intermediate render. This render is still distorted twice, once per eye, because the lenses are not exactly in front of the user’s eyes. However, this is still a significant performance increase. 

Setting a virtual IPD to zero means that everything will seem gigantic and infinitely far away, and of course the user will lose much of the sense of depth in the scene. 

Note: It is important to scale virtual IPD and virtual head motion together so, if the virtual IPD is set to zero, all virtual head motion due to neck movement is also be eliminated. Sadly, this loses much of the depth cues due to parallax. But, if the head motion and IPD do not agree, it can cause significant disorientation and discomfort. Experiment with caution!## Using Octilinear Rendering for NVIDIA Lens Matched Shading

Octilinear rendering implements NVIDIA Lens Matched Shading. You can use octilinear rendering to improve the performance of your application when it executes on an NVIDIA GPU.

Octilinear rendering avoids the need to render a significant number of pixels that would otherwise be discarded before the image is output to the headset. The application has to draw a larger image than is displayed on the Rift. It requires extra time to draw these larger images. So Lens Matched Shading allows the system to draw a smaller image, because it draws a pre-compressed image. An octilinear image appears as follows:

![](/images/documentation-pcsdk-latest-concepts-dg-render-advanced-dg-render-advanced-0.png)  
Using octilinear rendering reduces the size of the drawing area by about 20%. The bounding box remains the same as for the non-octilinear image.

The requirements for using octilinear rendering are as follows:

1. You must run your application on an NVIDIA GPU that supports lens mapped shading. (See the NVIDIA documentation for more information.)
2. You must use an NVIDIA SDK that supports the lens mapped shading feature of the GPU. (See the NVIDIA documentation for more information.)
3. You must generate textures in the right format with the NVIDIA SDK.
4. Your application must call ovr\_EnableExtension to enable the octilinear extension from the Oculus side. 
5. Then, the Oculus runtime will automatically consume your specially-format images at runtime.
## Protecting Content

There are some cases where you only want the content to display on the headset. The protected content feature is designed to prevent any mirroring of the compositor.

To use the protected content feature, configure your application to create one or more ovrTextureSwapChain objects with the ovrTextureMisc\_ProtectedContent flag specified. Any submission which references a protected swap chain is considered a protected frame; any protected frames are composited and displayed in the HMD, but are not replicated to mirrors or available to the capture buffer API. 

If the HMD is not HDCP compliant, the texture swap chain creation API will fail with ovrError\_ContentProtectionNotAvailable. If the textures can be created (HDCP-compliant HMD), but the link is broken later, the next ovr\_EndFrame call that references protected texture swap chains will fail with the ovrError\_ContentProtectionNotAvailable error. Configure your application to respond according to your requirements. For example, you might submit that next frame without protected swap chains, but at a lower quality that doesn’t require protection. Or, you might stop playback and display an error or warning to the user. 

Note: Because the mirror window is in the control of the application, if your application does not use the mirror texture, it is up to your application to render something to the preview window. Make sure your application does not display protected content. Since the surfaces are not known to be protected by the OS, they will be displayed normally inside the application that created them. To enable protected content, specify the ovrTextureMisc\_ProtectedContent flag similarly to the following:ovrTextureSwapChainDesc desc = {}; desc.Type = ovrTexture\_2D; desc.ArraySize = 1; desc.Format = OVR\_FORMAT\_R8G8B8A8\_UNORM\_SRGB; desc.Width = sizeW; desc.Height = sizeH; desc.MipLevels = 1; desc.SampleCount = 1; desc.MiscFlags = ovrTextureMisc\_DX\_Typeless | ovrTextureMisc\_ProtectedContent; desc.BindFlags = ovrTextureBind\_DX\_RenderTarget; desc.StaticImage = ovrFalse; ovrResult result = ovr\_CreateTextureSwapChainDX(session, Device, &desc, &TextureChain); 