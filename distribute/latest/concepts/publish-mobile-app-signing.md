
  
  
  
  
  
  
# Application Signing
  
   
Gear VR apps require two different types of signatures. These are independent but easy to confuse.
   
These two signatures are:
   
   
- "osig" Oculus Signature File (required during development)
   
- Android Application Signature (required for release)
   
   
   
## Oculus Signature "osig" Files for Development
   
To develop a Gear VR application, you will need an Oculus-issued Oculus Signature File (osig) for each of your development devices. The osig is a file that you include in your application to access protected low-level VR functionality on your mobile device. Each signature file is tied to a specific device, so you need to generate osig files for each device you use for development.
   
You can remove your osig file when preparing the release version of your app, though doing so is not required. Applications served through the Oculus store, either through release channels or keys, can be run on any Gear VR device.
   
To create an osig file, go to the 
[Oculus Signature File Generator]
(https://dashboard.oculus.com/tools/osig-generator/ "")
   page.
   
   
   
## Android Application Signing for Release
   
Sign the release version of your app with an Android certificate before you submit it for review.
   
Android uses a digital certificate (also called a keystore) to cryptographically validate the identity of application authors. All Android applications must be digitally signed with such a certificate in order to be installed and run on an Android device.
   
All developers must create their own unique digital signature and sign their applications before submitting them to Oculus for approval. For more information, see 
[Sign Your App]
(http://developer.android.com/tools/publishing/app-signing.html "")
   in the Android documentation.
   
Make sure to save the certificate file you use to sign your application. All subsequent updates to your application must be signed with the same certificate file.
   
   
   
## Unity Settings for Android Application Signing
   
Unity automatically signs Android applications with a temporary debug certificate by default. Before building your final release build, create a new Android keystore and assign it with the Use Existing Keystore option, found in Edit > Project Settings > Player > Publishing Options. For more information, see 
[Android Player Settings: Publishing Settings]
(http://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html "")
   in the Unity documentation.
   
  
  
  
  
  
   
[
   Previous: Application Manifests for Release Builds]
(/distribute/latest/concepts/publish-mobile-manifest/ "")
  
  
  
   
[
   Next: Uploading Rift Apps]
(/distribute/latest/concepts/publish-uploading-rift/ "")
  
  
  
  
  
  
