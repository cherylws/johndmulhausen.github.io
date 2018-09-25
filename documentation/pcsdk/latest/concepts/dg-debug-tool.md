---
title: Oculus Debug Tool
---
The Oculus Debug Tool (IDT) enables you to view performance or debugging information within your game or experience. It also enables you to tune or configure related parameters, such as the field of view (FOV) size for a mirrored flat-screen view of the VR experience (which could be streamed to an audience in a more comfortable viewing format).

**Startup ODT**

To start the Oculus Debug Tool:

1. Make sure that you have admin privilege. This is required in order to run the Oculus Debug Tool.
2. Browse to Program Files\Oculus\Support\oculus-diagnostics\. Note that the Oculus Debug Tool should always be run directly from this location, in order to ensure a version match with the Oculus distribution. If you copy the Oculus Debug Tool to another location, it might not work after subsequent Oculus updates.
3. Double-click OculusDebugTool.exe. The Oculus Debug Tool opens. The main window is shown below with all of the first-level list headings expanded:![](/images/documentation-pcsdk-latest-concepts-dg-debug-tool-0.png)  

The ODT user interface is described in the following paragraphs.

**File Menu**

![](/images/documentation-pcsdk-latest-concepts-dg-debug-tool-1.png)  
* Launch App...: Launches a VR application.
* Validate App...: Launches the VRC Validator, which enables you to test your application for compliance with the Oculus Virtual Reality Check guidelines. See the "GUI Interface to the VRC Validator" section in [VRC Validator](/documentation/pcsdk/latest/concepts/dg-vrcvalidator/ "The Virtual Reality Check (VRC) Validator utility runs automated tests to determine if your Rift app is ready for Oculus Store technical review. The VRC Validator can reveal shortcomings that need to be addressed before your app can pass the Oculus Store review process. The VRC Validator has a command line interface as well as a GUI interface.").
* Restart as administrator: Restarts the Oculus Debug Tool with administrator permissions.
**Tools Menu**

![](/images/documentation-pcsdk-latest-concepts-dg-debug-tool-2.png)  
* Performance Profiler: Launches the Performance Profiler. For more information, see [Performance Profiler](/documentation/pcsdk/latest/concepts/dg-performance-profiler/ "The Oculus Performance Profiler displays a graph that shows statistics on the performance of your application."). 
* Lost Frame Capture: Launches the Lost Frame Capture too. For more information, see [Lost Frame Capture Tool](/documentation/pcsdk/latest/concepts/dg-performance-lostframes/ "The Lost Frame Capture tool collects information about dropped frames while your VR application is running. You can then replay the dropped frames while viewing statistical data, in order to help track down performance problems within your application.").
* Scene View: Visualizes your HMD and controller position. 
* Mirror: Displays the content that is rendered in HMD on your PC monitor. For more information, see [Compositor Mirror](/documentation/pcsdk/latest/concepts/dg-compositor-mirror/ "The Compositor Mirror tool displays the content that appears within the Rift headset on your computer monitor. It has several display options that are useful for development, troubleshooting, and presentations.").
**Service Menu**

![](/images/documentation-pcsdk-latest-concepts-dg-debug-tool-3.png)  
* Restart Oculus Service: Restarts the Oculus service on your local computer.
* Start Oculus Service: Starts the Oculus service on your local computer.
* Stop Oculus Service: Stops the Oculus service on your local computer.
* Toggle console window visibility: Turns the visibility of the console output window on and off. The console window shows the details of all the scripts and applications that run behind the scenes when you are using the ODT. Most users do not need to enable this option.
* Logs: Brings up a log window that tracks the details of all the scripts and applications that run behind the scenes when you are using the ODT. Most users do not need to enable this option.
**Using ODT**

1. It is a good idea to turn off Asynchronous Spacewarp (ASW), so that you can get a true sense of how your application is performing (without the assistance of ASW). To do this, set the Asynchronous Spacewarp option to Disabled: ![](/images/documentation-pcsdk-latest-concepts-dg-debug-tool-4.png)  

2. Select the Visible HUD display that you wish to view. Options include: None (no HUD is displayed), Performance HUD, Stereo Debug HUD, or Layer HUD.
3. If you selected Performance HUD, select which Performance HUD you want to view. Options include: Latency Timing, Render Timing, Performance Headroom, and Version Information. For more information, see [Performance Head-Up Display](/documentation/pcsdk/latest/concepts/dg-hud/ "The Performance Head-Up Display (HUD) enables you or your users to view performance information for applications built with the SDK."). The following is an example of the Performance HUD:

![](/images/documentation-pcsdk-latest-concepts-dg-debug-tool-5.png)  

4. If you selected Stereo Debug HUD, configure the mode, size, position, and color from the Stereo Debug HUD options. The following is an example of the Stereo Debug HUD:

![](/images/documentation-pcsdk-latest-concepts-dg-debug-tool-6.png)  

5. If you selected Layer HUD. select the layer for which to show information or select the Show All check box. The following is an example of the Layer HUD:

![](/images/documentation-pcsdk-latest-concepts-dg-debug-tool-7.png)  

6. Select Launch App from the File menu and select the executable of the application.
7. Put on the headset and view the results.
**Larger FOV for Streaming Game Play**

The FOV-Tangent Multiplier setting is provided by the Oculus Debug Tool, as shown in the following screenshot. This setting can be used to improve the viewing experience when streaming game play to an audience. With this feature, you can increase the size of the field of view (FOV) as it appears on mirrored flat screens, relative to what is displayed within the headset. This makes it more comfortable to view streamed or recorded game play since the FOV that is used within the headset can appear too constricted on flat screens, and thereby cause motion sickness on the part of the viewing audience. The FOV-Tangent Multiplier feature has two settings: Horizontal and Vertical. Simply set these values to the desired multiplier for the FOV. For example, if you set Horizontal to 1.2 and Vertical to 1.1, then the streamed FOV will be 20% larger horizontally, and 10% larger vertically, relative to the FOV within the headset. The ODT shows the Horizontal setting, followed by a semicolon, followed by the Vertical setting. So the previous example would be entered as 1.2;1.1 on the FOV-Tangent Multiplier line: 

![](/images/documentation-pcsdk-latest-concepts-dg-debug-tool-8.png)  
