---
title: Locomotion
---

This section offers tips about how to move the user through the virtual world.

Implementing locomotion in VR is one of the most difficult things to do, and one of the most important to get right. Poorly designed or improperly implemented locomotion can easily make even seasoned VR users uncomfortable or sick.

For this guide locomotion refers to any acceleration, rotation, or movement not initiated by real-world movement of a user.

Locomotion in VR is usually a user’s avatar moving through the virtual environment (by walking/running or riding a vehicle) while the user’s real-world body is stationary. These situations can be uncomfortable because the user’s vision tells them they are moving through space, but their body perceives the opposite (vestibular sense and proprioception). This illusory perception of self-motion from vision alone has been termed vection, and is a major underlying cause of visually induced VR discomfort.

It is especially important when designing locomotion that you test your experience with a wide audience of users. Your app’s developers may have learned to tolerate the locomotion mechanism that you implement and are not a good representation of the average user.

## General Guidelines

In general, there are some things about locomotion and user comfort that you should know when designing your VR experience.

Consider the type of app you’re designing and audience you’re designing for. Apps that wish to target a broad, novice audience may wish to avoid acceleration completely. Some apps have successfully incorporated more intense locomotion schemes, but these experiences may limit the number of potential users. If you choose to implement a more intense locomotion method, we recommend also implementing a comfort mode that is less intense for other users.

**Acceleration** in VR not initiated by a user’s real-world movement is the primary cause of discomfort in VR experiences. Acceleration is any change in velocity in any direction. Acceleration can refer to decreasing the speed of movement, rotating or turning, and moving (or ceasing to move) sideways or vertically. Acceleration conveyed visually but not to the vestibular organs constitutes a sensory conflict that can cause discomfort.

Discomfort may increase as the frequency, size, and duration of the acceleration increases. Any period of visually-presented acceleration represents a conflict between senses, and it is best to avoid them as much as possible.

**Speed** and discomfort in VR do not demonstrate a straightforward relationship to one another. Slow speeds (i.e. slow-motion) have been reported as less discomforting than a normal pace of human locomotion. Unnaturally rapid velocity has also been shown to be less discomforting than a normal human pace. As a reference, human locomotion generally falls between 1.4 m/s (walking) and 3 m/s (light jog).

Allowing **user control** over the motion they experience can minimize discomfort. Allowing users to initiate the movement they experience appears to reduce discomfort, especially when the real-world movement and VR movement map 1:1. Allow users to move themselves around the virtual world instead of taking them for a ride.

**Direction of locomotion** impacts the comfort of users in VR. In the real world, we most often stand still or move forward. We rarely back up, and we almost never strafe (move side to side). Therefore, when movement is necessary, forward user movement is most comfortable. Left or right lateral movement is more problematic because we don’t normally walk sideways and it presents an unusual optic flow pattern to the user.

**Pixel flow** or noise should be minimized when a user is moving in VR, especially in the user’s periphery. Avoid moving users through enclosed spaces, like hallways. Open environments are typically more comfortable for users. 

## VR Locomotion Techniques

We’re still in the early days of exploring VR locomotion. So far, we haven’t found the “magic bullet” for locomotion that works with uniform efficacy across all users. These methods may have some trade-off in the user’s experience, and that experience will vary from person to person. It may be beneficial to offer users flexibility and a range of options in mitigating discomfort than to impose any one solution on them.

The general theme among these methods are that they all are intended to avoid the conflict for the user, by convincing the brain that the user is not in fact moving, that essentially their senses are correct. This means that sufficient visual cues need to be present to reinforce the senses perception of the actual motion.

Most users will acclimate to your VR experience over time making them less susceptible to discomfort. You may choose to offer more comfortable experiences early, then introduce more intense experiences later in the app.

There may be some users who are discomforted by the methods you choose for locomotion. Consider including a comfort mode to reach as broad of an audience as possible.

**No locomotion by design.** A bit counterintuitive for this section, but the most effective means of avoiding discomfort from locomotion is designing an experience that does not need locomotion. Although moving the player around the VR environment without input or explanation can feel artificial, good narrative design can provide a mental model that maintains immersion.

One approach is to have players progress through discrete levels or areas, providing some mechanism for the transportation that doesn’t expose them to vection. For example, the player might ride an elevator or other encapsulated mode of transportation, or have their view of the world fade to black for story reasons (e.g. losing consciousness, being blindfolded).

**Teleportation** allows users to move around a scene without having to deal with vection-inducing acceleration. Users can indicate where they want to move in the scene through an input method. They are then teleported to a location they indicate; eliminating any issues associated with acceleration in VR.

It is important to note that applying large changes to the user’s location in the virtual environment can be disorienting. Players should have ample means of predicting where they will be and where they will face upon teleporting to their destination, as well as clear landmarks to aid orientation if possible. Our [Teleport Curves with the Gear VR Controller](/blog/teleport-curves-with-the-gear-vr-controller/) tech note reviews teleporting in a bit more detail. 

**Artificial movement** allows you to move users through the scene at a constant velocity and along a straight line. For example, a user “walking” between predefined fixed points or in a railroad car that moves within a scene, but at a fixed pace and direction that eliminates vection inducing acceleration. Allow users to initiate and terminate the movement through some form of input.

**Blinks and snap turns** omit visual information that’s likely to cause vection by simply cutting to black or instantaneously changing the viewpoint. The brain is well suited to filling in interruptions in our perceptual streams (e.g. you don’t notice the visual interruptions that occur when you blink or when your eyes jump from one location to another), and we can leverage that ability to transition the user’s viewpoint through motions that are likely to cause vection.

These mechanisms work by disrupting the perception of motion, which occurs when incremental updates to the visual scene occur too infrequently for the brain to stitch them together into a coherent movement. Therefore, the efficacy of these methods can be compromised if the user is able to rapidly change their viewpoint (e.g., snap rotating or blinking from one location to another) at a rate of 8 times per second or faster. At that point, the changes become perceived as motion and once again induce vection.

**HMD Acceleration** allows users to initiate and control the movement of their virtual user by tilting in the direction that they want to move. In addition to forward and backward movement, this mechanism works well when a user needs to strafe (move laterally) side-to-side. However, when moving the virtual user using this mechanism, it is important that tilting the head does not rotate the user. This can lead to an uncomfortable coriolis effect for users.

**Tunnel vision** allows the vignetting of the eye buffers so that the field of view is narrowed and peripheral vision blocked off. Some apps fade out the peripheral view only when moving, others get it for free by virtue of the way the scene is framed (for instance, a diving helmet or dark room lit only by a flashlight effectively limit pixel flow in the peripheral vision without explicit vignetting). Some apps will only vignette the scene when pixel flow in the periphery is intense. For example, in a flight simulator when approaching a building or mountain.

A variation of tunnel vision is to introduce a static world when the user is moving. This static world is revealed at the periphery, and then only during locomotion that would otherwise create a mismatch between visuals and senses. The user is able to comprehend a confirmation of their senses, while also perceiving the full locomotion of the virtual use. A variation of this method is to pause rendering the periphery when the user initiates movement and only update the center of the view. The periphery could then update in jumps or when the user stops moving to minimize pixel flow.

**Move the environment**, not the user. This one is tough to effectively implement, but done properly users can comfortably “grab” and pull the scene towards them. Here we are creating the illusion that the user isn’t moving, instead the world is moving under the user. The user is pulling or manipulating the world underneath them as if it were mobile.

There are numerous other experimental locomotion methods that you may wish to consider. We recommend that you see the OculusRoomTiny_Advanced sample app that ships with the [PC SDK](/documentation/pcsdk/latest/concepts/pcsdk-intro/) for demos of some of the experimental methods described. 
