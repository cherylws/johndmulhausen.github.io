---
title: Screenshot and Video Capture
---

Full-resolution, undistorted, single-eye, full-layer-support 2D screenshots and video capture for VR apps are available through the sharing menu. Video capture is also available by configuring localprefs. 

## Photo and Video Capture Using the Sharing Menu

The sharing menu, available by pressing the Oculus button and selecting **Sharing**, allows you to take screenshots and record video anywhere in VR.



![](/images/documentationmobilesdklatestconceptsmobile-testing-capture-0.jpg)



These captures and recordings are stored locally until you export them. 

## Video Capture using Android System Properties

To enable video capture, set the debug.oculus.enableVideoCapture to 1 with the following command: 

```
adb shell setprop debug.oculus.enableVideoCapture 1
```

When enabled, each enterVrMode will generate a new mp4 file, and every vrapi_EnterVrMode() will create a new video file. For example, if you launch an app from Home, you may find one video file for your Home session, one for the app you launch, one for System Activities if you long-press, and so forth.

To help ensure that there is no disruption to the play experience while recording, you may wish to force the GPU level up and chromatic correction off:

```
adb shell setprop debug.oculus.enableVideoCapture 1 debug.oculus.gpuLevel 3
```

The FOV is reduced to 80 degrees, so you are unlikely to see any black pull-in at the edges.
