
  
  
  
  
  
  
# Functional
  
   
These requirements ensure your app functions according to Oculus Store standards. 
   
   
## Single player apps must pause when the user removes the HMD or opens the Universal Menu
   
After a user opens the Universal Menu or removes the HMD in a single player experience, pause your app. 
   
   
   
## The app must not submit frames or accept input when the user removes the HMD or opens the Universal Menu 
   
After a user opens the Universal Menu or removes the HMD, stop submitting frames or accepting user input. 
   
   
   
## The app must not leave the user stuck at any point in the experience 
   
Examples:
   
   
- If you require a login, it must also be possible to create an account.
   
- Game levels must not have broken logic that prevents progress.
   
   
   
   
## Apps with a 2D desktop mode must launch and be usable on the main display. The user must not be forced to use the HMD or Oculus Touch controllers.
   
For specific recommendations on switching between 2D desktop mode and VR modes, see 
[Rift Apps with Non-VR Desktop Modes]
(https://developer.oculus.com/distribute/latest/concepts/publish-packaging-rift-desktopmode/ "")
  .
   
   
   
## The app does not launch with a Windows Firewall dialog box or a Unity graphics mode dialog box
   
In Unity, set 
   Display Resolution Dialog
    to  
   Hidden By Default
   . See 
[Standalone Player Settings in the Unity documentation]
(https://docs.unity3d.com/Manual/class-PlayerSettingsStandalone.html "")
  .
   
   
   
## The app must set the audio target to the audio device selected in the Audio Output in VR setting in the Oculus app.
   
The app must do this at app launch, and regardless of the default Windows audio device. If the user changes the audio device after the app has launched, you do not need to track that. See 
[Rift Audio]
(https://developer.oculus.com/documentation/pcsdk/latest/concepts/dg-vr-audio/ "")
  .
   
   
   
## The app must not lose the user's data.
   
The app must persist saves and settings throughout the user’s experience.
   
  
  
  
  
  
   
[
   Previous: Graphics and Performance]
(/distribute/latest/concepts/publish-reqs-rift-performance/ "")
  
  
  
   
[
   Next: Security]
(/distribute/latest/concepts/publish-reqs-rift-security/ "")
  
  
  
  
  
  
