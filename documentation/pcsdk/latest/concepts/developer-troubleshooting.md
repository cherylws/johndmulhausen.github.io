---
title: Troubleshooting
---
## Oculus Room Tiny Compile Errors

For Visual Studio 2010 through 2015, the Oculus Room Tiny (DX12) sample projects require you to specify an appropriate Windows 10 SDK for the build. 

Projects that use Windows SDK v10.0.10240.0 or later should compile without issue. Other SDKs might result in receive compile errors, such as missing dx12.h. 

For Visual Studio 2010 through 2013, edit the Samples\OculusRoomTiny\OculusRoomTiny (DX12)\Projects\Windows\Windows10SDKPaths.props file with a text editor and update it to your Windows 10 SDK, typically installed with headers at C:\Program Files (x86)\Windows Kits\10\Include. 

For Visual Studio 2015, select Project Properties -> General -> Target. Then, select the platform version from the list box.

## Installation Repeatedly Fails

If installation repeatedly fails, check for a similar message in the Windows Event Viewer: 

The OVRLibraryService service was unable to log on as NT SERVICE\OVRLibraryService with the currently configured password due to the following error: Log-on failure: the user has not been granted the requested log-on type at this computer.If you encounter this message, make sure the NT SERVICE\ALL SERVICES account has Log on as a servicerights through Local Security Settings (Secpol.msc). 

If you previously set this right and the right was removed, contact your administrator to check if a Group Policy Object (GPO) is removing the right. 

