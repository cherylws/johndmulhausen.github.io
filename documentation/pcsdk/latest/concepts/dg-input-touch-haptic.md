---
title: Haptic Feedback
---

In addition to reporting input state, Oculus touch controllers can provide haptic feedback through vibration.

The SDK supports two types of haptics:

* **Non-Buffered Haptics** – With this approach, haptics are controlled by simply turning vibrations on and off, while specifying a frequency (160Hz or 320Hz) and an amplitude (0 to 255). Non-buffered haptics are designed for simple effects that don't have tight latency requirements, since the controller requires 33ms to respond to the API call that modifies the haptics settings.
* **Buffered Haptics** – This approach enables a much wider variety of effects, such as patterning vibrational amplitudes around sine wave or tangent functions, panning the vibrations across controllers, generating a variety of low-frequency carrier waves, and more. With buffered haptics, your application sends a buffer of bytes to one or both controllers, where the bytes are interpreted as a series of amplitude values, from 0 (no vibrational amplitude) to 255 (maximum vibrational amplitude). The controller then “plays” the buffered amplitude values at 320Hz (or one byte every 3.125ms). Thus, you can control the vibrational amplitudes at a much finer degree of granularity when compared to non-buffered haptics (although it requires about 10ms from the time of the API call until the buffer is available to be played within the controller).


## Using Non-Buffered Haptics

Vibration can be enabled by calling `ovr_SetControllerVibration`: 

```
ovr_SetControllerVibration( Hmd, ovrControllerType_LTouch, freq, trigger);
```

Vibration is enabled by specifying the frequency. Specifying 0.0f will vibrate at 160Hz. Specifying 1.0f will vibrate at 320Hz.

## Buffered Haptics Overview

Buffered haptics enable you to create many cool effects beyond what is possible with non-buffered haptics. For example, the buffered haptics sample app that is provided with the PC-SDK (and which is described later in this section) produces the following effects:

* Smooth sine wave vibration with a "buzz down" effect at the end of each wave cycle
* Vibrational panning across the left and right controllers, again with a "buzz down" effect at the end of the panning cycle
* Ultra low-frequency buzz, essentially a series of ticks at 64Hz
* A "messed up" low frequency vibration based on a chaotic formula that utilizes a trigonometric tangent wave function


A buffer consists of a series of bytes with values from 0 to 255, where 0 represents no amplitude (i.e no vibration), and 255 represents the maximum amplitude (or intensity) of vibration that is allowed by the SDK. After your code fills in the values within a buffer, you send the buffer to one or both Touch controllers via `ovr_SubmitControllerVibration`. Each byte in the buffer is then "played" in sequence at a rate of 320Hz. The maximum buffer size (i.e. the maximum number of bytes that can be sent to a controller at one time, and also the maximum size of the controller's internal buffer) is 256 bytes. The length of time that it takes to "play" a single 256 byte buffer is 0.8 seconds (256 bytes played at a rate of 320Hz). So, you have full control over the amplitude of the vibrational effects down to a resolution of 3.125ms (which equates to 320Hz). However, the frequency can only be 320Hz or some integral quotient of 320Hz, such as 320/2=160Hz, 320/3=106.7Hz, 320/4=80Hz, 320/5=64Hz, etc. You can achieve these lower frequencies by sending bytes that are zero filled, interspersed with bytes that have amplitude values that are greater than zero. Here are some examples:

* 320Hz, full amplitude - [255, 255, 255, 255, ...]
* 160Hz, full amplitude - [255, 0, 255, 0, 255, 0, 255, 0, ...]
* 320Hz, half amplitude - [127, 127, 127, ..., 127, ...]
* 160Hz, half amplitude - [127, 0, 127, 0, 127, 0, â€¦, 127, 0, ...]
* Single sharp tick (320Hz) - [0, 0, 255, 255, 255, 0, 0] [delay x ms] [0, 0, 255, 255, 255, 0, 0] 
* Single blunt tick (160Hz) - [0, 255, 0, 255, 0, 255, 0] [delay x ms] [0, 255, 0, 255, 0, 255, 0]


In general, use the 320Hz resonant mode for lighter, sharper actions and the 160Hz mode for heavier, blunter actions.

In the above "sharp tick" and "blunt tick" examples, you can try varying the pulse count anywhere from 1 to 50 to obtain different lengths of effect. You can also try varying the amplitude to obtain different vibrational intensities. In general, you can vary both the amplitude and the frequencies in a more random or chaotic way. You can also vary the vibrational effects based on input streams, such as controller movement or position, or any other conditions or events within the VR experience.

In addition to the types of effects described above, there are many other possibilities, including: 

* Hybrid Ticks and Modulation You can combine a repeating tick with an amplitude modulated segment.


* Mixing Multiple Input StreamsYou can pre-mix multiple input streams prior to passing to the haptics buffer API.




It is important to keep your sample pipeline at around the right size. Assuming a haptic frequency of 320 Hz and an application frame rate of 90 Hz, we recommend targeting a buffer size of around 10 samples per frame. This allows you to play 3-4 haptics bytes per frame, while preserving a buffer zone to account for any asynchronous interruptions. The more bytes you queue, the safer you are from interruptions, but you add additional latency before newly queued vibrations will be played. 

Take care to not overflow or underflow the 256 byte internal buffer within the controller. If you call `ovr_SubmitControllerVibration` with a larger buffer than the number of bytes that are currently available within the (circular) internal buffer, the entire submitted buffer is discarded. On the other hand, if you submit bytes at a rate that fails to keep up with the consumption of buffered bytes within the controller, there will be gaps in the vibrational playback.

## Using Buffered Haptics

To check the status of the buffer, call `ovr_GetControllerVibrationState`:

```
ovr_GetControllerVibrationState(ovrSession session, ovrControllerType controllerType, ovrHapticsPlaybackState* outState);
```

To submit to the buffer, call `ovr_SubmitControllerVibration`:

```
ovr_SubmitControllerVibration(ovrSession session, ovrControllerType controllerType, const ovrHapticsBuffer* buffer);
```

The following code sample shows how to produce some interesting and cool effects. This code extends the basic sample application contained in the Oculus PC-SDK distribution, in the following Visual Studio project &lt;install_folder&gt;\Samples\OculusRoomTiny_Advance\ORT (Buffered Haptics). You can copy/paste this code into the project, overwriting main.cpp, if desired.

```
/// A sample to show vibration generation, using buffered input.
/// Press A to generate a sine wave vibration in the right controller.
/// Press B to generate a 320 Hz vibration that pans from the right controller to the left controller.
/// Press X to generate a low-frequency buzz at 64 hz (320 Hz / 5) in the left controller.
/// Press Y to generate a "messed up" low frequency vibration in the left controller, based on a tangent function.
/// Hold any of the buttons down in order to repeat the pattern continuously.
/// Note: In order to keep the sample minimal, the Touch controller is not graphically displayed within the VR scene.

#include "../Common/Win32_DirectXAppUtil.h" // DirectX
#include "../Common/Win32_BasicVR.h"        // Basic VR

struct BufferedHaptics : BasicVR
{
       BufferedHaptics(HINSTANCE hinst) : BasicVR(hinst, L"BufferedHaptics") {}

       void MainLoop()
       {
             Layer[0] = new VRLayer(Session);

             // We create haptic buffers that will be associated with the A, B, X, and Y buttons. 
             int bufferSize = 256;
             unsigned char * dataBufferA = (unsigned char *)malloc(bufferSize);
             unsigned char * dataBufferBRight = (unsigned char *)malloc(bufferSize);
             unsigned char * dataBufferBLeft = (unsigned char *)malloc(bufferSize);
             unsigned char * dataBufferX = (unsigned char *)malloc(bufferSize);
             unsigned char * dataBufferY = (unsigned char *)malloc(bufferSize);

             // Verify that the buffer format is what we expect.
             ovrTouchHapticsDesc desc = ovr_GetTouchHapticsDesc(Session, ovrControllerType_LTouch);
             if (desc.SampleSizeInBytes != 1)        FATALERROR("Our assumption of 1 byte per element, is no longer valid");
             if (desc.SubmitMaxSamples &lt; bufferSize) FATALERROR("Can't handle this many samples");
             desc = ovr_GetTouchHapticsDesc(Session, ovrControllerType_RTouch);
             if (desc.SampleSizeInBytes != 1)        FATALERROR("Our assumption of 1 byte per element, is no longer valid");
             if (desc.SubmitMaxSamples &lt; bufferSize) FATALERROR("Can't handle this many samples");

             // Fill dataBufferA with a sine wave amplitude pattern that will smoothly 
             // rise and fall over a cycle period of 0.8 seconds. The 0.8 value is 
             // equal to 256/320, where 256 is the number of bytes that we will use 
             // to define a single sine wave cycle, and the bytes are "played" 
             // on the controller at 320 Hz. An interesting effect is added by lowering 
             // the effective frequency in latter half of the cycle by setting 
             // alternate intensities (amplitudes) to zero. The overall effect is a 
             // smoothly repeating vibrational pattern that "buzzes down" at the end of 
             // the wave cycle.
             for (int i = 0; i &lt; bufferSize; i++)
             {
                    dataBufferA[i] = (unsigned char)(255.0f*(sin(((3.14159265359f*i) / ((float)bufferSize)))));
                    if ((i &gt; bufferSize / 2) &amp;&amp; (i % 2)) dataBufferA[i] = 0;
             }

             // Fill dataBufferBRight with values that decrement from 255 down to 0. 
             // Similarly, fill dataBufferBLeft with values that increment from 0 up to 255. 
             // An interesting effect is added by lowering the effective frequency in 
             // latter half of dataBufferBLeft by setting intensities (amplitudes) to zero
             // for odd numbered bytes that are not divisible by 3. The overall effect 
             // is a right-to-left vibrational pan, with a distinct "buzzing down" feeling 
             // at the end of the panning cycle.
             for (int i = 0; i &lt; bufferSize; i++)
             {
                    dataBufferBRight[i] = (unsigned char)(255.0f*(255 - i / ((float)bufferSize)));
                    dataBufferBLeft[i] = (unsigned char)(255.0f*(i / ((float)bufferSize)));
                    if ((i &gt; bufferSize / 2) &amp;&amp; ((i % 2) || (i % 3))) dataBufferBLeft[i] = 0;
             }

             // Fill dataBufferX with zeros, and set every fifth byte to 255. This creates
             // maximum amplitude ticks at 64 Hz. (This is calculated by dividing
             // the number of ticks in the buffer, 256/5 = 51.2, and dividing that 
             // by the time period over which the buffer is played, 256/320 of a second, 
             // which is 0.8 seconds.)  
             for (int i = 0; i &lt; bufferSize; i++)
             {
                    dataBufferX[i] = (unsigned char)0;
                    if (i % 5 == 0) dataBufferX[i] = 255;
             }

             // Fill dataBufferY with a tangent wave function that varies the intensity 
             // amplitude) between 0 and 255, but set every other byte to 0. This produces a
             // "messed up" low frequency vibration. 
             for (int i = 0; i &lt; bufferSize; i++)
             {
                    dataBufferY[i] = (unsigned char)0;
                    if (i % 2 == 0) dataBufferY[i] = (unsigned char)(255.0f*(tan(((3.14159265359f*i) / ((float)bufferSize)))));
             }

             // Create the SDK structures that contain the buffers, and prepare 
             // them to be submitted to the controllers.
             ovrHapticsBuffer bufferX;
             bufferX.SubmitMode = ovrHapticsBufferSubmit_Enqueue;
             bufferX.SamplesCount = bufferSize;
             bufferX.Samples = (void *)dataBufferX;

             ovrHapticsBuffer bufferY;
             bufferY.SubmitMode = ovrHapticsBufferSubmit_Enqueue;
             bufferY.SamplesCount = bufferSize;
             bufferY.Samples = (void *)dataBufferY;

             ovrHapticsBuffer bufferA;
             bufferA.SubmitMode = ovrHapticsBufferSubmit_Enqueue;
             bufferA.SamplesCount = bufferSize;
             bufferA.Samples = (void *)dataBufferA;

             ovrHapticsBuffer bufferBRight;
             ovrHapticsBuffer bufferBLeft;
             bufferBRight.SubmitMode = ovrHapticsBufferSubmit_Enqueue;
             bufferBRight.SamplesCount = bufferSize;
             bufferBRight.Samples = (void *)dataBufferBRight;
             bufferBLeft.SubmitMode = ovrHapticsBufferSubmit_Enqueue;
             bufferBLeft.SamplesCount = bufferSize;
             bufferBLeft.Samples = (void *)dataBufferBLeft;

             // Main Loop
             while (HandleMessages())
             {
                    Layer[0]-&gt;GetEyePoses();

                    // Submit the haptic buffers to "play" upon pressing A, B, X or Y buttons.
                    ovrInputState inputState;
                    ovr_GetInputState(Session, ovrControllerType_Touch, &amp;inputState);
                    if (inputState.Buttons &amp; ovrTouch_A)
                    {
                           // Only submit the buffer if there is enough space available.
                           ovrHapticsPlaybackState playbackState;
                           ovrResult result = ovr_GetControllerVibrationState(Session, ovrControllerType_RTouch, &amp;playbackState);
                           if (playbackState.RemainingQueueSpace &gt;= bufferSize)
                           {
                                 ovr_SubmitControllerVibration(Session, ovrControllerType_RTouch, &amp;bufferA);
                           }
                    }
                    if (inputState.Buttons &amp; ovrTouch_B)
                    {
                           // Only submit the buffers if there is enough space available.
                           ovrHapticsPlaybackState playbackState;
                           ovrResult result = ovr_GetControllerVibrationState(Session, ovrControllerType_LTouch, &amp;playbackState);
                           if (playbackState.RemainingQueueSpace &gt;= bufferSize)
                           {
                                 ovr_SubmitControllerVibration(Session, ovrControllerType_LTouch, &amp;bufferBLeft);
                           }
                           result = ovr_GetControllerVibrationState(Session, ovrControllerType_RTouch, &amp;playbackState);
                           if (playbackState.RemainingQueueSpace &gt;= bufferSize)
                           {
                                 ovr_SubmitControllerVibration(Session, ovrControllerType_RTouch, &amp;bufferBRight);
                           }
                    }
                    if (inputState.Buttons &amp; ovrTouch_X)
                    {
                           // Only submit the buffer if there is enough space available.
                           ovrHapticsPlaybackState playbackState;
                           ovrResult result = ovr_GetControllerVibrationState(Session, ovrControllerType_LTouch, &amp;playbackState);
                           if (playbackState.RemainingQueueSpace &gt;= bufferSize)
                           {
                                 ovr_SubmitControllerVibration(Session, ovrControllerType_LTouch, &amp;bufferX);
                           }
                    }
                    if (inputState.Buttons &amp; ovrTouch_Y)
                    {
                           // Only submit the buffer if there is enough space available.
                           ovrHapticsPlaybackState playbackState;
                           ovrResult result = ovr_GetControllerVibrationState(Session, ovrControllerType_LTouch, &amp;playbackState);
                           if (playbackState.RemainingQueueSpace &gt;= bufferSize)
                           {
                                 ovr_SubmitControllerVibration(Session, ovrControllerType_LTouch, &amp;bufferY);
                           }
                    }

                    // Just render a standard scene in the HMD, to keep the code as simple as possible.
                    // The controllers are not rendered in the scene.
                    for (int eye = 0; eye &lt; 2; ++eye)
                    {
                           XMMATRIX viewProj = Layer[0]-&gt;RenderSceneToEyeBuffer(MainCam, RoomScene, eye);
                    }

                    Layer[0]-&gt;PrepareLayerHeader();
                    DistortAndPresent(1);
             }

             free(dataBufferX);
             free(dataBufferY);
             free(dataBufferA);
             free(dataBufferBLeft);
             free(dataBufferBRight);
       }
};
};
```
