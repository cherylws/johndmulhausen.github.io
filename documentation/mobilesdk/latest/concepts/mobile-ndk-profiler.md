---
title: NDK Profiler
---
Use NDK Profiler to generate gprof-compatible profile information.

The Android NDK profiler is a port of gprof for Android.

The latest version, which has been tested with this release, is 3.2 and can be downloaded from the following location: <https://code.google.com/p/android-ndk-profiler/>

Once downloaded, unzip the package contents to your NDK sources path, e.g.: C:\Dev\Android\android-ndk-r9c\sources.

Add the NDK pre-built tools to your PATH, e.g.: C:\Dev\Android\android-ndk-r9c\toolchains\arm-linux-androideabi-4.8\prebuilt\windows-x86\_64\bin.

## Android Makefile Modifications

1. Compile with profiling information and define NDK\_PROFILE

LOCAL\_CFLAGS := -pg -DNDK\_PROFILE2. Link with the ndk-profiler library

LOCAL\_STATIC\_LIBRARIES := android-ndk-profiler3. Import the android-ndk-profiler module

$(call import-module,android-ndk-profiler)## Source Code Modifications

Add calls to monstartup and moncleanup to your Init and Shutdown functions. Do not call monstartup or moncleanup more than once during the lifetime of your app.

#if defined( NDK\_PROFILE ) extern "C" void monstartup( char const * ); extern "C" void moncleanup(); #endif extern "C" { void Java\_oculus\_VrActivity2\_nativeSetAppInterface( JNIEnv * jni, jclass clazz ) { #if defined( NDK\_PROFILE ) setenv( "CPUPROFILE\_FREQUENCY", "500", 1 ); // interrupts per second, default 100 monstartup( "libovrapp.so" ); #endif app->Init(); } void Java\_oculus\_VrActivity2\_nativeShutdown( JNIEnv *jni ) { app->Shutdown(); #if defined( NDK\_PROFILE ) moncleanup(); #endif } } // extern "C"## Manifest File Changes

You will need to add permission for your app to write to the SD card. The gprof output file is saved in /sdcard/gmon.out.

<uses-permission android:name="android.permission.WRITE\_EXTERNAL\_STORAGE" />## Profiling your App

To generate profiling data, run your app and trigger the moncleanup function call by pressing the Back button on your phone. Based on the state of your app, this will be triggered by OnStop() or OnDestroy(). Once moncleanup has been triggered, the profiling data will be written to your Android device at /sdcard/gmon.out.

Copy the gmon.out file to the folder where your project is located on your PC using the following command: adb pull /sdcard/gmon.out

To view the profile information, run the gprof tool, passing to it the non-stripped library, e.g.:

arm-linux-androideabi-gprof obj/local/armeabi/libovrapp.soFor information on interpreting the gprof profile information, see the following: <http://sourceware.org/binutils/docs/gprof/Output.html>

