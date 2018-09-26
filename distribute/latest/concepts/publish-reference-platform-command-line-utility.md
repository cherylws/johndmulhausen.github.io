---
title: Oculus Platform Command Line Utility
---

The Oculus Platform Command Line Utility lets you upload builds to your release channels much faster than using the Oculus dashboard web interface. It also allows you to incorporate automated uploads into your existing build system.

Compared to using the Oculus Dashboard, the Oculus Platform Command Line Utility uploads builds faster because it analyzes your build and only uploads the parts that have changed since your last upload.

## Installing the Command Line Utility

1. Go to &lt;https://dashboard.oculus.com/tools/cli&gt;.
2. Under **Download**, click **Mac OS X** or **Windows 32-bit and 64-bit** to download the appropriate command line tool executable.
3. Copy the command line utility to the directory of your choice.


## Syntax

See [Oculus Platform Command Line Utility](https://dashboard.oculus.com/tools/cli) for the full syntax and parameters list reference.

To toggle between the available reference information, click the headings **upload-rift-build**, **upload-gear-build**, and **download-build**.

## Rift Command Line Examples

This upload example uses the fictitious app "Rabbit Hole" and assumes the following sample parameters:

* App ID: 10001234
* App Secret Token: 1234abcd.
* Build Directory: C:\Rabbit Hole
* Launch File: C:\Rabbit Hole\bin\badrabbits.exe
* New version: 1.1
* Release Note: Fixes the rabbit spawn bug.


**Simple Rift Upload Example**

To upload version 1.1 of Rabbit Hole to the RC release channel, enter: 

```
ovr-platform-util upload-rift-build -a 10001234 -s 1234abcd -d "C:\Rabbit Hole" -l "bin\badrabbits.exe" -n "Fixes the rabbit spawn bug." -v 1.1 -c rc 
```

**Redistributables Example**

If the app requires .NET Framework 3.5 and Visual C++ 2013 x86 redistributable files, enter:

```
ovr-platform-util upload-rift-build -a 10001234 -s 1234abcd -d "C:\Rabbit Hole" -l "bin\badrabbits.exe" -n "Fixes the rabbit spawn bug." -v 1.1 -c rc -r "606493776156948, 910524935693407" 
```

**2D Mode with Firewall Exception Example**

If the app requires a Windows Firewall exception, Windows 10 as a minimum version, and has a 2D mode executable file and argument string of badrabbits2d.exe -force2dfix, enter:

```
ovr-platform-util upload-rift-build -a 10001234 -s 1234abcd -d "C:\Rabbit Hole" -l "bin\badrabbits.exe" -n "Fixes the rabbit spawn bug." -v 1.1  -c rc -L badrabbits2d.exe -P "-force2dfix" -f -w "10" 
```

**Multi-line Release Note Example**

If you have a multi-line release note, enter:

```
ovr-platform-util upload-rift-build -a 10001234 -s 1234abcd -d "C:\Rabbit Hole" -l "bin\badrabbits.exe" -n  "Carrots now available as in-app purchases.\nBlue rabbits no longer \"glitch\" and get stuck in terrain.\nSpawn sound spatialization adjusted for realism." -v 1.1 -c rc 
```

**Download Example**

To download the app build with build ID 3141592653589793 to “C:\Pie Thrower”:

1. Enter: ovr-platform-util download-build -b 3141592653589793 -d "C:\Pie Thrower"
2. Enter the email address and password of an Oculus user authorized to download the app.
3. The build should download to the specified directory.


## Gear VR Command Line Examples

This upload example uses the fictitious app "Rabbit Hole".

* App ID: 10001234
* App Secret Token: 1234abcd
* APK Path: C:\Rabbithole.apk
* APK Package name: com.oculus.rabbits


**Simple Gear VR Upload Example**

To upload Rabbit Hole to the Alpha release channel, enter:

```
ovr-platform-util upload-gear-build --app_id 10001234 --app_secret 1234abcd --apk C:\RabbitHole.apk --channel alpha --notes "Fixes the rabbit spawn bug."
```

**Multi-line Release Note Example**

If you have a multi-line release note, enter:

```
ovr-platform-util upload-gear-build --app_id 10001234 --app_secret 1234abcd --apk C:\RabbitHole.apk --channel alpha --notes "Carrots now available as in-app purchases.\nBlue rabbits no longer \"glitch\" and get stuck in terrain.\nSpawn sound spatialization adjusted for realism."
```

**Expansion File Example**

If you split version 2 of Rabbit Hole into separate APK and APK expansion files (see [APK Expansion File Requirements](/distribute/latest/concepts/publish-uploading-mobile/#apkexpansionfile)) we specify the full path to the expansion file with `--obb`. Enter:

```
ovr-platform-util upload-gear-build --app_id 10001234 --app_secret 1234abcd --apk C:\RabbitHole.apk --obb C:\main.2.com.oculus.rabbits.obb --channel alpha --notes "Split data and code to provide smaller and faster patch updates."
```
