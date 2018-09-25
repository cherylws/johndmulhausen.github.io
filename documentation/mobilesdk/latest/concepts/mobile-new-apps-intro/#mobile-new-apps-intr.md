---
title: Creating New Apps with the Framework Template
---
This section will get you started with creating new native applications using VrAppFramework.

## Template Project Using the Application Framework

VrTemplate is the best starting place for creating your own mobile app using VrAppFramework. The VrTemplate project is set up for exploratory work and as a model for setting up similar native applications using the Application Framework. 

We include the Python script make\_new\_project.py (for Mac OS X) and make\_new\_project.bat (with wrapper for Windows) to simplify renaming the project name set in the template. 

**Usage Example: Windows**

To create your own mobile app based on VrTemplate, perform the following steps:

1. Run <install path>\VrSamples\Native\VrTemplate\make\_new\_project.bat, passing the name of your new app and your company as arguments. For example: make\_new\_project.bat VrTestApp YourCompanyName
2. Your new project will now be located in <install path>\VrSamples\Native\VrTestApp. The packageName will be set to com.YourCompanyName.VrTestApp.
3. Copy your oculussig file to the Project/assets/ folder of your project. (See [Application Signing](/distribute/latest/concepts/publish-mobile-app-signing/) for more information.) 
4. Navigate to your new project directory. With your Android device connected, execute the build.bat located inside your test app directory to verify everything is working.
5. build.bat should build your code, install it to the device, and launch your app on the device. One parameter controls the build type:
	* clean - cleans the projectâ€™s build files
	* debug - builds a debug application
	* release - builds a release application
	* -n - skips installation of the application to the phone
	
The Java file VrSamples/Native/VrTestApp/java/com/YourCompanyName/vrtestapp/MainActivity.java handles loading the native library that was linked against VrApi, then calls nativeSetAppInterface() to allow the C++ code to register the subclass of VrAppInterface that defines the application. See VrAppFramework/Include/App.h for comments on the interface.

The standard Oculus convenience classes for string, vector, matrix, array, et cetera are available in the Oculus LibOVRKernel, located at LibOVRKernel\Src\. You will also find convenience code for OpenGL ES texture, program, geometry, and scene processing that is used by the demos. 

