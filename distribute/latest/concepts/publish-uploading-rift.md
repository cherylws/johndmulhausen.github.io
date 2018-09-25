---
title: Uploading Rift Apps
---
 Rift apps are packaged as .zip files if uploading through the web interface. If uploading through the command line interface, your app is uploaded using its native file and folder structure. Uploads that do not meet these requirements are rejected by the upload validator. 

## Rift Build Packaging Requirements

Rift apps have different packaging requirements depending if you upload them through the Oculus Developer Dashboard web interface or through the command line interface.

**Web Upload Packaging Requirements**

*  All necessary files and folders must be packaged in a .zip file.
* The launch executable file does not need to be at the root of the file structure.
**Command Line Upload Packaging Requirements**

* All necessary files and subdirectories must be inside a single directory that you can specify to the command line tool.
## Uploading Rift Builds

Before you can upload an app build, you must first create an app page for it in the Oculus Developer Dashboard. For more information, see [App Submission and Store Review](/distribute/latest/concepts/publish-create-app/ "This guide will review the process to upload and submit an app to the Oculus Dashboard.").

To upload your build through the web interface:

1. Log on to the Oculus Developer Dashboard at [https://dashboard.oculus.com](https://dashboard.oculus.com/).
2. Hover over your Rift app and then click **Manage Build**.
3. If this is the first upload for this app, click **Upload Build**.
4. If this is not the first upload for this app, click **...** in the release channel you want to upload to and then select **Upload New Binary**.Note: When uploading a new build for an existing app, it is important to make sure that the file path doesn't change. We will only update files on user's devices that have changed and changing the file path may result in multiple copies of your app existing on a user's PC.
5. Click **Choose File** and select the .zip file of your build.
6. Select the Upload Settings options appropriate for your build. Note the following:
	* Paths are relative to the root directory of your .zip file
	* If your app has separate 2D and 3D modes of operation, see [Rift Apps with Non-VR Desktop Modes](/distribute/latest/concepts/publish-packaging-rift-desktopmode/ "This topic describes how to support apps that can be launched in a non-VR desktop modes.").
	
7. Click **Upload**.
To upload your app through the command line interface:

* See [Oculus Platform Command Line Utility](/distribute/latest/concepts/publish-reference-platform-command-line-utility/ "The Oculus Platform Command Line Utility lets you upload builds to your release channels much faster than using the Oculus dashboard web interface. It also allows you to incorporate automated uploads into your existing build system.").
If there are any packaging problems with your build, the upload validator lets you know what they are so that you can correct the issue and try again.

* **[Rift Apps with Non-VR Desktop Modes](/distribute/latest/concepts/publish-packaging-rift-desktopmode/)**  
This topic describes how to support apps that can be launched in a non-VR desktop modes.
