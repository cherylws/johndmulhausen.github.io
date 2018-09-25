---
title: Power Management
---
Power management is a crucial consideration for mobile VR development.

A governor process on the device monitors an internal temperature sensor and tries to take corrective action when the temperature rises above certain levels to prevent malfunctioning or scalding surface temperatures. This corrective action consists of lowering clock rates.

If you run hard into the limiter, the temperature will continue climbing even as clock rates are lowered, and CPU clocks may drop resulting in a significantly degraded VR experience.

If your app consistently uses most of the available processing power, you will eventually run into the thermal governor, even if you have no problem at first. A typical manifestation is poor app performance after ten minutes of play. If you filter logcat output for "thermal" you will see various notifications of sensor readings and actions being taken. (For more on logcat, see [Android Debugging: Logcat](/documentation/mobilesdk/latest/concepts/mobile-logcat/#mobile-logcat "The Android SDK provides the logcat logging utility, which is essential for determining what an application and the Android OS are doing.").)

A difference to note between mobile and PC/console development is that no optimization is ever wasted. Without power considerations, if you have the frame ready in time, it doesn't matter if you used 90% of the available time or 10%. On mobile, every operation drains the battery and heats the device. Of course, optimization entails effort that comes at the expense of something else, but it is important to note the tradeoff.

## Managing Power Consumption

To deal with the power and heat issues identified above, the Fixed Clock Level API on Gear VR and Dynamic Clock Throttling on Oculus Go allows your app to manage heat and power consumption. 

**Fixed Clock Level API**

On current devices, the CPU and GPU clock rates are fixed to the application set values until the device temperature reaches the limit, at which point the CPU and GPU clocks will change to the power save levels. This change can be detected (see [Power State Notification and Mitigation Strategy](/documentation/mobilesdk/latest/concepts/mobile-power-overview/#mobile-power-state "The VrAPI provides power level state detection and handling.") below). Apps may choose to continue operating in a degraded fashion, perhaps by changing to 30 FPS or monoscopic rendering. Others may display a warning screen saying that play cannot continue.

The fixed CPU level and fixed GPU level set by the Fixed Clock Level API are abstract quantities, not MHz / GHz, so some effort can be made to make them compatible with future devices. For current hardware, the levels can be 0, 1, 2, or 3 for CPU and GPU. 0 is the slowest and most power efficient; 3 is the fastest and hottest.

Not all clock combinations are valid for all devices. For example, the highest GPU level may not be available for use with the two highest CPU levels. If an invalid matrix combination is provided, the system will not acknowledge the request and clock settings will go into dynamic mode. VrApi asserts and issues a warning in this case.

The Samsung Galaxy S8 and higher devices have a CPU frequency range instead of a set clock. CPU levels will be set to the minimum frequency in that range and scale up as needed.

Note: Use caution with combinations (2,3) and (3,3) because they are likely to lead quickly to overheating. For most apps, we recommend ensuring it runs well at (2,2).To set the CPU and GPU clock levels call:

vrapi\_SetClockLevels( ovrMobile * ovr, const int32\_t cpuLevel, const int32\_t gpuLevel );With your desired clock level. Default clock levels are cpuLevel = 2, gpuLevel = 2.

**Dynamic Clock Throttling on Oculus Go**

Oculus Go introduces Dynamic Clock Throttling which scales the performance of the CPU and GPU up as necessary to maintain performance. As they use similar components, clock frequencies will be similar to the Samsung Galaxy S7. 

Oculus Go apps still set levels using the Fixed Clock Level API as described above, but these levels are now treated as a baseline and the system can choose to dynamically increase the CPU and GPU clock up based on the app and system performance. The Dynamic Clock will never downclock your app's performance. 

As Oculus Go is able to manage thermal issues much more efficiently than a phone, we’ve opened CPU and GPU level 4 as an even higher performance benchmark.

More information about how Dynamic Clock Throttling works is available on the [Optimizing Oculus Go for Performance](/blog/optimizing-oculus-go-for-performance/) blog post.

When testing and debugging your app, you should disable Dynamic Throttling so that it does not interfere with performance timing. You can do this via adb:

adb shell setprop debug.oculus.adaclocks.force 0The system will remain off until you restart the device, or turn Dynamic Throttling back on by setting the above property to 1.

Alternatively, you can also test your app by using the VrAPI logs to review the clock level of your app. Please review the [Testing and Troubleshooting](/documentation/mobilesdk/latest/concepts/book-testing/ "Welcome to the testing and troubleshooting guide.") guide for more information. 

## Power Management and Performance

There are no magic settings in the SDK to fix power consumption - this is critical.

The length of time your application will be able to run before running into the thermal limit depends on two factors: how much work your app is doing, and what the clock rates are. Changing the clock rates all the way down only yields about a 25% reduction in power consumption for the same amount of work, so most power saving has to come from doing less work in your app.

If your app can run at the (0,0) setting, it should never have thermal issues. It is certainly possible to make sophisticated applications at that level, but Unity-based applications might be difficult to optimize for this setting.

There are effective tools for reducing the required GPU performance:

* Don’t use chromatic aberration correction on TimeWarp.
* Don’t use 4x MSAA.
* Reduce the eye target resolution.
* Using 16-bit color and depth buffers may help.
* It is probably never a good trade to go below 2x MSAA – you should reduce the eye target resolution instead.
These all entail quality tradeoffs which need to be balanced against steps you can take in your application:

* Reduce overdraw (especially blended particles) and complex shaders.
* Always make sure textures are compressed and mipmapped.
In general, CPU load seems to cause more thermal problems than GPU load. Reducing the required CPU performance is much less straightforward. Unity apps should always use the multithreaded renderer option, since two cores running at 1 GHz do work more efficiently than one core running at 2 GHz. 

If you find that you just aren’t close, then you may need to set *MinimumVsyncs* to *2* and run your game at 30 FPS, with TimeWarp generating the extra frames. Some things work out okay like this, but some interface styles and scene structures highlight the limitations. For more information on how to set MinimumVsyncs, see the [TimeWarp](/documentation/mobilesdk/latest/concepts/mobile-timewarp-overview/#mobile-timewarp-overview "Asynchronous TimeWarp (ATW) transforms stereoscopic images based on the latest head-tracking information to significantly reduce the motion-to-photon delay. reducing latency and judder in VR applications.") technical note.

In summary, our general advice:

If you are making an app that will probably be used for long periods of time, like a movie player, pick very low levels. Ideally use (0,0), but it is possible to use more graphics if the CPUs are still mostly idle, perhaps up to (0,2).

If you are okay with the app being restricted to ten-minute chunks of play, you can choose higher clock levels. If it doesn’t work well at (2,2), you probably need to do some serious work.

With the clock rates fixed, observe the reported FPS and GPU times in logcat. The GPU time reported does not include the time spent resolving the rendering back to main memory from on-chip memory, so it is an underestimate. If the GPU times stay under 12 ms or so, you can probably reduce your GPU clock level. If the GPU times are low, but the frame rate isn’t 60 FPS, you are CPU limited.

Always build optimized versions of the application for distribution. Even if a debug build performs well, it will draw more power and heat up the device more than a release build.

Optimize until it runs well. 

For more information on how to improve your Unity application’s performance, see [Best Practices and Performance Targets](/documentation/unity/latest/concepts/unity-best-practices-intro/) in our Unity documentation.

## Power State Notification and Mitigation Strategy

The VrAPI provides power level state detection and handling.

Power level state refers to whether the device is operating at normal clock frequencies or if the device has risen above a thermal threshold and thermal throttling (power save mode) is taking place. In power save mode, CPU and GPU frequencies will be switched to power save levels. The power save levels are equivalent to setting the fixed CPU and GPU clock levels to (0, 0). If the temperature continues to rise, clock frequencies will be set to minimum values which are not capable of supporting VR applications.

Once we detect that thermal throttling is taking place, the app has the choice to either continue operating in a degraded fashion or to immediately exit to the Oculus Menu with a head-tracked error message.

In the first case, when the application first transitions from normal operation to power save mode, the following will occur:

* A system menu will be brought up to display a dismissible warning message indicating that the device needs to cool down.
* Once the message is dismissed, the application will resume in 30Hz TimeWarp mode with correction for chromatic aberration disabled.
* If the device clock frequencies are throttled to minimum levels after continued use, a non-dismissible error message will be shown and the user will have to undock the device.
In this mode, the application may choose to take additional app-specific measures to reduce performance requirements. For Native applications, you may use the following VrApi call to detect if power save mode is active:

vrapi\_GetSystemStatusInt( &java, VRAPI\_SYS\_STATUS\_THROTTLED ) != VRAPI\_FALSE ).In the second case, when the application transitions from normal operation to power save mode, a system menu will be brought up to display a non-dismissible error message and the user will have to undock the device to continue. This mode is intended for applications which may not perform well at reduced levels even with 30Hz TimeWarp enabled.

To enable power save mode, the native application should specify the ovrModeFlags flag VRAPI\_MODE\_FLAG\_ALLOW\_POWER\_SAVE on the ovrModeParms for vrapi\_EnterVrMode.

