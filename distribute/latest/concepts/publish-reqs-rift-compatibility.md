
  
  
  
  
  
  
# Compatibility
  
   
These requirements ensure that your app remains compatible with Oculus runtime libraries and you are mindful of Oculus recommended hardware specifications.
   
   
## The app meets all graphics and performance guidelines running on the recommended spec system specification with the specified alternative graphics card
   
Our lab tests on the 
[Oculus recommended computer spec]
(https://support.oculus.com/help/oculus/170128916778795/ "")
   with the alternative graphics card option. That is: 
   
   
-  NVIDIA GTX 970 or AMD Radeon R9 290 
   
- Intel i5-4590
   
-  8GB of RAM
   
-  Microsoft Windows 7.
   
   
Keep in mind that Microsoft Windows 7 does not support Asynchronous SpaceWarp and that it has a more limited asynchronous timewarp compared to Microsoft Windows 8 or 10. If you designed your app to run on a system more powerful, your app might not meet the level of performance we expect for Oculus Store apps. 
   
   
   
## C/C++ apps must be written for Oculus PC SDK version 1.8 or later 
   
Any C/C++ native apps must be written to target a supported version of the Oculus PC SDK. Currently, this is PC SDK version 1.8 and later.
   
   
   
## Apps that use Audiokinetic Wwise must be built with Wwise version 2016.1 or later 
   
Oculus development requires Wwise or Wwise plugins based on Wwise version 2016.1 or later. See 
[https://www.audiokinetic.com/downloads/]
(https://www.audiokinetic.com/downloads/ "")
  
   
   
   
   
## Unity apps must be built with a supported version 
   
Some versions of Unity are not compatible with Oculus or VR development. You must ensure you are building your app using a supported version of Unity. Supported versions are:
   
   
- Unity 4 apps must use version 4.7.0f1.
   
- Unity 5.4 apps must use version 5.4.5f1 or later.
   
- Unity 5.5 apps must use version 5.5.2p3 or later.
   
- Unity 5.6 apps must use version 5.6.0f3 or later.
   
   
   
   
## Unreal Engine apps must be built with a supported distribution 
   
Some versions of Unreal Engine are not compatible with Oculus or VR development. You must ensure you are building your app using a supported distribution of Unreal Engine. 
   
   Note: These GitHub links display a 404 Not Found error unless you are both logged on to your GitHub account and are subscribed to the private EpicGames/UnrealEngine repository. See  
[https://www.unrealengine.com/ue4-on-github]
(https://www.unrealengine.com/ue4-on-github "")
   for more information. 
   
Supported distributions are: 
   
   
- 
   Unreal Engine version 4.14 or later from the Epic GitHub repository.
   
     https://github.com/EpicGames/UnrealEngine
   
   
   
- 
   Unreal Engine version 4.12 or later from the OculusVR GitHub repository.
   
     https://github.com/Oculus-VR/UnrealEngine.git
   
   
   
   
  
  
  
  
  
   
[
   Previous: Rift Virtual Reality Check (VRC) Guidelines]
(/distribute/latest/concepts/publish-rift-app-submission/ "")
  
  
  
   
[
   Next: Graphics and Performance]
(/distribute/latest/concepts/publish-reqs-rift-performance/ "")
  
  
  
  
  
  
