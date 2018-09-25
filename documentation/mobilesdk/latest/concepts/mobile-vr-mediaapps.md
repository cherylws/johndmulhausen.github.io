---
title: Native VR Media Applications
---
## Oculus Cinema

Oculus Cinema uses the Android MediaPlayer class to play videos, both conventional (from /sdcard/Movies/ and /sdcard/DCIM/) and side by side 3D (from /sdcard/Movies/3D and /sdcard/DCIM/3D), in a virtual movie theater scene (from sdCard/Oculus/Cinema/Theaters). See [Mobile VR Media Overview](/documentation/mobilesdk/latest/concepts/mobile-media-overview/#mobile-media-overview) for more details on supported image and movie formats.

Before entering a theater, Oculus Cinema allows the user to select different movies and theaters.

A theater is typically one big mesh with two textures. One texture with baked static lighting for when the theater lights are one, and another texture that is modulated based on the movie when the theater lights are off. The lights are gradually turned on or off by blending between these two textures. To save battery, the theater is rendered with only one texture when the lights are completely on or completely off. The texture with baked static lighting is specified as the diffuse color texture. The texture that is modulated based on the movie is specified as the emissive color texture.

The two textures are typically 4096 x 4096 with 4-bits/texel in ETC2 format. Using larger textures may not work on all devices. Using multiple smaller textures results in more draw calls and may not allow all geometry to be statically sorted to reduce the cost of overdraw. The theater geometry is statically sorted to guarantee front-to-back rendering on a per triangle basis which can significantly reduce the cost of overdraw. 

In addition to the mesh and textures, Oculus Cinema currently requires a 350x280 icon for the theater selection menu. 

## Oculus 360 Photos

Oculus 360 Photos is a viewer for panoramic stills. The SDK version of the application presents a single category of panorama thumbnail panels which are loaded in from *Oculus/360Photos* on the SDK sdcard. Gazing towards the panels and then swiping forward or back on the Gear VR touchpad will scroll through the content. When viewing a panorama still, touch the Gear VR touchpad again to bring back up the panorama menu which displays the attribution information if properly set up. Additionally, the top button or tapping the back button on the Gear VR touchpad will bring back the thumbnail view. The bottom button will tag the current panorama as a Favorite which adds a new category at the top of the thumbnail views with the panorama you tagged. Pressing the *Favorite* button again will untag the photo and remove it from *Favorites*. Gamepad navigation and selection is implemented via the left stick and d-pad used to navigate the menu, the single dot button selects and the 2-dot button backs out a menu. See [Mobile VR Media Overview](/documentation/mobilesdk/latest/concepts/mobile-media-overview/#mobile-media-overview) for details on creating custom attribution information for panoramas.

## Oculus 360 Videos

Oculus 360 Videos works similarly to 360 Photos as they share the same menu functionality. The application also presents a thumbnail panel of the movie read in from Oculus/360Videos which can be gaze selected to play. Touch the Gear VR touchpad to pause the movie and bring up a menu. The top button will stop the movie and bring up the movie selection menu. The bottom button restarts the movie. Gamepad navigation and selection is implemented via the left stick and d-pad used to navigate the menu, the single dot button selects and the 2-dot button backs out a menu. See [Mobile VR Media Overview](/documentation/mobilesdk/latest/concepts/mobile-media-overview/#mobile-media-overview) for details on the supported image and movie formats.

