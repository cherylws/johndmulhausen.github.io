---
title: Getting Started with the Demos
---

Now that the Rift is plugged in, the drivers are installed, and the SDK is installed, you are ready to begin using the SDK. 

## Software Developers and Integration Engineers

If you’re integrating the Oculus SDK into your game engine, Oculus recommends starting with the sample projects.

Open the following projects, build them, and experiment with the provided sample code:

* Samples/Projects/Windows/VSxxxx/Samples.sln


### OculusRoomTiny

This is a good place to start because its source code compactly combines all critical features of the Oculus SDK. It contains logic necessary to initialize LibOVR core, access Oculus devices, use the player’s profile, implement head-tracking, sensor fusion, stereoscopic 3D rendering, and distortion processing. OculusRoomTiny comes with Direct3D 11, OpenGL and Direct3D 12 variants each with their own separate projects and source files.

![](/images/documentationpcsdklatestconceptsgsg-intro-oneworld-0.png)

### OculusWorldDemo

This is a more complex sample. It is intended to be portable and support many more features. These include windowed/full-screen mode switching, XML 3D model and texture loading, movement collision detection, adjustable view size and quality controls, 2D UI text overlays, and so on.

This is a good application to experiment with after you are familiar with the Oculus SDK basics. It also includes an overlay menu with options and toggles that customize many aspects of rendering including FOV, render target use, timewarp and display settings. Experimenting with these options may provide developers with insight into what the related numbers mean and how they affect things behind the scenes. 

When running OculusWorldDemo in Windows, is uses Direct3D 11 by default. However, you can choose the OpenGL rendering path by appending the command-line argument "-r GL" to the executable.

Beyond experimenting with the provided sample code, Oculus recommends reading the rest of this guide. It covers LibOVR initialization, head-tracking, rendering for the Rift, and minimizing latency.

## Artists and Game Designers

If you’re integrating the Oculus SDK into your game engine, Oculus recommends starting with the sample projects.

If you’re an artist or game designer unfamiliar with C++, we recommend downloading Unity along with the corresponding Oculus integration. You can use our out-of-the-box integrations to begin building Oculus-based content immediately. 

We also recommend reading through the **Oculus Best Practices Guide**, which has tips, suggestions, and research oriented around developing great VR experiences. Topics include control schemes, user interfaces, cut-scenes, camera features, and gameplay. The **Best Practices Guide** should be a go-to reference when designing your Oculus-ready games. 

Aside from that, the next step is to start building your own Oculus-ready game or application. Thousands of other developers are out building the future of virtual reality gaming. To see what they are talking about, go to [forums.oculus.com](https://forums.oculus.com/).

## OculusWorldDemo Demo

 Oculus recommends running the pre-built OculusWorldDemo to explore the SDK. You can find a link to the executable file in the root of the Oculus SDK installation. 

The following is a screenshot of the OculusWorldDemo application:

![](/images/documentationpcsdklatestconceptsgsg-intro-oneworld-1.png)

### OculusWorldDemo Controls

The OculusWorldDemo uses a mix of standard and specialized controls.

The following table describes keys and devices that you use for movement:

|    Key or Input    |      Movement      |
|---------------------|--------------------|
|        W, S        | Move forward, back |
|        A, D        | Strafe left, right |
|        Mouse        |  Look left, right  |
| Left gamepad stick |        Move        |
| Right gamepad stick |        Turn        |

The following table describes keys that you use for functions:

|  Key(s)  |              Function              |
|----------|------------------------------------|
|    F4    |        Multisampling toggle        |
|    F5    |            sRGB toggle            |
|    F7    |    Mono/stereo view mode toggle    |
|    F9    | Hardware full-screen (low latency) |
|   F11   |       Performance HUD toggle       |
|    E    |    Motion relative to head/body    |
|    R    |      Reset sensor orientation      |
|   Esc   |         Cancel full-screen         |
|   -, +   |         Adjust eye height         |
|    L    |      Adjust fourth view value      |
|   Tab   |            Options Menu            |
| Spacebar |     Toggle debug info overlay     |
|    T    |       Reset player position       |
|  Ctrl+Q  |                Quit                |
|    G    |      Cycle grid overlay mode      |
|   U, J   |      Adjust second view value      |
|   I, K   |      Adjust third view value      |
|    ;    |       Cycle rendered scenes       |
|  +Shift  |       Adjust values quickly       |
|    O    |          Toggle Time-Warp          |
|    C    |       Toggle FreezeEyeUpdate       |
|    V    |            Toggle Vsync            |

### OculusWorldDemo Usage

Once you’ve launched OculusWorldDemo, you should see a window on your PC monitor similar to the previous screenshot.

When the image correctly displays inside the Rift, take a moment to look around in VR and double-check that all of the hardware is working properly. You should be able to see that physical head translation is now also recreated in the virtual world as well as rotation. 

**Important: **If you need to move the sensor for any reason after initial calibration, be sure to minimize the movement of the HMD for a few seconds while holding it within the tracking frustum. This will give the system a chance to recalibrate the sensor pose. 

If you would like to explore positional tracking in more detail, you can press the semicolon (;) key to bring the “sea of cubes” field that we use for debugging. In this mode, cubes are displayed that allow you to easily observe positional tracking behavior. Cubes are displayed in green when head position is being tracked and in red when sensor fusion falls back onto the head model. 

There are a number of interesting things to take note of the first time you experience OculusWorldDemo. First, the level is designed to scale. Thus, everything appears to be roughly the same height as it would be in the real world. The sizes for everything, including the chairs, tables, doors, and ceiling, are based on measurements from real-world objects. All of the units are measured in meters. 

Depending on your actual height, you may feel shorter or taller than normal. The default eye height of the player in OculusWorldDemo is 1.61 meters (approximately the average adult eye height), but this can be adjusted using the using the ‘+’ and ‘-’ keys. 
