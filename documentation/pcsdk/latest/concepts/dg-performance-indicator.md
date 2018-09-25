---
title: Performance Indicator
---
Asynchornous TimeWarp (ATW) can mask latency and judder issues that would normally be apparent. To help you identify when your application or experience isn't performing and to test your game or experience before submitting it, Oculus provides performance indicators.

When enabled, a letter code appears in the upper right of the headset whenever the application is experiencing a performance issue. The following figure shows an example of a performance indicator with L and F displayed:

![](/images/documentation-pcsdk-latest-concepts-dg-performance-indicator-0.png)  
Performance IndicatorTo enable the Performance Indicator, start the Oculus Debug Tool, which is located here:

C:\Program Files\Oculus\Support\oculus-diagnostics\OculusDebugToolSet the Visible HUD option to Performance:

![](/images/documentation-pcsdk-latest-concepts-dg-performance-indicator-1.png)  
The performance indicator can return the following codes: 

* L - A latency issue is occurring; more than one frame of queue ahead is being applied.
* F - The application is not maintaining frame rate.
* C - The compositor is not maintaining frame rate. Possible causes include:


	+ Programs, such as anti-virus software, are overloading the CPU.
	+ The CPU cannot handle the number of threads.
	+ The CPU or GPU does not meet the recommended specification.
	+ Certain patterns of GPU usage, such as heavy usage of shaders and tessellation, are affecting frame rate.
	+ There is an issue with the GPU driver.
	+ There is an unknown hardware issue.
	
* U - An unknown error occurred.
Each warning lasts one frame. So, if L stays visible, the application is having continuous latency issues.

