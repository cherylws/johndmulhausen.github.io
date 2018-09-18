
  
  
  
  
  
  
# User Interaction
  
   
These requirements ensure your app provides a user experience consistent with Oculus user interaction standards.
   
   
## Selecting Exit to Oculus Home from the Universal Menu must exit to Oculus Home
   
Your app must not prevent the Oculus service from exiting your app when the user requests it.
   
   
   
## Selecting Reset View in the Universal Menu must reset the user’s position and orientation
   
Apps that do not use the Oculus Guardian System play area should reset the user's home position and orientation to their current position and orientation, using built-in Oculus API functionality:
   
   
- If using Unity, add the OVRManager script from Oculus Utilities for Unity to your scene.
   
- If using Unreal, bind the HMDRecentered Delegate event to a handler  node.
   
- If using native code, poll ovr_GetSessionStatus in your game loop  for ShouldRecenter==true and call   ovr_RecenterTrackingOrigin
   .
   
   
Apps that use the Oculus Guardian System play area may use more advanced reorientation logic. See 
[Oculus Guardian System]
(https://developer.oculus.com/documentation/pcsdk/latest/concepts/dg-guardian-system/ "")
  .
   
If Oculus Guardian System bounds are not configured, re-center must work regardless of app tracking or movement type. 
   
   
   
## The app must map all the buttons a user needs to all the controllers that the app supports.
   
Users should be able to experience your app fully with any controller your app supports.  
   
   
   
## The app must not claim Oculus Touch as a supported input device unless Touch position and orientation data facilitate player movement or manipulate the environment. 
   
If your app merely emulates gamepad control schemes, indicate 
   Touch (as  Gamepad)
    on the Oculus Store 
   App  Specifications
    page. 
   
   
   
## The app must meet the requirements for sitting, standing, or roomscale play modes.
   
When submitting your app, you must affirm that your app complies with the requirements for one or more of the following play modes:
   
   
- 
   
     Sitting. The app must be completely playable while seated.
   
   
- 
   
     Standing. The app must be completely usable within a 7' x 5' play  area.
   
   
- 
   
     Roomscale. The app must be completely usable within a 7' x 5' play area with a  3-sensor roomscale setup.
   
   
   
   
   
## The app must meet the requirements for front-facing or 360 tracking modes.
   
When submitting your app, you must affirm that your app complies with the requirements for one or both of the following tracking modes:
   
   
- 
   
     Front-facing
   
   
     
     The app must be completely usable with the standard 2-sensor desk set   up.
     
     
     The app must provide a way for users to pick up VR objects on the ground even if  the desk occludes the sensors.
     
     
     The app must not require users to interact with content behind them. If you place  content behind the user, the app must take steps to keep the user facing frontwards  to avoid occluding the sensors with their body.
     
   
   
   
- 
   
     360
   
   
     
     The app must provide interactive content behind the user.
     
     
     If the app is roomscale, the app must be completely usable with the 3-sensor  setup.
     
     
     If the app is not roomscale, the app must be completely usable with the 2-sensor  360 experimental setup.
     
   
   
   
   
  
  
  
  
  
   
[
   Previous: Security]
(/distribute/latest/concepts/publish-reqs-rift-security/ "")
  
  
  
   
[
   Next: Mobile Virtual Reality Check (VRC) Guidelines]
(/distribute/latest/concepts/publish-mobile-req/ "")
  
  
  
  
  
  
