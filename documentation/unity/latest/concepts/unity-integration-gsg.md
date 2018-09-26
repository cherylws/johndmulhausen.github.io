---
title: Getting Started
---



This section describes how to begin working in Unity.

## Importing the Unity Integration

The Oculus Integration asset package is the heart of the supplied development resources. Importing it will install the minimum set of required files necessary for VR integration into Unity. We have also included various assets, scripts, and sample scenes to assist with development.

### Create or Open Unity Project

If you are already working in a Unity project, save your work before beginning.

Otherwise, create a new project into which you will import the Oculus assets:

1. From the Unity menu, select **File** &gt; **New Project**.
2. Click the **Browse** button and select the folder where the Unity project will be located.
3. Make sure that the **Setup defaults for:** field is set to **3D**.
4. You do not need to import any standard or pro Unity asset packages, as the Oculus Unity integration is fully self-contained.
5. Click the **Create** button. Unity will reopen with the new project loaded.


### Delete Previously-Imported Assets

If you have previously imported a Unity Integration package, delete all Oculus Integration content before importing the new Unity package. Be sure to close the Unity Editor, then navigate to your Unity project folder and delete the following: 

|         Folder         |                  Content to Delete                  |
|-------------------------|------------------------------------------------------|
|     Assets/Plugins     |                    Oculus.*OVR.*                    |
| Assets/Plugins/Android/ | *Oculus*AndroidManifest.xml*vrapi**vrlib**vrplatlib* |
|   Assets/Plugins/x86/   |                    Oculus.*OVR.*                    |
| Assets/Plugins/x86_64/ |                    Oculus.*OVR.*                    |

### Import Integration Package

To import the integration into Unity, select **Assets** &gt; **Custom Package...** and select the Unity Integration .unityPackage to import the assets into your new project. Alternately, you can simply find the .unityPackage file in your file system and double-click to launch.

When the **Importing package** dialog box opens, leave all of the boxes checked and select **Import**. The import process may take a few minutes to complete.

### Copy Project Settings (Mobile)

The mobile Unity Integration includes a **Project Settings** folder which provides default settings for a VR mobile application. You may manually copy these files to your [Project]/Assets/ProjectSettings folder. Be sure to keep a copy in your Mobile SDK folder to copy later for use with additional projects.

### To Import BlockSplosion Sample Application (Mobile)

To import the SDKExamples into Unity, select **Assets** &gt; **Custom Package...** and select BlockSplosion.unityPackage to import the assets into your new project. Alternately, you can simply find the .unityPackage file in your file system and double-click to launch.

When the **Importing package** dialog box opens, leave all of the boxes checked and select **Import**. The import process may take a few minutes to complete.

Each sample application project includes a **ProjectSettings** folder, which provides default settings for the VR mobile application. Copy these files to your [Project]/Assets/ProjectSettings folder.

## Adding VR to an Existing Unity Project



The Unity Integration package may be used to integrate Oculus VR into an existing project. This may be useful as a way of getting oriented to VR development, but dropping a VR camera into a Unity game that wasn't designed with VR best practices in mind is unlikely to produce a great experience.

1. Import package.
2. Instantiate OVRCameraRig if you already have locomotion figured out or instantiate OVRPlayerController to walk around.
3. Copy any scripts from the non-VR camera to the OVRCameraRig. Any image effect should go to both the Left/RightEyeAnchor GameObjects. These are children of a TrackingSpace GameObject, which is itself a child of OVRCameraRig. The TrackingSpace GameObject allows clients to change the frame of reference used by tracking, e.g., for use with a game avatar. 
4. Disable your old non-VR camera.
5. Build your project and run normally.

