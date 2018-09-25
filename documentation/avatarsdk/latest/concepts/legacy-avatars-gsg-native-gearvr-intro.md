---
title: Native C/C++ (Gear VR) Getting Started
---
Get started using Oculus Avatars in native GearVR code by creating an avatar project using the Native Application Framework Template.

## Download and Prepare Oculus SDKs

Our SDKs are packaged in .zip files on our developer website.

1. Download the Oculus Avatars SDK from [https://developer.oculus.com/downloads/package/oculus-avatar-sdk/](/downloads/package/oculus-avatar-sdk/) and then extract the contents to C:\dev.
2. Download the Oculus Mobile SDK from [https://developer.oculus.com/downloads/package/oculus-mobile-sdk/](/downloads/package/oculus-mobile-sdk/), create a folder in C:\dev named ovr\_sdk\_mobile, and extract the contents of the download to it.
3. Download the Oculus Platform SDK from [https://developer.oculus.com/downloads/package/oculus-platform-sdk/](/downloads/package/oculus-platform-sdk/), create a folder in C:\dev named OVRPlatformSDK, and extract the contents of the download to it.
4. Save the text below as a text file named C:\dev\OVRPlatformSDK\Android\jni\Android.mk: LOCAL\_PATH := $(call my-dir) include $(CLEAR\_VARS) LOCAL\_MODULE := libovrplatformloader LOCAL\_SRC\_FILES := ../libs/$(TARGET\_ARCH\_ABI)/$(LOCAL\_MODULE).so LOCAL\_EXPORT\_C\_INCLUDES := $(LOCAL\_PATH)/../../Include ifneq (,$(wildcard $(LOCAL\_PATH)/$(LOCAL\_SRC\_FILES))) include $(PREBUILT\_SHARED\_LIBRARY) endif
## Create a New App Using the Application Framework

Use the Native Application Framework Template to create a new Gear VR project called mirror and place your Android device OSIG file inside the assets folder.

1. Run these commands from a Windows command prompt: cd C:\dev\ovr\_sdk\_mobile\VrSamples\Native\VrTemplate make\_new\_project.bat mirror oculus
2. Connect your Android device to your computer.
3. Create an Oculus Signature File for your Android device at <https://dashboard.oculus.com/tools/osig-generator/>and then copy it to the folder C:\dev\ovr\_sdk\_mobile\VrSamples\Native\mirror\assets.
For more information, see [Creating New Apps with the Framework Template](/documentation/mobilesdk/latest/concepts/mobile-new-apps-intro/).

## Modify the Sample Code with a Gear VR App ID

The Avatar SDK Samples folder contains a Gear VR version of our Rift mirror sample. Because this sample uses Oculus platform calls, you must add your own Gear VR app ID to the sample code. 

Note: This app ID must be from a Gear VR app owned by your developer organization and your Oculus user must be subscribed to at least one release channel in that app.1. Copy the contents of C:\dev\OVRAvatarSDK\Samples\MirrorAndroid to C:\dev\ovr\_sdk\_mobile\VrSamples\Native\mirror\Src
2. Change #define APP\_ID "1221388694657274" in Src\OvrApp.cpp so that it contains the Gear VR app ID of an app that belongs to your developer organization.
## Modify the Android.mk Makefile

We need to modify the Android.mk makefile with the paths to our sources and our Avatar and Platform SDK library files.

1. Locate the Android.mk file in C:\dev\ovr\_sdk\_mobile\VrSamples\Native\mirror\Projects\Android\jni.
2. Modify the contents of Android.mk as follows:
LOCAL\_PATH := $(call my-dir) include $(CLEAR\_VARS) include ../../../../../cflags.mk LOCAL\_MODULE := ovrapp LOCAL\_SRC\_FILES := ../../../Src/OvrApp.cpp ../../../Src/AvatarManager.cpp LOCAL\_STATIC\_LIBRARIES := vrsound vrmodel vrlocale vrgui vrappframework libovrkernel LOCAL\_SHARED\_LIBRARIES := vrapi libovrplatformloader libovravatarloader include $(BUILD\_SHARED\_LIBRARY) $(call import-module,LibOVRKernel/Projects/AndroidPrebuilt/jni) $(call import-module,VrApi/Projects/AndroidPrebuilt/jni) $(call import-module,VrAppFramework/Projects/AndroidPrebuilt/jni) $(call import-module,VrAppSupport/VrGUI/Projects/AndroidPrebuilt/jni) $(call import-module,VrAppSupport/VrLocale/Projects/AndroidPrebuilt/jni) $(call import-module,VrAppSupport/VrModel/Projects/AndroidPrebuilt/jni) $(call import-module,VrAppSupport/VrSound/Projects/AndroidPrebuilt/jni) $(call import-module,../OVRPlatformSDK/Android/jni) $(call import-module,../OVRAvatarSDK/Android/jni) ## Build and Launch the Project

Run C:\dev\ovr\_sdk\_mobile\VrSamples\Native\mirror\Projects\Android\build.bat to build and launch the app on your device.

![](/images/documentation-avatarsdk-latest-concepts-legacy-avatars-gsg-native-gearvr-intro-0.jpg)  
