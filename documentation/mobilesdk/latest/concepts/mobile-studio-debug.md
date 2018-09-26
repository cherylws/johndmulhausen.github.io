---
title: Native Debugging with Android Studio
---

This section introduces debugging our sample native apps in Android Studio.

The default configurations created during project import only support Java debugging.

Select **Edit Configurations…** in the **Configurations** drop-down menu in the Android Studio toolbar.

![](/images/documentationmobilesdklatestconceptsmobile-studio-debug-0.png)

Create a new **Android Native** configuration as show below:

![](/images/documentationmobilesdklatestconceptsmobile-studio-debug-1.png)

In the **General** tab of the **Run/Debug Configuration** dialog box, assign your configuration a name, select the target module, and select the target device mode: 

![](/images/documentationmobilesdklatestconceptsmobile-studio-debug-2.png)

In the **Native** tab of the **Run/Debug Configuration** dialog box, add symbol paths:

![](/images/documentationmobilesdklatestconceptsmobile-studio-debug-3.png)

Note that ndk-build places stripped libraries inside the **libs/** directory. You must point the symbol search paths at the obj/local/&lt;arch&gt; directory. This is also not a recursive search path, so you must put the **full** path to the obj/local/armeabi-v7a directory.

![](/images/documentationmobilesdklatestconceptsmobile-studio-debug-4.png)
