---
title: Button State
---

The input button state is reported based on the HID interrupts arriving to the computer and can be polled by calling ovr_GetInputState.

The following example shows how input can be used in addition to hand poses:

```
double displayMidpointSeconds = ovr_GetPredictedDisplayTime(session, frameIndex);
ovrTrackingState trackState = ovr_GetTrackingState(session, displayMidpointSeconds, ovrTrue);
ovrPosef         handPoses[2];
ovrInputState    inputState;

// Grab hand poses useful for rendering hand or controller representation
handPoses[ovrHand_Left]  = trackState.HandPoses[ovrHand_Left].ThePose;
handPoses[ovrHand_Right] = trackState.HandPoses[ovrHand_Right].ThePose;

if (OVR_SUCCESS(ovr_GetInputState(session, ovrControllerType_Touch, &amp;inputState)))
{
    if (inputState.Buttons &amp; ovrButton_A)
    {
        // Handle A button being pressed
    }
    if (inputState.HandTrigger[ovrHand_Left] &gt; 0.5f)
    {
        // Handle hand grip...
    }
}

  
```

The ovrInputState struct includes the following fields: 

|           Field           |     Type     |                                                                                                                                                                                                                Description                                                                                                                                                                                                                |
|---------------------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       TimeInSeconds       |    double    |                                                                                                                                                                                          System time when the controller state was last updated.                                                                                                                                                                                          |
|      ControllerType      | unsigned int | Described by ovrControllerType. Indicates which controller types are present; you can check the ovrControllerType_LTouch bit, for example, to verify that the left touch controller is connected. Options include:* ovrControllerType\_None (0x0000) * ovrControllerType\_LTouch (0x0001) * ovrControllerType\_RTouch (0x0002) * ovrControllerType\_Touch (0x0003) * ovrControllerType\_Remote (0x0004) * ovrControllerType\_XBox (0x0010) |
|          Buttons          | unsigned int |                                                                                                                                                                         Button state described by ovrButtons. A corresponding bit is set if the button is pressed.                                                                                                                                                                         |
|          Touches          | unsigned int |                                                                                                                           Touch values for buttons and sensors as indexed by ovrTouch. A corresponding bit is set if users finger is touching the button or is in a gesture state detectable by the controller.                                                                                                                           |
|      IndexTrigger[2]      |    float    |                                                                                                                                          Left and right finger trigger values (ovrHand_Left and ovrHand_Right), in the range 0.0 to 1.0f. A value of 1.0 means that the trigger is fully pressed.                                                                                                                                          |
|      HandTrigger[2]      |    float    |                                                                                                                      Left and right grip button values (ovrHand_Left and ovrHand_Right), in the range 0.0 to 1.0f. Hand trigger is often used to grab items. A value of 1.0 means that the trigger is fully pressed.                                                                                                                      |
|       Thumbstick[2]       | ovrVector2f |                                                                                                                 Horizontal and vertical thumbstick axis values (ovrHand_Left and ovrHand_Right), in the range -1.0f to 1.0f. The API automatically applies the dead zone, so developers dont need to handle it explicitly.                                                                                                                 |
| IndexTriggerNoDeadzone[2] |    float    |                                                                                                                                Left and right finger trigger values (ovrHand_Left and ovrHand_Right), in the range 0.0 to 1.0f, without a deadzone. A value of 1.0 means that the trigger is fully pressed.                                                                                                                                |
| HandTriggerNoDeadzone[2] |    float    |                                                                                         Left and right grip button values (ovrHand_Left and ovrHand_Right), in the range 0.0 to 1.0f, without a deadzone. The grip button, formerly known as the hand trigger, is often used to grab items. A value of 1.0 means that the button is fully pressed.                                                                                         |
|  ThumbstickNoDeadzone[2]  | ovrVector2f |                                                                                                                                                      Horizontal and vertical thumbstick axis values (ovrHand_Left and ovrHand_Right), in the range -1.0f to 1.0f, without a deadzone.                                                                                                                                                      |
|    IndexTriggerRaw[2]    |    float    |                                                                                                                          Raw left and right grip button values (ovrHand_Left and ovrHand_Right), in the range 0.0 to 1.0f, without a deadzone or filter. A value of 1.0 means that the trigger is fully pressed.                                                                                                                          |
|     HandTriggerRaw[2]     |    float    |                                                                                    Left and right grip button values (ovrHand_Left and ovrHand_Right), in the range 0.0 to 1.0f, without a deadzone or filter. The grip button, formerly known as the hand trigger, is often used to grab items. A value of 1.0 means that the button is fully pressed.                                                                                    |
|     ThumbstickRaw[2]     | ovrVector2f |                                                                                                                                                 Horizontal and vertical thumbstick axis values (ovrHand_Left and ovrHand_Right), in the range -1.0f to 1.0f, without a deadzone or filter.                                                                                                                                                 |

The ovrInputState structure includes the current state of buttons, thumb sticks, triggers and touch sensors on the controller. You can check whether a button is pressed by checking against one of the button constants, as was done for ovrButton_A in the above example. The following is a list of binary buttons available on touch controllers: 

| **Button Constant** |                                              **Description**                                              |
|---------------------|-----------------------------------------------------------------------------------------------------------|
|     ovrButton_A     |                                  A button on the right Touch controller.                                  |
|     ovrButton_B     |                                  B button on the right Touch controller.                                  |
|  ovrButton_RThumb  |                             Thumb stick button on the right Touch controller.                             |
|     ovrButton_X     |                                  X button on the left Touch controller.                                  |
|     ovrButton_Y     |                                  Y button on the left Touch controller.                                  |
|  ovrButton_LThumb  |                             Thumb stick button on the left Touch controller.                             |
|   ovrButton_Enter   | Enter button on the left Touch controller. This is equivalent to the Start button on the Xbox controller. |
