---
title: Native Debugging with ndk-gdb
---

This guide provides basic recommendations for using ndk-gdb to debug native mobile VR projects, and is intended to supplement the relevant Android Studio documentation.

The Android NDK includes a powerful debugging tool called ndk-gdb, a small shell script wrapped around GDB. Using ndk-gdb from the command line adds convenient features to your debugging workflow by allowing, for example, adding breakpoints, stepping through code, and inspecting variables.

## Create Breakpoints

**Break On Function**

```
(gdb) break SomeFunctionName()
```

or

```
(gdb) break SomeClass::SomeMethod()
```

Example usage:

```
(gdb) break OVR::VrCubeWorld::Frame(OVR::VrFrame const&amp;)
    Breakpoint 2 at 0xf3f56118: file jni/../../../Src/VrCubeWorld_Framework.cpp, line 292.
```

**Break On File:Line**

```
(gdb) break SomeFile.cpp:256
```

**Conditional Breakpoints**

Add if &lt;some condition&gt; to the end of your break command.

Example usage:

```
(gdb) break OVR::VrCubeWorld::Frame(OVR::VrFrame const&amp;) if vrFrame.PredictedDisplayTimeInSeconds &gt; 24250.0
 Breakpoint 6 at 0xf3f58118: file jni/../../../Src/VrCubeWorld_Framework.cpp, line 292.
```

**Break At Current Execution**

Example usage:

```
(gdb) break OVR::VrCubeWorld::Frame(OVR::VrFrame const&amp;) if vrFrame.PredictedDisplayTimeInSeconds &gt; 24250.0
   Breakpoint 6 at 0xf3f58118: file jni/../../../Src/VrCubeWorld_Framework.cpp, line 292.
```

**Break At Current Execution**

When an application is actively running, press control-c to break immediately and bring up the gdb prompt.

## Stepping

**Step Over**

```
(gdb) next
```

or

```
(gdb) n
```

**Step Into**

```
(gdb) step
```

or

```
(gdb) s 
```

**Continue Execution**

```
(gdb) continue
```

or

```
(gdb) c
```

## Printing

**Print Struct**

You may enable pretty printing mode to add new lines between struct elements (optional):

```
 (gdb) set print pretty on
```

To print the struct:

```
 (gdb) print SomeStructVariable
```

Example usage: 

```
(gdb) print currentRotation
 $1 = {
  x = 23185.9961, 
  y = 23185.9961, 
  z = 0, 
  static ZERO = {
   x = 0, 
   y = 0, 
   z = 0, 
   static ZERO = &lt;same as static member of an already seen type&gt;
  }
 }
```

**printf**

Example usage: 

```
(gdb) printf "x = %f\n", currentRotation.x
x = 23185.996094
```

## Breakpoint Commands

GDB breakpoints may be set to automatically execute arbitrary commands upon being hit. This feature is useful for inserting print statements into your code without recompiling or even modifying data at key points in your program without halting execution entirely. It is controlled by the commands command.

You may specify the breakpoint number with an optional single argument; if omitted, the final breakpoint is used. You are then presented with a series of lines beginning with &gt; where you may enter GDB commands (one per line) that will be executed upon hitting the breakpoint, until the command sequence is terminated with **end**.

In the following example, we create a breakpoint automatically prints the value of a local variable and then continues execution, upon being hit:

```
(gdb) break OVR::VrCubeWorld::Frame(OVR::VrFrame const&amp;) 
 Breakpoint 1 at 0xf3f56118: file jni/../../../Src/VrCubeWorld_Framework.cpp, line 292.
 (gdb) commands
 Type commands for breakpoint(s) 1, one per line.
 End with a line saying just "end".
 &gt;silent
 &gt;printf "time = %f\n", vrFrame.PredictedDisplayTimeInSeconds
 &gt;continue
 &gt;end
```

## Text User Interface (TUI)

To enable or disable the [TUI](https://sourceware.org/gdb/onlinedocs/gdb/TUI.html), press CTRL+x followed by CTRL+a.

For more information on TUI keyboard shortcuts, see [https://sourceware.org/gdb/onlinedocs/gdb/TUI-Keys.html](https://sourceware.org/gdb/onlinedocs/gdb/TUI-Keys.html).
