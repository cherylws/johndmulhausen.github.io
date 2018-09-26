---
title: SysTrace
---



SysTrace is the profiling tool that comes with the Android Developer Tools (ADT) Bundle. SysTrace can record detailed logs of system activity that can be viewed in the Google Chrome browser.

With SysTrace, it is possible to see an overview of what the entire system is doing, rather than just a single app. This can be invaluable for resolving scheduling conflicts or finding out exactly why an app isn’t performing as expected.

Under Windows: the simplest method for using SysTrace is to run the monitor.bat file that was installed with the ADT Bundle. This can be found in the ADT Bundle installation folder (e.g., C:\android\adt-bundle-windows-x86_64-20131030) under the sdk/tools folder. Double-click monitor.bat to start Android Debug Monitor.

![](/images/documentationmobilesdklatestconceptsmobile-sys-trace-0.png)

Select the desired device in the left-hand column and click the icon highlighted in red above to toggle Systrace logging. A dialog will appear enabling selection of the output .html file for the trace. Once the trace is toggled off, the trace file can be viewed by opening it up in Google Chrome.

You can use the WASD keys to pan and zoom while navigating the HTML doc. For additional keyboard shortcuts, please refer to the following documentation: [http://developer.android.com/tools/help/systrace.html](https://developer.android.com/tools/help/systrace.html)
