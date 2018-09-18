
  
  
  
  
  
  
# Gear VR Technical Requirements
  
   
Your Gear VR app must meet or exceed these minimum requirements to be considered for publication on the Oculus Store.
   
   
- Runs on all Gear VR devices.
   
- Meets all Oculus Mobile SDK or game engine version requirements:
   Oculus Mobile SDK version 1.0 or later. We advise using the latest SDK.
   Unity game engine 5.3 must be version 5.3.6p3 or newer.
   Unity game engine 5.4 must be version 5.4.1p1 or newer.
   Unity versions 5.3.6p1 and p2, as well as 5.4.0p1 and p2 are unsupported. Do not use  these versions to build Gear VR software.
   Unreal game engine must be version 4.10 or later.
   
   
   
- Meets all performance requirements:
   Maintains 60 FPS throughout the app. For information on performance debugging and best  practices, see Squeezing Performance out of your Unity Gear VR Game Part 1 and   Part 2.
   No systemic judder. Asynchronous Timewarp can help with minor rotational judder, but  your application still needs to be at 60 FPS most of the time.
   Uses the most efficient power level state and CPU / GPU throttling possible to avoid  overheating and excessive battery drain. See Power Management.
   Runs with normal usage for 45 minutes or longer without triggering the device’s  overheat warning.
   
   
   
- Meets all graphics requirements:
   All graphics resolve correctly into 3D images with no convergence issues or unusual  distortion. See Binocular Vision, Stereoscopic Imaging and Depth Cues.
   No major graphics issues. This includes z-fighting, depth conflicts, and so on.
   
   
   
- Meets all Android application packaging requirements:
   The application manifest must conform to the release manifest requirements.
   The application must be signed with your unique digital certificate. All subsequent  versions of your app must also be signed with the same certificate. See Application Signing.
   
   
   
- Meets all functional requirements:
   Does not crash, freeze, or enter an extended unresponsive state.
   Correctly uses entitlement checks to prevent unauthorized access. See Getting Started and Checking Entitlements.
   Requests only those permissions that are required by the app.
   Declare in the app review submission form and privacy policy any user data you  transmit to an external server. This includes analytics, save state backup, multiplayer  pairing, and so on.
   No data loss. All saves, settings, and content persist through the user’s  experience.
   Users do not get stuck in any section. For example, if you require a login, we must be  able to successfully create an account. Game levels must not have broken logic that  prevents progressing to the next level.
   Display graphics and respond to head tracking within 4 seconds of launch. Longer  launch times are allowed if there is a head-tracked loading indicator.
   If your app requires Internet connectivity for its core functionality, notify users  without an active Internet connection that one is required.
   Continue to download content if users remove the Gear VR or remove the phone from the  Gear VR.
   Reorient the view forward if users remove the Gear VR and put it back on.
   
   
   
- Meets all input requirements:
   If your application requires a Gear VR Controller or a gamepad and one is not detected  at launch, notify users of the controller requirement.
   If your application supports both touchpad and a Gear VR Controller, users should be  able to seamlessly switch between both input devices without having to change any other  app settings.
   The controller should work with both left hand mode and right hand mode, as set in the  Oculus app setup.
   
   
   
- Meets all reserved interaction requirements:
   Apps must not submit frames or accept input while the Universal Menu is open or the  Gear VR is not worn.
   Single-player apps must pause while the Universal Menu is open or the Gear VR is not  worn.
   Pressing the Gear VR or Gear VR Controller back button for 0.75 seconds or more must  open the Universal Menu in all areas of the app.
   Pressing and releasing the Gear VR or Gear VR Controller back button for less than  0.75 seconds must back out one level in your UI. If already at the top level of your UI,  prompt the user to return to Oculus Home using the standard Quit Menu provided in the  Mobile SDK.
   Pressing the Gear VR or Gear VR Controller volume buttons must adjust the volume using  the VR volume UI provided in the Mobile SDK.
   Your app experience should reorient forward when using the reorientation option in the  Universal Home menu.
   
   
   
  
  
  
  
  
   
[
   Previous: User Interaction]
(/documentation/distribute/latest/concepts/publish-reqs-rift-ui/ "")
  
  
  
   
[
   Next: Managing Apps]
(/documentation/distribute/latest/concepts/publish-create-app/ "")
  
  
  
  
  
  
