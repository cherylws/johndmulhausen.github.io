---
title: Runtime Threads
---



The **UI thread** is the launch thread that runs the normal Java code.

The **VR Thread** is spawned by the UI thread and is responsible for the initialization, the regular frame updates, and for drawing the eye buffers. All of the AppInterface functions are called on the VR thread. You should put any heavyweight simulation code in another thread, so this one basically just does drawing code and simple frame housekeeping. Currently this thread can be set to the real-time SCHED_FIFO mode to get more deterministic scheduling, but the time spent in this thread may have to be limited.

Non-trivial applications should create additional threads -- for example, music player apps run the decode and analyze in threads, app launchers load JPG image tiles in threads, et cetera. Whenever possible, do not block the VR thread on any other thread. It is better to have the VR thread at least update the view with new head tracking, even if the world simulation hasn't finished a time step.

The **Talk To Java (TTJ) Thread** is used by the VR thread to issue Java calls that aren't guaranteed to return almost immediately, such as playing sound pool sounds or rendering a toast dialog to a texture.

Sensors have their own thread so they can be updated at 500 Hz.
