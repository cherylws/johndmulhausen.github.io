---
title: Native Samples
---
The mobile SDK includes a set of sample projects that prove out virtual reality application development on the Android platform and demonstrate high-performance virtual reality experiences on mobile devices.

## Sample Applications and Media

The sample projects included with the SDK are provided as a convenience for development purposes. Some of these projects are similar to apps available for download from the Oculus Store. Due to the potential for conflict with these versions, we do not recommend running these sample apps on the same device on which you have installed your retail experience.

Note: Due to limitations of Android ndk-build, your Oculus Mobile SDK must not contain spaces in its path. If you have placed your Oculus Mobile SDK in a path or folder name that contains spaces, you must move or rename the folder before you build our samples.The following samples can be found in \VrSamples\:

* **Oculus 360 Photos**: A viewer for panoramic stills.
* **Oculus 360 Videos**: A viewer for panoramic videos.
* **Oculus Cinema**: Plays 2D and 3D movies in a virtual movie theater.
* **VrController**: A simple scene illustrating use of the VrApi Input API.
* **VR Compositor**: A simple scene illustrating use of the different layer types available with vrapi\_SubmitFrame2.
* **VR Cube World**: A simple scene with colorful cubes illustrating construction of basic native apps using different tools provided by the SDK. There are three versions of VR Cube World:
	+ **VrCubeWorld\_SurfaceView** is closest to the metal. This sample uses a plain Android SurfaceView and handles all Android Activity and Android Surface lifecycle events in native code. This sample does not use the application framework or LibOVRKernel - it only uses the VrApi. It provides a good example of how to integrate the VrApi in an existing engine. The MULTI\_THREADED define encapsulates the code that shows how the VrApi can be integrated into an engine with a separate renderer thread.
	+ **VrCubeWorld\_NativeActivity** uses the Android NativeActivity class to avoid manually handling all the lifecycle events. This sample does not use the application framework or LibOVRKernel - it only uses the VrAPI. It provides a good example of how to integrate the VrApi in an existing engine that uses a NativeActivity. The MULTI\_THREADED define encapsulates the code that shows how the VrApi can be integrated into an engine with a separate renderer thread.
	+ **VrCubeWorld\_Vulkan** uses the Android NativeActivity class similar to **VrCubeWorld\_NativeActivity**. The difference is that it provides an example of how to integrate the VrApi into an existing Vulkan-based engine.
	
## How to Build A Sample App

Information about how to build apps in Android Studio can be found on the [Android Studio Basics](/documentation/mobilesdk/latest/concepts/mobile-studio-basics/ "This guide introduces the Android Studio IDE and reviews some basic features.") page.

## How to Install Sample Media

Use one of the following methods to install the sample media on your mobile device.

1. Use the supplied script - 
	* Connect to the device via USB.
	* Ensure you have permissions to transfer files to the device.
	* Run installtophone.bat from your Oculus Mobile SDK directory e.g., C:\Dev\Oculus\Mobile\installToPhone.bat}.
	
2. Use an ADB command - 
	* Connect to the device via USB.
	* Ensure you have permissions to transfer files to the device.
	* Issue the following commands from your development folder e.g., C:\Dev\Oculus\Mobile\
	
	adb push sdcard\_SDK /sdcard/
	
3. Use Windows Explorer - 
	* Connect to the device via USB.
	* Ensure you have permissions to transfer files to the device.
	* Open a Windows Explorer window and transfer the contents of the sample media folder, e.g., C:\Dev\Oculus\Mobile\sdcard\_SDK\oculus\ to the mobile device location e.g., \MobileDevice\Phone\Oculus\.
	
