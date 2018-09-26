---
title: Button Touch State
---

In addition to buttons, Touch controllers can detect whether user fingers are touching some buttons or are in certain positions.

These states are reported as bits in the Touches field, and can be checked through one of the following constants:

|       ovrTouch_A       |                                   User in touching A button on the right controller.                                   |
|-------------------------|------------------------------------------------------------------------------------------------------------------------|
|       ovrTouch_B       |                                   User in touching B button on the right controller.                                   |
|     ovrTouch_RThumb     |                             User has a finger on the thumb stick of the right controller.                             |
|   ovrTouch_RThumbRest   |                         User has a finger on the textured thumb rest of the right controller.                         |
| ovrTouch_RIndexTrigger |                           User in touching the index finger trigger on the right controller.                           |
|       ovrTouch_X       |                                   User in touching X button on the left controller.                                   |
|       ovrTouch_Y       |                                   User in touching Y button on the left controller.                                   |
|     ovrTouch_LThumb     |                              User has a finger on the thumb stick of the left controller.                              |
|   ovrTouch_LThumbRest   |                          User has a finger on the textured thumb rest of the left controller.                          |
| ovrTouch_LIndexTrigger |                           User in touching the index finger trigger on the left controller.                           |
| ovrTouch_RIndexPointing |                             Users right index finger is pointing forward past the trigger.                             |
|    ovrTouch_RThumbUp    | Users right thumb is up and away from buttons on the controller, a gesture that can be interpreted as right thumbs up. |
| ovrTouch_LIndexPointing |                             Users left index finger is pointing forward past the trigger.                             |
|    ovrTouch_LThumbUp    |  Users left thumb is up and away from buttons on the controller, a gesture that can be interpreted as left thumbs up.  |
