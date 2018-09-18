
  
  
  
  
  
  
# Uploading Gear VR Apps
  
   
Gear VR apps have a stringent set of packaging requirements and any app you upload must be packaged accordingly. The upload validator rejects apps that do not meet these requirements.
   
   
## APK Requirements
   
Gear VR apps must be packaged as APK files and meet the following specifications:
   
   
- The APK may be up to 1GB in size.
   
- The APK must have an application manifest fit for a release build. See Application Manifests for Release Builds.
   
- The APK must be signed with an Android certificate. Specifically, it must be signed with  the older JAR signing scheme and not with the newer APK Signature Scheme v2 introduced in  Android Nougat. See Application Signing.
   
   
   Note: We encourage you to break large apps into separate APK and expansion files to improve both the developer and the user experience. 
For developers:
   
   
- Apps split into APK and expansion files take less time to upload.
   
- Expansion files are hosted and served from Oculus servers. There is no need to set up  your own hosting such as is usually required by Unity asset bundles. 
   
   
For users:
   
   
- It takes less time to download and apply patch updates.
   
   
   
   
   
## APK Expansion File Requirements
   
You can supplement your APK file with an APK expansion file. If you are familiar with Google Play APK expansion files, be aware that Oculus APK expansion file sizes and naming patterns are different. Oculus APK expansion files must meet the following specifications:
   
   
- 
   The APK expansion file may be up to 4 GB in size.
   
   
- 
   There must be only one expansion file.
   
   
- 
   The filename of the APK expansion file should be   main.
     versionCode.packageName
     .obb
   
   
     
     versionCode - the version code of the APK you are uploading with the   expansion file. For Unity developers, this is the 
     Bundle Version   Code
      in 
     Player Settings
     .
     
     packageName - the package name of the APK.
   
   
     Example:If you are uploading APK version 3 and your package name is  com.oculus.example, your expansion file name should be   main.3.com.oculus.example.obb
   
   
   
   
   Note: Apps with APK expansion files can only be uploaded with the 
[Oculus Platform Command Line Utility]
(/documentation/distribute/latest/concepts/publish-reference-platform-command-line-utility/ "The Oculus Platform Command Line Utility lets you upload builds to your release channels much faster than using the Oculus dashboard web interface. It also allows you to incorporate automated uploads into your existing build system.")
  .
   

   APK Expansion Files and APKs Must Be Updated Together
   
   
Expansion files must be updated together with an APK. This means that even if your update contains changes only to the APK or only to the .obb, you must increment the version code for each and upload new versions of them together. 
   
The only exception is if you decide to stop using an expansion file and go back to distributing a single APK. In this particular scenario, you would upload a new APK but omit the --obb parameter. 
   
   
   
## Uploading Gear VR Builds
   
You can upload builds through the Oculus Developer Dashboard web interface or using the Oculus Platform Command Line Utility. We recommend using the Oculus Platform Command Line Utility because it is faster. It uses delta-patching techniques to upload only the portions of your app that have changed. 
   
If there are any packaging problems with your app, the upload validation routines inform you after uploading your build so that you can correct the issue and try again. 
   

   Prerequisites:
   
   
Before you can upload a Gear VR app, you must first create an app page for it in the Oculus Developer Dashboard. For more information, see 
[Managing Apps]
(/documentation/distribute/latest/concepts/publish-create-app/ "")
  .
   

   To upload your build through the web interface:
   
   
   
- Log on to the Oculus Developer Dashboard at https://dashboard.oculus.com.
   
- Hover over your Gear VR app and then click Manage Build.
   
- If this is the first upload for this app, click Upload Build.
   
- If this is not the first upload for this app, click ... in the release channel  you want to upload to and then select Upload New Binary.
   
- Click Choose File and select the .apk file of your build.
   
- Enter any release notes you have for this build, and then click Upload.
   
   

   To upload your app through the command line interface:
   
   
   
- See Oculus Platform Command Line Utility.
   
   
  
  
   
   
- 
   
   Application Manifests for Release Builds
   
    The application manifest of your Gear VR app must conform to our specifications if you want to upload the app to the Oculus Store.
   
- 
   
   Application Signing
   
   Gear VR apps require two different types of signatures. These are independent but easy  to confuse.
   
  
  
  
  
   
[
   Previous: Managing Apps]
(/documentation/distribute/latest/concepts/publish-create-app/ "")
  
  
  
   
[
   Next: Application Manifests for Release Builds]
(/documentation/distribute/latest/concepts/publish-mobile-manifest/ "")
  
  
  
  
  
  
