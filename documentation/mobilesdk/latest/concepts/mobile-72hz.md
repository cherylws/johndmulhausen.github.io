---
title: 72 Hz Mode
---



Oculus Go can optionally render your application at 72 frames per second rather than the normal 60 frames. The resulting output is brighter with improved color clarity.

To change the refresh rate, call `vrapi_SetDisplayRefreshRate()`.

The available refresh rates can be queried with `vrapi_GetSystemPropertyInt()` using `VRAPI_SYS_PROP_NUM_SUPPORTED_DISPLAY_REFRESH_RATES` to get the number of supported rates, and `vrapi_GetSystemPropertyFloatArray()` with `VRAPI_SYS_PROP_SUPPORTED_DISPLAY_REFRESH_RATES` to get an array of the actual rates that are supported.

An app rendering at 72 Hz requires roughly 20% more power to maintain the same framerate as rendering at 60 Hz.

Our [Optimizing Oculus Go for Performance](/blog/optimizing-oculus-go-for-performance/) blog post contains recommendations for when to use 72 Hz mode. 
