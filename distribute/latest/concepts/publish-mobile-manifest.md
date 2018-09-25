---
title: Application Manifests for Release Builds
---
 The application manifest of your mobile app must conform to our specifications if you want to upload the app to the Oculus Store.

Note: Effective 2017-4-20, apps must specify installLocation="auto" instead of installLocation="internalOnly" or be rejected by the upload validator. This accommodates installing apps on SD card external storage. If you have a special circumstance and require a different install location setting, contact us at submissions@oculus.com.## Unity Application Manifests

The Unity Android project settings let you set some of the required application manifest options for building a mobile app suitable for the Oculus Store. To set the remaining manifest settings, use the Oculus Utilities for Unity 5 plugin.

The steps below describe how to configure Unity to build Oculus Store-compatible Android .apk packages.

Note: These steps only work for Oculus Utilities for Unity 5 version 1.10 and later. 1. Click **Tools > Oculus > Create store-compatible AndroidManifest.xml**.
2. Click **Edit > Project Settings > Player**.
3. Expand the **Other Settings** properties.
4. Enter a unique name in the **Package Name** field. The package name must be unique within the entire Oculus ecosystem.
5. Increment the **Bundle Version Code**. This value must always be greater than the value in the last build uploaded to any release channel.
6. Set **Minimum API Level** to **Android 5.0 'Lollipop' (API level 21)**.
7. Set **Install Location** to **Automatic**.
## Unreal Application Manifests

Unreal Engine ignores the Android project settings options when building mobile apps and instead uses instructions in an XML file to create the application manifest file. This XML requires a small modification to make builds suitable for the Oculus Store.

The steps below describe how to configure Unreal Engine to build Oculus Store-compatible Android .apk packages.

1. From the main menu, select **Edit** then **Project Settings**.
2. Under the **Platforms** tab, select **Android**.
3. Change **Install Location** to **Auto** and close the **Project Settings** window.
4. From the main menu, select **File** > **Package Project** > **Packaging Settings**.
5. Check the **For Distribution** box.
6. Under the **Platforms** tab, select **Android**.
7. Verify that **Remove Oculus Signature Files from Distribution APK** is not checked. If selected, please uncheck this box.
8. Finally, sign your Android package by following the steps in Epic's [How To Sign UE4 Android Package](https://wiki.unrealengine.com/How_To_Sign_UE4_Android_Package) guide.
## Application Manifest Specification

Your AndroidManifest.xml file must meet the specifications outlined on the [Android Manifest Settings](/documentation/mobilesdk/latest/concepts/mobile-native-manifest/) page.

At APK upload your application manifest will be checked to ensure it meets the requirements. Common rejection causes include: * The package name left as default or copy/pasted from another app. It must not be shared with any other Oculus Store app.
* The installLocation must be set to auto.
* The versionCode must be greater than the value used in a previous build of this app.
* The android:debuggable value must be false. Your app must be a release version, not a debug version.
* The minSdkVersion should be 21, API versions greater than 21 will prevent Android L 'Lollipop' users from installing your app. If you have previously released your app, use caution when changing the minSdkVersion. Increasing the API version may break the compatibility for users on older versions of Android. 
* You must have android.intent.category.INFO, instead of android.internet.category.LAUNCHER. Your app must only appear in Oculus Home. It must not appear in the phoneâ€™s launcher.
* The excludeFromRecents value be set to true.
