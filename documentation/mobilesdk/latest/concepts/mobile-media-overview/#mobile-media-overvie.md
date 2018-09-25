---
title: Mobile VR Media Overview
---
Author all media, such as panoramas and movies, at the highest-possible resolution and quality, so they can be resampled to different resolutions in the future.

This topic entails many caveats and tradeoffs.

## Panoramic Stills

Use 4096x2048 equirectangular projection panoramas for both games and 360 photos. 1024x1024 cube maps is for games, and 1536x1536 cube maps is for viewing in 360 Photos with the overlay code.

## Panoramic Videos

The Qualcomm H.264 video decoder is spec driven by the ability to decode 4k video at 30 FPS, but it appears to have some headroom above that. The pixel rate can be flexibly divided between resolution and frame rate, so you can play a 3840x1920 video @ 30 FPS or a 2048x2048 video @ 60 FPS.

The Android software layer appears to have an arbitrary limit of 2048 rows on video decode, so you may not choose to encode, say, a 4096x4096 video @ 15 FPS. The compressed bit rate does not appear to affect the decoding rate; panoramic videos at 60 Mb/s decode without problems, but most scenes should be acceptable at 20 Mb/s or so.

The conservative specs for panoramic video are: 2880x1440 @ 60 FPS or 2048x2048 @ 60 FPS stereo. If the camera is stationary, 3840x1920 @ 30 FPS video may be considered. The GALAXY S7 decoder allows 4K at 10-bit color, 3840x2160 @ 60 FPS (HEVC) or 8-bit, 3840x2160 @ 60 FPS (VP9). The GALAXY S8 decoder allows 4k at 3840x2160 @ 60 FPS.

Oculus 360 Video is implemented using equirectangular mapping to render panoramic videos. Top-bottom, bottom-top, left-right, and right-left stereoscopic video support is implemented using the following naming convention for videos:

"\_TB.mp4"

Top / bottom stereoscopic panoramic video

"\_BT.mp4"

Bottom / top stereoscopic panoramic video

"\_LR.mp4"

Left / right stereoscopic panoramic video

"\_RL.mp4"

Right / left stereoscopic panoramic video

Default

Non stereoscopic video if width does not match height, otherwise loaded as top / bottom stereoscopic video

## Movies on Screens

Comfortable viewing size for a screen is usually less than 70 degrees of horizontal field of view, which allows the full screen to be viewed without turning your head significantly. For video playing on a surface in a virtual world using the recommended 1024x1024 eye buffers, anything over 720x480 DVD resolution is wasted, and if you don’t explicitly build mipmaps for it, it will alias and look worse than a lower resolution video.

With the TimeWarp overlay plane code running in Oculus Cinema on the 1440 devices, 1280x720 HD resolution is a decent choice. The precise optimum depends on seating position and may be a bit lower, but everyone understands 720P, so it is probably best to stick with that. Use more bit rate than a typical web stream at that resolution, as the pixels will be magnified so much. The optimal bit rate is content dependent, and many videos can get by with less, but 5 Mb/s should give good quality.

1080P movies play, but the additional resolution is wasted and power consumption is needlessly increased.

3D movies should be encoded "full side by side" with a 1:1 pixel aspect ratio. Content mastered at 1920x1080 compressed side-by-side 3D should be resampled to 1920x540 resolution full side-by-side resolution.

## Movie Meta-data

When loading a movie from the sdcard, Oculus Cinema looks for a sidecar file with metadata. The sidecar file is simply a UTF8 text file with the same filename as the movie, but with the extension .txt. It contains the title, format (2D/3D), and category.

{ "title": "Introducing Henry", "format": "2D", "category": "trailers", "theater": "" }Title is the name of the movie. Oculus Cinema will use this value instead of the filename to display the movie title.

Format describes how the film is formatted. If left blank, it will default to 2D (unless the movie has ‘3D’ in its pathname). Format may be one of the following values:

2D

Full screen 2D movie

3D

3DLR

3D movie with left and right images formatted side-by-side

3DLRF

3D movie with left and right images formatted side-by-side full screen (for movies that render too small in 3DLR)

3DTB

3D movie with left and right images formatted top-and-bottom

3DTBF

3D movie with left and right images formatted top-and-bottom full screen (for movies that render too small in 3DTB)

Category can be one of the following values:

Blank

Movie accessible from "My Videos" tab in Oculus Cinema

Trailers

Movie accessible from "Trailers" tab in Oculus Cinema

Multiscreen

Movie accessible from "Multiscreen" tab in Oculus Cinema

## Oculus 360 Photos and Videos Meta-data

The retail version of 360 Photos stores all its media attribution information in a meta file that is packaged into the apk. This allows the categories to be dynamically created and/or altered without the need to modify the media contents directly. For the SDK 360 Photos, the meta file is generated automatically using the contents found in Oculus/360Photos. 

The meta data has the following structure in a meta.json file which is read in from the assets folder:

{ "Categories":[ { "name" : "Category1" }, { "name" : "Category2" } ], "Data":[ { "title": "Media title", "author": "Media author", "url": "relative/path/to/media" "tags" : [ { "category" : "Category2" } ] } { "title": "Media title 2", "author": "Media author 2", "url": "relative/path/to/media2" "tags" : [ { "category" : "Category" }, { "category" : "Category2" } ] } }For both the retail and sdk versions of 360 Videos, the meta data structure is not used and instead the categories are generated based on what’s read in from the media found in Oculus/360Videos.

## Media Locations

The SDK comes with three applications for viewing stills and movies. The Oculus Cinema application can play both regular 2D movies and 3D movies. The Oculus 360 Photos application can display 360 degree panoramic stills and the Oculus 360 Videos application can display 360 degree panoramic videos. These applications have the ability to automatically search for media in specific folders on the device. Oculus 360 Photos uses metadata which contains the organization of the photos it loads in addition to allowing the data to be dynamically tagged and saved out to its persistent cache. This is how the "Favorite" feature works, allowing the user to mark photos as favorites without any change to the media storage itself. The following table indicates where to place additional media for these applications.

MediaFoldersApplication2D Movies

Movies\

DCIM\

Oculus\Movies\My Videos

Oculus Cinema

3D Movies

Movies\3D

DCIM\3D

Oculus\Movies\My Videos\3D

Oculus Cinema

360 degree panoramic stills

Oculus\360Photos

(In the app - assets\meta.json)

Oculus 360 Photos

360 degree panoramic videos

Oculus\360Videos

Oculus 360 Videos

Movie Theater .ovrscene 

Oculus\Cinema\Theaters

Oculus Cinema

