
  
  
  
  
  
  
# Uploading Rift Apps
  
   
 Rift apps are packaged as .zip files if uploading through the web interface. If uploading through the command line interface, your app is uploaded using its native file and folder structure. Uploads that do not meet these requirements are rejected by the upload validator. 
   
   
## Rift Build Packaging Requirements
   
Rift apps have different packaging requirements depending if you upload them through the Oculus Developer Dashboard web interface or through the command line interface.
   

   Web Upload Packaging Requirements
   
   
   
-  All necessary files and folders must be packaged in a .zip file.
   
- The launch executable file does not need to be at the root of the file structure.
   
   

   Command Line Upload Packaging Requirements
   
   
   
- All necessary files and subdirectories must be inside a single directory that you can specify to the command line tool.
   
   
   
   
## Uploading Rift Builds
   
Before you can upload an app build, you must first create an app page for it in the Oculus Developer Dashboard. For more information, see 
[Managing Apps]
(/documentation/distribute/latest/concepts/publish-create-app/ "")
  .
   
To upload your build through the web interface:
   
   
- Log on to the Oculus Developer Dashboard at https://dashboard.oculus.com.
   
- Hover over your Rift app and then click Manage Build.
   
- If this is the first upload for this app, click Upload Build.
   
- If this is not the first upload for this app, click ... in the release channel  you want to upload to and then select Upload New Binary.
   
- Click Choose File and select the .zip file of your build.
   
- Select the Upload Settings options appropriate for your build. Note the following:
     Paths are relative to the root directory of your .zip file
     If your app has separate 2D and 3D modes of operation, see Rift Apps with Non-VR Desktop Modes.
   
   
   
- Click Upload.
   
   
To upload your app through the command line interface:
   
   
- See Oculus Platform Command Line Utility.
   
   
If there are any packaging problems with your build, the upload validator lets you know what they are so that you can correct the issue and try again.
   
  
  
   
   
- 
   
   Rift Apps with Non-VR Desktop Modes
   
   This topic describes how to support apps that can be launched in a non-VR desktop  modes.
   
  
  
  
  
   
[
   Previous: Application Signing]
(/documentation/distribute/latest/concepts/publish-mobile-app-signing/ "")
  
  
  
   
[
   Next: Rift Apps with Non-VR Desktop Modes]
(/documentation/distribute/latest/concepts/publish-packaging-rift-desktopmode/ "")
  
  
  
  
  
  
