---
title: VRC Validator
---

The Virtual Reality Check (VRC) Validator utility runs automated tests to determine if your Rift app is ready for Oculus Store technical review. The VRC Validator can reveal shortcomings that need to be addressed before your app can pass the Oculus Store review process. The VRC Validator has a command-line interface as well as a GUI interface. 

## Running All Default Tests

VRC Validator is included in the Oculus Runtime. You do not need to wear the Rift during the tests.

To run the VRC Validator:

1. Start a Windows Command Prompt window. 
2. Enter: cd "C:\Program Files\Oculus\Support\oculus-diagnostics\"
3. Run OculusVRCValidator.exe with the --path parameter set to the executable file of your Rift app. For example:OculusVRCValidator --path "C:\Program Files\Oculus\Software\Software\oculus-first-contact\TouchNUX.exe"




The tests results are written to the command prompt window. You can also log the test results to a .txt file. 

**Lost events:** The VRC Validator will retry the tests if any events were lost while the application was being evaluated.

## Logging Test Results to a File

Append the `-l` option to your OculusVRCValidator command line to write the test results to the text file. For example: `C:\Program Files\Oculus\Support\oculus-diagnostics\OculusVrcValidator_Log.txt`

If you want to write the test results to a different file, use `--log_file **fullpath**`. 

Example:

`OculusVRCValidator --path "C:\Program Files\Oculus\Software\Software\oculus-oculus-video\Cinema.exe" --log_file "C:\temp\log.txt"`

## Delaying the Start Time of Tests with the --load_time_ms Option

If you need to add a delay before each test begins to navigate to a specific part of your app you wish to test, append the `--load_time_ms **duration**` option to your OculusVRCValidator command line.

You can specify the wait duration in milliseconds. This example delays for 30 seconds:

`OculusVRCValidator --path "C:\Program Files\Oculus\Software\Software\oculus-first-contact\TouchNUX.exe" --load_time_ms 30000`

To make the tests wait until you press ENTER in the command prompt window, specify a duration of 0. The command prompt window must have focus. For example: 

`OculusVRCValidator --path "C:\Program Files\Oculus\Software\Software\oculus-first-contact\TouchNUX.exe" --load_time_ms 0`

## Running Selected Tests

To retrieve the complete list of tests, run `OculusVRCValidator --list_tests`.

Append the `--test testname` option to your OculusVRCValidator command line to specify that you want to run a particular test. If you want to run several selected tests, specify more than one `--test testname` option.

For example, to run the TestFrameRate and TestAppShouldQuit tests:

```
OculusVRCValidator --path "C:\Program Files\Oculus\Software\Software\oculus-first-contact\TouchNUX.exe" --test TestFrameRate --test TestAppShouldQuit
```

## Tests and Pass Criteria

The default tests of the OculusVRCValidator test your app against specific VRC criteria. If your app fails any of these default tests, it is likely to fail its official Oculus Store technical review.

There are also a number of optional tests. We do not run these tests during Oculus Store technical review, but ensuring that your app can pass them adds quality to your app.

**Default Tests (in order they will be tested)**

|                                                                         Test Name                                                                         |                                      Pass Criteria                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
|                         TestSdkVersion_  .. _TestSdkVersion: /documentation/pcsdk/latest/concepts/dg-vrcvalidator/#TestSdkVersion                         |    Your app must use the correct versions of Oculus PC SDK, Unity, or Unreal Engine.    |
|                TestEntitlementCheck_  .. _TestEntitlementCheck: /documentation/pcsdk/latest/concepts/dg-vrcvalidator/#TestEntitlementCheck                | Your app must perform an Oculus Platform entitlement check within 10 seconds of launch. |
|              TestOculusDLLIncludes_  .. _TestOculusDLLIncludes: /documentation/pcsdk/latest/concepts/dg-vrcvalidator/#TestOculusDLLIncludes              |               Your app must not distribute its own copies of Oculus DLLs.               |
|                      TestLaunchIntoVR_  .. _TestLaunchIntoVR: /documentation/pcsdk/latest/concepts/dg-vrcvalidator/#TestLaunchIntoVR                      |    Your app must launch into VR within 4 seconds and display a non-headlocked layer.    |
|                          TestFrameRate_  .. _TestFrameRate: /documentation/pcsdk/latest/concepts/dg-vrcvalidator/#TestFrameRate                          |                      Your app must maintain 90 frames per second.                      |
|     TestSubmitFramesWhenVisible_  .. _TestSubmitFramesWhenVisible: /documentation/pcsdk/latest/concepts/dg-vrcvalidator/#TestSubmitFramesWhenVisible     |                        Your app must submit frames when visible.                        |
| TestSubmitFramesWhenNotVisible_  .. _TestSubmitFramesWhenNotVisible: /documentation/pcsdk/latest/concepts/dg-vrcvalidator/#TestSubmitFramesWhenNotVisible |          Your app must stop submitting frames when the Universal Menu is open.          |
|  TestResponseToRecenterRequest_  .. _TestResponseToRecenterRequest: /documentation/pcsdk/latest/concepts/dg-vrcvalidator/#TestResponseToRecenterRequest  |                  Your app must respond to requests to reset the view.                  |
|                    TestAppShouldQuit_  .. _TestAppShouldQuit: /documentation/pcsdk/latest/concepts/dg-vrcvalidator/#TestAppShouldQuit                    |                             Your app must quit gracefully.                             |
|           CheckForExtraneousFiles_  .. _CheckForExtraneousFiles: /documentation/pcsdk/latest/concepts/dg-vrcvalidator/#CheckforExtraneousFiles           |                  Your app must not contain DLLs from other platforms.                  |
|                       TestAudioOutput_  .. _TestAudioOutput: /documentation/pcsdk/latest/concepts/dg-vrcvalidator/#TestAudioOutput                       |           Your app must target the audio device specified in the Oculus app.           |

**Optional Tests (in order they will be tested)**

|                                                                 Test Name                                                                 |                                            Pass Criteria                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
|     TestMismatchedAdapters_  .. _TestMismatchedAdapters: /documentation/pcsdk/latest/concepts/dg-vrcvalidator/#TestMismatchedAdapters     |   Your app must run correctly when the HMD is connected to a different GPU than the main display.   |
| TestResponseToDisplayLost_  .. _TestResponseToDisplayLost: /documentation/pcsdk/latest/concepts/dg-vrcvalidator/#TestResponseToDisplayLost | Your app must either quit properly or stop submitting frames when the HMD is unplugged from the GPU. |
|           TestPropertyAccess_  .. _TestPropertyAccess: /documentation/pcsdk/latest/concepts/dg-vrcvalidator/#TestPropertyAccess           |                           Your app must not use any deprecated properties.                           |
|                RunErrorCapture_  .. _RunErrorCapture: /documentation/pcsdk/latest/concepts/dg-vrcvalidator/#RunErrorCapture                |                              Your app must not generate runtime errors.                              |
|  TestResponseToIadChanges_  .. _TestResponseToIadChanges: /documentation/pcsdk/latest/concepts/dg-vrcvalidator/#TestResponseToIadChanges  |                         Your app must respond to changes in the lens slider.                         |

## Individual Test Details

The following are details of the tests as they will be run by the validator.

**TestSdkVersion**

Tests if your app is built with the supported versions of Oculus PC SDK, Unity, or Unreal Engine.

**TestEntitlementCheck**

Tests if your app performs an Oculus Platform entitlement check within 10 seconds of launch.

**TestOculusDLLIncludes**

Tests if your app is distributing copies of the following Oculus DLLs instead of loading the DLLs from the Oculus runtime directory:

* LibOVRRT32\_1.dll
* LibOVRRT64\_1.dll 
* LibOVRPlatform32\_1.dll
* LibOVRPlatform64\_1.dll
* LibOVRP2P32\_1.dll
* LibOVRP2P64\_1.dll
* LibOVRAvatar32\_1.dll 
* LibOVRAvatar64\_1.dll


**TestLaunchIntoVR**

Tests if your app displays a non-headlocked graphic in VR and responds to head tracking within 4 seconds of launch. If you want to test a different duration, append the `--max_time_to_frame **duration**` option to your command line. Specify the duration in milliseconds.

**TestFrameRate**

Tests if your app displays graphics in the headset at 90 frames per second.

**TestSubmitFramesWhenVisible**

Tests if your app renders when it is visible. The test counts the number of texture swap chains committed and reports it at the end of the test.

**TestSubmitFramesWhenNotVisible**

Tests if your app stops submitting frames when the Universal Menu is open. 

**TestResponseToRecenterRequest**

Tests if your app resets the user's position and orientation when a user selects Reset View in the Universal Menu. 

**TestAppShouldQuit**

Tests if your app quits properly from the Universal Menu with ovr_Destroy when it receives a quit request.

**CheckforExtraneousFiles**

Tests if your app folder contains extraneous .pdb symbol files.

**TestAudioOutput**

Tests if your app targets the audio device selected in the “Audio Output in VR” setting in the Oculus app. 

**TestMismatchedAdapters**

Tests if the application supports plugging the HMD and the primary display into different display adapters. To run this test, the system must have at least two separate display adapters, with the HMD and primary display connected to different display adapters.

**TestResponseToDisplayLost**

Tests if the application responds gracefully if the HMD cable is unplugged from the display adapter. Once the HMD display is lost, the application should either quit with ovr_Destroy, or pause and stop submitting frames to the HMD. Example:

`OculusVRCValidator --path "C:\Program Files\Oculus\Software\Software\oculus-first-contact\TouchNUX.exe" --test TestResponseToDisplayLost`

 During this test, you will be asked to unplug the HMD from the display adapter, allow the test to run, and then plug the HMD back in.

**TestPropertyAccess**

Tests if your app calls any internal, deprecated, or otherwise unsupported API functions that are carryovers from DK2 development. Deprecated property functions include:

* User
* Name 
* Gender 
* PlayerHeight 
* EyeHeight 
* NeckEyeDistance 
* EyeNoseDist


**RunErrorCapture**

Tests if your app generates runtime errors. Some common errors include:

* ovrError\_InvalidParameter - invalid parameter provided. More information is output about the function which is called with invalid parameter.
* ovrError\_MismatchedAdapters - occurs when the HMD is not plugged in the primary display adapter and the application is not handling this.
* ovrError\_LeakingResources - calling application has leaked resources
* ovrError\_TextureSwapChainFull - ovr\_CommitTextureSwapChain was called too many times on a texture swapchain without calling submit to use the chain


**TestResponseToIadChanges**

Tests if your app correctly adjusts for Inter Axial Distance (IAD) changes by getting updated HmdToEyeOffset values from ovr_GetRenderDesc at least once every 500ms. It also tests that your app actually responds to IAD changes. 

## GUI Interface to VRC Validator

The Oculus Debug Tool provides a VRC Validator dialog. To use this GUI interface, follow these steps:

1. Make sure the Oculus application is running, and the headset is connected.
2. Start the Oculus Debug Tool as described in [Oculus Debug Tool](/documentation/pcsdk/latest/concepts/dg-debug-tool/ "The Oculus Debug Tool (IDT) enables you to view performance or debugging information within your game or experience. It also enables you to tune or configure related parameters, such as the field of view (FOV) size for a mirrored flat-screen view of the VR experience (which could be streamed to an audience in a more comfortable viewing format)."). Then, select File &gt; Validate App...: ![](/images/documentationpcsdklatestconceptsdg-vrcvalidator-0.png)


3. The Validate App dialog appears (as shown below). For Executable Path, browse to an executable VR application that you wish to test. For Arguments, enter any arguments that you wish to specify for the VR application. Then, select the VRC tests that you wish to run. In this example, three VRC tests are selected: ![](/images/documentationpcsdklatestconceptsdg-vrcvalidator-1.png)


4. Click OK to run the tests. The Validating App dialog appears (as shown below). In the left panel, a check mark indicates a successful test, an x indicates a failed test, and an animated clock icon indicates a test that is currently underway. The detailed results are shown in the right panel:![](/images/documentationpcsdklatestconceptsdg-vrcvalidator-2.png)



