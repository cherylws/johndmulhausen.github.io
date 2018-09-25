---
title: Android Studio Basics
---
This guide introduces the Android Studio IDE and reviews some basic features. 

## Getting Started with Oculus Native Samples: Import Gradle Project

1. If this is the first time you are launching Android Studio, select **Open an existing Android Studio project**. If you have launched Android Studio before, click **File > Open** instead. ![](/images/documentation-mobilesdk-latest-concepts-mobile-studio-basics-0.png)  

2. Open any build.gradle project file from the Mobile SDK VRSamples folders. For example, VrSamples/VrCubeworld\_Framework/Projects/Android/build.gradle. ![](/images/documentation-mobilesdk-latest-concepts-mobile-studio-basics-1.png)  

3. When asked if you would like the project to use the Gradle wrapper, click **OK**. ![](/images/documentation-mobilesdk-latest-concepts-mobile-studio-basics-2.png)  

Note: If this is your first time opening a native project in Android Studio, you are likely to be asked to install some dependencies. Follow the on-screen instructions to install all the required dependencies before you continue.## Troubleshooting Gradle Sync Errors

Here are some possible solutions if Android Studio reports a Gradle sync or configuration error:

* The most common cause of such an error is that the Android SDK or NDK locations are wrong. Verify that the SDK and NDK locations are specified correctly in **File > Project Structure**. If either are wrong or missing, you cannot continue until you fill in the correct path.
* On macOS, sometimes Android Studio reports a missing SDK location error even when the correct paths are listed in the **Project Structure** dialog box. To correct this problem, copy the local.properties file from your project folder up to the root of your Oculus Mobile SDK folder. 
![](/images/documentation-mobilesdk-latest-concepts-mobile-studio-basics-3.png)  
## Project Overview

Android Studio displays project files in the **Android** view by default. We recommend changing it to the **Project** view, which provides a good overview of the entire directory structure and highlights imported project directories in bold.

![](/images/documentation-mobilesdk-latest-concepts-mobile-studio-basics-4.png)  
## Select Target Configuration, Build, and Run

You can build and run your application on your device directly from Android Studio. This will compile your project, build the APK, copy it to the phone over USB orWi-Fi, and prepare it for launching.

If you are developing for Gear VR and your phone is set to Developer Mode, your application can launch without being inserted into your Gear VR headset. Otherwise, when the process completes you will be prompted to insert your mobile device into the headset to launch the application. 

Make sure you have followed the configuration steps in the Mobile SDK Setup Guide to ensure your device is configured appropriately.

Select the target configuration you wish to build before building by selecting **Edit Configurations** in the project menu in the Android Studio toolbar.

![](/images/documentation-mobilesdk-latest-concepts-mobile-studio-basics-5.png)  
Note: Before you can run the application, you must create and then copy the **oculussig** file for your device to the assets folder of your project. See [Application Signing](/distribute/latest/concepts/publish-mobile-app-signing/) for more information.To build and run your app:

1. Click **Run** in the toolbar. ![](/images/documentation-mobilesdk-latest-concepts-mobile-studio-basics-6.png)  

2. The Select Deployment Target dialog box appears. This is sometimes set to an emulator by default.
3. Select a device listed under **Connected Device** instead. ![](/images/documentation-mobilesdk-latest-concepts-mobile-studio-basics-7.png)  

4. If your device asks you to **Allow USB debugging**, click **OK**.
Troubleshooting: If USB debugging does not seem to be working:

1. Go to **Developer Options** on your phone.
2. Toggle **USB Debugging** off and then back on.
Troubleshooting: If stepping into certain functions results in an illegal instruction exception (SIGILL) / crash while debugging:

1. In Android Studio, go to **Run > Debug > Edit Configurations**.
2. Select the **Debugger** pane.
3. Select the **LLDB Post Attach Commands** pane.
4. Click **+** to add a new command.
5. Add the following command:   
process handle --pass true --stop false --notify true SIGILL
## Syncing Projects

If you edit a *.gradle file or install an update to the Oculus Mobile SDK which includes updated Gradle projects, click **Sync Project with Gradle Files** to update your Android Studio project files.

![](/images/documentation-mobilesdk-latest-concepts-mobile-studio-basics-8.png)  
