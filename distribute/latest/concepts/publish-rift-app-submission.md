
  
  
  
  
  
  
# Rift Virtual Reality Checks
  
   
Your Rift app must meet or exceed these guidelines to be considered for distribution on the Oculus Store.
   
   
## Compatibility
   
These requirements ensure that your app remains compatible with Oculus runtime libraries and you are mindful of Oculus recommended hardware specifications.
   
   
   
     
     Type
     Description
     
   
   
     
     Hardware
     The app meets all graphics and performance guidelines running on the  recommended spec system specification with the specified alternative graphics card.   (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-compatibility/ "")
  ) 
     
     
     SDK
     C/C++ apps must be written for 
[Oculus PC SDK version 1.8]
(https://developer.oculus.com/downloads/package/oculus-sdk-for-windows/ "")
   or later. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-compatibility/ "")
  )
     
     
      
     Apps that use Audiokinetic Wwise must be built with 
[Wwise version 2016.1]
(https://www.audiokinetic.com/downloads/ "")
   or later. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-compatibility/ "")
  )
     
     
     Game Engine
     Unity apps must be built with 
[a supported version]
(https://developer.oculus.com/documentation/unity/latest/concepts/unity-req "")
  . (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-compatibility/ "")
  ) 
     
     
      
     Unreal Engine apps must be built with a supported distribution. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-compatibility/ "")
  )
     
   
   
   
   
   
   
## Graphics and Performance
   
These requirements ensure your app is responsive, performant, and able to render graphics at the quality expected for an Oculus Store app.
   
   
   
     
     Type
     Description
     
   
   
     
     Performance
     The app displays graphics in the headset at 90 frames per second. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-performance/ "")
  )
     
     
      
     The app displays graphics without judder. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-performance/ "")
  ) 
     
     
     Stability
     The app runs and installs without crashes, freezes, or extended unresponsive  states. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-performance/ "")
  ) 
     
     
     Graphics
     The app renders without convergence errors or unusual distortion extended  unresponsive states. (
[(more)]
(http://example.com "")
  ) 
     
     
      
     The app renders without visible z-fighting or depth conflict artifacts. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-performance/ "")
  ) 
     
     
      
     The app must either display head-tracked graphics in the headset within 4  seconds of launch or provide a loading indicator in VR. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-performance/ "")
  ) 
     
     
      
     The app must not synchronize animation or physics to an assumed 90Hz frame  rate. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-performance/ "")
  )
     
     
      
     The app should render head-locked UI elements in a compositor layer to avoid  judder if the app misses frames or runs with Asynchronous Spacewarp. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-performance/ "")
  )
     
   
   
   
   
   
   
## Functional
   
These requirements ensure your app functions according to Oculus Store standards.
   
   
   
     
     Type
     Description
     
   
   
     
     State
     Single player apps must pause when the user removes the HMD or opens the  Universal Menu. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-functional/ "")
  )
     
     
      
     The app must not submit frames or accept input when the user removes the HMD or  opens the Universal Menu. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-functional/ "")
  )
     
     
      
     The app must not leave the user stuck at any point in the experience. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-functional/ "")
  )
     
     
     Usability
     Apps that have a 2D desktop mode must launch and be usable on the main display.  The user must not be forced to use the HMD or Oculus Touch controllers. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-functional/ "")
  )
     
     
      
     The app does not launch with a Windows Firewall dialog box or a Unity graphics  mode dialog box. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-functional/ "")
  )
     
     
      
     The app must set the audio target to the audio device selected in the Audio  Output in VR setting in the Oculus app. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-functional/ "")
  )
     
     
     Data Integrity
     The app must not lose the user's data. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-functional/ "")
  )
     
   
   
   
   
   
   
## Security
   
These requirements ensure your app safeguards the privacy and integrity of Oculus and customer data.
   
   
   
     
     Type
     Description
     
   
   
     
     Security
     The app must perform an Oculus Platform entitlement check within 10 seconds of  launch. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-security/ "")
  )
     
     
      
     The app must not contain debugger symbolics or files. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-security/ "")
  )
     
     
      
     The app must not contain extraneous files such as marketing assets or libraries  for other VR APIs and distribution platforms. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-security/ "")
  )
     
   
   
   
   
   
   
## User Interaction
   
These requirements ensure that your app remains compatible with Oculus runtime libraries and you are mindful of Oculus recommended hardware specifications.
   
   
   
     
     Type
     Description
     
   
   
     
     Navigation
     Selecting Exit to Oculus Home from the Universal Menu must exit to Oculus Home.   (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-ui/ "")
  )
     
     
      
     Selecting Reset View in the Universal Menu must reset the user’s position and  orientation. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-ui/ "")
  )
     
     
     Input
     The app must map all the buttons a user needs to all the controllers that the  app supports. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-ui/ "")
  )
     
     
      
     The app must not claim Oculus Touch as a supported input device unless Touch  position and orientation data facilitate player movement or manipulate the  environment. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-ui/ "")
  )
     
     
     Tracking
     The app must meet the requirements for sitting, standing, or roomscale play  modes. (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-ui/ "")
  )
     
     
      
     The app must meet the requirements for front-facing or 360 tracking modes.   (
[more]
(/documentation/distribute/latest/concepts/publish-reqs-rift-ui/ "")
  )
     
   
   
   
   
  
  
   
   
- 
   
   Compatibility Requirements
   
   These requirements ensure that your app remains compatible with Oculus runtime libraries and you are mindful of Oculus recommended hardware specifications.
   
- 
   
   Graphics and Performance Requirements
   
   These requirements ensure your app is responsive, performant, and able to render graphics at the quality expected for an Oculus Store app.
   
- 
   
   Functional
   
   These requirements ensure your app functions according to Oculus Store standards. 
   
- 
   
   Security
   
   These requirements ensure your app safeguards the privacy and integrity of Oculus and customer data.
   
- 
   
   User Interaction
   
   These requirements ensure your app provides a user experience consistent with Oculus user interaction standards.
   
  
  
  
  
   
[
   Previous: Our Basic Content Policy]
(/documentation/distribute/latest/concepts/publish-content-guidelines/ "")
  
  
  
   
[
   Next: Compatibility Requirements]
(/documentation/distribute/latest/concepts/publish-reqs-rift-compatibility/ "")
  
  
  
  
  
  
