---
title: Oculus Rift: Quick Start
---
This guide covers everything you need to know to get started developing Unreal applications for the Oculus Rift.

## Setup the Oculus Rift

Setup the headset, as described in [Get Started with Rift](https://www.oculus.com/setup/).

Note: An Oculus Signature File (OSIG) is **not** required for the Oculus Rift.## Select an Unreal Engine Distribution

There are a number of ways that you can obtain the Oculus Unreal distributions:

* A binary distribution is provided through the [Epic Game Launcher](https://www.unrealengine.com/download?sessionInvalidated=true). This Oculus code may be a version or two behind the latest Oculus SDK. We recommend that beginning developers use this binary distribution. It is stable, and does not require pulling the source from GitHub, setting up Visual Studio, and performing a lengthy compilation of the entire Unreal game engine source code. 
* A source distribution is provided through the [Epic GitHub Repository](https://github.com/EpicGames). This Oculus code may be a version or two behind the latest Oculus SDK. Please see the Epic GitHub Repository table in [Version Compatibility Reference](/documentation/unreal/latest/concepts/unreal-compatibility-matrix/ "This section provides compatibility information for Oculus OVRPlugin and UE4 versions. To access these GitHub repositories, you must be subscribed to the private EpicGames/UnrealEngine repository. If you are not subscribed and logged into your GitHub account, you will get a 404 error. An Unreal license is not required."), in order to choose the specific downloads that best suit your development criteria. 
* A source distribution is provided through the [Oculus GitHub Repository](https://github.com/Oculus-VR/UnrealEngine.git). These distributions are always up to date with the latest Oculus SDKs. We support the current release of UE4 and any preview of the next release of UE4. Please see the Oculus GitHub Repository table in [Version Compatibility Reference](/documentation/unreal/latest/concepts/unreal-compatibility-matrix/ "This section provides compatibility information for Oculus OVRPlugin and UE4 versions. To access these GitHub repositories, you must be subscribed to the private EpicGames/UnrealEngine repository. If you are not subscribed and logged into your GitHub account, you will get a 404 error. An Unreal license is not required."), in order to choose the specific downloads that best suit your development criteria. While new Oculus features ship first to the Oculus GitHub versions, API changes may occur when these branches are merged back into Epicâ€™s version of the engine. We recommend these distributions for professional developers who would like to access the latest Oculus SDK features. In order to build this source, see [Building UE4 from Source](/documentation/unreal/latest/concepts/unreal-building-ue4-from-source/ "The following section describes how to download, compile, and launch UE4 from the Oculus GitHub repository using Visual Studio 2015 or 2017."). ![](/images/documentation-unreal-latest-concepts-unreal-quick-start-guide-rift-0.png)  

To access these GitHub repositories, you must be subscribed to the private EpicGames/UnrealEngine repository (see [UE4 of GitHub](https://www.unrealengine.com/ue4-on-github) for details). If you are not subscribed and logged into your GitHub account, you will receive a 404 error. An Unreal license is not required.

All versions of the Oculus Unreal SDK require Windows 7 or later.

## Enabling Unknown Sources

In order to play an in-development application, you will need to enable the Oculus system to run applications from unknown sources by using the Oculus app settings, available through the gear icon in the upper-right. Select **Settings > General** and turn on **Unknown Sources** on to allow this. 

![](/images/documentation-unreal-latest-concepts-unreal-quick-start-guide-rift-1.png)  
The first time you run an application that you have not downloaded from the Oculus Store, you will need to launch it directly. Once you have run an application from an unknown source at least once, it will then appear in the Library section of Home and the Oculus app, and may be launched normally, as long as **Unknown Sources** is enabled.

## Developing Applications with the UE4 Editor

1. Download and setup the Unreal engine that you wish to use. Make sure you are using a compatible set of SDKs, as shown in the [Version Compatibility Reference](/documentation/unreal/latest/concepts/unreal-compatibility-matrix/ "This section provides compatibility information for Oculus OVRPlugin and UE4 versions. To access these GitHub repositories, you must be subscribed to the private EpicGames/UnrealEngine repository. If you are not subscribed and logged into your GitHub account, you will get a 404 error. An Unreal license is not required.").
2. Follow the instructions in the [Oculus Rift Quick Start](https://docs.unrealengine.com/en-us/Platforms/Oculus/QuickStart) provided by Epic.
## Application Distribution Requirements and Guidelines

Also see the Oculus [Distribute](/distribute/) document.

