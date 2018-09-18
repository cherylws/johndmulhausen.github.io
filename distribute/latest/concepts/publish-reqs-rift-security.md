
  
  
  
  
  
  
# Security
  
   
These requirements ensure your app safeguards the privacy and integrity of Oculus and customer data.
   
   
## The app must perform an Oculus Platform entitlement check within 10 seconds of launch
   
It is not sufficient to merely perform the entitlement check. If the check fails, the app must either exit the app or run in a limited demo mode. See 
[Initializing and Checking Entitlements]
(https://developer.oculus.com/documentation/platform/latest/concepts/pgsg-get-started-with-sdk/ "")
  .
   
   
   
## The app must not be debuggable or contain debugger symbolics
   
Upload the release version of your app, not the debug version. 
   
   
   
## The app must not contain extraneous files such as marketing assets or libraries for other VR APIs and distribution platforms
   
This includes art and media assets not directly referenced by your app and any .dll files specific to other app stores.
   
  
  
  
  
  
   
[
   Previous: Functional]
(/documentation/distribute/latest/concepts/publish-reqs-rift-functional/ "")
  
  
  
   
[
   Next: User Interaction]
(/documentation/distribute/latest/concepts/publish-reqs-rift-ui/ "")
  
  
  
  
  
  
