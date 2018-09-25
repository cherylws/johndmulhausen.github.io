---
title: Native Debugging with Android Studio
---
This section introduces debugging our sample native apps in Android Studio.

Note: Native support in Android Studio is still under development. Some developers have reported problems using run-as with the Note 4 with Lollipop (5.0.x) and S6 with 5.0.0, which may cause issues with debugging. If you have problems debugging, try updating to the latest system software, and please let us know on the [Oculus Forums](https://forums.oculus.com/developer).The default configurations created during project import only support Java debugging.

Select *Edit Configurationsâ€¦* in the *Configurations* drop-down menu in the Android Studio toolbar.

![](/images/documentation-mobilesdk-latest-concepts-mobile-studio-debug-0.png)  
Create a new *Android Native* configuration as show below:

![](/images/documentation-mobilesdk-latest-concepts-mobile-studio-debug-1.png)  
In the *General* tab of the *Run/Debug Configuration* dialog box, assign your configuration a name, select the target module, and select the target device mode: 

![](/images/documentation-mobilesdk-latest-concepts-mobile-studio-debug-2.png)  
In the *Native* tab of the *Run/Debug Configuration* dialog box, add symbol paths:

![](/images/documentation-mobilesdk-latest-concepts-mobile-studio-debug-3.png)  
Note that ndk-build places stripped libraries inside the *libs/* directory. You must point the symbol search paths at the obj/local/<arch> directory. This is also not a recursive search path, so you must put the *full* path to the obj/local/armeabi-v7a directory.

![](/images/documentation-mobilesdk-latest-concepts-mobile-studio-debug-4.png)  
