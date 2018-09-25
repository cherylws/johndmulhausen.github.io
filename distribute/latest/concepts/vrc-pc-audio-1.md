---
title: VRC.PC.Audio.1
---
App must target the audio device selected in the "Audio Output in VR" setting in the Oculus app.

**Required** - Yes

## Additional Details

No additional details for this VRC.

## Steps to Test

1. Run the VRC Validator with the TestAudioOutput argument.
Optional Manual Tests

1. Plug in a set of headphones.
2. In the Windows Sound settings, set the headphones to be the default audio device.
3. In the Oculus Home app, open the Devices settings and select Rift, then ensure the "Audio Output in VR" setting is set to "Rift headphones."
4. Launch the app and listen for audio to play.
## Expected Result

The VRC Validator will report "INFO: Test PASSED".

If testing manually, your application's audio should come from the Rift headset, not from the headphones plugged into the PC.

