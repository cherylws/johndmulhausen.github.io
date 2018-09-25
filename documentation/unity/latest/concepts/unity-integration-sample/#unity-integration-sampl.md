---
title: Sample Unity Application Demos
---
This section describes the sample Unity applications provided by Oculus as a reference for development.

## Running Pre-Built demos: PC

To run the pre-built demos, download the appropriate demo zip file for the platform you need.

* For Windows, download the *demo win.zip file.
* For Mac, download the *demo mac.zip file.
Run the OculusUnityDemoScene.exe (Windows) or OculusUnityDemoScene.app (Mac) pre-built demo. If prompted with a display resolution dialog, hit the Play button. The demo will launch in full-screen mode.

Note: If you are using Direct Display mode, you will be able to see the stereo image on your 2D display as well.## Running Pre-Built demos: Mobile

To run the pre-built demos, you must first install the demo packages (.apk) and sample media to your Android device.

Connect to the device via USB and open a command prompt. Run the installToPhone.bat script included with the SDK. This script will copy and install both the Unity and Native sample applications as well as any sample media to your Android device. You should now see application icons for the newly-installed apps on the Android Home screen.

For more information about these sample apps please review the *Initial SDK Setup* section in *Device and Environment Setup Guide*.

To test a sample application, perform the following steps:

* From the Android Home screen, press the icon of the VR app you wish to run.
* A toast notification will appear with a dialog like the following: “Insert Device: To open this application, insert your device into your Gear VR”
* Insert your device into the supported Gear VR hardware.
The app should now launch.

## Pre-Built Demo Controls

### BlockSplosion (mobile only)

In BlockSplosion, the camera position does not change, but the user's head orientation will be tracked, allowing them to aim before launching a block.

* 1-dot Button or Samsung gamepad tap launches a block in the facing direction.
* 2-dot Button resets the current level.
* Left Shoulder Button (L) skips to the next level.
### Tuscany (PC only)

**Gamepad Control**

* If you have a compliant gamepad controller for your platform, you can control the movement of the player controller with it.
* The left analog stick moves the player around as if you were using the W,A,S,D keys.
* The right analog stick rotates the player left and right as if you were using the Q and E keys.
* The left trigger allows you to move faster, or run through the scene.
* The Start button toggles the scene selection. Pressing D-Pad Up and D-Pad Down scrolls through available scenes. Pressing the A button starts the currently selected scene.
* If the scene selection is not turned on, Pressing the D-Pad Down resets the orientation of the tracker.
**Mouse Control**

Using the mouse will rotate the player left and right. If the cursor is enabled, the mouse will track the cursor and not rotate the player until the cursor is off screen.

### Shadowgun

In Shadowgun, locomotion allows the camera position to change.

* Left Analog Stick will move the player forward, back, left, and right.
* Right Analog Stick will rotate the player view left, right, up, and down. However, you will likely want to rotate your view just by looking with the VR headset.
