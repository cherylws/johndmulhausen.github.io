---
title: Android Manifest Settings
---

Configure your manifest with the necessary VR settings, as shown in the following manifest segment.

```
&lt;manifest xmlns:android="http://schemas.android.com/apk/res/android" package="&lt;packagename&gt;"  
android:versionCode="1" android:versionName="1.0" android:installLocation="auto"&gt;
&lt;application&gt;
&lt;meta-data android:name="com.samsung.android.vr.application.mode" android:value="vr_only"/&gt;
&lt;activity android:screenOrientation="landscape" 
     android:theme="@android:style/Theme.Black.NoTitleBar.Fullscreen"
     android:configChanges="density|keyboard|keyboardHidden|navigation|orientation|screenLayout|screenSize|uiMode"
     android:launchMode="singleTask"
     android:resizeableActivity="false"&gt;
&lt;/activity&gt;
&lt;/application&gt; 
&lt;uses-sdk android:minSdkVersion="21"/&gt;
&lt;uses-feature android:glEsVersion="0x00030001" /&gt;
&lt;/manifest&gt;
```

* Replace &lt;packagename&gt; with your actual package name, such as "com.oculus.cinema".
* The Android theme should be set to the solid black theme for comfort during application transitioning: Theme.Black.NoTitleBar.Fullscreen
* The vr\_only meta data tag should be added for VR mode detection.
* The required screen orientation is landscape: android:screenOrientation="landscape"
* It is recommended that your configChanges are as follows: android:configChanges="density|keyboard|keyboardHidden|navigation|orientation|screenLayout|screenSize|uiMode". Note that the density config change is only required when targeting API level 24 or greater.
* Setting android:resizeableActivity is only required when targeting API level 24 or greater.
* The minSdkVersion is set to API level 21. This ensures that the app will run on all supported mobile devices. 
* **Do not** add the noHistory attribute to your manifest.


Applications submission requirements may require additional adjustments to the manifest. Please refer to [Application Manifests for Release Versions](/distribute/latest/concepts/publish-mobile-manifest/) in our Publishing Guide.
