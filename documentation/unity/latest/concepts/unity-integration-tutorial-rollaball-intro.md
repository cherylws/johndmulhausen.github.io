---
title: "Tutorial: Build a Simple VR Unity Game"
---

This section describes the steps necessary to build, load, and run a simple Unity 3D application on the Oculus Rift or Samsung Gear VR.

It is intended to serve as a basic introduction for developers who are new to VR development and to Unity. Once the necessary tools are set up, this process should take a few hours to complete. By the end, you will have a working mobile application that you can play and demonstrate on your Oculus Rift or Gear VR device, to the amazement of your friends and loved ones.

We will build and modify the Unity game Roll-a-ball to add VR capability. The game is controllable by keyboard or by the Samsung EI-GP20 gamepad.

## Requirements

* Oculus Rift or Gear VR with compatible Samsung phone
* Samsung EI-GP20 gamepad (required for Mobile; optional for Desktop)
* PC running Windows 7, 8 or 10, or a Mac running OS X 10
* Unity 4 (for version compatibility, see [Compatibility and Requirements](/documentation/unity/latest/concepts/unity-integration-req/))


You will also need to refer to the relevant Oculus SDK documentation, available for download here: [https://developer.oculus.com/documentation/](/documentation/)

## Installation and Preparation



1. Install the appropriate Oculus SDK and prepare for development.**Desktop**: Download and install the Oculus PC SDK and Unity Integration from [Oculus PC SDK Downloads](https://developer.oculus.com/downloads/#sdk=pc). Prepare for development as described in the *Oculus Rift Getting Started Guide*. By the time you have completed this process, you should be able to run the Demo Scene as described in that guide.

**Mobile**: Download and install the Oculus Mobile SDK from [Oculus Mobile SDK Downloads](https://developer.oculus.com/downloads/#sdk=mobile). Prepare for development as described by the *Device and Environment Setup Guide*. By the time you have completed this process, you should be able to communicate with your Samsung phone via USB. To verify this, retrieve the device ID from your phone by connecting via USB and sending the command adb devices from a command prompt. If you are communicating successfully, the phone will return its device ID. You may wish to make a note of it - you will need it later to request a Oculus Signature File (see step four in [Modify Roll-a-ball for VR](/documentation/unity/latest/concepts/unity-integration-tutorial-rollaball-intro/#unity-integration-tutorial-rollaball-modify) for more information).


2. Install Unity.Check which version of the Unity editor you should download and install in our [Compatibility and Version Requirements](/documentation/unity/latest/concepts/unity-req/ "This guide describes Unity Editor version recommendations and system requirements."), then download the appropriate version here: &lt;http://docs.unity3d.com/Manual/index.html&gt;. Unity provides extensive documentation to introduce users to the environment. You may wish to begin by reviewing their documentation to gain a basic familiarity with core concepts such as the Editor, GameObjects, prefabs, projects, and scenes.


3. Build the Unity Roll-a-ball application.Unity provides a number of video tutorials that walk you through the process of creating a simple game. The first in the series provides instructions for creating the Roll-a-ball application, in which you use the keyboard or gamepad to control a ball that rolls around a game board and picks up floating token counters:&lt;http://unity3d.com/learn/tutorials/projects/roll-a-ball&gt;

The development process is covered in eight short video tutorials which run from around five to fifteen minutes in length. Allow for a few hours to complete the procedure.

The final video in the series, "107. Publishing the game," describes building the Roll-a-ball game for play in a web browser. You may skip this lesson if you wish for the purposes of this exercise, as we will follow a different procedure for building a playable application (PC/Mac) or APK (Android).

Note: We refer to the assets, folders, and so forth by the names used in the Unity tutorial, so it is helpful to follow the names they use in their example.
4. Duplicate your Roll-a-ball project (optional).Once you have completed building Roll-a-ball, you may wish to create a duplicate Roll-a-ball project specifically for VR development. It can be useful to retain a backup of the original unmodified Roll-a-ball project in case you make mistakes or wish to work with it later without the VR assets.

To duplicate the Roll-a-ball project, simply navigate in your OS to the Unity project folder containing your Roll-a-ball project, copy the folder and all of its contents, and rename it. For this tutorial, we will use the project folder name **Roll-a-ball-VR**.


5. Launch the new project and prepare the game scene.
	1. Launch Unity and select **File** &gt; **Open Project...** and select the project folder location for Roll-a-ball-VR in order to launch the project.
	2. In your **Project** tab, open **Assets** &gt; **\_Scenes** and select "MiniGame." 
	3. Press F2 and rename the scene "VRMiniGame."
	4. Open the scene "VRMiniGame."
	


## Modify Roll-a-ball for VR



1. Import the Oculus Unity Integration Package.In Unity, select **Assets** &gt; **Import Package** &gt; **Custom Package...**. Navigate to the folder where you have installed the Oculus SDK. 

**PC SDK**: open the **OculusUnityIntegration** folder, select OculusUnityIntegration.unitypackage, and click **Open**. 

**Mobile SDK**: open the **UnityIntegration** folder in **VrUnity**, select UnityIntegration.unityPackage, and click **Open**.

This will open Unity's **Import Package** dialog box, which lists the assets included in the package. Leave all boxes checked and select **Import**.

For more information on the contents of the integration package, see [A Detailed Look at the Unity Integration](/documentation/unity/latest/concepts/unity-integration-overview/#unity-integration-integration "This section examines the Unity integration, including the directory structure of the integration, the Unity prefabs are described, and several key C# scripts.").


2. Replace Main Camera with OVRCameraRig.We will replace the Roll-a-ball Main Camera with OVRCameraRig, an Oculus prefab VR camera included with our Unity Integration. OVRCameraRig renders two stereoscopic images of the game scene with the appropriate distortion. 

Main Camera tracks the player ball, but we will modify our camera to overlook the game board from a fixed position, so the player may look around at whatever angle they choose.

Rather than deleting the Main Camera, simply deselect it to make it inactive in the scene. Select **Main Camera** in your Hierarchy view and uncheck the check box at the top left of the Inspector view. 

![](/images/documentationunitylatestconceptsunity-integration-tutorial-rollaball-intro-0.png)

Note: Only one camera may be active in a Unity scene at any given time.In the Project view, open the **OVR** folder and select the **Prefabs** folder. Select **OVRCameraRig** and drag it into the Hierarchy view to instantiate it.


3. Elevate OVRCameraRig above the game board.Select **OVRCameraRig** in the Hierarchy view and set the **Position** fields of the OVRCameraRig Transform to the following values: X = 0; Y = 10; Z = -15.


4. Rotate OVRCameraRig forward for a better view.Set the **Rotation** field of the **OVRCameraRig Transform** to the following value: X = 35; Y = 0; Z = 0.

Enter Play mode by pressing the play button, and note that the Game view now shows the image rendered in two distorted and stereoscopic views as illustrated below. If you are using the PC SDK, you will see the **Health and Safety Warning** appear over the game; press any key to continue past it. 

![](/images/documentationunitylatestconceptsunity-integration-tutorial-rollaball-intro-1.png)

Roll-a-ball VR in Unity Scene and Game Views
5. Save your scene and project before building your application.
6. Sign your application (Mobile Only).To access your Samsung phone's VR capabilities, you will need to sign your application with an Oculus Signature File (osig). If you recorded your device ID earlier, you may use it now to request your osig file. Note that you need only one osig per mobile device.

You may obtain an osig from our self-service portal here: &lt;https://dashboard.oculus.com/tools/osig-generator/&gt;. Once you have received an osig, copy it to your Unity project folder in /Roll-a-ball-VR/Assets/Plugins/Android/assets/. 

More information may be found on application signing in [Application Signing](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-submission-sig-file/) in our Mobile guide.




## Build and Play



### Build and Launch

If you are developing for desktop, you will build an executable file that you may launch with your PC or Mac. If you are developing for mobile, you will build an APK and load it onto your phone, and then insert the phone into the Gear VR to launch your game. Follow the build instructions as described by the section [Configuring for Build](/documentation/unity/latest/concepts/unity-integration-build/#unity-integration-build) section. 

### Play

Go ahead and try it out! You may use your keyboard or a paired Samsung gamepad to control your ball and collect the game pickup objects.

### Launching the Game on Gear VR

If you select **Apps** from the Samsung home screen, you will see Roll-a-ball-VR listed with the other apps. You may launch the application directly, and when instructed, put the phone in the Gear VR. It will not be visible from Oculus Home.
