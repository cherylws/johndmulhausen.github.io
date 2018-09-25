---
title: User Input
---
This section offers information about how users should interact with the virtual world.

Every Oculus VR device is accompanied by a default controller or input method. We strongly recommend designing your VR application or experience to be designed to use these input devices. There are two categories that ship with our VR devices, the controllers that ship with the mobile devices, like Gear VR and Go, and those that ship with positional tracking, like Rift.

Controllers for these platforms have different capabilities, and therefore different best practices. Mobile device controllers have 3 degree of freedom, while the Rift controller has 6 degree of freedom (commonly referred to as 3DOF and 6DOF). 3DOF controllers allow for orientation tracking of the controller, but do not track the controller’s position in space. Mobile VR devices that use 3DOF controllers only support one controller as the HMD cannot differentiate between multiple controllers. 6DOF controllers support both orientation and positional tracking allowing for a pair of controllers enabling virtual hands that can interact with the VR environment in devices like the Rift.

## General Recommendations

In general, there are some things about user input that you should know when designing your VR experience.

Maintain a **1:1 ratio** between the movement of the user’s controller in the real world and the movement of the virtual representation. This can be rotational or translational movement in space. If you choose to exaggerate the user’s movement in VR, make it so exaggerated (e.g. 4x) that it is readily obvious that it is not a natural sensory experience. 

Use the **standard button mapping** for your application. Experienced VR users are accustomed to certain buttons or movements performing certain actions. Continuing these mappings makes your application feel familiar, even to first time users. Our [Button Mapping Tech Note](/blog/tech-note-touch-button-mapping-best-practices/) details these mappings.

**Menus** should be touch or controller input based, not gazed based. This is a change from the early iterations of Oculus hardware but offers a more engaging and interactive experience.

VR users are both **left and right handed**. Accommodate both sets of users by allowing any interaction to be done with either hand if 2 controllers are present, or respect the default hand set by the system if the device supports a single controller.

## 3DOF Controller Best Practices

The recommendations and best practices in this section are specific to 3DOF controllers, like the Gear VR Controller.

If you choose to represent the controller in-app, we do not recommend representing the controller as a hand, or hand-like object, implying that the controller can be used to grab or manipulate objects. That would be difficult to accomplish with the capabilities of the controller.

3DOF controllers work well as a pointing devices when **pointing at UI elements**. Generally, users find it intuitive to point and select with these controllers. We recommend rendering the controller in the scene and drawing a laser shooting out of the end of the controller (either extending all the way to the UI or fading after a few inches), and rendering a cursor over your UI at the intersection of the ray cast from the controller. The Oculus Home app provides an example of the interaction you could mimic in your app.

If you have a menu that can be **paged through**, or smooth scrolled through, use the controller touchpad. Swiping across the touchpad should move your UI in the same direction as the swipe. For example, if you have a long vertical page, swiping up should move the page upwards to let you see more at the bottom of the page. Allow the user to select with either the trigger or touchpad click, unless you need to reserve one of those for another action.

When using the controller to **aim at objects in VR** (e.g., for a shooter), we recommend that you leave the ray-cast pointer on at all times. Your ray-cast origin should emanate from the end of the virtual controller rendered in your application. To differentiate between objects that are and are not interactive in the virtual environment, render the ray-cast at partial opacity unless it is pointed at an interactive object where it becomes full opacity.

It is usually a good idea to include some form of visual cue when **interacting with an object in VR**, such as highlighting or making the object slightly larger on hover. This provides the user two pieces of information; first that the object is interactive, and second that the object will be selected if an action is taken.

One of the other common uses of the controller is to **control a vehicle** in VR. There are many ways to accomplish this. We’ve found the one-handed tilt approach to be comfortable and intuitive: tilt left to steer left, tilt right to steer right. This method makes the trigger and touchpad available for use during vehicle control.

## 6DOF Controller Best Practices

The recommendations and best practices in this section are specific to 6DOF controllers, like the Touch controllers.

**Hands**

Good **hand registration** is worth the development time. Touch controllers give you access to hands in VR, not just implements that you can hold, but actual hands. When done properly, virtual hands let you interact with the virtual world intuitively; after all, you already know how to use your hands. When implemented poorly, virtual hands can cause an "uncanny hand valley" effect. In extreme cases, poor hand registration and tracking can cause a proprioceptive mismatch and make the user feel uncomfortable. Getting virtual hands right means you need good hand registration.

Registration occurs when the brain sees virtual hands and accepts them as a representation of the physical hands. For this to happen, a number of requirements need to be met. Most importantly, the hand position and orientation needs to match the user’s actual hand. It’s common for a slight offset of rotational error in the hand models to lead to poor registration.

To get registration right, one method is to put a controller model in the scene and ensure its pivot is correct by peeking out from the bottom of the HMD as you move the controller near your face. Properly implemented, you should see the controller pass from the real world into the virtual world seamlessly. From there, the next step is to model hands around the controller and then hide the controller model.

An easy way to test registration is to use the “back of the hand” test. Run your index finger along the back of your other hand in VR and look to see if the touch you’re feeling aligns with the positions of your hand graphics. Poorly aligned hands will often be wildly off, but virtual hands with good registration should match closely.

We’ve published a detailed look at [Implementing Quality Hands With Oculus Touch](/blog/implementing-quality-hands-with-oculus-touch/) on our developer blog, including an overview of some of the tools that Oculus provides.

**Fleshy, realistic hand models** can make users feel uncomfortable if the model does not match their real-world hands. Allow users to customize the appearance of their hands, making them feel more (or less if that is their preference) real. While large hands or attaching other objects to the hand is usually accepted by the brain (people can assume their hands are “inside” those objects), hands that are too small can be disconcerting. Using semi-transparent ethereal or robot hands is generally successful because they believably map to a wide range of user regardless of gender, age, race, or ethnicity.

**Hand-object intersection** should not cause a user’s virtual hands to stop tracking in VR. You can’t prevent people from putting their hands through virtual geometry, trying to prevent this with collision detection makes it feel like hand tracking has been lost and is uncomfortable. If you choose to use life-like hands, consider using physical hands that collide with world geometry, but then immediately display a second set of **ethereal or transparent hands** that continue to track with the player’s motion when the life-like hands get stuck or collide with a solid object. This visually indicates that tracking hasn’t been lost, and the ethereal appearance of the hands suggests that they can’t be used to manipulate the world.

**Avoid hand animations.** Hand registration requires that your brain, somewhat, believes that your avatar’s hands are your own. Having the hands animate, or move without any real-world input, can be very uncomfortable. The exception appears to be quick animations that are expected from user input. For example, animating gun recoil when a user fires a virtual gun.

**Virtual forearms and elbows are difficult to get right. **Discomfort can be caused by proprioception, or your brain’s innate sense of where your limbs are located in physical space, even when you aren’t looking at them. This sensory system is so accurate that trying to simulate virtual limbs, like forearms and elbows, can be difficult. You can see virtual limbs, but you can’t feel them (in the absence of haptic feedback) or locate them using proprioception. It’s common for developers to attempt to attach an IK arm to a tracked controller, but this solution often results in discontinuity between the rendered virtual arm position and the person’s real arm, which proprioception can detect. There are titles that have achieved very believable forearms and elbows, but this is a design problem that requires a great deal of patience and attention. Incorrect arms are worse than no arms at all. We generally recommend not drawing anything above the wrist.

**Interacting with the Virtual World**

Tracked controllers can give you virtual hands, but they can’t simulate the **torque or resistance** we feel when manipulating weighty objects. Interactions that involve significant resistance, like lifting a heavy rock or pulling a large lever don’t feel believable. However, **lightweight interactions** that involve objects for which we don’t expect to feel significant physical resistance like flicking a light switch are readily believable. When designing hand interactions, consider the apparent weight of the objects people are manipulating and look for ways to make the lack of physical resistance believable.

Use caution when working with **interactions that require two hands**. Lifting a heavy box or holding a pitchfork with two hands is likely to feel strange because the rigid constraints we expect between the hands won’t exist in VR.

The best way to pick up an object in VR is to **grab the object the way it was designed to be held**. Nobody expects to pick a gun up by its barrel or a coffee cup by its base. When a person tries to pick up an object that affords gripping in an obvious way, you should snap the object into their hand at the correct alignment. They reach for the gun, close their hand, and come away with the gun held perfectly, just as they expected. We don’t recommend objects that require shifting of grip, like ping pong paddles. The process of changing hands can feel unnatural. When picking up and gripping an object, we recommend using the grip button on the Touch controller. 

We recommend that you **avoid having users pick up objects off the floor**. Sensors are frequently positioned on a desk and may be occluded if the user bends down to pick up an object below the elevation of the desk. Distance grabbing is an effective way to allow users to interact with objects outside of their normal reach. See the [Distance Grab Sample Now Available in Oculus Unity Sample Framework](/blog/distance-grab-sample-now-available-in-oculus-unity-sample-framework/) tech note for information about this concept and how to implement this method.

**Some objects don’t have an obvious handle or grip** (e.g. a soccer ball) and should attach to the hand at the moment that the grip trigger is depressed. In this case, the offset and orientation of the object to the hand is arbitrary, but as long as the object sticks to the hand it will feel believable. You shouldn’t snap or correct the object in this case—just stick it to the hand at whatever positional offset it was at when the grip was invoked.

**Throwing** objects reliably with tracked controllers is harder than it looks. Different objects afford throwing in different ways. For example, a frisbee is thrown using a completely different motion than the way a paper airplane is thrown. Making both of these actions believable requires building per-object physics rules to govern throwing. When designing your control scheme for throwing objects, use caution if you use the grip button for hold/release. Consider using the trigger button for throw interactions that require force. Users have been known to throw the Touch controller in the real world if the grip button is used.

Use **haptics** to indicate when a user has interacted with an object. This simple addition makes the interaction with objects more believable. 

