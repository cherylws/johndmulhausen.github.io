---
title: Cubemap Screenshots
---

The OVR Screenshot Wizard allows you to easily export a 360 screenshot in cubemap format.

Cubemap previews may be submitted with applications to provide a static in-VR preview for the Oculus Store. For more information, see [Oculus Store Art Guidelines](https://scontent-sjc3-1.xx.fbcdn.net/v/t39.2365-6/10000000_2007708799495262_8508290021072044032_n.pdf?_nc_cat=111&amp;oh=5a41a1fd066453853ad1ee4880be6e93&amp;oe=5C5CF91A) (PDF).

You may also use OVRCubemapCaptureProbe to take a 360 screenshot from a running Unity app. (see [Prefabs](/documentation/unity/latest/concepts/unity-utilities-overview/#unity-prefabs) for more information).

![](/images/documentationunitylatestconceptsunity-cubemap-0.png)

## Basic Usage

![](/images/documentationunitylatestconceptsunity-cubemap-1.png)

When you import the Oculus Utilities OVRScreenshotWizard into your project, it will add a new **Tools** pull-down menu to your menu bar. Select **Tools** &gt; **Oculus** &gt; **OVR Screenshot Wizard** to launch the tool.

By default, the screenshot will be taken from the perspective of your Main Camera. To set the perspective to a different position, assign any Game Object to the **Render From** field in the Wizard and click **Render Cubemap** to save.

The generated cubemap may be saved either as a Unity Game Object, or as a horizontal 2D atlas texture in PNG or JPG format with the following face order (Horizontal left to right): +x, -x, +y, -y, +z, -z.

## Options

![](/images/documentationunitylatestconceptsunity-cubemap-2.png)

**Render From**: You may use any Game Object as the "camera" that defines the position from which the cubemap will be captured.

To assign a Game Object to function as the origin perspective, select any instantiated Game Object in the Hierarchy View and drag it here to set it as the rendering position in the scene. You may then position the Game Object anywhere in the scene.

If you do not specify a Game Object in this field, the screenshot will be taken from the Main Camera.

**Size**: Sets the resolution for each "tile" of the cubemap face. For submission to the Oculus Store, select 2048 (default, see [ Oculus Store Art Guidelines](https://scontent-sjc3-1.xx.fbcdn.net/v/t39.2365-6/10000000_2007708799495262_8508290021072044032_n.pdf?_nc_cat=111&amp;oh=5a41a1fd066453853ad1ee4880be6e93&amp;oe=5C5CF91A) for more details).

**Save Mode**

* Save Cube Map: Generate Unity format Cubemap
* Save Cube Map Screenshot: Generate a horizontal 2D atlas texture, resolution: ( 6 * Size ) * Size
* Both: Save both Unity Cubemap and 2D atlas texture


**Cube Map Folder**: The directory where OVR Screenshot Wizard creates the Unity format Cubemap. The path must be under the root asset folder "Assets"

**Texture Format**: Sets the image format of 2D atlas texture (PNG or JPEG).

**Render Cubemap**: Click the button to generate cubemap.
