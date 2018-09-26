---
title: Measuring Loudness
---

The Loudness Meter continuously monitors the selected audio interface to compile an overall loudness profile for your app.

The loudness computation begins as soon as the Loudness Meter detects an audio signal stronger than -70 LUFS. The longer you monitor your audio, the less fluctuation you will see in the integrated LUFS. 

## Measuring Rift Loudness

Rift apps should not exceed the loudness target of -18 LUFS. The observed LUFS value turns red if this threshold is exceeded.

1. Start your Rift app.
2. Set the app audio volume (if any) and Rift audio volume to 100%.
3. Start OculusLoudnessMeter.exe.
4. On the **Options** menu, point to **LUFS Threshold Target**, and then click **-18 (Rift)**.
5. Play a typical scene or level.


## Measuring Gear VR Loudness

Gear VR apps should not exceed the loudness target of -16 LUFS. The observed LUFS value turns red if this threshold is exceeded.

1. Connect the stereo audio cable between the Gear VR headphone jack and your computer's line-in jack.
2. Set the Windows sound mixer line-in level to 100%.
3. Start your Gear VR app.
4. Set the Gear VR audio volume to 100%.
5. Verify that you can hear the Gear VR app audio through your current Windows playback device.
6. Start OculusLoudnessMeter.exe.
7. On the **Options** menu, point to **Input**, and then click the current Windows playback device.
8. On the **Options** menu, point to **LUFS Threshold Target**, and then click **-16 (Gear VR)**.
9. Play a typical scene or level.


## Resetting the Meter

Click **RESET** to discard the current loudness measurement and start over. Keep in mind that integrated LUFS are not calculated until the audio signal is stronger than -70 LUFS.

## Measuring Momentary Loudness

Right-click the contents of the Loudness Meter to toggle momentary loudness measurement mode. This mode uses a 400ms time interval for calculating loudness, and is therefore good for observing peaks in the audio mix while the audio is being analyzed.

You may switch freely between momentary and integrated loudness measurement modes. Switching to momentary mode does not affect the integrated loudness that is continuously calculated in the background.
