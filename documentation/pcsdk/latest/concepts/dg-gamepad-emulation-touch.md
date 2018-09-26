---
title: Emulating Gamepad Input with Touch
---

Touch controllers can partially emulate Microsoft XInput API gamepad input without any code changes. However, you must account for the missing logical and ergonomic equivalences between the two types of controllers.

## How it Works

The Oculus runtime has a gamepad emulation mode to map Touch controller input to Microsoft XInput API input. This lets you allow users to use their Touch controllers in games designed for gamepad controllers without having to modify your code.

* VR must have focus.
* The app must have the Gamepad Emulation Via Touch option enabled.
* The Touch controllers must be detected.
* A gamepad must not be detected. You cannot use Touch to emulate a second gamepad.


Touch controllers revert back to being Touch controllers when the app closes or when the user presses the Oculus button and exits to Home.

## Activating and Deactivating Gamepad Emulation

Gamepad emulation is an Oculus Store attribute attached to the build binary. It can only be enabled or disabled by uploading a new build.

1. Upload a new Rift build from the Oculus Developer Dashboard.
2. On the build upload information page, select the appropriate **Gamepad Emulation Via Touch** option: * Off * Twin Stick * Left D-pad * Right D-pad 




## Gamepad Emulator Compatibility Guidelines

If your gamepad control mechanism is affected by any of the following limitations, your game is probably a poor candidate for using gamepad emulation. Instead of emulation, consider creating a new control scheme for Touch controllers to provide a better experience for your users.

**Haptics**

The current implementation does not include haptics. If vibration and haptics are critical to your experience, such as in a rhythm game, your app might not work well with emulation.

**D-pad**

The Touch controller does not have a D-pad. If your control scheme uses the D-pad and both sticks, your app might not work well with emulation.

If your control scheme only needs one stick, you can use our emulation modes to map the D-pad to either the right or left Touch.

**View button**

Twin stick emulation does not have a view button (⧉). If this button is critical to your control scheme, your app might not work well with twin-stick emulation mode.

The D-pad emulation modes do feature a mapping for this button.

**Left Touch thumbstick can’t be used with the X or Y buttons**

Any action that combines left Touch thumbstick movement with X or Y button presses will be difficult or impossible for users because these actions are controlled by the same thumb. If your control scheme requires such an action, your app might not work well with emulation.

## Testing Gamepad Emulation

You can force a gamepad emulation mode in the Oculus Runtime for testing purposes.

To force gamepad emulation:

1. Add or modify the following DWORD value in the Windows registry:

[HKEY\_CURRENT\_USER\SOFTWARE\Oculus]

"GamepadEmulationMode"=dword:*mode\_enum*

where *mode\_enum* is one of the following: * 00000002 - Twin stick mode. * 00000003 - Right D-pad mode. * 00000004 - Left D-pad mode. 


2. Restart the Oculus runtime service. The service name is "OVRService" and the display name is "Oculus VR Runtime Service".




To revert to normal behavior, delete the `GamepadEmulationMode` value from the Windows registry and then restart OVRService.

## Twin Stick Gamepad Emulation Mode

Maps the two gamepad sticks to the Touch thumbsticks. The D-pad and view button (⧉) are not mapped.



![](/images/documentationpcsdklatestconceptsdg-gamepad-emulation-touch-0.png)



| Gamepad Input | Touch Equivalent |
|----------------|------------------|
|   vibration   |       NONE       |
|     D-pad     |       NONE       |
|   left stick   | left thumbstick |
|  left bumper  |    left grip    |
|  left trigger  |   left trigger   |
| view button () |       NONE       |
|  Xbox button  |  Oculus button  |
| menu button () |  menu button ()  |
|  right stick  | right thumbstick |
|  right bumper  |    right grip    |
| right trigger |  right trigger  |
|    A button    |     A button     |
|    B button    |     B button     |
|    X button    |     X button     |
|    Y button    |     Y button     |

## Left D-Pad Gamepad Emulation Mode

Same as twin stick gamepad emulation mode except for the following:



![](/images/documentationpcsdklatestconceptsdg-gamepad-emulation-touch-1.png)



| Gamepad Input |   Touch Equivalent   |
|----------------|-----------------------|
|     D-pad     |    left thumbstick    |
|   left stick   |         NONE         |
| view button () | left thumbstick press |

## Right D-Pad Gamepad Emulation Mode

Same as twin stick gamepad emulation mode except for the following:



![](/images/documentationpcsdklatestconceptsdg-gamepad-emulation-touch-2.png)



| Gamepad Input |    Touch Equivalent    |
|----------------|------------------------|
|     D-pad     |    right thumbstick    |
|  right stick  |          NONE          |
| view button () | right thumbstick press |
