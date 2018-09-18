
  
  
  
  
  
  
# Application Manifests for Release Builds
  
   
 The application manifest of your Gear VR app must conform to our specifications if you want to upload the app to the Oculus Store.
   
   Note: Effective 2017-4-20, apps must specify installLocation="auto" instead of installLocation="internalOnly" or be rejected by the upload validator. This  accommodates installing apps on SD card external storage. If you have a special circumstance  and require a different install location setting, contact us at submissions@oculus.com.
   
   
## Unity Application Manifests
   
The Unity Android project settings let you set some of the required application manifest options for building a Gear VR app suitable for the Oculus Store. To set the remaining manifest settings, use the Oculus Utilities for Unity 5 plugin.
   
The steps below describe how to configure Unity to build Oculus Store-compatible Android .apk packages.
   
   Note: These steps only work for Oculus Utilities for Unity 5 version 1.10 and later. 
   
   
- Click Tools > Oculus > Create store-compatible AndroidManifest.xml.
   
- Click Edit > Project Settings > Player.
   
- Expand the Other Settings properties.
   
- Enter a unique package name in the Bundle Identifier field. The package name must  be unique within the entire Oculus ecosystem.
   
- Increment the Bundle Version Code. This value must always be greater than the  value in the last build uploaded to any release channel.
   
- Set Minimum API Level to Android 5.0 'Lollipop' (API level 21).
   
- Set Install Location to Auto.
   
   
   
   
## Unreal Application Manifests
   
Unreal Engine ignores the Android project settings options when building Gear VR apps and instead uses instructions in an XML file to create the application manifest file. This XML requires a small modification to make builds suitable for the Oculus Store.
   
The steps below describe how to configure Unreal Engine to build Oculus Store-compatible Android .apk packages.
   
   
- Navigate to your Unreal Engine folder, for example, C:\Epic  Games\UnrealEngine-4.15.
   
- Locate the Engine\Plugins\Runtime\GearVR\Source\GearVR\GearVR_API.xml  file.
   
- Modify line 71 from:  <addAttribute tag="manifest" name="android:installLocation" value="internalOnly"/>  to  <addAttribute tag="manifest" name="android:installLocation" value="auto"/>
   
   
   
   
   
## Application Manifest Specification
   
Your AndroidManifest.xml file must:
   
   
- Have the correct attributes and values in the <manifest> element,  including the following mandatory attributes
     Set a unique package name for the application in the package   attribute. package="YOURNAME"
     
     Set android:installLocation="auto"
     
     Set the versionName. It is shown in the store.   android:versionName="1.0"
     
     Set the versionCode. It is used to deliver updates to users. This   value must be an integer greater than 0, and must increment with subsequent revisions.   android:versionCode="1"
     
     Set the SDK versions to 21.   <uses-sdk android:minSdkVersion="21" android:targetSdkVersion="21" />
     
     Set the OpenGL ES version accordingly. OpenGL ES 2
     <uses-feature android:glEsVersion="0x00020000" android:required="true" />
     OpenGL ES 3.0
     <uses-feature android:glEsVersion="0x00030000" android:required="true" />
     OpenGL ES 3.1 (preferred):
     <uses-feature android:glEsVersion="0x00030001" android:required="true" />
     
   
   
   
- Include the following metadata attribute in the <application>  element:  <meta-data android:name="com.samsung.android.vr.application.mode" android:value="vr_only"/>
   
   
- Structure the <activity> element as shown:  <activity
  android:name="YOUR ACTIVITY"
  android:theme="@android:style/Theme.Black.NoTitleBar.Fullscreen"
  android:label="@string/app_name"
  android:launchMode="singleTask"
  android:screenOrientation="landscape"
  android:configChanges="screenSize|screenLayout|orientation|keyboardHidden|keyboard|navigation"
  android:excludeFromRecents="true">
  <intent-filter>
  <action android:name="android.intent.action.MAIN" />
  <category android:name="android.intent.category.INFO" />
  </intent-filter>
 </activity>
 
   
   
- Remove any unnecessary permissions from your AndroidManifest.xml file.  Only include permissions that are absolutely necessary for your app to function. 
   
   
   
   
## Sample Oculus Store-Compatible App Manifest
   <?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
 package="com.yourcompany.yourappnameCHANGETHIS"
 android:versionCode="1" 
 android:versionName="1.0" 
 android:installLocation="auto" >

 <uses-sdk android:minSdkVersion="21" android:targetSdkVersion="21" />
 <uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
 <uses-permission android:name="android.permission.INTERNET" />
 <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
 <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
 <uses-feature android:name="android.hardware.usb.host" />
 <uses-feature android:glEsVersion="0x00030000" android:required="true" />

 <application
 android:allowBackup="true"
 android:icon="@drawable/ic_launcher"
 android:label="@string/app_name" >
 <meta-data android:name="com.samsung.android.vr.application.mode" android:value="vr_only"/>
 <activity
  android:name="com.yourcompany.vrtemplate.MainActivity"
  android:theme="@android:style/Theme.Black.NoTitleBar.Fullscreen"
  android:label="@string/app_name"
  android:launchMode="singleTask"
  android:screenOrientation="landscape"
  android:configChanges="screenSize|screenLayout|orientation|keyboardHidden|keyboard|navigation"
  android:excludeFromRecents="true"> 
  <intent-filter>
 <action android:name="android.intent.action.MAIN" />
 <category android:name="android.intent.category.INFO" />
  </intent-filter>
 </activity>
 </application>
</manifest>
   
   
   
## Common Manifest Mistakes
   The upload verifier checks common application manifest errors and rejects any uploads that do not pass. Common pitfalls include: 
   
- The package name left as default or copy/pasted from another app. It  must not be shared with any other Oculus Store app.
   
- The installLocation must be set to auto.
   
- The versionCode must be greater than the value used in a previous  build of this app.
   
- The android:debuggable value must be false. Your app  must be a release version, not a debug version.
   
- The minSdkVersion value must be at least 21. If you used a higher   minSDKVersion in a previous build of this app,and the current value  must at least be equal to that. 
   
- You must have android.intent.category.INFO, instead of   android.internet.category.LAUNCHER. Your app must only appear in  Oculus Home. It must not appear in the phone’s launcher.
   
- The excludeFromRecents value be set to true.
   
   
   
  
  
  
  
  
   
[
   Previous: Uploading Gear VR Apps]
(/documentation/distribute/latest/concepts/publish-uploading-mobile/ "")
  
  
  
   
[
   Next: Application Signing]
(/documentation/distribute/latest/concepts/publish-mobile-app-signing/ "")
  
  
  
  
  
  
