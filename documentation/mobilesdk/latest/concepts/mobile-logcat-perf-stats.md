---
title: Basic Performance Stats through Logcat
---
A simple way to get some basic performance numbers is to use logcat with a filter for VrApi.

Sample usage:

adb logcat -s VrApiA line resembling this example will be displayed every second:

I/VrApi (26422): FPS=60,Prd=49ms,Tear=0,Early=60,Stale=0,VSnc=1,Lat=1,CPU4/GPU=2/1,1000/350MHz,OC=FF,TA=F0/F0/F0/F0,SP=F/F/N/N,Mem=1026MHz,Free=1714MB,PSM=0,PLS=0,Temp=31.5C/27.**FPS**: Frames Per Second. An application that performs well will continuously display 59-60 FPS.

**Prd**: The number of milliseconds between the latest sensor sampling for tracking and the anticipated display time of new eye images. For a single-threaded application this time will normally be 33 milliseconds. For an application with a separate renderer thread (like Unity) this time will be 49 milliseconds. New eye images are not generated for the time the rendering code is executed, but are instead generated for the time they will be displayed. When an application begins generating new eye images, the time they will be displayed is predicted. The tracking state (head orientation, et cetera) is also predicted ahead for this time. 

**Tears**: The number of tears per second. A well behaved and well performing application will display zero tears.

Tears can be related to Asynchronous TimeWarp, which takes the last completed eye images and warps them onto the display. The time warp runs on a high priority thread using a high priority OpenGL ES context. As such, the time warp should be able to preempt any application rendering and warp the latest eye images onto the display just in time for the display refresh. However, when there are a lot of heavyweight background operations or the application renders many triangles to a small part of the screen, or uses a very expensive fragment program, then the time warp may have to wait for this work to be completed. This may result in the time warp not executing in time for the display refresh, which, in return, may result in a visible tear line across one of the eyes or both eyes. 

**Early**: The number of frames that are completed a whole frame early.

**Stale**: The number of stale frames per second. A well-behaved application performing well displays zero stale frames.

New eye images are generated for a predicted display time. If, however, the new eye images are not completed by this time, then the time warp may have to re-project and display a previous set of eye images. In other words, the time warp displays a stale frame. Even though the time warp re-projects old eye images to make them line up with the latest head orientation, the user may still notice some degree of intra-frame motion judder when displaying old images. 

**Vsnc**: The value of MinimumVsyncs, which is the number of V-Syncs between displayed frames. This value directly controls the frame rate. For instance, MinimumVsyncs = 1 results in 60 FPS and MinimumVsyncs = 2 results in 30 FPS.

**CPU0/GPU**: The CPU and GPU clock levels and associated clock frequencies, set by the application. Lower clock levels result in less heat and less battery drain.

**F/F [Thread Affinity]**: This field describes the thread affinity of the main thread (first hex nibble) and renderer thread (second hex nibbles). Each bit represents a core, with 1 indicating affinity and 0 indicating no affinity. For example, F/1 (= 1111 0001) indicates the main thread can run on any of the lower four cores, while the rendered thread can only run on the first core. In practice, F/F and F0/F0 are common results. 

**Free**: The amount of available memory, displayed every second. It is important to keep a reasonable amount of memory available to prevent Android from killing backgrounded applications, like Oculus Home.

**PLS**: Power Level State, where "0" = normal, "1" = throttled, and "2" = undock required.

**Temp**: Temperature in degrees Celsius. Well-optimized applications do not cause the temperature to rise quickly. There is always room for more optimization, which allows lower clock levels to be used, which, in return, reduces the amount of heat that is generated.

