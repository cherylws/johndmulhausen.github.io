---
title: Building Mobile Applications
---
This section describes the steps necessary for building Unity applications for Oculus Go and Samsung Gear VR.

## Android Manifest

During the build process, Unity projects with VR support enabled are packaged with an automatically-generated manifest which is configured to meet our requirements (landscape orientation, vr\_only, et cetera). All other values, such as Entitlement Check settings, are not modified. **Do not** add the noHistory attribute to your manifest.

To build an application for submission to the Oculus Store, you must build a custom manifest using the Oculus Utilities for Unity. See [Building Mobile Apps for Submission to the Oculus Store](/documentation/unity/latest/concepts/unity-build-android/#unity-build-android-store "If you are building an application for the Oculus Store, you will need to take a few extra steps.") for details.

## Oculus Signature File

Your application must include an Oculus Signature File or osig. See "Sign your App with an Oculus Signature File" in [Preparing for Mobile Development](/documentation/unity/latest/concepts/unity-mobileprep/ "To prepare for Unity mobile development for Oculus Go and Samsung Gear VR, you must set up the Unity Editor for Android development and install the Android SDK. The Oculus Mobile SDK is not required.") for more information.

## Build Settings

From the **File** menu, select **Build Settings…**. Select **Android** as the platform. Set **Texture Compression** to **ASTC**.

We recommend unchecking **Development Build** for your final build, as it may impact performance. 

![](/images/documentation-unity-latest-concepts-unity-build-android-unity-build-android-0.png)  
## Player Settings

1. Click the **Player Settings…** button and select the **Android** tab. ![](/images/documentation-unity-latest-concepts-unity-build-android-unity-build-android-1.png)  

2. Set a Bundle Identifier under **Identification** in **Other Settings**.
3. Select **Virtual Reality Supported** under **Rendering** in **Other Settings**.
All required settings are enforced automatically, but you may wish to make additional settings as appropriate, such as enabling **Multithreaded Rendering**. For more information on our recommended settings, see the [Best Practices for Rift and Mobile](/documentation/unity/latest/concepts/unity-best-practices-intro/ "This section describes performance targets and offers recommendations for developers.") section.

![](/images/documentation-unity-latest-concepts-unity-build-android-unity-build-android-2.png)  
## Quality Settings

Navigate to **Edit > Project Settings > Quality**. We recommend the following settings:

Pixel Light Count

1

Texture Quality

Full Res

Anisotropic Textures

Per Texture

Anti Aliasing

2x or 4x Multi Sampling

Soft Particles

Deselect

Realtime Reflections Probes

Select

Billboards Face Camera

Select

The **Anti-aliasing** setting is particularly important. It must be increased to compensate for stereo rendering, which reduces the effective horizontal resolution by 50%. An anti-aliasing value of 2X is ideal, 4x may be used if you have performance to spare. We do not recommend 8x.

For more information on our recommended settings, see [Best Practices for Rift and Mobile](/documentation/unity/latest/concepts/unity-best-practices-intro/ "This section describes performance targets and offers recommendations for developers.").

## Build and Run the Application

Build your application for the Android Platform and load it onto your phone. When you launch the application, you will be prompted to insert your phone into the Gear VR headset.

1. Save the project before continuing. If you are not already connected to your phone via USB, connect now. Unlock the phone lock screen.
2. On some Samsung models, you must set the default USB connection from **Connected for charging** or similar to **Software installation** or similar in the Samsung pulldown menu.
3. From the **File** menu in the Unity Editor, select **Build Settings…**. While in the Build Settings menu, add your scenes to **Scenes in Build** if necessary.
4. Verify that Android is selected as your **Target Platform** and select **Build and Run**. If asked, specify a name and location for the APK.
5. The APK will be installed and launched on your Android device.
To run your application later, remove your phone from the Gear VR headset and launch the app from the phone desktop or Apps folder. Then insert the device into the Gear VR when prompted to do so.

Note that your will not see your application listed in your Oculus Home Library - only applications approved and published by Oculus are visible there. 

### Sideloading Unity Applications

You may build an APK locally and sideload it to your phone.

To do so, follow all of the instructions above, except in the final steps, select **Build** instead of **Build and Run**.

Once you have built an APK on your local system, you may copy it to your phone by following the instructions in [Using adb to Install Applications](/documentation/mobilesdk/latest/concepts/mobile-adb/) in our Mobile SDK Developer Guide.

### Running Mobile Apps Outside of the Gear VR Headset

When Developer Mode is enabled on your phone, Oculus applications will run without inserting the phone into the Gear VR headset. This can be convenient during development.

VR applications run in Developer Mode play with distortion and stereoscopic rendering applied, and with limited orientation tracking using the phone's sensors.

For instructions on setting your device to Developer Mode, see [Developer Mode: Running Apps Outside of the Gear VR Headset](/documentation/mobilesdk/latest/concepts/mobile-troublesh-device-run-app-outside/) in our Mobile SDK Developer Guide.

## Building Mobile Apps for Submission to the Oculus Store

If you are building an application for the Oculus Store, you will need to take a few extra steps.

1. Create a custom manifest using the Oculus Utilities for Unity
2. Remove your osig
3. Sign your application with an Android Keystore
4. Enable Entitlement Checking with the Oculus Platform SDK
For more information on the submission process, see our Publishing Guide.

### 1. Build a Custom Manifest for Submission

To build an APK that includes a manifest with the values required by the Oculus Store, you must download the Oculus Utilities for Unity package and import it into your project as described in [Importing the Oculus Utilities Package](/documentation/unity/latest/concepts/unity-import/ "Oculus Utilities for Unity is an optional Unity Package that includes scripts, prefabs, and other resources to assist with development."). 

Once you have a done so, in the Unity Editor, select **Tools > Oculus > Create store-compatible AndroidManfiest.xml**. Then build your project normally. 

### 2. Remove your osig

We recommend removing your Oculus Signature File before building your application for submission.

### 3. Sign your application with an Android Keystore

Mobile applications must be signed with an Android signature for submission. Unity automatically signs applications with a temporary Android debug certificate by default. Before building your final release build, create a new Android keystore by following the “Sign Your App Manually” instructions in Android's [Sign your Applications](https://developer.android.com/tools/publishing/app-signing.html) guide. Then assign it with the **Use Existing Keystore** option, found in **Edit > Project Settings > Player > Publishing Options**. 

For more information, see the [Android section](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html) of Unity's documentation.

### 4. Enable Entitlement Checking with the Oculus Platform SDK

Entitlement checking is used to protect apps from unauthorized distribution. It is disabled by default in Unity. Entitlement checking is not required for development, but it is required for submitting an application to the Oculus Store.

For more information and instructions, see [Getting Started with the SDK](https://developer3.oculus.com/documentation/platform/latest/concepts/pgsg-get-started-with-sdk/) in our Platform guide.

