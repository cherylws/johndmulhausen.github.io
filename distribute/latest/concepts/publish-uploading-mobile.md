---
title: Uploading Gear VR and Go Apps
---
Mobile apps have a stringent set of packaging requirements and any app you upload must be packaged accordingly. The upload validator rejects apps that do not meet these requirements.

## APK Requirements

All mobile apps, both Gear VR and Go, must be packaged as APK files and meet the following specifications:

* The APK may be up to 1GB in size.
* The APK must have an application manifest fit for a release build. See [Application Manifests for Release Builds](/distribute/latest/concepts/publish-mobile-manifest/ "The application manifest of your mobile app must conform to our specifications if you want to upload the app to the Oculus Store.").
* The APK must be signed with an Android certificate. Specifically, it must be signed with the older JAR signing scheme and not with the newer APK Signature Scheme v2 introduced in Android Nougat. See [Application Signing](/distribute/latest/concepts/publish-mobile-app-signing/ "Mobile apps may require two different types of signatures during the development and release process. These are independent but easy to confuse.").
Note: We encourage you to break large apps into separate APK and expansion files to improve both the developer and the user experience. For developers:

* Apps split into APK and expansion files take less time to upload.
* Expansion files are hosted and served from Oculus servers. There is no need to set up your own hosting such as is usually required by Unity asset bundles. 
For users:

* It takes less time to download and apply patch updates.
## APK Expansion File Requirements

You can supplement your APK file with an APK expansion file. If you are familiar with Google Play APK expansion files, be aware that Oculus APK expansion file sizes and naming patterns are different. Oculus APK expansion files must meet the following specifications:

* The APK expansion file may be up to 4 GB in size.


* There must be only one expansion file.


* The filename of the APK expansion file should be main.*versionCode*.*packageName*.obb


	+ *versionCode* - the version code of the APK you are uploading with the expansion file. For Unity developers, this is the **Bundle Version Code** in **Player Settings**.
	+ *packageName* - the package name of the APK.
	**Example:** If you are uploading APK version 3 and your package name is com.oculus.example, your expansion file name should be main.3.com.oculus.example.obb


Note: Apps with APK expansion files can only be uploaded with the [Oculus Platform Command Line Utility](/distribute/latest/concepts/publish-reference-platform-command-line-utility/ "The Oculus Platform Command Line Utility lets you upload builds to your release channels much faster than using the Oculus dashboard web interface. It also allows you to incorporate automated uploads into your existing build system.").**APK Expansion Files and APKs Must Be Updated Together**

Expansion files must be updated together with an APK. This means that even if your update contains changes only to the APK or only to the .obb, you must increment the version code for each and upload new versions of them together. 

The only exception is if you decide to stop using an expansion file and go back to distributing a single APK. In this particular scenario, you would upload a new APK but omit the --obb parameter. 

## Uploading Mobile Builds

You can upload builds through the Oculus Developer Dashboard web interface or using the Oculus Platform Command Line Utility. We recommend using the Oculus Platform Command Line Utility because it is faster. It uses delta-patching techniques to upload only the portions of your app that have changed. 

If there are any packaging problems with your app, the upload validation routines inform you after uploading your build so that you can correct the issue and try again. 

Some apps may not support all Gear VR devices, please see the [Managing Supported Devices](/distribute/latest/concepts/publish-mobile-supported-devices/ "Your mobile app may not run on all devices supported Oculus. Select the devices your app will support.") page for information about managing the devices your app supports. This can be configured anytime after you upload your app.

**Prerequisites:**

Before you can upload an app, you must first create an app page for it in the Oculus Developer Dashboard. For more information, see [App Submission and Store Review](/distribute/latest/concepts/publish-create-app/ "This guide will review the process to upload and submit an app to the Oculus Dashboard.").

**To upload your build through the web interface:**

1. Log on to the Oculus Developer Dashboard at [https://dashboard.oculus.com](https://dashboard.oculus.com/).
2. Hover over your Gear VR app and then click **Manage Build**.
3. If this is the first upload for this app, click **Upload Build**.
4. If this is not the first upload for this app, click **...** in the release channel you want to upload to and then select **Upload New Binary**.
5. Click **Choose File** and select the .apk file of your build.
**To upload your app through the command line interface:**

See our [Oculus Platform Command Line Utility](/distribute/latest/concepts/publish-reference-platform-command-line-utility/ "The Oculus Platform Command Line Utility lets you upload builds to your release channels much faster than using the Oculus dashboard web interface. It also allows you to incorporate automated uploads into your existing build system.") doc for information about using the utility. ## Supporting Gear VR and Go in the Same APK

You're able to build a single APK that runs on both the Gear VR and Oculus Go. However, there are a few things to be aware of when developing an app for both platforms.

1. **Select the correct devices** - Make sure you select the devices your app supports. Information about how to select the devices your app supports can be found on the [Managing Supported Devices](/distribute/latest/concepts/publish-mobile-supported-devices/ "Your mobile app may not run on all devices supported Oculus. Select the devices your app will support.") page.
2. **Scanned at upload** - Your app will be scanned at upload for features that are not supported on Go. We'll notify you of any issues that exist. You'll be allowed to proceed an release on Gear VR, but updates will be required to release on Go. For example, on Go you may not have the following:
	* You cannot rely on Google Play Services (e.g. Google Firebase, Google Cloud Messaging, etc), or third-party libraries that depend on Google Play Services (e.g. OneSignal) when running on Oculus Go.
	* Oculus Go does not have a 2D phone display, and therefore some app behaviors (such as push notifications, or authentication via a separate Android application) do not make sense on Oculus Go.
	* Oculus Go does not have a camera, and cannot run applications that rely upon access to a camera.
	* Oculus Go does not have a touchpad on the HMD. Your app should not refer to an HMD touchpad when running on Oculus Go.
	Additionally, we will check to ensure the following are met for Go apps:


	* Proper controller support. The Oculus Go Controller and Gear VR Controller share the same inputs: both are 3DOF controllers with clickable trackpads and an index finger trigger. Though these two devices provide the same inputs, the physical design of each is distinct. If your app displays a visible controller, you should change the model displayed depending on whether you are running on Gear VR or Oculus Go. Alternatively, a stylized controller model that is distinct from both the Oculus Go Controller and the Gear VR Controller is acceptable.
	* Recent SDK. Some very old Gear VR apps are still running on pre-1.0 releases of the Mobile SDK. These apps are not supported on Oculus Go. 
	
* **[Application Manifests for Release Builds](/distribute/latest/concepts/publish-mobile-manifest/)**  
 The application manifest of your mobile app must conform to our specifications if you want to upload the app to the Oculus Store.
* **[Application Signing](/distribute/latest/concepts/publish-mobile-app-signing/)**  
Mobile apps may require two different types of signatures during the development and release process. These are independent but easy to confuse.
* **[Managing Supported Devices](/distribute/latest/concepts/publish-mobile-supported-devices/)**  
Your mobile app may not run on all devices supported Oculus. Select the devices your app will support. 
