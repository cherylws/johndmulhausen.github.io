---
title: Vision
---

This section offers tips about how to display the virtual world you’re creating to your users and is provided with a bit more explanation due to its complexity.

## Using Monocular Depth Clues

Failing to properly represent the depth of objects will break a VR experience. Stereopsis, the perception of depth based on disparity between the viewpoints of each eye, is the most salient depth cue, but it is only one of many ways the brain processes depth information.

Many visual depth cues are **monocular**; that is, they convey depth even when they are viewed by only one eye or appear in a flat image viewed by both eyes.

One such depth cue is **motion parallax**, or the degree to which objects and different distances appear to move at different rates during head movement.

Other depth cues include: **curvilinear perspective** (straight lines converge as they extend into the distance), **relative scale** (objects get smaller when they are farther away), **occlusion** (closer objects block our view of more distant objects), **aerial perspective** (distant objects appear fainter than close objects due to the refractive properties of the atmosphere), **texture gradients** (repeating patterns get more densely packed as they recede into the distance) and **lighting** (highlights and shadows help us perceive the shape and position of objects).

Current-generation computer-generated content (such as content created in Unreal and Unity) leverage a lot of these depth cues, but we mention them because it can be easy to neglect their importance. If implemented improperly, the experience may become uncomfortable or difficult to view as a result of conflicting depth signals. 

## Comfortable Viewing Distances

Two issues are of primary importance to understanding eye comfort when the eyes are focusing on an object in VR: **accommodative demand** and **vergence demand**. Accommodative demand refers to how your eyes have to adjust the shape of their lenses to bring a depth plane into focus (a process known as accommodation). Vergence demand refers to the degree to which the eyes have to rotate inwards so their lines of sight intersect at a particular depth plane. In the real world, these two are strongly correlated with one another; so much so that we have what is known as the accommodation-convergence reflex: the degree of convergence of your eyes influences the accommodation of your lenses, and vice-versa.

VR creates an unusual situation that decouples accommodative and vergence demands, where accommodative demand is fixed but vergence demand can change. This is because the actual images for creating stereoscopic 3D are always presented on a screen that remains at the same distance optically, but the different images presented to each eye still require the eyes to rotate so their lines of sight converge on objects at a variety of different depth planes.

The degree to which the accommodative and vergence demands can differ before the experience becomes uncomfortable to the viewer varies. In order to prevent eyestrain, objects that you know the user will be fixating their eyes on for an extended period of time (e.g., a menu, an object of interest in the environment) should be rendered at least 0.5 meters away. Many have found that 1 meter is a comfortable distance for menus and GUIs that users may focus on for extended periods of time.

Obviously, a complete virtual environment requires rendering some objects outside the comfortable range. As long as users are not required to focus on those objects for extended periods, they should not cause discomfort for most individuals.

Some developers have found that depth-of-field effects can be both immersive and comfortable for situations in which you know where the user is looking. For example, you might artificially blur the background behind a menu the user brings up, or blur objects that fall outside the depth plane of an object being held up for examination. This not only simulates the natural functioning of your vision in the real world, it can prevent distracting the eyes with salient objects outside the user’s focus.

You have no control over a user who chooses to behave in an unreasonable manner. A user may choose to stand with their eyes inches away from an object and stare at it all day. Your responsibility is to avoid requiring scenarios that may cause discomfort.

## Viewing Objects at a Distance

At a certain distance depth perception becomes less sensitive. Up close, stereopsis might allow you to tell which of two objects on your desk is closer on the scale of millimeters. This becomes more difficult further out. If you look at two trees on the opposite side of a park, they might have to be meters apart before you can confidently tell which is closer or farther away. At even larger scales, you might have trouble telling which of two mountains in a mountain range is closer to you until the difference reaches kilometers.

Use this relative insensitivity to depth perception in the distance to free up computational power by using **imposter** or **billboard** textures in place of fully 3D scenery. For instance, rather than rendering a distant hill in 3D, you might simply render a flat image of the hill onto a single polygon that appears in the left and right eye images. This image appears to the eyes in VR the same as in traditional 3D games.

## Rendering Stereoscopic Images

We often face situations in the real world where each eye gets a very **different viewpoint**, and we generally have little problem with it. Peeking around a corner with one eye works in VR just as well as it does in real life. In fact, the eyes’ different viewpoints can be beneficial: say you’re a special agent (in real life or VR) trying to stay hidden in some tall grass. Your eyes’ different viewpoints allow you to look “through” the grass to monitor your surroundings as if the grass weren’t even there in front of you. Doing the same in a video game on a 2D screen may leave the world completely occluded behind each blade of grass.

Still, VR (like any other stereoscopic imagery) can give rise to some situations that can be uncomfortable for the user. For instance, rendering effects (such as light distortion, particle effects, or light bloom) should always appear in both eyes and with correct disparity. Improperly rendering these effects gives the appearance of flickering/shimmering (when something appears only in one eye) or floating at the wrong depth (if disparity is off, or if the post-processing effect is not rendered to contextual depth of the object it should be; for example, a specular shading pass). It is important to ensure that the images between the two eyes do not differ aside from the slightly different viewing positions inherent to binocular disparity.

It’s typically not a problem in a complex 3D environment, but be sure to give the user’s brain enough information to fuse the stereoscopic images together. The lines and edges that make up a 3D scene are generally sufficient. However, be very cautious of using wide swaths of repeating patterns or textures, which could cause people to fuse the images differently than intended. Be aware also that optical illusions of depth (such as the [hollow mask illusion](https://en.wikipedia.org/wiki/Hollow-Face_illusion), where concave surfaces appear convex) can sometimes lead to misperceptions, particularly in situations where monocular depth cues are sparse.

## Displaying Information in VR

We discourage the use of traditional HUDs to display information in VR. Instead, embed the information into the environment or the user’s avatar. Although certain traditional conventions can work with thoughtful re-design, simply porting over the HUD from a non-VR game into VR content introduces new issues that make them impractical or even discomforting.

Should you choose to incorporate some HUD elements, be aware of the following issues.

1. **Don’t occlude the scene with the HUD.** This isn’t a problem in non-stereoscopic games, because the user can easily assume that the HUD actually is in front of everything else. Adding binocular disparity (the slight differences between the images projected to each eye) as a depth cue can create a contradiction if a scene element comes closer to the user than the depth plane of the HUD. Based on occlusion, the HUD is perceived to be closer than the scene element because it covers everything behind it, yet binocular disparity indicates that the HUD is farther away than the scene element it occludes. This can lead to difficulty and/or discomfort when trying to fuse the images for either the HUD or the environment.
2. **Don’t draw the elements “behind” anything in the scene.** This effect is extremely common with reticles, subtitles, and other sorts of floating UI elements. It’s common for an object that should be “behind” a wall (in terms of distance from the camera) to be drawn “in front” of the wall because it’s been implemented as an overlay. This sends conflicting cues about the depth of these objects, which can be uncomfortable.




![](/images/designlatestconceptsbp-vision-0.jpg)



Instead, we recommend that you **build the information into the environment**. Users can move their heads to retrieve information in an intuitive way. For instance, rather than including mini map and compass in a HUD, the player might get their bearings by glancing down at an actual map and compass in their avatar’s hands or cockpit or a watch that displays the player’s vital information.. This is not to say realism is necessary, enemy health gauges might float over their heads. What’s important is presenting information in a clear and comfortable way that does not interfere with the player’s ability to perceive a clear, single image of the environment or the information they are trying to gather.

Targeting reticles are common elements to games, and are a good example of where we can adapt an old information paradigm to VR. While a reticle is critical for accurate aiming, simply pasting it over the scene at a fixed depth plane will not yield the behavior players expect in a game. For example, if the reticle is rendered at a depth different from where the eyes are converged, it is perceived as a double image. In order for the targeting reticle to work the same way it does in traditional video games, it must be drawn directly onto the object it is targeting on screen, presumably where the user’s eyes are converged when aiming. The reticle itself can be a fixed size that appears bigger or smaller with distance, or you can program it to maintain an absolute size to the user; this is largely an aesthetic decision.

Place critical gameplay elements in the user's **immediate line of sight**. UI or elements displayed outside the user's immersive line of sight are more likely to be missed. 



![](/images/designlatestconceptsbp-vision-1.jpg)



**http://buildmedia.com/portfolio-items/what-are-survey-accurate-visual-simulations/**

## Camera Origin &amp; User Perspective

You should consider the altitude of the user, or height of the user’s point of view (POV), as this can be a factor in causing discomfort. The lower the user’s POV, the more rapidly the ground plane changes, creating a more intense display of optic flow. This can create an uncomfortable sensation for the same reason that moving up staircases is uncomfortable: doing so creates an intense optic flow across the visual field.

When developing a VR app, you can choose to make the camera’s origin rest on people’s floor or on their eyes (these are called “floor” and “eye” origins, respectively). Both options have certain advantages and disadvantages.

**Using the floor as the origin** will cause people’s viewpoint to be at the same height off the ground that they are in real life. Aligning their virtual viewpoint height with their real-world height can increase the sense of immersion. However, you can’t control how tall people in your virtual worlds are. If you want to render a virtual body, you’ll need to build a solution that can scale to different people’s height.

**Using the user’s eyes as the camera’s origin means** that you can control their height within the virtual world. This is useful for rendering virtual bodies that are a specific height and also for offering perspectives that differ from people’s real-world experience (for example, you can show people what the world looks like from the eyes of a child). However, by using the eye point as the origin, you no longer know where the physical floor is. This complicates interactions that involve ducking low or picking things up from the ground. Since you won't actually know the user’s height, you may wish to add a recentering step at the beginning of your app to accurately record the user’s real world height. 
