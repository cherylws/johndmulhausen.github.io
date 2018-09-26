---
title: VRC.Mobile.Input.3
---

When the user presses the back button, the app must either go back one level in your UI or display a menu with an option to quit the app.

**Required** - Yes

## Additional Details

The purpose of this requirement is to ensure that there is always an escape route from an application, even on older Gear headsets that do not have a Home button. As long as the back button presents the standard Oculus quit dialog, exiting instead of going back a UI level is fine.

## Steps to Test

1. Launch the title.
2. If applicable, select a menu item to begin the experience.
3. Press the back button.
4. Observe the display.
5. Press the back button again.


## Expected Result

The first time the back button is pressed, the UI either goes back to the previous level or displays a menu with an option to exit the current scene (like go back to your main menu). If no menu is displayed, pressing the back button multiple times should eventually show the Oculus quit menu.
