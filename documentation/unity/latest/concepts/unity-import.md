---
title: Importing the Oculus Utilities Package
---
Oculus Utilities for Unity is an optional Unity Package that includes scripts, prefabs, and other resources to assist with development.

For more details, see [Oculus Utilities for Unity](/documentation/unity/latest/concepts/unity-utilities-overview/#unity-utilities-overview "This section provides an overview of the Utilities package, including its directory structure, the supplied prefabs, and several key C# scripts.").

Importing Oculus Utilities for Unity has the following steps:

1. If you have previously imported an earlier Utilities version into your project, you must delete its content before importing a new version.
2. Open the project you would like to import the Utilities into, or create a new project.
3. Import the Utilities Unity Package.
4. Update OVRPlugin (optional)
## 1. Delete Previously-Imported Assets If Necessary

If you have previously imported another version of the Utilities package, delete all Oculus content from your Unity project before importing the new version.

Be sure to close the Unity Editor, navigate to your Unity project folder, and delete the following:

Folder

Content to Delete

Assets/Plugins

Oculus.*

OVR.*

Assets/Plugins/Android/

*Oculus*

AndroidManifest.xml

*vrapi*

*vrlib*

*vrplatlib*

Assets/Plugins/x86/

Oculus.*

OVR.*

Assets/Plugins/x86\_64/

Oculus.*

OVR.*

## 2. Open or Create a Unity Project

If you are already working in a Unity project, save your work before beginning. Otherwise, create a new project:

1. From the Unity menu, select **File > New Project**.
2. Click the **Browse** button and select the folder where the Unity project will be located.
3. Make sure that the **Setup defaults for:** field is set to **3D**.
4. You do not need to import any standard or pro Unity asset packages, as the Oculus Utilities package is fully self-contained.
5. Click the **Create** button. Unity will reopen with the new project loaded.
## 3. Import the Unity Package

Select **Assets > Custom Package...** and select the Utilities Unity Package to import it.

Alternately, you can locate the .unityPackage file in your file system and double-click it to launch.

When the **Importing package** dialog box opens, leave all of the boxes checked and select **Import**. The import process may take a few minutes to complete.

## 4. Update OVRPlugin (optional)

The Oculus OVRPlugin provides built-in Editor support and some additional features. It is bundled with all versions of the Unity Editor.

We also include the latest version in the Utilities for Unity package, and if the Utilities version is later than the detected version in the Editor, you will be given the option to automatically update your project to the latest version. We always recommend using the latest available version.

For more information, see [OVRPlugin](/documentation/unity/latest/concepts/unity-utilities-overview/#unity-utilities-ovrplugin "OVRPlugin provides Rift and mobile support to the Unity Editor.").

