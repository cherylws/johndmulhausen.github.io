---
title: Logcat
---
The Android SDK provides the logcat logging utility, which is essential for determining what an application and the Android OS are doing.

To use logcat, connect the Android device via USB or Wi-Fi, launch an OS shell, and type:

adb logcatIf the device is connected and detected, the log will immediately begin outputting to the shell. In most cases, this raw output is too verbose to be useful. Logcat solves this by supporting filtering by tags. To see only a specific tag, use:

adb logcat -s <tag>This example:

adb logcat -s VrAppwill show only output with the "VrApp" tag.

In the native VrAppFramework code, messages can generally be printed using the LOG() macro. In most source files this is defined to pass a tag specific to that file. Log.h defines a few additional logging macros, but all resolve to calling \_\_android\_log\_print().

## Using Logcat to Determine the Cause of a Crash

Logcat will not necessarily be running when an application crashes. Fortunately, it keeps a buffer of recent output, and in many cases a command can be issued to logcat immediately after a crash to capture the log that includes the backtrace for the crash:

adb logcat > crash.logSimply issue the above command, give the shell a moment to copy the buffered output to the log file, and then end adb (Ctrl+C in a Windows cmd prompt or OS X Terminal prompt). Then search the log for "backtrace:" to locate the stack trace beginning with the crash.

If too much time as elapsed and the log does not show the backtrace, there a full dump state of the crash should still exist. Use the following command to redirect the entire dumpstate to a file:

adb shell dumpstate > dumpstate.logCopying the full dumpstate to a log file usually takes significantly longer than simply capturing the currently buffered logcat log, but it may provide additional information about the crash.

## Getting a Better Stack Trace

The backtrace in a logcat capture or dumpstate generally shows the function where the crash occurred, but does not provide line numbering. To get more information about a crash, the Android Native Development Kit (NDK) must be installed. When the NDK is installed, the ndk-stack utility can be used to parse the logcat log or dumpstate for more detailed information about the state of the stack. To use ndk-stack, issue the following:

ndk-stack -sym <path to symbol file> -dump <source log file> > stack.logFor example, this command:

ndk-stack -sym VrNative\Oculus360Photos\obj\local\armeabi-v7a -dump crash.log > stack.loguses the symbol information for Oculus 360 Photos to output a more detailed stack trace to a file named stack.log, using the backtrace found in crash.log.

