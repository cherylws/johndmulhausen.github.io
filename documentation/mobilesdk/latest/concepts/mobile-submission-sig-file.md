---
title: Oculus Signature File (osig) and Application Signing
---

Oculus mobile apps may require two distinct signatures at different stages of development.

* Oculus Signature File (required during development, remove for submission, only required for Gear VR apps)
* Android Application Signature (required for submission)


## Oculus Signature File (osig) - Gear VR only

During development, your application must be signed with an Oculus-issued Oculus Signature File, or **osig**. This signature comes in the form of a file that you include in your application in order to access protected low-level VR functionality on your mobile device. Each signature file is tied to a specific device, so you will need to generate osig files for each device that you use for development. When your application is submitted and approved, Oculus will modify the APK so that it can be used on all devices.

Please see our osig self-service portal for more information and instructions on how to request an osig for development: [https://dashboard.oculus.com/tools/osig-generator/](https://dashboard.oculus.com/tools/osig-generator/)

## Android Application Signing

Android uses a digital certificate (also called a **keystore**) to cryptographically validate the identity of application authors. All Android applications must be digitally signed with such a certificate in order to be installed and run on an Android device.

All developers must create their own unique digital signature and sign their applications before submitting them to Oculus for approval. For more information and instructions, please see Android's "Signing your Applications" documentation: [http://developer.android.com/tools/publishing/app-signing.html](https://developer.android.com/tools/publishing/app-signing.html)

Make sure to save the certificate file you use to sign your application. Every subsequent update to your application must be signed with the same certificate file, or it will fail.

## Android Application Signing and Unity

Unity automatically signs Android applications with a temporary debug certificate by default. Before building your final release build, create a new Android keystore by following the "Sign Your App Manually" instructions in Android's [Sign your Applications](https://developer.android.com/tools/publishing/app-signing.html) guide. Then assign it with the **Use Existing Keystore** option, found in **Edit** &gt; **Project Settings** &gt; **Player** &gt; **Publishing Options**. For more information, see the "Android" section of Unity's documentation here: [http://docs.unity3d.com/Manual/class-PlayerSettings.html](http://docs.unity3d.com/Manual/class-PlayerSettings.html). 

## Android Application Signing and Unreal

Once you add an osig to the appropriate Unreal directory, it will be added automatically to every APK that you build. You will need one osig for each mobile device.

To add your osig to Unreal for development:

1. Download an osig as described in above.
2. Navigate to the directory &lt;Unreal-directory&gt;\Engine\Build\Android\Java\.
3. Create a new directory inside \Engine\Build\Android\Java\ and name it assets. The name must not be capitalized.
4. Copy your osig to this directory.


When you are ready to build an APK for submission to release, we recommend that you exclude the osig in your APK. To do so, select **Edit** &gt; **Project Settings** &gt; **Android**, scroll down to **Advanced APKPackaging**, and verify that **Remove Oculus Signature Files from Distribution APK** is checked.

Before building your final release build, create a new Android keystore by following the "Sign Your App Manually" instructions in Android's [Sign your Applications](https://developer.android.com/tools/publishing/app-signing.html) guide. Once you have generated your distribution keystore, go to Edit &gt; Project Settings &gt; Platforms &gt; Android, scroll down to Distribution Signing, and entered the required information.
