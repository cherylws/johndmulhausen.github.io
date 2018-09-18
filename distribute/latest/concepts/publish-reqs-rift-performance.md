
  
  
  
  
  
  
# Graphics and Performance Requirements
  
   
These requirements ensure your app is responsive, performant, and able to render graphics at the quality expected for an Oculus Store app.
   
   
## The app displays graphics in the headset at 90 frames per second
   
Rift apps must maintain steady 90 frames per second to avoid user discomfort. 
   
   
   
## The app runs and installs without crashing, freezing, or entering extended unresponsive states. 
   
Apps that are not stable are not accepted into the Oculus Store. 
   
   
   
## The app displays graphics without judder 
   
Judder is an undesirable visual effect that occurs when an app cannot maintain consistent frame rate and displays images in the headset that are not congruent with the user’s movement. While Asynchronous TimeWarp reduces some perceived judder, your application must still perform at a steady 90 frames per second. 
   
   
   
## The app renders without convergence errors or unusual distortion 
   
This is less of a concern for Unity and Unreal developers because our game engine integration always uses correct convergence. However, all developers must ensure that any pre-rendered stereo media content is free from convergence issues that could have been introduced during media production. 
   
   
   
## The app renders without visible z-fighting or depth conflict artifacts 
   
There must not be any z-fighting flickering amongst coplanar polygons. 
   
   
   
## The app must either display head-tracked graphics in the headset within 4 seconds of launch or provide a loading indicator in VR 
   
If your app takes longer than 4 seconds to launch, you must provide a head-tracked loading indicator. 
   
   
   
## The app must not synchronize animation or physics to an assumed 90 Hz frame rate 
   
Animations and physics synced to a fixed frame rate go out of sync when your app drops frames or when Asynchronous SpaceWarp is active. 
   
   
   
## The app should render head-locked UI elements in a compositor layer to avoid judder if the app misses frames or runs with asynchronous spacewarp. 
   
VR compositor layers update independent of the app frame rate. See 
[VR Compositor Layers]
(https://developer.oculus.com/documentation/unity/latest/concepts/unity-ovroverlay/ "")
  . 
   
  
  
  
  
  
   
[
   Previous: Compatibility Requirements]
(/documentation/distribute/latest/concepts/publish-reqs-rift-compatibility/ "")
  
  
  
   
[
   Next: Functional]
(/documentation/distribute/latest/concepts/publish-reqs-rift-functional/ "")
  
  
  
  
  
  
