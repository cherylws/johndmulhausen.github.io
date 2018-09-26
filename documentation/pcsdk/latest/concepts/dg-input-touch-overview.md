---
title: Oculus Touch Controllers
---

This section describes Oculus Touch best practices gathered from developing and reviewing large numbers of games and experiences. These are not requirements and we expect them to evolve over time. 

**Note: **To view application requirements, go to [https://developer.oculus.com/distribute/latest/concepts/publish-rift-app-submission/](/distribute/latest/concepts/publish-rift-app-submission/)

## Input, Hands, and Controller Basics

When developing applications that use Oculus Touch, consider the following:

* If your application supports multiple input methods (such as Oculus Touch, Xbox 360 Controller, and Oculus Remote), use ovrControllerType\_Active to determine which one is in use. You can also use this to determine if one or both Touch controllers are in use. Some applications render the Touch controllers differently (e.g. as hands vs. controllers) depending on their in-use state. For more information, see this section and the API reference [Developer Reference/](https://developer.oculus.com/documentation/pcsdk/latest/concepts/api-reference/). 
* Unless you have an uncommon use case, use the Avatar SDK to represent high quality hands and/or controllers in your app.
* Map the grip button to grab actions. Although there are some exceptions to the rule (especially involving throwing), the new user experience and most applications condition users to use it this way. If you break expectations, make sure to educate your users.
* Prefer hands over controller models, especially for any application that involves social interaction or picking things up.
* In-application hands and controllers should line up with the user’s real-world counterparts in position and orientation as closely as possible. We call this “registration” and recommend the Avatar SDK as an example. When testing your application, one technique is to hold your hands in front of your face and raise your headset slightly so you can compare your real-world hands and your virtual hands.
* Fully animate all hands and controllers in the game, to reflect what the user is doing. Users will expect to be able to grab, point, and thumbs-up with their hands. They will expect controller joysticks, buttons, and triggers to animate on use. We have demos with full code and blueprints for doing this in UE4 and Unity.
* To support left- and right-handed players, we recommend designing objects for use with either hand. For example, if the player is going to use a double rotating-wheel can opener to open a can in VR, make sure the cutting wheel handle faces the other hand.
* When controllers are mirrored, make controls identical. When controllers have different functions, make sure to establish a dominant and non-dominant hand (instead of favoring the right hand). For example, in the Toy Box demo, players usually use their non-dominant to hold the slingshot and their dominant hand to pull the ammunition holder.
* Unless important to the experience, do not render additional body parts besides the hands in single player games. Although inverse kinematics (i.e., extrapolating body part positions based on how the body can and cannot move) are a tempting solution to represent more the player’s body, they become less accurate as you try to simulate more of the body. The mismatch can end up being distracting and ironically less immersive.

For multiplayer games, you can render the hands of the first person and the up to the full bodies of the other players.




## Tracking

The following are basic tracking tips:

* For front-facing apps, keep the action in front of the user. Don’t encourage users to do things that will break the line of sight between the controllers and sensors, which will lead to poor tracking.
* Don’t require the user to interact with VR elements near the floor or far above their heads. Remove those objects, or allow a distance grab. If you decide to allow interactions at a distance, make sure to indicate that the object is available through a highlight, glow, shake, haptics, or another mechanism.
* Avoid interactions that encourage users to get too close or too far from one or more position trackers.


## Large Play Areas

For applications that use a large amount of the tracking space, either horizontally or vertically, you’ll want to put a little more effort into making the best use of the available space:

* Our user-facing description of “Standing” apps is “may require a step in any direction.” Even if your application uses a lot of space, if it is going to be submitted as a standing app, it needs to meet that description. Additionally, Standing apps must be fully usable in a 2m x 1.5 tracking area.
* If your application requires lots of space, use the user’s Guardian boundaries to make sure you place game objects within reachable areas. For more information, see [Oculus Guardian System](/documentation/pcsdk/latest/concepts/dg-guardian-system/ "The Oculus Guardian System is designed to display in-application wall and floor markers when users get near boundaries they defined. When the user gets too close to the edge of a boundary, translucent boundary markers are displayed in a layer that is superimposed over the game or experience.").
* Applications can modify recenter behavior in a way that makes sense for the app. For example, an app might clamp the recenter origin inside of the play area by some amount of padding, so that all gameplay elements are reachable. Or it might choose to ignore the yaw component, to maintain an axis-aligned play area. If an app substantially violates user expectations for recenter, it should inform the user about what’s happening. For more information, see [VR Focus Management](/documentation/pcsdk/latest/concepts/dg-vr-focus/ "When you submit your application to Oculus, you provide the application and metadata necessary to list it in the Oculus Store and launch it from Oculus Home.").
* Applications can also use the above recenter functionality to set an optimal center position (overriding the user’s home position) on launch. You can use the default recenter behavior on subsequent user-initiated recenters, or continue to use modified recenter logic. 
* If the user’s play space is undefined, create your own play space around the user’s recenter/home point. This assumed play space should not exceed 2m x 1.5m (the recommended play space size). If your application can use a smaller space, default to that.
*  If your app requires high or low tracking, keep the shape of the sensor frustums in mind. For example, a front-facing app that involves shooting basketballs will want to keep the user towards the rear of the play area, where the tracking frustums are taller. For more information on sensor field of view and tracking ranges, see: [Initialization and Sensor Enumeration](/documentation/pcsdk/latest/concepts/dg-sensor/#dg_sensor "This example initializes LibOVR and requests information about the available HMD."). 
* Some users might not have the full 2m x 1.5m recommended play space, but will play your game despite warnings. If your application requires this full amount of space, choose the best fallback. Possible solutions include:


	+ It is generally better to overflow away from the sensors, not towards, since tracking is better further back (and closer might put you past the sensor position).
	+ Users can attempt to use recenter to reach playable areas they would otherwise be unable to reach.
	


* **[Controller Data](/documentation/pcsdk/latest/concepts/dg-input-touch/)**  
The Oculus SDK provides APIs that return the position and state for each Oculus Touch controller. 
* **[Hand Tracking](/documentation/pcsdk/latest/concepts/dg-input-touch-poses/)**  
The constellation sensor used to track the head position of the Oculus Rift also tracks the hand poses of the Oculus Touch controllers.
* **[Button State](/documentation/pcsdk/latest/concepts/dg-input-touch-buttons/)**  
The input button state is reported based on the HID interrupts arriving to the computer and can be polled by calling ovr\_GetInputState.
* **[Button Touch State](/documentation/pcsdk/latest/concepts/dg-input-touch-touch/)**  
In addition to buttons, Touch controllers can detect whether user fingers are touching some buttons or are in certain positions.
* **[Haptic Feedback](/documentation/pcsdk/latest/concepts/dg-input-touch-haptic/)**  
In addition to reporting input state, Oculus touch controllers can provide haptic feedback through vibration.
* **[Emulating Gamepad Input with Touch](/documentation/pcsdk/latest/concepts/dg-gamepad-emulation-touch/)**  
Touch controllers can partially emulate Microsoft XInput API gamepad input without any code changes. However, you must account for the missing logical and ergonomic equivalences between the two types of controllers.

