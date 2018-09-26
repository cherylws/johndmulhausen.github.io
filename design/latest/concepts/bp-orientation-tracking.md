---
title: User Orientation and Positional Tracking
---

This section offers best practices about how to track and translate a user's real-world movements to the virtual world.

User orientation and positional tracking only applies to VR devices with 6DOF tracking capabilities, like the Rift.

**Do not disable or modify position tracking.** This is especially important while the user is moving in the real world. Any discernible difference between movement in the real world that does not map to movement in VR, or vice versa, causes a conflict of the senses and is extremely discomforting.

Allow users to set their **origin point**. Users may prefer to orient themselves in the real world a certain way. This may be due to how their room is set up in the real world. Add guidance to your app helping them to position themselves in their preferred orientation. Users may shift or move during gameplay, and therefore should have the ability to reset the origin at any time.

**Roomscale** holds a great deal of potential, it also introduces new challenges. First, users can leave the viewing area of the tracking camera and lose position tracking, which can be a very jarring experience. To maintain an uninterrupted experience, the Oculus Guardian system provides users with warnings as they approach the edges of the camera’s tracking volume before position tracking is lost. They should also receive some form of feedback that will help them better position themselves in front of the camera for tracking. For example, you can display the user’s origin point in the scene to help users position themselves. You could also query and display an outline of the user’s boundary.

Proper positional tracking requires people to define a play area in their homes for VR. This area is created in the first time setup for each user and is used with the Guardian system to help protect users. The amount of **tracked size space** available varies from user to user, making it difficult to know how large to make their virtual spaces. Most people have, on average, four square meters of trackable space available. If that were a square, it would be roughly six feet per side, but many users will not have a perfectly square area. Some people have more space than that available, but a large number of people have less. Design your content and interactions with these tracked space requirements in mind. You should not require interactions that occur outside a user's Guardian configuration or defined play area.

Both **roomscale** and **tracked size space** may benefit from querying the player's play area and rendering the important and interactive scene objects within that area. This allows you to help the player stay within the tracked volume and ensure that everything interactive is within the player’s reach.

A challenge unique to VR is that users can now move the **virtual camera** into unusual positions that might have been previously impossible. For instance, users can move the camera to look under objects or around barriers to see parts of the environment that would be hidden in a conventional video game. While this opens up new methods of interaction, like physically moving to peer around cover or examine objects in the environment, this also allows users to discover technical shortcuts you might have taken in designing the environment that would normally be hidden. Make sure that your art and assets do not break the user’s sense of immersion in the virtual environment.

**Head-object intersections** are another issue that is unique to positionally tracked VR. Users could potentially use position tracking to clip through the virtual environment by leaning through a wall or object. Ensure that your design does not allow a user to get close enough to “solid” objects that they may intersect with causing a discomforting experience.
