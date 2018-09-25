---
title: Single Pass Known Issues
---
Several known issues currently affect Single Pass Stereo Rendering. 

## Graphics Driver Issues

Two known graphics driver issues affect mobile applications using Single Pass in certain Unity/phone combinations:

* Affected phones: SM-G955F (S8+) / SM-G950F (S8)
* Affected Unity versions: 5.6.0p2 / 5.6.0p3
A fix is being deployed, but it will take some time for users to get it from OTA.

**Issues**

1. When “Standard Shader Quality” is low in your graphics config, the standard shader may appear black.

![](/images/documentation-unity-latest-concepts-unity-single-pass-known-issues-0.png)  
2. If you create tree objects, using the default “Optimized Bark Material” may cause the tree to disappear.

![](/images/documentation-unity-latest-concepts-unity-single-pass-known-issues-1.png)  
 Both issues requires shader overwriting to workaround. The process is similar.

## Workaround for the Standard Shader Issue

Note: Before proceeding, we recommend backing up your project.1. Download the build-in shader package from Unity website for [5.6.0p2](https://unity3d.com/unity/qa/patch-releases/5.6.0p3).
2. Copy the following files from the shader package to your project folder: 
	1. All files under Assets\Shaders\CGIncludes. Not every file is necessary, but we recommend simply copying all of them, as the dependencies can be complicated.
	2. \DefaultResourcesExtra\Standard.shader
	
3. In your project, modify the file UnityStandardCoreForwardSimple.cginc in Assets\Shaders\CGIncludes\ by adding the following code to the end of FragmentSetupSimple() before return s;#if defined(UNITY\_STEREO\_MULTIVIEW\_ENABLED) s.smoothness = saturate(s.smoothness); #endif
4. Navigate to Assets\Shaders\CGIncludes\ and rename **Standard.shader** to **StandardS8.shader**.
5. Open StandardS8.shader and change the first line from Shader "Standard" to Shader "StandardS8".
6. After you finished modifying the shaders, you need apply them. Change the shader for any affected material from **Standard** to **StandardS8**.
If you have a lot of affected materials, it may be easier to use an editor script to apply these changes, such as this:

[MenuItem("Tools/Oculus/ApplyS8Workaround")] static void ApplyS8Workaround() { Renderer[] \_renderers = Component.FindObjectsOfType<Renderer>(); foreach (Renderer \_renderer in \_renderers) { Material[] \_materials = \_renderer.sharedMaterials; foreach (Material \_material in \_materials) { if (\_material.shader.name.Equals("Standard")) { \_material.shader = Shader.Find("StandardS8"); } } } }## Workaround for the Optimized Bark Material Issue

Note: Before proceeding, we recommend backing up your project.1. Download the build-in shader package from Unity website for [5.6.0p2](https://unity3d.com/unity/qa/patch-releases/5.6.0p3).
2. Copy the following files from the shader package to your project folder 
	1. \DefaultResourcesExtra\Standard.shader
	2. \DefaultResourcesExtra\Nature\TreeCreator\TreeCreatorBarkOptimized.shader
	
3. In your project, modify the file TerrainEngine.cginc in Assets\Shaders\CGIncludes\ by adding the following code right after the line float2 vWavesIn = \_Time.yy + float2(fVtxPhase, fBranchPhase ): #if defined(UNITY\_STEREO\_MULTIVIEW\_ENABLED) vWavesIn.x += saturate(fVtxPhase) * 0.00000001f; #endif
4. Navigate to Assets\Shaders\CGIncludes\ and rename TreeCreatorBarkOptimized.shader to TreeCreatorBarkOptimizedS8.shader.
5. Open TreeCreatorBarkOptimizedS8.shader and change the first line from Shader "Hidden/Nature/Tree Creator Bark Optimized" to Shader "Hidden/Nature/Tree Creator Bark Optimized S8"
6. After you finished modifying the shaders, you will need apply them. Change the shader for any affected material from Tree Creator Bark Optimized to Tree Creator Bark Optimized S8.
If you have a lot of affected materials, you may wish to write an Editor script to do this conversion similar to the example given in the standard shader issue workaround above.

## Compiling Issues

When Single Pass is enabled in Unity 5.6.0p2, building mobile projects will fail if either of the two cases are true:

1. You are using Standard Shader and have enabled both specular highlights and normal mapping; or
2. You are using the old mobile bumped diffuse detail shader.
You will see a shader error referring to bumped detail that says “Duplicated input semantics can't change type, size, or layout ('TEXCOORD7').”

Note: This issue is fixed in Unity 2017.1.0b5 and later.**Workaround**

The actual details will differ depending on which shader you have problems with - these instructions use Mobile-Bumped.shader as an example.

Note: Before proceeding, we recommend backing up your project.1. Download the build-in shader package from Unity website for [5.6.0p2](https://unity3d.com/unity/qa/patch-releases/5.6.0p3).
2. Copy any shaders reported by the compiler error the following files from the shader package to your project folder, such as Mobile-Bumped.shader (for example).
3. In the file \Assets\Shaders\CGIncludes\UnityInstancing.cginc, replace #define UNITY\_VERTEX\_OUTPUT\_STEREO float stereoTargetEyeIndex : TEXCOORD7; with: #define UNITY\_VERTEX\_OUTPUT\_STEREO float stereoTargetEyeIndex : TEXCOORD10;
4. Navigate to Assets\Shaders\CGIncludes\ and rename Mobile-Bumped.shader to Mobile-BumpedS8.shader.
5. Open Mobile-BumpedS8.shader and change the first line from Shader "Mobile-Bumped"  to Shader "Mobile-BumpedS8"
6. After you finished modifying the shaders, you need apply them. Change the shader for any affected material from Mobile-Bumped to Mobile-BumpedS8.
If you have a lot of affected materials, you may wish to write an Editor script to do this conversion similar to the example given in the standard shader issue workaround above.

