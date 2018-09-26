---
title: Building UE4 from Source
---

The following section describes how to download, compile, and launch UE4 from the Oculus GitHub repository using Visual Studio **2015 or 2017**.

Professional developers who wish to take full advantage of the features available with our Unreal integration should download and build the source code.

This guide assumes you have installed Visual Studio **2015 or 2017** and are familiar with its use. 

Several of these steps may take some time to complete. Some of the steps typically take over an hour, depending on your computer and the speed of your Internet connection.

1. Clone or download the UE4 source code from the Oculus GitHub repository here: &lt;https://github.com/Oculus-VR/UnrealEngine&gt;. To access this repository, **you must** have access to the private Epic GitHub repository (see &lt;https://www.unrealengine.com/ue4-on-github&gt; for details).
2. If you downloaded a zip archive of the code, extract the archive contents to a directory where you would like to build the engine, e.g., C:\Unreal\4.xx-oculus. We recommend installing to a short path, or you may have errors in the next step with files that exceed the Windows length limit for file names. Alternately, you can map your install directory as a Windows drive to reduce the path length. 
3. Run Setup.bat. You may need to **Run as Administrator**. 
4. Run GenerateProjectFiles.bat. You may need to **Run as Administrator**. By default, GenerateProjectFiles.bat creates project files for Visual Studio 2017. If you are using Visual Studio 2015, you must use the -2015 flag (GenerateProjectFiles.bat -2015).
5. Launch UE4.sln to open the project solution in Visual Studio.
6. In the menu bar, select **Build** &gt; **Configuration Manager**. Verify that **Active solution configuration** is set to **Development Editor**, and that **Active solution platform** is set to **Win64**. ![](/images/documentationunreallatestconceptsunreal-building-ue4-from-source-0.png)


7. In the Solution Explorer, right-click **UE4** under **Engine** and select **Set as Startup Project**. ![](/images/documentationunreallatestconceptsunreal-building-ue4-from-source-1.png)


8. Select **Build** from the same context menu as the previous step. 
9. To launch the engine: * With command-line arguments: Right-click UE4 in the Solution Explorer and select **Properties**. In the UE Property Pages dialog, select **Configuration Properties** &gt; **Debugging** on the left. Enter any desired configuration options in the **Command Arguments** field on the top. * Without command-line arguments: In the Solution Explorer on the right, right-click UE4 under Engine and, in the context menu, select **Debug** &gt; **Start New Instance** to launch the engine. 

![](/images/documentationunreallatestconceptsunreal-building-ue4-from-source-2.png)


10. Select the project you would like to open, or specify a new project. If you are creating a new project, donâ€™t forget to specify a project name.
11. At this point, the engine will close and a new instance of Visual Studio will launch with your selected or new project. Repeat step 6 to launch the engine with the specified project.


For Epic's instructions on building the Unreal Engine from source, see [Building Unreal Engine from Source](https://docs.unrealengine.com/latest/INT/Programming/Development/BuildingUnrealEngine/) guide.
