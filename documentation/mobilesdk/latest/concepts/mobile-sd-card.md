---
title: SD Card Support - Gear VR
---

All Gear VR applications submitted to the Oculus Store must support installation to SD Card.

SD Card installation support is enabled with the manifest setting `android:installLocation="auto"` as described in [Android Manifest Settings](/documentation/mobilesdk/latest/concepts/mobile-native-manifest/).

To test application performance after installing to an SD Card:

1. Verify that AndroidManifest.xml is set to android:installLocation="auto".
2. Build an APK of your application.
3. Sign your application as described in [Oculus Signature File (osig) and Application Signing](/documentation/mobilesdk/latest/concepts/mobile-submission-sig-file/#mobile-submission-sig-file "Oculus mobile apps may require two distinct signatures at different stages of development.").
4. Sideload your app as described in “Using adb to Install Applications” in our [adb guide](/documentation/mobilesdk/latest/concepts/mobile-adb/#mobile-android-debug-intro "This guide describes how to perform common tasks using adb."). Be sure to install the application to internal storage,
5. Go to the Android Application Manager and move the application to an SD Card. For more details, see our Developer Blog post [Gear VR SD Card Support](https://developer.oculus.com/blog/gear-vr-sd-card-support/).
6. Launch your application and verify that it works properly.


Users who install mobile applications from the Oculus Store who wish to store them on their SD Card must manually move them following the steps described by our Developer Blog post [Gear VR SD Card Support](/blog/gear-vr-sd-card-support/).
