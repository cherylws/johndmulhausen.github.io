---
title: "Tutorial: Build Your First VR App"
---
This short tutorial walks you through creating and running a simple Unity app for Rift or Gear VR.

When you finish, you will have a working VR application that you can play on your Rift or Gear VR device, to the amazement of your friends and loved ones.

## Requirements

* Unity 5 (see [Compatibility and Version Requirements](/documentation/unity/latest/concepts/unity-req/ "This guide describes Unity Editor version recommendations and system requirements.") for version recommendations)
* Rift or Gear VR
* Compatible gamepad: optional for Rift, but a Bluetooth gamepad is required to control the player on Gear VR.
## Preparation

Before beginning, you will need to set up your development environment.

If you are building for Rift, please follow the instructions in [Preparing for Rift Development](/documentation/unity/latest/concepts/unity-pcprep/ "Unity 5 or later offers built-in Rift support. The Oculus SDK is not required."). Be sure to configure the Oculus app to run apps from unknown sources, as described in that section.

If you are building for mobile, please follow the instructions in [Preparing for Mobile Development](/documentation/unity/latest/concepts/unity-mobileprep/ "To prepare for Unity mobile development for Oculus Go and Samsung Gear VR, you must set up the Unity Editor for Android development and install the Android SDK. The Oculus Mobile SDK is not required."). You should be able to communicate with your Samsung phone via USB before beginning. To verify this, retrieve the device ID from your phone by connecting via USB and sending the command adb devices from a command prompt. The phone should return its device ID. Make a note of it - you will need it later to request a Oculus Signature File.

## Build Your Simple Application

We are going to build a simple game with a play area that consists of a floor and some walls. Then we’ll add a ball and attach a controller script so we can move it around the play area with a keyboard or gamepad. Finally, we’ll add VR support so we can run the game on Rift, Oculus Go, or Gear VR.

So, let’s get started without any further ado.

![](/images/documentation-unity-latest-concepts-unity-tutorial-0.png)  
**Part 1: Build a Play Area and Add a Player**

In this part of the tutorial, we’ll build a simple play area consisting of a floor and four walls, and add a sphere as a player.

1. Launch the Unity Editor and, in the initial launch dialog, create a new project by clicking **New**. Give it a creative name like VRProject, and select a location for the files to live in. Verify that the 3D option is selected, and click **Create Project**.
2. Save the Scene.
	1. Select the File pulldown menu, and click **Save Scene as…**.
	2. Give the scene a creative name like VRScene.

3. Let’s create a floor.
	1. In the GameObject pulldown menu, select **3D Object > Plane**.
	2. In the Inspector, verify that the Position is set to origin (0,0,0). If not, set it to origin by selecting the gear icon pulldown in the upper-right of the Transform section of the Inspector and clicking **Reset**.
	3. Find Plane in the Hierarchy View and right-click it. Select **Rename** in the context menu, and rename it **Floor**.

4. Now we’ll create the first wall.
	1. In the GameObject pulldown menu, select **3D Object > Cube**.
	2. If the cube isn’t at origin, reset its Transform like we did in the preceding step.
	3. Longify the cube by setting the X value of Scale to **10** under Transform.
	4. Move it up slightly by setting the Y value of Position to **.5** under Transform. It should now rest upon the floor.
	5. Find Cube in the Hierarchy View and right-click it. Select **Rename** in the context menu, and name it **Wall1**.
	![](/images/documentation-unity-latest-concepts-unity-tutorial-1.png)  

5. Move the wall to the outer edge of the play area.
	1. Select Wall1 in the Hierarchy View or in the Scene View.
	2. In the Inspector, set the Z value of Position to **5** under Transform.

6. Make a second wall and move it to the opposite edge of the play area.
	1. Right-click Wall1 in the Hierarchy View and select **Duplicate** in the context menu. You will see a second wall named **Wall1 (1)**.
	2. Right-click Wall1 (1) in the Hierarchy View. Select **Rename** in the context menu, and rename it **Wall2**.
	3. Select Wall2 in the Hierarchy View or in the Scene View.
	4. In the Inspector, set the Z value of Position to **-5** under Transform.
	![](/images/documentation-unity-latest-concepts-unity-tutorial-2.png)  

7. Make a third wall, rotate it, and move it into place.
	1. Right-click Wall1 in the Hierarchy View and select **Duplicate** in the context menu. You will see a wall named **Wall1 (1)**.
	2. Right-click Wall1 (1) in the Hierarchy View and select **Rename** in the context menu, and rename it **Wall3**.
	3. Select Wall3 in the Hierarchy View or in the Scene View.
	4. In the Inspector, set the **Y** value of Rotation to **90** under Transform.
	5. Select Wall3 in the Hierarchy View or in the Scene View.
	6. In the Inspector, set the X value to **4.5** and the Z value to **0** in Position, under Transform.

8. Make a fourth wall and move it into place.
	1. Right-click Wall3 in the Hierarchy View and select **Duplicate** in the context menu. You will see a wall named **Wall3 (1)**.
	2. Right-click Wall3 (1) in the Hierarchy View and select **Rename** in the context menu. Name it **Wall4**.
	3. Select Wall4 in the Hierarchy View or in the Scene View.
	4. In the Inspector, set the X value of Position to **-4.5** under Transform.

9. Now we have a play area with a floor surrounded by walls. Let’s add a sphere player.
	1. In the GameObject pulldown menu, select **3D Object > Sphere**.
	2. In the Inspector, set the Position to **0, .5, 0**.
	3. Right-click Sphere in the Hierarchy View and select **Rename** in the context menu. Name it **Player**.
	![](/images/documentation-unity-latest-concepts-unity-tutorial-3.png)  

10. Adjust your camera so we can see the play area better.
	1. Select Main Camera in the Hierarchy View.
	2. In the Inspector, set Position to **0, 5, 0** and Rotation to **20, 0, 0** under Transform.

**Part 2: Add a control script to your Player**

In this part of the tutorial, we will prepare the Player so we can control its movement programmatically, based on user input from keyboard or gamepad.

1. Add a RigidBody component to the Player. This will allow us to move it (for more details, [RigidBody](https://docs.unity3d.com/Manual/RigidbodiesOverview.html) in Unity’s manual).
	1. Select Player in the Hierarchy View or in the Scene View.
	2. In the Inspector, click Add Component at the bottom. Select the **Physics** category, then select **RigidBody**.

2. Create a new script, which we will use to control the Player.
	1. Select Player in the Hierarchy View or in the Scene View.
	2. In the Inspector, click Add Component at the bottom. Select the **New Script** category.
	3. Set the name of our new script to PlayerController, and set the language to **C Sharp**. Click **Create and Add**.
	4. Right-click Player Controller (Script) in the Inspector, and select **Edit Script** in the context menu. This will launch the editor Unity associates with editing C# scripts (MonoDevelop by default). You should see the following:  using System.Collections; using System.Collections.Generic; using UnityEngine; public class temp : MonoBehaviour { // Use this for initialization void Start () { } // Update is called once per frame void Update () { } }

3. Add a new function to move your Player. Add the text in bold:  using System.Collections; using System.Collections.Generic; using UnityEngine; public class PlayerController : MonoBehaviour { public int speed = 0; // Use this for initialization void Start () { } // Update is called once per frame void Update () { // get input data from keyboard or controller float moveHorizontal = Input.GetAxis("Horizontal"); float moveVertical = Input.GetAxis("Vertical"); // update player position based on input Vector3 position = transform.position; position.x += moveHorizontal * speed * Time.deltaTime; position.z += moveVertical * speed * Time.deltaTime; transform.position = position; } }
4. Attach the Player Controller script to your Player.
	1. Select Player in the Hierarchy View or in the Scene View.
	2. In the Project View, select **All Scripts**. You should see PlayerController on the right side of the Project View.
	3. Click on PlayerController in the Project View and drag it into the Inspector, below **Add Component**. You should see it added as a new component to the Player. ![](/images/documentation-unity-latest-concepts-unity-tutorial-4.png)  

	4. Set speed to **3**.

At this point if you preview your game in the Game View by pressing the Play button, you’ll find you can control the Player with the arrow keys or W-A-S-D on your keyboard. If you have a Unity-compatible gamepad controller you can control it with a joystick. Try it out!

**Part 3: Modify your project for VR**

In this step we'll enable VR support in Player Settings.

1. In the Edit menu, select **Project Settings > Player**.
2. In the Inspector window, locate the platform selection tabs. If developing for the PC, select the PC platform tab. It looks like a download icon. If developing for Android, select the Android platform tab. It looks like an Android icon.![](/images/documentation-unity-latest-concepts-unity-tutorial-5.png)  
Android Platform
3. In **Other Settings > Rendering**, select the **Virtual Reality Supported** check box. ![](/images/documentation-unity-latest-concepts-unity-tutorial-6.png)  

That’s it! That’s all you need to do to make your game into a VR application.

If you have a Rift, go ahead and try it out. Press the Play button to launch the application in the Play View. If the Oculus app is not already running, it will launch automatically, as it must be running for a VR application to play.

Go ahead and put on the Rift and accept the Health and Safety Warnings. The game will be viewable in the Rift, and the Unity Game View will show the undistorted left eye buffer image.

Save your scene and project before proceeding.

![](/images/documentation-unity-latest-concepts-unity-tutorial-7.png)  
## Play

If you are developing for Rift, follow the [Building Rift Applications](/documentation/unity/latest/concepts/unity-build-pc/ "This section describes the steps necessary for building Rift apps in Unity.") to build an executable file.

If you are developing for mobile, follow the [Preparing for Mobile Development](/documentation/unity/latest/concepts/unity-mobileprep/ "To prepare for Unity mobile development for Oculus Go and Samsung Gear VR, you must set up the Unity Editor for Android development and install the Android SDK. The Oculus Mobile SDK is not required.") instructions to build an APK and load it onto your phone, then launch your game. Be sure to copy your osig to the specified folder as described in that section, or you will not be able to run your application.

Once you have run your application, it will then be available in your Oculus Library, and you may re-launch it from there.
