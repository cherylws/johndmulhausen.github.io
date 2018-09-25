---
title: VRC.PC.Input.6
---
The app must not claim Oculus Touch as a supported input device unless Touch position and orientation data facilitate player movement or manipulate the environment.

**Required** - Yes

## Additional Details

Apps that merely emulate gamepad control schemes using Touch must not indicate Oculus Touch as a supported input device and shall indicate "Touch (as Gamepad)" instead.

## Steps to Test

1. Launch the title.
2. Play through several levels of the game.
## Expected Result

The app must use Touch controllers to be able to grab things or interact with the environment.

