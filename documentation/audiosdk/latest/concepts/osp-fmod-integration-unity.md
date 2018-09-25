---
title: Installing with the FMOD Studio Unity Integration
---
The FMOD Studio Unity Integration is a Unity plugin which allows the use of FMOD in Unity games. 

## Compatibility

The Oculus Spatializer Plugin (OSP) for FMOD is compatible with FMOD Studio Unity Integration for projects targeting Windows (32/64 bit), OS X, and Android. Two versions of the FMOD Studio Unity Integration are currently available: 2.0 and Legacy. The OSP for FMOD is compatible with:

* 2.0 (1.07.04 and higher)
* Legacy Version 1.07.03
## 2.0 Integration Installation

If you are migrating from the Legacy Integration, please follow FMODâ€™s migration guide here: [https://www.fmod.com/resources/documentation-api?page=content/generated/engine\_new\_unity/migration.html#/](https://www.fmod.com/resources/documentation-api?page=content/generated/engine_new_unity/migration.html#/)

Otherwise, take the following steps:

1. Follow the guide for setting up the 2.0 Integration here: [https://www.fmod.com/resources/documentation-api?page=content/generated/engine\_new\_unity/overview.html#/](https://www.fmod.com/resources/documentation-api?page=content/generated/engine_new_unity/overview.html#/)
2. Follow instructions for using the OSP in FMOD Studio here: [https://developer.oculus.com/documentation/audiosdk/latest/concepts/osp-fmod-usage/](/documentation/audiosdk/latest/concepts/osp-fmod-usage/)
3. Open your project in the Unity Editor. Select *Assets* > *Import* > *Custom Package*, and select OculusSpatializerFMODUnity.unitypackage in AudioSDK\Plugins\FMOD\Unity to import into your project.
4. In the *Project* tab of *FMOD Settings*, click the *Add Plugin* button, and enter OculusSpatializerFMOD in the new text field.
You should now be able to load and play FMOD Events that use the OSP in your Unity application runtime.

## Legacy Integration Installation

1. Follow instructions for setting up the Legacy Integration here: [https://www.fmod.com/resources/documentation-api?page=content/generated/engine\_unity/getting\_started.html](https://www.fmod.com/resources/documentation-api?page=content/generated/engine_unity/getting_started.html)
2. Follow instructions for using the OSP in FMOD Studio: [https://developer.oculus.com/documentation/audiosdk/latest/concepts/osp-fmod-usage/](/documentation/audiosdk/latest/concepts/osp-fmod-usage/)
3. Open your project in the Unity Editor. Then select *Assets* > *Import* > *Custom Package*, and select OculusSpatializerFMODUnity.unitypackage in AudioSDK\Plugins\FMOD\Unity to import it into your project.
4. In the Project view, select the FMOD\_Listener script, which should be attached to an object in the root of the scene. In the Unity Inspector view, increment the Size of Plugin Paths by one, and add ovrfmod in the new element.
5. **OS X platform only**: In FMOD\_Listener.cs, in LoadPlugins(), modify the body of the foreach loop with the following code inside the OCULUS start/end tags:
foreach (var name in pluginPaths) { // OCULUS start var path = pluginPath + "/"; if(name.Equals("ovrfmod") && (Application.platform == RuntimePlatform.OSXEditor || Application.platform == RuntimePlatform.OSXPlayer || Application.platform == RuntimePlatform.OSXDashboardPlayer) ) { path += (name + ".bundle"); FMOD.Studio.UnityUtil.Log("Loading plugin: " + path); } else { path += GetPluginFileName(name); FMOD.Studio.UnityUtil.Log("Loading plugin: " + path); #if UNITY\_5 && (UNITY\_64 || UNITY\_EDITOR\_64) if (!System.IO.File.Exists(path)) { path = pluginPath + "/" + GetPluginFileName(name + "64"); } #endif #if !UNITY\_METRO if (!System.IO.File.Exists(path)) { FMOD.Studio.UnityUtil.LogWarning("plugin not found: " + path); } #endif } // OCULUS end uint handle; FMOD.RESULT res = sys.loadPlugin(path, out handle); ERRCHECK(res); }Now you should be able to load and play FMOD Events that use the OSP in your Unity application runtime.

