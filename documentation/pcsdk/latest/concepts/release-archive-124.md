---
title: Changes in Version 1.24.x
---



## New Features for 1.24.x

* **Larger FOV for streaming game play:** The Oculus Debug Tool now provides a feature called FOV-Tangent Multiplier. This can be used to improve the viewing experience when streaming game play to an audience. With this feature, you can increase the size of the field of view (FOV) as it appears on mirrored flat screens, relative to what is displayed within the headset. This makes it more comfortable to view streamed or recorded game play since the FOV that is used within the headset can appear too constricted on flat screens, and thereby cause motion sickness on the part of the viewing audience. The FOV-Tangent Multiplier feature has two settings: Horizontal and Vertical. Simply set these values to the desired multiplier for the FOV. For example, if you set Horizontal to 1.2 and Vertical to 1.1, then the streamed FOV will be 20% larger horizontally, and 10% larger vertically, relative to the FOV within the headset. 
* **Improved Dash documentation:** The Dash documentation for the PC-SDK has been improved. Notably, the documentation now describes how to submit depth with your geometry. If you are rendering of lot of geometry near the user, it may cause uncomfortable visual disparities when a Dash panel renders on top of geometry that is closer to the player than the Dash panel. To avoid that disparity, you can submit depth with your eye buffers. This will allow Dash to draw an x-ray effect that prevents this discomfort. For this reason, and for future improvements, we recommend submitting depth data with your eye buffers. For more information see &lt;https://developer.oculus.com/documentation/pcsdk/latest/concepts/dg-dash/&gt;


## API Changes

* There are no breaking API changes in this release.


## Known SDK Issues

* The sample project, LibOVR.vcxproj, cannot be used with Visual Studio 2010 and 2012. If you compile this project with those Visual Studio versions, it will not load. A fix for this issue is expected in the 1.23 PC-SDK release. 
* There's a bug affecting the Guardian System API by which color set operations to the visualized grid don't work if they are called while the HMD is not being worn.

