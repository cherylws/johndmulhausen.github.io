---
title: Mobile Native SDK Migration Guide
---
This section details migrating from earlier versions of the Mobile SDK for native development. 

## Migrating to Mobile SDK 1.18.0

This section is intended to help you upgrade from the Oculus Mobile SDK version 1.17.0 to 1.18.0.

### Overview

* This release provides support for the Samsung Galaxy Note 9 smartphone.


### VrApi Changes

* Added Samsung Galaxy Note 9 Device Type to the API.


* Explicit completion fences are now marked deprecated and will be removed in a future SDK.


* Deprecated vrapi\_SetTextureSwapchainHandle has been removed from the API.


* Deprecated ovrTextureSwapChain type VRAPI\_TEXTURE\_TYPE\_2D\_EXTERNAL has been removed from the API.


* Deprecated ovrLayerHeader parameter SurfaceTextureObject\_DEPRECATED has been removed from the API. 


### Build Changes

The Android build scripts used by the SDK samples now use c++\_static for the C++ runtime as gnustl\_static is deprecated. For more information, see <https://developer.android.com/ndk/guides/cpp-support>. 

## Migrating to Mobile SDK 1.17.0

This section is intended to help you upgrade from the Oculus Mobile SDK version 1.16.0 to 1.17.0.

### Overview

* There are no developer-facing changes in this release.


## Migrating to Mobile SDK 1.16.0

This section is intended to help you upgrade from the Oculus Mobile SDK version 1.15.0 to 1.16.0.

### Overview

* This release exposes experimental Vulkan support for the Oculus Go.


### VrApi Changes

* Android gamepad events will now be eaten in the lower level system, since they are exposed through the Input API. This behavior can be changed by setting the ovrProperty VRAPI\_EAT\_NATIVE\_GAMEPAD\_EVENTS to false. If this property is set to false on native activity apps, they must handle the events.


* The default behavior for recenter is to additionally recenter the headset for applications built with 1.16.0 and higher. This behavior can be disabled by setting the ovrProperty VRAPI\_REORIENT\_HMD\_ON\_CONTROLLER\_RECENTER to false.


* VrApi Vulkan entry points and structure types are now exposed. See the new VrCubeWorld\_Vulkan sample for example API usage.


## Migrating to Mobile SDK 1.15.0

This section is intended to help you upgrade from the Oculus Mobile SDK version 1.14.0 to 1.15.0.

### Overview

This release provides support for the Samsung Galaxy A8 smartphone.

### VrApi Changes

* Added Samsung A8 Star Device Type to the API. 


* Added a new entry point, vrapi\_SetTextureSwapChain3, for creating a texture SwapChain by passing a platform specific texture format instead of the ovrTextureFormat type. The available formats may be queried by passing VRAPI\_SYS\_PROP\_SUPPORTED\_SWAPCHAIN\_FORMATS to vrapi\_GetSystemPropertyInt64Array. 


* vrapi\_SetTextureSwapChainHandle has been marked deprecated and should no longer be used.


* Deprecated ovrFrameLayerFlags flag, VRAPI\_FRAME\_LAYER\_FLAG\_WRITE\_ALPHA, and corresponding ovrFrameLayerBlend blend modes, VRAPI\_FRAME\_LAYER\_BLEND\_DST\_ALPHA and VRAPI\_FRAME\_LAYER\_BLEND\_ONE\_MINUS\_DST\_ALPHA, have been removed from the API.


* Added new entry points for creating and obtaining a cross-process friendly Android Surface SwapChain, vrapi\_CreateAndroidSurfaceSwapChain and vrapi\_GetTextureSwapChainAndroidSurface. 


* ovrTextureType VRAPI\_TEXTURE\_TYPE\_2D\_EXTERNAL and corresponding ovrLayerHeader2 SurfaceTextureObject are marked deprecated and should no longer be used. Instead the application should use the new cross-process friendly Android Surface texture SwapChain creation method, vrapi\_CreateAndroidSurfaceSwapChain.


* ovrSystemProperty VRAPI\_SYS\_PROP\_BACK\_BUTTON\_SHORTPRESS\_TIME has been removed as it should no longer be necessary when using the Input API.


* Emulation of the remote controllers as a headset now defaults to false for applications built with 1.15.0 and higher, as applications are expected to use the Input API for querying remote and headset input. To maintain the old behavior, pass false to vrapi\_SetRemoteEmulation.


* Remote controllers will no longer send Java input events when headset emulation is off. This behavior can be changed by setting the ovrProperty VRAPI\_BLOCK\_REMOTE\_BUTTONS\_WHEN\_NOT\_EMULATING\_HMT to true.


* When a back button press is detected, the Input API now reports the back button as down for an entire frame instead of only for the next input query. This behavior can be changed by setting the ovrProperty VRAPI\_LATCH\_BACK\_BUTTON\_ENTIRE\_FRAME to false.


### Input API

**Migrating from Android Java Input to VrApi Input**

Remote emulation of the headset now defaults to false, which means remotes will no longer send Java input events. Applications are expected to use the VrApi Input API for querying headset and remote input state.

For a detailed description of the Input API, see [VrApi Input API](/documentation/mobilesdk/latest/concepts/mobile-vrapi-input-api/ "This document describes using the VrApi Input API.").

Example usage can be found in the VrController native sample app.

General Concepts

* Instead of an event-based Java input system, the VrApi Input API is a C-based polling input system.


* Similar to the way the tracking pose of the remote and headset are queried per frame, the button states of the input devices can be queried per frame.


## Migrating to Mobile SDK 1.14.0

This section is intended to help you upgrade from the Oculus Mobile SDK version 1.12.0 to 1.14.0.

### Overview

This release provides support for the Samsung Galaxy s9 smartphone as well as provides support for a new gamepad input API.

### VrApi Changes

* vrapi\_Initialize can now return a new error code on failure, VRAPI\_INITIALIZE\_ALREADY\_INITIALIZED


* Added Samsung s9 Device Types to the API.


* VRAPI\_FRAME\_FLAG\_INHIBIT\_SRGB\_FRAMEBUFFER has been deprecated in favor of using the per-layer flag VRAPI\_FRAME\_LAYER\_FLAG\_INHIBIT\_SRGB\_FRAMEBUFFER.


* Input API now exposes and enumerates Gamepads.


* vrapi\_ReturnToHome has been removed.


* vrapi\_ShowSystemUIWithExtra is marked deprecated and should no longer be used.


* VRAPI\_REORIENT\_HMD\_ON\_CONTROLLER\_RECENTER property provided to allow apps the ability to opt into a behavior that combines the controller recenter action with reorienting the headset. To enable this, set the property to 1 using vrapi\_SetPropertyInt. This feature is disabled by default.
### Gamepad Input API

The VrApi Input Api now exposes gamepads in addition to the tracked remotes and the headset.

* The new enumeration for the gamepad is ovrControllerType\_Gamepad.
* The capabilities struct is ovrInputGamepadCapabilities.
* The input state struct is ovrInputStateGamepad.
* The queries are handled in the same way as the tracked remote, and the headset, using:


	+ vrapi\_enumerateInputDevices
	+ vrapi\_GetInputDeviceCapabilities
	+ vrapi\_GetCurrentInputState
	
Example:

for ( int i = 0; ; i++ ) { ovrInputCapabilityHeader cap; ovrResult result = vrapi\_EnumerateInputDevices( app->Ovr, i, &cap ); if ( result < 0 ) { Break; } if ( cap.Type == ovrControllerType\_Gamepad ) { ovrInputStateGamepad gamepadState; gamepadState.Header.ControllerType = ovrControllerType\_Gamepad; result = vrapi\_GetCurrentInputState( app->Ovr, i, &gamepadState.Header ); if ( result == ovrSuccess ) { backButtonDownThisFrame |= gamepadState.Buttons & ovrButton\_Back; aButtonDownThisFrame |= gamepadState.Buttons & ovrButton\_A; rightTriggerValueThisFrame = gamepadState.RightTrigger; leftJoystickValueThisFrame = gamepadState.LeftJoyStick; } break; } }## Migrating to Mobile SDK 1.12.0

This section is intended to help you upgrade from the Oculus Mobile SDK version 1.9.0 to 1.12.0.

### Overview

This release provides support for Oculus Go and Samsung Galaxy A8/A8+ (2018) smartphones.

### Build System Changes

The following build tool versions have been changed to:

* Android NDK r16b
* Gradle 4.3.1
* Android Plugin for Gradle 3.0.1
* Android SDK Build-Tools 26.0.2
Manifest requirements have been updated to account for new Android-OS versions, please see the [Android Manifest Settings](/documentation/mobilesdk/latest/concepts/mobile-native-manifest/ "Configure your manifest with the necessary VR settings, as shown in the following manifest segment.") page for more information. 

### VrApi Changes

* Added a mechanism to specify the Foveation Level for the Eye-Buffer SwapChain Textures.
* Added Oculus Go Device Types to the API.
* Added Samsung A-series (2018) Device Types to the API.
* Added a new ovrModeFlags flag, VRAPI\_MODE\_FLAG\_CREATE\_CONTEXT\_NO\_ERROR, to support applications which want to create a no-error GL context.
* VRAPI\_TEXTURE\_SWAPCHAIN\_FULL\_MIP\_CHAIN has been removed. Applications will need to explicitly pass in the number of mipLevels on SwapChain creation.
* Controllers are now affected by the application specified Tracking Transform.
* The SwapChain represented by VRAPI\_DEFAULT\_TEXTURE\_SWAPCHAIN now defaults to white instead of black. This is to support solid color frames of more than just black. The application layer’s ColorScale parameter will determine the solid color used.
* The ovrMobile structure will now always be freed on vrapi\_LeaveVrMode.
* Applications are now required to pass through explicit EGL objects (Display, ShareContext, NativeWindow) to vrapi\_EnterVrMode, otherwise the call will fail.
* VRAPI\_SYS\_PROP\_BACK\_BUTTON\_DOUBLETAP\_TIME has been removed. If applications implement double-tap logic, they can still detect this by checking if the time is less than the VRAPI\_SYS\_PROP\_BACK\_BUTTON\_SHORTPRESS\_TIME.
### Foveation

The new Foveation API allows the application to adjust the multi-resolution level for the eye-texture SwapChain.

This value may be specified using the following API call:

vrapi\_SetPropertyInt( &Java, VRAPI\_FOVEATION\_LEVEL, level );Where:

* Level = 0 disables multi-resolution
* Level = 1 low setting (good image quality, not as good performance gains)
* Level = 2 medium setting
* Level = 3 maximum setting
Currently, this is only available for Oculus Go developer kits. More information can be found in the High Fidelity OC4 talk (<https://youtu.be/pjg309WSzlM?t=1677>).

### LibOVRKernel Changes

OVR\_Geometry source files have been moved to VrAppFramework.

### VrAppFramework Changes

OVR\_Geometry source files have been added to VrAppFramework.

LoadTextureBuffer now generates mipmaps after loading png / jpg / bmp files.

Double-tap Back-Button logic has been removed.

## Migrating to Mobile SDK 1.9.0

This section is intended to help you upgrade from the Oculus Mobile SDK version 1.7.0 to 1.9.0.

### Overview

This release provides support for a new frame submission path which allows for new layer types such as Cylinder, Cube, and Equirect; it enables you to specify a user-defined tracking transform; and it adds support for a new performance API.

### Build System Changes

* We recommend NDK version r15c . With NDK r15, app\_dummy is now deprecated in favor of force exporting ANativeActivity\_onCreate.
* Pre-built libraries are no longer provided by default for the VrAppFramework and VrAppSupport libraries. If your application build files are relying on the pre-built libraries, you will need to change your build files to reference the library’s build path as **Projects/Android** instead of **Projects/AndroidPrebuilt**.
### VrApi Changes

* This version adds a new entry point, vrapi\_SubmitFrame2, which adds support for flexible layer lists, new layer types, and a single fence to signal completion for the frame. This new frame submission API no longer takes performance parameters as input, and therefore, the new performance API should be used when moving to this path.
* New entry points were added for specifying performance parameters:
	+ vrapi\_SetClockLevels
	+ vrapi\_SetPerfThread
	+ vrapi\_SetExtraLatencyMode
	
* ovrHeadModelParms and corresponding helper functions were removed from the API. Applications should no longer apply the head model to the tracking head pose as this is done by the VrApi runtime.
* New entry points for specifying a user-defined tracking transform have been added. The default tracking transform is Eye-Level.
* vrapi\_RecenterInputPose has been marked deprecated and should not be used.
* VRAPI\_SYS\_STATUS\_HEADPHONES\_PLUGGED\_IN is no longer provided on the API. For an example of how to query the headphone plugged state, see VrFrameBuilder in the native SDK library, VrAppFramework.
* The default swapchain provided by VrApi has been renamed to VRAPI\_DEFAULT\_TEXTURE\_SWAPCHAIN. Note that if you want an application to create a frame of solid black, the ColorScale parameter on the layer must be set to { 0.0f, 0.0f, 0.0f, 0.0f } to prevent any compatibility issues with newer runtimes which expect the ColorScale to be set.
### Frame Submission Updates

The new frame submission API adds support for flexible layer lists and now requires only one completion fence to represent the entire frame. Performance parameters are no longer specified through this API, and should instead be specified through the new Performance API (see below).

The following is an example of how to construct frame submission with the new API for the simple case of basic eye buffer rendering:

ovrLayerProjection2 & worldLayer = Layers[LayerCount++ ].Projection; worldLayer = vrapi\_DefaultLayerProjection2(); worldLayer.HeadPose = Tracking.HeadPose; for ( int eye = 0; eye < VRAPI\_FRAME\_LAYER\_EYE\_MAX; eye++ ) { worldLayer.Textures[eye].ColorSwapChain =ColorTextureSwapChain[eye]; worldLayer.Textures[eye].SwapChainIndex = TextureSwapChainIndex; worldLayer.Textures[eye].TexCoordsFromTanAngles = TexCoordsFromTanAngles; } ovrLayerHeader2 * LayerHeaderList[ovrMaxLayerCount] = {}; for ( int i = 0; i < LayerCount; i++ ) { LayerHeaderList[i] = &Layers[i].Header; } ovrSubmitFrameDescription2 frameDesc = {}; frameDesc.Flags = 0; frameDesc.SwapInterval = 1; frameDesc.FrameIndex = FrameIndex; frameDesc.CompletionFence = (size\_t)Fence->Sync; frameDesc.DisplayTime = PredictedDisplayTime; frameDesc.LayerCount = LayerCount; frameDesc.Layers = LayerHeaderList; vrapi\_SubmitFrame2( OvrMobile, &frameDesc );### Performance API

Performance parameters such as clock levels, application high-performance threads, and extra latency mode are now specified independently of frame submission via the following performance API:

vrapi\_SetClockLevels( ovr, PerformanceParms.CpuLevel, PerformanceParms.GpuLevel ); vrapi\_SetPerfThread( ovr, VRAPI\_PERF\_THREAD\_TYPE\_MAIN,PerformanceParms.MainThreadTid ); vrapi\_SetPerfThread( ovr, VRAPI\_PERF\_THREAD\_TYPE\_RENDERER,PerformanceParms.RenderThreadTid ); vrapi\_SetExtraLatencyMode( ovr, VRAPI\_EXTRA\_LATENCY\_MODE\_OFF );Note that these entry points take an ovrMobile pointer and therefore should only be called when in VR Mode, ie between vrapi\_EnterVrMode and vrapi\_LeaveVrMode. The performance parameters provided by the application will take effect on the next call to vrapi\_SubmitFrame(2).

### Tracking Transform API

The new tracking transform API allows applications to specify which space the tracking poses are reported in. The default tracking transform is Eye-Level. To change the transform space, the application may call the following:

vrapi\_SetTrackingTransform( ovr, vrapi\_GetTrackingTransform( ovr, VRAPI\_TRACKING\_TRANSFORM\_SYSTEM\_CENTER\_FLOOR\_LEVEL ) );### Head Model Updates

The head model is now applied internally in the VrApi runtime, and ovrHeadModelParms and corresponding helper functions are no longer present on the API.

Applications migrating from SDKs 1.7.0 or earlier should no longer apply their own head model. Helper functions for deriving IPD and eye height from the ovrTracking2 data have been added to VrApi\_Helpers.h.

If you previously built an application with SDK 1.7.0 and your app assumes 1) that poses will have the head model applied, and 2) the y-position is relative to the floor, then update your application to issue the following call immediately after vrapi\_EnterVrMode() to get the expected behavior:

vrapi\_SetTrackingTransform( ovr, vrapi\_GetTrackingTransform( ovr, VRAPI\_TRACKING\_TRANSFORM\_SYSTEM\_CENTER\_FLOOR\_LEVEL ) );

### VrAppFramework Changes

VrAppFramework has been ported to work with the new frame submission path, performance api, and user-defined tracking transform api.

## Migrating to Mobile SDK 1.7.0

This section is intended to help you upgrade from the Oculus Mobile SDK version 1.5.0 to 1.7.0.

### Overview

Mobile SDK 1.7.0 provides a new VrApi interface method for obtaining predicted tracking information along with the corresponding view and projection matrices as well as provides build system improvements and native debugging support with *externalNativeBuild*.

### Build System Changes

* The SDK now uses *externalNativeBuild* for *ndkBuild* instead of the deprecated *ndkCompile* path. *externalNativeBuild* provides a more robust Native Debugging mechanism that works out of the box and allows for stepping seamlessly between Java and Native code. Ensure you set the ANDROID\_NDK\_HOME environment variable to your ndk path location.
* Android KitKat support has been deprecated. Both the minSdkVersion and compileSdkVersion must now be 21 (Lollipop 5.0) or later.
* The build tools have been updated to the following versions: 
	+ Android SDK Build Tools Revision 25.0.1
	+ Android Plugin for Gradle 2.3.2
	+ Gradle 3.3
	
* We recommend NDK version r14b. 
### VrApi Changes

* A new entry point, vrapi\_GetPredictedTracking2(), was added for querying the predicted tracking info along with corresponding view and projection matrices for each eye. 
* The default head model is now applied in vrapi\_GetPredictedTracking() and vrapi\_GetPredictedTracking2() for apps targeting SDK 1.7.0 and higher. Apps should no longer apply the head model themselves.
* For apps targeting SDK 1.7.0 and higher, the head pose Y translation will now include eye height above floor.
* The vrapi\_GetCenterEye() helper functions have been removed and replaced with vrapi\_GetFromPose()* helper functions to remove the notion of a 'center eye'.
* VrApi\_LocalPrefs.h has been removed. Applications can use android system properties for any development debug needs.
* VRAPI\_FRAME\_LAYER\_FLAG\_WRITE\_ALPHA and DST\_ALPHA layer blend modes have been deprecated.
* vrapi\_Initialize now returns an error code when the Oculus System Driver is not found on the device instead of forcing the app to exit(0).
### LibOVRKernel Changes

Deprecated OVR\_Math constants have been removed. See OVR\_Math.h for the equivalent replacements.

### VrAppFramework Changes

 VrAppFramework now queries the predicted tracking state using the new vrapi\_GetPredictedTracking2 method and, as such, no longer explicitly applies the head model or manages head model parameters. 

 The following methods are therefore no longer provided: 

* const ovrHeadModelParms & GetHeadModelParms() const;
* void SetHeadModelParms( const ovrHeadModelParms & parms );
### VrModel changes

* ModelFile now has additional data structures that describe a full scene of data, instead of just a single ModelDef with a list of draw surfaces.
* LoadModelFile(...) now returns nullptr if the system failed to load the file.
* OvrSceneView.GetWorldModel(...) now returns a pointer instead of a reference.
* The correct way to iterate over all the draw surfaces in a model file is now: for ( int i = 0; i < modelFile->Models.GetSizeI(); i++ ) { for ( int j = 0; j < modelFile->Models[i].surfaces.GetSizeI(); j++ ) { // work } }
* ModelState.modelMatrix is now private and must be accessed through the Get and Set commands.
## Migrating to Mobile SDK 1.5.0

This section is intended to help you upgrade from the Oculus Mobile SDK version 1.0.4 to 1.5.0.

### Overview

Mobile SDK 1.5.0 provides:

* VrApi Input API for Gear VR Controller and Gear VR headset
* Experimental 64-bit SDK libraries
* Removal of deprecated DrawEyeView render path.
* Removal of deprecated VrApi Layer Types.
* Removal of deprecated VrApi Frame Flags.
### Build System Changes

We now recommend NDK version r13b.

We now provide experimental 64-bit SDK Libraries at the following library path: Libs/Android/arm64-v8a/

### VrApi Changes

VrApi now provides a new Input API which includes support for the Gear VR Controller and headset. See [VrApi Input API](/documentation/mobilesdk/latest/concepts/mobile-vrapi-input-api/ "This document describes using the VrApi Input API.") and VrApi/Include/VrApi\_Input.h. For example usage, see VrSamples/Native/VrController/.

The deprecated ovrFrameLayerType types are now removed. Explicit indices should be used to index the layer list instead.

The deprecated TimeWarp Debug Graph ovrFrameFlags types are now removed. OvrMonitor should be used for performance analysis instead. For more information, see [Oculus Remote Monitor](/documentation/mobilesdk/latest/concepts/mobile-remote-monitor/#mobile-remote-monitor "The Oculus Remote Monitor client connects to VR applications running on remote devices to capture, store, and analyze data streams.").

### LibOVRKernel Changes

OVR\_GlUtils files have been moved to VrAppFramework.

### VrAppFramework Changes

OVR\_GlUtils files have been added to VrAppFramework.

VrAppFramework no longer overrides application specified frame parameters : FrameIndex, MinimumVSyncs, PerformanceParms.

Note: If your application was previously relying on this behavior, make sure to add the following to your ovrFrameParms per-frame set up:frameParms.FrameIndex = vrFrame.FrameNumber; frameParms.MinimumVsyncs = app->GetMinimumVsyncs(); frameParms.PerformanceParms = app->GetPerformanceParms();VrAppFramework no longer provides the deprecated DrawEyeView render path. See "Restructing App Rendering For Multi-view" in the 1.0.3 SDK Migration section for more information regarding how to restructure your application to use the multiview compatible render path. The VrSamples included with the SDK also provides examples of this render path.

## Migrating to Mobile SDK 1.0.4

This section is intended to help you upgrade from the Oculus Mobile SDK version 1.0.3 to 1.0.4.

### Overview

Mobile SDK 1.0.4 provides :

* System Utilities Library Dependency is removed and functionality is handled directly within VrApi.
* Long-press back button handling (including gaze timer rendering) is now detected and handled directly within VrApi. Applications should no longer implement this logic.
* VrApi Loader is now Java free.
* The VrApi implementation is now distributed through the Oculus System Driver application.
### Build System Changes

The SDK now defaults to building with clang as GCC is no longer supported starting with ndk r13 and higher. See NDK Release Notes rev 13 for more information.

We now recommend NDK version r12b.

SDK libraries no longer provide jar file equivalents. The aar files should be used instead.

The SDK now provides both debug and release versions of the sdk libraries. Note the new paths to these libraries:

* Libs/Android/armeabi-v7a/Release/
* Libs/Android/aar/Release/
### VrApi Changes

VrApi now handles Long-Press Back Button detection and logic to show the UM as well as the gaze timer rendering on Back Button down.

VrApi now handles System Utilities functionality behind the scenes. A new API has been provided for interacting with System Menus, see VrApi\_SystemUtils.h.

vrapi\_Initialize now handles displaying of fatal error cases internally. The application should only need to check for failure cases on return and handle appropriately, ie:

int32\_t initResult = vrapi\_Initialize( &initParms ); if ( initResult != VRAPI\_INITIALIZE\_SUCCESS ) { // As of 1.0.4, vrapi directly triggers the display of Fatal Errors in vrapi\_Initialize. vrapi\_Shutdown(); exit( 0 ); }ovrFrameLayerType types are now deprecated. Explicit indices should be used to index the layer list instead.

The TimeWarp Debug Graph has been removed. OvrMonitor should be used for performance analysis instead.

VrApi Loader is now Java free. Build files should no longer specify VrApi-Loader.aar as a dependency or VrApi:Projects:AndroidPrebuilt as a dependency path.

### VrAppFramework Changes

Input.h has been renamed to OVR\_Input.h.

Calls to StartSystemActivity( PUI\_XXX ) should be replaced with ShowSystemUI( VRAPI\_SYS\_UI\_XXX ).

Apps should remove Back Button Long Press Handling as this is now handled directly by VrApi. The following input key event is no longer provided: KEY\_EVENT\_LONG\_PRESS .

### VrAppsupport Changes

SystemUtils

The System Utils Library has been removed and all functionality subsumed by VrApi.

Build files should no longer specify systemutils.a or SystemUtils.aar as build dependencies. Any references to "SystemActivities.h" should be replaced with "VrApi\_SystemUtils.h".

Values for BACK\_BUTTON\_DOUBLE\_TAP\_TIME\_IN\_SECONDS and BACK\_BUTTON\_SHORT\_PRESS\_TIME\_IN\_SECONDS are now exposed on the VrApi System Property interface and can be queried as:

float doubleTapTimeInSeconds = vrapi\_GetSystemPropertyFloat( &app->Java, VRAPI\_SYS\_PROP\_BACK\_BUTTON\_DOUBLETAP\_TIME );

float shortPressTimeInSeconds = vrapi\_GetSystemPropertyFloat( &app->Java, VRAPI\_SYS\_PROP\_BACK\_BUTTON\_SHORTPRESS\_TIME );

Applications are no longer responsible for managing the SystemUtils app events and should remove the following function calls:

* SystemActivities\_Init
* SystemActivities\_Shutdown
* SystemActivities\_Update
* SystemActivities\_PostUpdate
Note: Recenter-on-mount is now handled directly within VrApi. Apps do not need to implement this logic any longer. If an application needs to detect that a recenter has occurred, they can now do so through checking a recenter count through VrApi, eg:const int currentRecenterCount = vrapi\_GetSystemStatusInt( &Java, VRAPI\_SYS\_STATUS\_RECENTER\_COUNT ); // Determine if the recenter count has changed since last frame if ( currentRecenterCount != RecenterCount ) { // reset menu orientations RecenterCount = currentRecenterCount; }SystemActivities\_SendIntent and SystemActivities\_SendLaunchIntent are no longer provided. Instead, the versions provided by VrAppframework can be used: SendIntent and SendLaunchIntent.

SystemActivities\_ReturnToHome is no longer provided. vrapi\_ReturnToHome should be used instead.

VrGui

The Gaze Timer has been removed as it is now handled directly by VrApi.

ShowInfoText and DebugFont is now provided through VrGui.

## Migrating to Mobile SDK 1.0.3

This section is intended to help you upgrade from the Oculus Mobile SDK version 1.0.0 to 1.0.3.

### Overview

Mobile SDK 1.0.3 provides support for multi-view rendering. In order for your application to take advantage of multi-view, you will need to restructure your application rendering to return a list of render surfaces from Frame instead of relying on the DrawEyeView path. Information regarding how to set up your application rendering for multi-view rendering can be found in "Restructing App Rendering For Multi-view" below.

Note: The DrawEyeView render path is deprecated and will be removed in a future SDK update.To make the VrApi more explicit and to make integration with heavily threaded engines easier, the EGL objects and ANativeWindow that are used by the VrApi can now be **explicitly** passed through the API.

The VrAppInterface has been refactored to simplify the interface, support multi-view rendering, and to enforce per-frame determinism.

Build steps have been moved from the Python build script into Gradle.

The following sections provide guidelines for updating your native project to the 1.0.3 mobile SDK. The native SDK samples which ship with the SDK are also a good reference for reviewing required changes (see VrSamples/Native).

### Build System Changes

The SDK now builds using gcc 4.9. For help porting your own code to gcc 4.9, refer to [https://gcc.gnu.org/gcc-4.9/porting\_to.html](https://gcc.gnu.org/gcc-4.9/porting_to.html).

The SDK now builds using Android SDK Build Tools Revision 23.0.1. All Gradle files specifying buildToolsVersion 22.0.1 should be revised to buildToolsVersion 23.0.1

Applications that build using build.py (including all projects in VrSamples/Native) will need their build configurations edited to include VrApp.gradle: 

1. In the project-level build.gradle (e.g. VrCubeWorld\_NativeActivity/Projects/Android/build.gradle), add the following lines to the top of the file: apply from: "${rootProject.projectDir}/VrApp.gradle"
2. Delete the brace-enclosed sections beginning with project.afterEvaluate and android.applicationVariants.all
Make the following changes all project-level build.gradle files:

1. In the brace-enclosed section marked android, add the following line: project.archivesBaseName = "<your project name>"
2. Make sure the brace-enclosed section marked android also contains the following: defaultConfig { applicationId "<your project application ID>" }
3. In the brace-enclosed section marked dependencies, replace the line: compile name: 'VrAppFramework', ext: 'aar' with the line: compile project(':VrAppFramework:Projects:AndroidPrebuilt') and add the following path to your settings.gradle include list: 'VrAppFramework:Projects:AndroidPrebuilt'
See VrTemplate/ gradle files for an example.

### VrApi Changes

VrApi now displays volume change overlays automatically. This behavior may be overridden if necessary by setting VRAPI\_FRAME\_FLAG\_INHIBIT\_VOLUME\_LAYER as an ovrFrameParm flag.

Note: When using the VrApi volume notifier, make sure that you do not render your own!The ANativeWindow used by the VrApi can now be explicitly passed through the API by specifying the following ovrModeParm flag:

parms.Flags |= VRAPI\_MODE\_FLAG\_NATIVE\_WINDOW;Note: While the VrApi currently continues to support the old behavior of not passing EGL objects explicitly with threading restrictions, this functionality will be removed in a future version of VrApi.ovrModeParms AllowPowerSave is now specified as an ovrModeParm flag:

parms.Flags |= VRAPI\_MODEL\_FLAG\_ALLOW\_POWER\_SAVEovrFrameLayer ProgramParms are now specified explicitly.

### LibOVRKernel Changes

ovrPose member names have changed:

Orientation -> Rotation

Position -> Translation

Size member names have changed:

Width -> w Height -> h

The Math<T> constants are deprecated in favor of the new MATH\_FLOAT\_ and MATH\_DOUBLE defines.

### VrAppFramework Changes

VrAppInterface Restructing

VrAppInterface has been refactored to simplify the interface, support multi-view, and enforce per-frame determinism.

The VrAppInterface::Frame() function signature has changed. Frame() now takes an ovrFrameInput structure that contains all of the per-frame state information needed for an application. It returns an ovrFrameResult structure that should contain all of the state information produced by a single application frame.

In particular, ovrFrameInput now contains key state changes and ovrFrameResult must return a list of surfaces to be rendered. When multi-view rendering is enabled, this list of surfaces is submitted only once, but rendered for both eyes. Prior to multi-view support, all surfaces were both submitted and rendered twice each frame.

At a minimum, Frame() must return a frame result with the center view matrix as follows:

ovrFrameResult res; res.FrameMatrices.CenterView = Scene.GetCenterEyeViewMatrix(); return res;As a result of the changes to support multi-view, DrawEyeView() is now deprecated.

OneTimeInit and NewIntent have been removed from the interface. Android intents are now passed into EnteredVrMode() along with an intentType flag. On the first entry into EnteredVrMode() after the application’s main Activity is created, intentType will be INTENT\_LAUNCH. If the application is re-launched while the main Activity is already running (normally when a paused application is resumed) with a new intent, intentType will be INTENT\_NEW. If the application was resumed without a new intent, intentType will be INTENT\_OLD.

Applications that implemented OneTimeInit() and NewIntent() must now call OneTimeInit() and NewIntent() explicitly from their overloaded EnteredVrMode() method instead. In general, this means:

* When intentType is INTENT\_LAUNCH, call OneTimeInit(), then NewIntent().
* When intentType is INTENT\_NEW, call NewIntent() only.
* When intentType is INTENT\_OLD, do not call OneTimeInit() or NewIntent().
OneTimeShutdown() has been removed from VrAppInterface. Application shutdown code must now be called from the destructor of the VrAppInterface derived class.

OnKeyEvent() was removed from VrAppInterface to allow all input events to be passed through the ovrFrameInput structure. This reduces the number of ways application code receives events to just ovrFrameInput. This requires each application to implement its own code to dispatch key events to OnKeyEvent(). The application’s existing OnKeyEvent() can remain intact and is called from the beginning of Frame() as follows:

 // process input events first because this mirrors the behavior when OnKeyEvent was // a virtual function on VrAppInterface and was called by VrAppFramework. for ( int i = 0; i < vrFrame.Input.NumKeyEvents; i++ ) { const int keyCode = vrFrame.Input.KeyEvents[i].KeyCode; const int repeatCount = vrFrame.Input.KeyEvents[i].RepeatCount; const KeyEventType eventType = vrFrame.Input.KeyEvents[i].EventType; if ( OnKeyEvent( keyCode, repeatCount, eventType ) ) { continue; // consumed the event } // If nothing consumed the key and it's a short-press of the back key, then exit the application to OculusHome. if ( keyCode == OVR\_KEY\_BACK && eventType == KEY\_EVENT\_SHORT\_PRESS ) { app->StartSystemActivity( PUI\_CONFIRM\_QUIT ); continue; } }LeavingVrMode() has been added. This will be called any time the application leaves VR mode, i.e., whenever the application is paused, stopped or destroyed.

App

CreateToast has been removed. Instead, App::ShowInfoText can be used for displaying debug text.

AppLocal

DrawScreenMask() and OverlayScreenFadeMaskProgram are no longer provided and should be implemented by the application which requires it. See VrSamples/Native/CinemaSDK for an example.

ovrDrawSurface

ovrDrawSurface has been refactored and now contains a matrix instead of a pointer to a matrix. The joints member was removed and joints must now be specified explicitly in the GlProgram uniform parms as a uniform buffer object.

ovrMaterialDef

The ovrMaterialDef interface has been merged into ovrGraphicsCommand and is marked for deprecation.

ovrMaterialDef programObject -> ovrGraphicsCommand Program.Program

ovrMaterialDef gpuState -> ovrGraphicsCommand GpuState

ovrSurfaceDef

The materialDef member has been replaced by graphicsCommand.

The cullingBounds member was removed from ovrSurfaceDef. GlGeometry now calculates and stores a localBounds.

GlGeometry

GlGeometry now calculates a localBounds on Create in order to guarantee that all geometry submitted to the renderer has valid bounds.

The BuildFadedScreenMask() function is no longer provided and should be implemented by the application which requires it. See VrSamples/Native/CinemaSDK for an example.

GlProgram

GlProgram has undergone significant refactoring for multi-view support:

Internal data members were renamed so that the first letter of each member is capitalized. For example, program is now Program.

GlProgram now defaults to building shader programs with version 300 to support multi-view. There is one exception: if a shader requires the use of image\_external (typically used for video rendering), the shader may be built with v100 due to driver incompatibility with image\_external and version 300. All drivers which fully support multi-view will support image\_external with version 300.

Any program which uses image\_external will need to make the following change so that the program is compatible with both v100 and v300, change:

#extension GL\_OES\_EGL\_image\_external : requireTo:

#extension GL\_OES\_EGL\_image\_external : enable#extension GL\_OES\_EGL\_image\_external\_essl3 : enableFor more information regarding version 300, see: https://www.khronos.org/registry/gles/specs/3.0/GLSL\_ES\_Specification\_3.00.3.pdf

Shader directives (extensions, optimizations, etc.) must now be specified separately from the main shader source. See VrSamples/Native/CinemaSDK for an example.

As part of multi-view support, uniformMvp is no longer part of GlProgram. To be multi-view compliant, apps must remove usage of Mvpm and instead use TransformVertex() for calculating the projected position, i.e.:

gl\_Position = TransformVertex( Position );Note: The TransformVertex function is provided in a default system header block which is added to every GlProgram.GlProgram now provides explicit support for uniform parm setup. The old path of relying on a small subset of hard-coded system level uniforms is now deprecated and will be removed in a future SDK. An example of setting up uniform parms with the new path is provided below.

GlTexture

GlTexture was changed to require the width and height of textures. In order to enforce this requirement, the GlTexture constructors were changed and a GlTexture cannot be implicitly constructed from an integer any longer.

Input

Application input handling was changed so that input is now passed into the application’s Frame() function via the ovrFrameInput structure. Please see the section on VrAppInterface restructuring for an explanation and example code.

VrAppFramework now also handles Android key code 82. A short-press of key code 82 opens the UM, while a long-press goes directly to Home.

### Texture Manager

 VrAppFramework now implements a Texture Manager. This allows VrGUI objects to share textures across surfaces, which in turn can make for significant load-time improvements for applications using VrGUI. At present, textures are not reference counted and will not be freed automatically when VrGUI objects are released. Projects that load significant numbers of textures onto VrGUI surfaces may need to use the texture manager to free texture memory explicitly. New instances of ovrTextureManager can be created by the application to manage separate texture memory pools. ### VrAppSupport

VrGUI

Individual instances of VrGUI components can now have names. GetComponentByName() was changed to GetComponentByTypeName() and a new template function, GetComponentByName(), exists for retrieving a VRMenuObject’s components by name. Because the new GetComponentByName() signature is different, old code calling GetComponentByName() will not compile until GetComponentByName() is changed to GetComponentByTypeName().

The OvrGuiSys::RenderEyeView() function interface has changed from:

GuiSys->RenderEyeView( Scene.GetCenterEyeViewMatrix(), viewMatrix, projectionMatrix );To:

GuiSys->RenderEyeView( Scene.GetCenterEyeViewMatrix(), viewMatrix, projectionMatrix, app->GetSurfaceRender() );Note: This functionality is specific to the DrawEyeView render path and will be removed in a future SDK.To support multi-view, VrGUI now provides an interface call for adding all gui surfaces to the application’s render surface list:

GuiSys->AppendSurfaceList( Scene.GetCenterEyeViewMatrix(), &res.Surfaces );VrLocale

The ovrLocale::Create function signature has changed:

Locale = ovrLocale::Create( *app, "default" );To:

Locale = ovrLocale::Create( *java->Env, java->ActivityObject, "default" );VrModel

The SceneView::DrawEyeView() function signature has changed::

Scene.DrawEyeView( eye, fovDegreesX, fovDegreesY );To:

Scene.DrawEyeView( eye, fovDegreesX, fovDegreesY, app->GetSurfaceRender() );### Restructuring App Rendering For Multi-view

In order to set up your rendering path to be multi-view compliant, your app should specify a list of surfaces and render state back to App Frame(). Immediate GL calls inside the app main render pass are not compatible with multi-view rendering and not allowed.

The first section below describes how to transition your app from rendering with DrawEyeview and instead return a list of surfaces back to the application framework.

The section below describes multi-view rendering considerations and how to enable it in your app.

### Return Surfaces From Frame

Set up the Frame Result:

Apps should set up the ovrFrameResult which is returned by Frame with the following steps:

1. Set up the ovrFrameParms - storage for which should be maintained by the application.
2. Set up the FrameMatrices - this includes the CenterEye and View and Projection matrices for each eye.
3. Generate a list of render surfaces and append to the frame result Surfaces list. 
	1. Note: The surface draw order will be the order of the list, from lowest index (0) to highest index.
	2. Note: Do not free any resources which surfaces in list rely on while Frame render is in flight.
	
4. Optionally, specify whether to clear the color or depth buffer with clear color.
### OvrSceneView Example

An example using the OvrSceneView library scene matrices and surface generation follows:

ovrFrameResult OvrApp::Frame( const ovrFrameInput & vrFrame ) { ... // fill in the frameresult info for the frame. ovrFrameResult res; // Let scene construct the view and projection matrices needed for the frame. Scene.GetFrameMatrices( vrFrame.FovX, vrFrame.FovY, res.FrameMatrices ); // Let scene generate the surface list for the frame. Scene.GenerateFrameSurfaceList( res.FrameMatrices, res.Surfaces ); // Initialize the FrameParms. FrameParms = vrapi\_DefaultFrameParms( app->GetJava(), VRAPI\_FRAME\_INIT\_DEFAULT, vrapi\_GetTimeInSeconds(), NULL ); for ( int eye = 0; eye < VRAPI\_FRAME\_LAYER\_EYE\_MAX; eye++ ) { FrameParms.Layers[0].Textures[eye].ColorTextureSwapChain = vrFrame.ColorTextureSwapChain[eye]; FrameParms.Layers[0].Textures[eye].DepthTextureSwapChain = vrFrame.DepthTextureSwapChain[eye]; FrameParms.Layers[0].Textures[eye].TextureSwapChainIndex = vrFrame.TextureSwapChainIndex; FrameParms.Layers[0].Textures[eye].TexCoordsFromTanAngles = vrFrame.TexCoordsFromTanAngles; FrameParms.Layers[0].Textures[eye].HeadPose = vrFrame.Tracking.HeadPose; } FrameParms.ExternalVelocity = Scene.GetExternalVelocity(); FrameParms.Layers[0].Flags = VRAPI\_FRAME\_LAYER\_FLAG\_CHROMATIC\_ABERRATION\_CORRECTION; res.FrameParms = (ovrFrameParmsExtBase *) & FrameParms; return res; }Custom Rendering Example

First, you need to make sure any immediate GL render calls are represented by an ovrSurfaceDef.

In the DrawEyeView path, custom surface rendering was typically done by issuing immediate GL calls. 

 glActiveTexture( GL\_TEXTURE0 ); glBindTexture( GL\_TEXTURE\_2D, BackgroundTexId ); glDisable( GL\_DEPTH\_TEST ); glDisable( GL\_CULL\_FACE ); GlProgram & prog = BgTexProgram; glUseProgram( prog.Program ); glUniform4f( prog.uColor, 1.0f, 1.0f, 1.0f, 1.0f ); globeGeometry.Draw(); glUseProgram( 0 ); glActiveTexture( GL\_TEXTURE0 ); glBindTexture( GL\_TEXTURE\_2D, 0 );Instead, with the multi-view compliant path, an ovrSurfaceDef and GlProgram would be defined at initialization time as follows.

static ovrProgramParm BgTexProgParms[] = { { "Texm", ovrProgramParmType::FLOAT\_MATRIX4 }, { "UniformColor", ovrProgramParmType::FLOAT\_VECTOR4 }, { "Texture0", ovrProgramParmType::TEXTURE\_SAMPLED }, }; BgTexProgram= GlProgram::Build( BgTexVertexShaderSrc, BgTexFragmentShaderSrc, BgTexProgParms, sizeof( BgTexProgParms) / sizeof( ovrProgramParm ) ); GlobeSurfaceDef.surfaceName = "Globe"; GlobeSurfaceDef.geo = BuildGlobe(); GlobeSurfaceDef.graphicsCommand.Program = BgTexProgram; GlobeSurfaceDef.graphicsCommand.GpuState.depthEnable = false; GlobeSurfaceDef.graphicsCommand.GpuState.cullEnable = false; GlobeSurfaceDef.graphicsCommand.UniformData[0].Data = &BackGroundTexture; GlobeSurfaceDef.graphicsCommand.UniformData[1].Data = &GlobeProgramColor; At Frame time, the uniform values can be updated, changes to the gpustate can be made, and the surface(s) added to the render surface list.

Note: This manner of uniform parm setting requires the application to maintain storage for the uniform data. Future SDKs will provide helper functions for setting up uniform parms and materials.An example of setting up FrameResult using custom rendering follows:

ovrFrameResult OvrApp::Frame( const ovrFrameInput & vrFrame ) { ... // fill in the frameresult info for the frame. ovrFrameResult res; // calculate the scene matrices for the frame. res.FrameMatrices.CenterView = vrapi\_GetCenterEyeViewMatrix( &app->GetHeadModelParms(), &vrFrame.Tracking, NULL ); for ( int eye = 0; eye < VRAPI\_FRAME\_LAYER\_EYE\_MAX; eye++ ) { res.FrameMatrices.EyeView[eye] = vrapi\_GetEyeViewMatrix( &app->GetHeadModelParms(), &CenterEyeViewMatrix, eye ); res.FrameMatrices.EyeProjection[eye] = ovrMatrix4f\_CreateProjectionFov( vrFrame.FovX, vrFrame.FovY, 0.0f, 0.0f, 1.0f, 0.0f ); } // Update uniform variables and add needed surfaces to the surface list. BackGroundTexture = GlTexture( BackgroundTexId, 0, 0 ); GlobeProgramColor = Vector4f( 1.0f, 1.0f, 1.0f, 1.0f ); res.Surfaces.PushBack( ovrDrawSurface( &GlobeSurfaceDef ) ); // Initialize the FrameParms. FrameParms = vrapi\_DefaultFrameParms( app->GetJava(), VRAPI\_FRAME\_INIT\_DEFAULT, vrapi\_GetTimeInSeconds(), NULL ); for ( int eye = 0; eye < VRAPI\_FRAME\_LAYER\_EYE\_MAX; eye++ ) { FrameParms.Layers[0].Textures[eye].ColorTextureSwapChain = vrFrame.ColorTextureSwapChain[eye]; FrameParms.Layers[0].Textures[eye].DepthTextureSwapChain = vrFrame.DepthTextureSwapChain[eye]; FrameParms.Layers[0].Textures[eye].TextureSwapChainIndex = vrFrame.TextureSwapChainIndex; FrameParms.Layers[0].Textures[eye].TexCoordsFromTanAngles = vrFrame.TexCoordsFromTanAngles; FrameParms.Layers[0].Textures[eye].HeadPose = vrFrame.Tracking.HeadPose; } FrameParms.ExternalVelocity = Scene.GetExternalVelocity(); FrameParms.Layers[0].Flags = VRAPI\_FRAME\_LAYER\_FLAG\_CHROMATIC\_ABERRATION\_CORRECTION; res.FrameParms = (ovrFrameParmsExtBase *) & FrameParms; return res; }### Specify the Render Mode:

In your app Configure(), specify the appropriate render mode. To configure the app to render using the surfaces returned by Frame, set the following:

settings.RenderMode = RENDERMODE\_STEREO;Note: A debug render mode option has been provided which alternates rendering between the deprecated DrawEyeView path and the new path for returning a render surface list from Frame. This aides the conversion process so it is easier to spot discrepancies between the two paths.settings.RenderMode = RENDERMODE\_DEBUG\_ALTERNATE\_STEREO;Multi-view Render Path

Before enabling the multi-view rendering path, you will want to make sure your render data is multi-view compatible. This involves:

Position Calculation

App render programs should no longer specify Mvpm directly and should instead calculate gl\_Position using the system provided TransformVertex() function which accounts for the correct view and projection matrix for the current viewID.

Per-Eye View Calculations

Apps will need to take into consideration per-eye-view calculations: Examples follow:

Per-Eye Texture Matrices:

In the DrawEyeView path, the texture matrix for the specific eye was bound at the start of each eye render pass. For multi-view, an array of texture matrices indexed by VIEW\_ID should be used.

Note: Due to a driver issue with the Adreno 420, KitKat, and version 300 programs, uniform array of matrices should be contained inside a uniform buffer object.Stereo Images:

In the DrawEyeView path, the image specific to the eye was bound at the start of each eye render pass. For multi-view, while an array of texture index by VIEW\_ID would be preferable, Android KitKat does not support the use of texture arrays. Instead, both textures can be specified in the fragment shader and the selection determined by the VIEW\_ID.

External Image Usage

Applications which make use of image\_external, i.e. video rendering applications, must take care when constructing image\_external shader programs.

Not all drivers support image\_external as version 300. The good news is that drivers which fully support multi-view will support image\_external in the version 300 path, which means image\_external programs will work correctly when the multi-view path is enabled. However, for drivers which do not fully support multi-view, these shaders will be compiled as version 100.

These shaders must continue to work in both paths, i.e., version 300 only constructs should not be used and the additional extension specification requirements, listed above, should be made.

For some cases, the cleanest solution may be to only use image\_external during Frame to copy the contents of the external image to a regular texture2d which is then used in the main app render pass (which could eat into the multi-view performance savings)

Enable Multi-view Rendering

Finally, to enable the multi-view rendering path, set the render mode in your app Configure() to the following:

settings.RenderMode = RENDERMODE\_MULTIVIEW;## Migrating to Mobile SDK 1.0.0

This section is intended to help you upgrade from the 0.6.2 SDK to 1.0.0. 

### VrApi Changes

The function vrapi\_Initialize now returns an ovrInitializeStatus. It is important to verify that the initialization is successful by checking that VRAPI\_INITIALIZE\_SUCCESS is returned.

The function vrapi\_GetHmdInfo has been replaced with vrapi\_GetSystemPropertyInt and vrapi\_GetSystemPropertyFloat. These functions use the ovrSystemProperty enumeration to get the individual properties that were previously returned on the ovrHmdInfo structure.

The functions ovr\_DeviceIsDocked, ovr\_HeadsetIsMounted, ovr\_GetPowerLevelStateThrottled, and ovr\_GetPowerLevelStateMinimum have been replaced with vrapi\_GetSystemStatusInt and vrapi\_GetSystemStatusFloat. These functions use the ovrSystemStatus enumeration to select the individual status to be queried. These functions may now be used to also query various performance metrics.

The other functions from VrApi\_Android.h wrapped Android functionality or dealt with launching or returning from System Activities (Universal Menu, et cetera). These functions were removed from VrApi because they are not considered part of the core minimal API for VR rendering. The functions to get/set brightness, comfort mode and do-not-disturb mode have been removed. The other functions are now available through the VrAppSupport/SystemUtils library. See the VrAppSupport Changes section for more detailed information about using the SystemUtils library.

The layer textures are passed to vrapi\_SubmitFrame() as "texture swap chains" (ovrTextureSwapChain). These texture swap chains are allocated through vrapi\_CreateTextureSwapChain(). It is important to allocate these textures through the VrApi to allow them to be allocated in special system memory. When using a static layer texture, the texture swap chain does not need to be buffered and the chain only needs to hold a single texture. When the layer textures are dynamically updated, the texture swap chain needs to be buffered. When the texture swap chain is passed to vrapi\_SubmitFrame(), the application also passes in the chain index to the most recently updated texture.

The behavior of the TimeWarp compositor is no longer specified by selecting a warp program with a predetermined composition layout. The ovrFrameLayers in ovrFrameParms now determine how composition is performed. The application must specify the number of layers to be composited by setting ovrFrameParms::LayerCount, and the application must initialize each ovrFrameLayer in ovrFrameParms::Layers to achieve the desired compositing. See CinemaSDK in the SDK native samples for an example of how to setup and configure layer composition.

The ovrFrameOption enumeration has been renamed to ovrFrameFlags, and the VRAPI\_FRAME\_OPTION\_* flags have been renamed to VRAPI\_FRAME\_FLAG\_*.

The VRAPI\_FRAME\_OPTION\_INHIBIT\_CHROMATIC\_ABERRATION\_CORRECTION flag has been replaced with VRAPI\_FRAME\_LAYER\_FLAG\_CHROMATIC\_ABERRATION\_CORRECTION. which is now set on ovrFrameLayer::Flags. Note that chromatic aberration correction is now disabled by default. The VRAPI\_FRAME\_LAYER\_FLAG\_CHROMATIC\_ABERRATION\_CORRECTION flag must be set on each layer that needs chromatic aberration correction. Only enable chromatic aberration correction on the layers that need it, to maximize performance and minimize power draw.

The ovrFrameLayer::WriteAlpha and ovrFrameLayer::FixedToView booleans have been replaced with the ovrFrameLayer::FlagsVRAPI\_FRAME\_LAYER\_FLAG\_WRITE\_ALPHA and VRAPI\_FRAME\_LAYER\_FLAG\_FIXED\_TO\_VIEW, respectively.

The ovrFrameLayerTexture::TextureRect member now affects composition. When there are opportunities to eliminate fragment shading work in the compositor, regions outside the TextureRect may be skipped. However, rendering must still work correctly, even if the regions are not skipped, because in some cases, regions outside the rect must still be rendered.

VrApi now allows several OpenGL objects to be explicitly passed through vrapi\_EnterVrMode and vrapi\_SubmitFrame.

The structure ovrModeParms now allows the Display, WindowSurface and ShareContext to be passed explicitly to vrapi\_EnterVrMode. If these OpenGL objects are explicitly set on the ovrModeParms, then it is not necessary to call vrapi\_EnterVrMode from a thread that has an OpenGL context current on the active Android window surface. If these objects are not explicitly set on ovrModeParms (i.e., they are set to the default value of 0), then vrapi\_EnterVrMode will behave the same way it used to, and vrapi\_EnterVrMode must be called from a thread that has an OpenGL context current on the active Android window surface.

The ovrFrameLayerTexture structure, as part of the ovrFrameParms, now allows a CompletionFence to be passed explicitly to vrapi\_SubmitFrame. If this OpenGL object is explicitly set on all layer textures, then it is not necessary to call vrapi\_SubmitFrame from the thread with the OpenGL context current that was used to render the eye images. If this object is not explicitly set on *all* layer textures, then vrapi\_SubmitFrame will behave the same it used to, and vrapi\_SubmitFrame must be called from the thread with the OpenGL context current that was used to render the eye images.

### VrAppSupport Changes

The support modules in VrAppSupport are now available as prebuilt libraries.

### SystemUtils Library

All Gear VR application interactions with the System Activities application are managed through the SystemUtils library under VrAppSupport, which contains the System Activities API. 

All native applications must now link in this VrAppSupport/SystemUtils library by including the following line in the Android.mk file and adding the SystemUtils.aar (jar additionally provided) as a build dependency:

$(call import-module,VrAppSupport/SystemUtils/Projects/AndroidPrebuilt/jni)In order to utilize the SystemUtils library, applications must do the following:

* Call SystemActivites\_Init() when the application initializes.
* Call SystemActivities\_Update() to retrieve a list of pending System Activities events.
* The application may then handle any events in this list that it wishes to process. The application is expected to call SystemActivities\_RemoveAppEvent() to remove any events that it handled.
* Call SystemActivities\_PostUpdate() during the application’s frame update.
* Call SystemActivities\_Shutdown() when the application is being destroyed.
Gear VR applications may use this API to send a specially formatted launch intent when launching the System Activities application. All applications may start System Activities in the Universal Menu and Exit to Home menu by calling SystemActivities\_StartSystemActivity() with the appropriate PUI\_ command. See the SystemActivities.h header file in the *VrAppSupport/SystemUtils/Include* folder for more details, and for a list of available commands.

In theory, Gear VR applications may receive messages from System Activities at any time, but in practice these are only sent when System Activities returns to the app that launched it. These messages are handled via SystemActivities\_Update() and SystemActivites\_PostUpdate(). When Update is called, it returns an array of pending events.

Applications may handle or consume events in this events array. If an application wishes to consume an event, it must be removed from the events array using SystemActivities\_RemoveAppEvent(). This array is then passed through PostUpdate, where default handling is performed on any remaining events that have default behaviors, such as the reorient event.

This example sequence illustrates how System Activities typically interacts with an application:

1. The user long-presses the back button.
2. The application detects the long-press and launches System Activities with SystemActivities\_StartSystemActivity and the PUI\_GLOBAL\_MENU command.
3. In the Universal Menu, the user selects Reorient.
4. System Activities sends a launch intent to the application that launched the Universal Menu.
5. System Activities sends a reorient message to the application that launched it.
6. The application receives the message and adds it to the System Activities event queue.
7. The application resumes.
8. The application calls SystemActivities\_Update() to get a list of pending events.
9. If the application has special reorient logic, e.g., to re-align UI elements to be in front of the user after reorienting, it can call vrapi\_RecenterPose(), reposition its UI, and then remove the event from list of events.
10. The application calls SystemActivities\_PostUpdate(). If the reorient event was not handled by the application, it is handled inside of PostUpdate.
In the case of an exitToHome message, the SystemUtils library always handles the message with a default action of calling finish() on the application’s main Activity object without passing it on through the Update/PostUpdate queue. This is done to allow the application to exit while still backgrounded.

The VrAppFramework library already handles System Activities events, so native applications using the VrAppFramework do not need to make any System Activities API calls. After VrAppFramework calls SystemActivities\_Update(), it places a pointer to the event array in the VrFrame object for that frame. Applications using the framework can then handle those System Activities events in their frame loop, or ignore them entirely. Any handled events should be removed from the event array using SystemActivities\_RemoveAppEvent() before the application returns from it’s VrAppInterface::Frame() method.

The Unity plugin (in Legacy 0.8+ and Utilities 0.1.3+) already includes the SystemUtils library and internally calls the System Activities API functions as appropriate. Unity applications cannot currently consume System Activities events, but can handle them by adding an event delegate using SetVrApiEventDelegate() on the OVRManager class.

### VrGui Library

The VrGui library contains functionality for a fully 3D UI implemented as a scene graph. Each object in the scene graph can be functionally extended using components. This library has dependencies on VrAppFramework and must be used in conjunction with it. See the CinemaSDK, Oculus360PhotosSDK and Oculus360Videos SDKs for examples.

### VrLocale Library

The VrLocale library is a wrapper for accessing localized string tables. The wrapper allows for custom string tables to be used seamlessly with Android’s own string tables. This is useful when localized content is not embedded in the application package itself. This library depends on VrAppFramework.

### VrModel Library

The VrModel library implements functions for loading 3D models in the .ovrScene format. These models can be exported from .fbx files using the FbxConverter utility (see FBXConverter). This library depends on rendering functionality included in VrAppFramework.

### VrSound

The VrSound library implements a simple wrapper for playing sounds using the android.media.SoundPool class. This library does not provide low latency or 3D positional audio and is only suitable for playing simple UI sound effects.

