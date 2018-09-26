---
title: Building Rift Applications
---

This section describes the steps necessary for building Rift apps in Unity.

## Build Settings

Click on **File** &gt; **Build Settings...** and select one of the following:

For Windows, set **Target Platform** to **Windows** and set **Architecture** to either **x86** or **x86 64**.

We recommend unchecking **Development Build** for your final build, as it may impact performance. 

![](/images/documentationunitylatestconceptsunity-build-pc-0.png)

For Mac, set **Target Platform** to **Mac OS X**.

![](/images/documentationunitylatestconceptsunity-build-pc-1.png)

## Player Settings

Within the **Build Settings** pop-up, click **Player Settings**. In the **Other Settings** frame, verify that **Virtual Reality Supported** is checked. All additional required settings are enforced automatically.

![](/images/documentationunitylatestconceptsunity-build-pc-2.png)

## Quality Settings

Navigate to **Edit &gt; Project Settings &gt; Quality**. We recommend the following settings:

|      Pixel Light Count      |            3            |
|-----------------------------|-------------------------|
|       Texture Quality       |        Full Res        |
|    Anisotropic Textures    |       Per Texture       |
|        Anti Aliasing        | 2x or 4x Multi Sampling |
|       Soft Particles       |        Deselect        |
| Realtime Reflections Probes |         Select         |
|   Billboards Face Camera   |         Select         |

![](/images/documentationunitylatestconceptsunity-build-pc-3.png)

The **Anti Aliasing** setting is particularly important. It must be increased to compensate for stereo rendering, which reduces the effective horizontal resolution by 50%. An anti-aliasing value of 2X is ideal, 4x may be used if you have performance to spare. We do not recommend 8x.

For more information on our recommended settings, see [Best Practices for Rift and Mobile](/documentation/unity/latest/concepts/unity-best-practices-intro/).

## Build and Run the Application

In the **Build Settings** dialog, click select **Build**. If prompted, specify a name and location for the build.

To run your application, you must allow apps that have not been reviewed by Oculus to run on your Rift:

1. Launch the Oculus app
2. Click the “gear” icon in the upper-right
3. Select **Settings &gt; General** and set **Unknown Sources** to allow. When prompted for confirmation, select **Allow** (check mark).


![](/images/documentationunitylatestconceptsunity-build-pc-4.png)

You may wish to disable the **Unknown Sources** option when you are not doing development work.

To run your application, navigate to the target folder of your build and launch the executable.

For information about packaging and uploading your Rift app to a Release Channel or Store, please see the [Uploading Rift Apps](/distribute/latest/concepts/publish-uploading-rift/) page.
