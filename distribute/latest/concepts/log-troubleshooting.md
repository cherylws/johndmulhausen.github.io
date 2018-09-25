---
title: Troubleshooting and Gathering Logs
---
Sometimes things don’t work how you expect them to. This page describes how you can retrieve logs to troubleshoot your app and request help.

## Troubleshooting the Oculus Run Time

OculusLogGatherer is included with every instance of the install and can be used when you have issues with the Oculus Run Time. Navigate to the .exe file and run the application (C:\Program Files (x86)\Oculus\Support\oculus-diagnostics\OculusLogGatherer.exe).

The application will launch and ask how much log data you want to export, the default is 24 hours. “Get All Logs” will export all available logs.

The export, a .zip file, will be copied to the clipboard and saved to your desktop. The .zip export organizes the files by log type.

Note: The tool requires local administrative privileges to run.## Troubleshooting Unity Editor Issues

If you're having issues with the Unity Editor, please review Unity's [How to Report Bugs](https://unity3d.com/unity/qa/bug-reporting) page for information about reporting bugs to Unity.

The [Issue Tracker](https://issuetracker.unity3d.com/?_ga=1.237215616.147149137.1481760426) has information about known issues, check to see if what you are experiencing has already been reported. If the issue is not already known, you can report the bug in the Unity Editor (Help->Report).

## Troubleshooting a Unity/Oculus Integration

**Using Log Files**

If your issue exists with the Unity/Oculus software integration, please review the Unity [Log Files](https://docs.unity3d.com/Manual/LogFiles.html) page for information on how to retrieve the logs.

The log file for your unity project can be retrieved by using the command %LOCALAPPDATA%\Unity\Editor\Editor.log.

If you experience a crash, retrieve the log and search for "tombstone", which is written and logged after the crash. If you scroll up from there, there will be a callstack, which describes the process that were occurring at the time of the crash.

**Using Crash/Dump Files**

When Unity or an app encounters a failed state, please ctr-alt-delete (windows only), right click on the failed process, and select "create dump file" from the menu. The dump file's location will be displayed to you upon successful creation.

## Troubleshooting Unreal Editor Issues

If you're having issues with the Unreal Editor, please review Unreal's [How to Report Bugs](https://www.unrealengine.com/en-US/support/report-a-bug) page for information about reporting bugs to Unreal.

The Unreal Engine [Issues Tracker](https://issues.unrealengine.com/) has information about known issues, check to see if what you are experiencing has already been reported. If the issue is not already known, please make a new report in the tracker.

## Troubleshooting an Unreal/Oculus Integration

**Using Log Files**

If your issue exists with the Unreal/Oculus software integration, please review the Unreal [Log Files](https://wiki.unrealengine.com/Locating_Project_Logs) page for information on how to retrieve the logs.

The Unreal Editor can pull a log files specific to the area where you're encountering issues. You can generate Editor Session Logs, Game Logs, Build/Cook Logs, Crash Logs, and Compile Logs.

When diagnosing specific issues it is helpful to have Editor Session Logs and Crash Logs to send to Oculus when requesting support.

The editor session log file for your Unreal project is located at Engine\Saved\Logs\UE4.log.

The crash logs file for your Unreal project can be retrieved using the command: %USERPROFILE%\AppData\Local\Microsoft\Windows.

**Using Crash/Dump Files**

If you experience a crash, retrieve the log and search for "tombstone", which is written and logged after the crash. If you scroll up from there, there will be a callstack that lists the process that were occurring at the time of the crash.

The crash dump is automatically generated by Unreal in the event of a crash in your project. You can find the file titled minidump.dmp in your C:\Users\UserName\AppData\WER\ReportQueue folder.

## Get Support

If you're unable to diagnose the issue yourself using the information you retrieved, there are two ways to request help.

1. [Oculus Discussion Forums](https://forums.oculus.com/developer/) - Ask questions, review answers, and connect with a community of Oculus developers. The Oculus team monitors the Forum and will provide support when needed.
2. [Contact Us Directly](/contact/) - Use the form to send us a message describing the issue you're having and indicate that you have a log or file that you would like to submit to Oculus for review.