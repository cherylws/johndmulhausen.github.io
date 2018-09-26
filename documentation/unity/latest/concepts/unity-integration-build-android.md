---
title: "Mobile Build Target: Android"
---



This section describes targeting Unity project builds to Android.

## Build Settings



1. From the **File** menu, select **Build Settings…**. From the **Build Settings…** menu, select **Android** as the platform. Set **Texture Compression** to **ETC2 (GLES 3.0)**.![](/images/documentationunitylatestconceptsunity-integration-build-android-0.png)


2. Add any scenes you wish to include in your build to **Scenes In Build.**.


## Player Settings



1. Click the **Player Settingsâ€¦** button and select the Android tab. Set **Default Orientation** to **Landscape Left** in **Settings for Android** (may be collapsed). Note: The **Use 24-bit Depth Buffer** option appears to be ignored for Android. A 24-bit window depth buffer always appears to be created.
2. As a minor optimization, 16 bit buffers, color and/or depth may be used. Most VR scenes should be built to work with 16 bit depth buffer resolution and 2x MSAA. If your world is mostly pre-lit to compressed textures, there will be little difference between 16 and 32 bit color buffers.
3. Select the **Splash Image** section. For **Mobile Splash** image, choose a solid black texture.Note: Custom Splash Screen support is not available with Unity Free. A head-tracked Unity logo screen is provided instead.
4. While still in **Player Settings**, select **Other Settings** and verify that **Rendering Path*** is set to **Forward**, **Multithreaded Rendering*** is selected, and **Install Location** is set to **Force Internal**, as shown below:![](/images/documentationunitylatestconceptsunity-integration-build-android-1.png)


5. Set the **Stripping Level** to the maximum level your app allows. It will reduce the size of the installed .apk file.Note: This feature is not available for Unity Free.Checking **Optimize Mesh Data** may improve rendering performance if there are unused components in your mesh data.


## Quality Settings



1. Go to the **Edit** menu and choose **Project Settings**, then **Quality**. In the Inspector, set **Vsync Count** to **Donâ€™t Sync**. The TimeWarp rendering performed by the Oculus Mobile SDK already synchronizes with the display refresh.![](/images/documentationunitylatestconceptsunity-integration-build-android-2.png)

Note:**Anti Aliasing** should **not** be enabled for the main framebuffer.
2. **Anti Aliasing** should be set to **Disabled**. You may change the camera render texture antiAliasing by modifying the Eye Texture Antialiasing parameter on OVRManager. The current default is 2x MSAA. Be mindful of the performance implications. 2x MSAA runs at full speed on chip, but may still increase the number of tiles for mobile GPUs which use variable bin sizes, so there is some performance cost. 4x MSAA runs at half speed, and is generally not fast enough unless the scene is very undemanding.
3. **Pixel Light Count** is another attribute which may significantly impact rendering performance. A model is re-rendered for each pixel light that affects it. For best performance, set **Pixel Light Count** to zero. In this case, vertex lighting will be used for all models depending on the shader(s) used.


## Time Settings



![](/images/documentationunitylatestconceptsunity-integration-build-android-3.png)

## Android Manifest File



Open the AndroidManifest.xml file located under Assets/Plugins/Android/. You will need to configure your manifest with the necessary VR settings, as shown in the following manifest segment:

```
&lt;manifest xmlns:android="http://schemas.android.com/apk/res/android" package="&lt;packagename&gt;"  
android:versionCode="1" android:versionName="1.0" android:installLocation="internalOnly"&gt;
&lt;application android:theme="@android:style/Theme.Black.NoTitleBar.Fullscreen" &gt;
&lt;meta-data android:name="com.samsung.android.vr.application.mode" android:value="vr_only"/&gt;
&lt;activity  android:screenOrientation="landscape" 
android:launchMode="singleTask"
android:configChanges="screenSize|orientation|keyboardHidden|keyboard"&gt;
&lt;/activity&gt;
&lt;/application&gt;
&lt;uses-sdk android:minSdkVersion="19" android:targetSdkVersion="19" /&gt;
&lt;uses-feature android:glEsVersion="0x00030000" /&gt;
```

* Replace &lt;packagename&gt; in the first line with your actual package name, such as "com.oculus.cinema".
* Unity will overwrite the required setting android:installLocation="internalOnly" if the Player Setting **Install Location** is not set to **Force Internal**.
* The Android theme should be set to the solid black theme for comfort during application transitioning: Theme.Black.NoTitleBar.Fullscreen
* The vr\_only meta data tag should be added for VR mode detection.
* The required screen orientation is landscape: android:screenOrientation="landscape"
* We recommended setting your configChanges as follows: android:configChanges="screenSize|orientation|keyboardHidden|keyboard"
* The minSdkVersion and targetSdkVersion are set to the API level supported by the device. For the current set of devices, the API level is 19.
* **Do not** add the noHistory attribute to your manifest.


## Running the Build

Now that the project is properly configured for VR, it’s time to install and run the application.

Applications written for development are not launched through the Oculus Home menu system. Instead, build the application directly to your phone, and you will be prompted to insert your phone into the Gear VR headset to launch the application automatically.

To run the application in the future, remove your phone from the Gear VR headset, launch the application directly from the phone desktop or Apps folder, and insert the device into the Gear VR when prompted to do so.

1. Copy an Oculus Signature File specific to your mobile device to the folder Project/Assets/Plugins/Android/assets/ or the application will not run. See the [Application Signing](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-submission-sig-file/) section of the Mobile SDK documentation for more information.
2. Be sure the project settings from the steps above are saved with **File** &gt; **Save Project**.
3. If you are not already connected to your phone via USB, connect now. Unlock the phone lock screen.
4. From the **File** menu, select **Build Settingsâ€¦**. While in the **Build Settings** menu, add the Main.scene to **Scenes in Build**. Next, verify that Android is selected as your **Target Platform** and select **Build and Run**. If asked, specify a name and location for the .apk.The .apk will be installed and launched on your Android device.

