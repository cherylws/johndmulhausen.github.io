---
title: Profiling Spatialized Audio
---



## Profiling Local Apps

To connect the profiler to a local app:

1. Start your app.
2. Start OculusAudioProfiler.exe.
3. Click **Connect**.


## Profiling Gear VR and Other Remote Apps

Your app must be running on the same local area network as the computer running the Oculus Audio SDK Profiler. Additionally:

* Windows apps must have the Oculus Audio Profiler port allowed in the Windows Firewall. The default port is 2121.
* Gear VR and other mobile Android devices must be placed into Wi-Fi debugging mode. See [Connecting adb via WIFI](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-adb/)


To connect the profiler to a remote app:

1. Obtain the IP address of the device running your app.
2. Start your app.
3. Start OculusAudioProfiler.exe.
4. Enter the IP address and port of the device. The default port is 2121.
5. Click **Connect**.


 If you cannot connect to your remote app, try these troubleshooting tips: 

* Make sure the port you are using is not blocked by your network settings or Windows Firewall.
* Make sure your computer and remote device are on the same LAN and subnet.
* If connecting to Gear VR or other mobile Android devices, try to connect the PC to the network over Wi-Fi so that both the device and the PC are connected to the same Wi-Fi network.


## Reading Profiler Analytics

![](/images/documentationaudiosdklatestconceptsaudio-profiler-using-0.png)

* **OSP Version**. The Oculus Audio SDK version of the connected OSP instance.
* **Spatialized Sounds**. The number of spatialized sounds currently processed by the OSP.
* **Ambisonic Sounds**. The number of ambisonic sounds currently processed by the OSP.
* **Reverb and Reflections**. The current reverb and reflections parameter settings.
* **CPU %**. Plots the estimated CPU usage of the process the OSP is running in. This is an estimated value and does not account for multi-processor architectures.
* **Processed Sounds**. Plots the total number of spatialized and ambisonic sounds processed by the OSP.

