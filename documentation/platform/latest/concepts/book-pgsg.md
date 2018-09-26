---
title: Getting Started Guide
---

The Getting Started Guide will review the onboarding and basic integration process for the Platform SDK, how to configure your development environment, and how to implement the required components of the SDK. 

The steps described on this page are required for publishing an app on the Oculus Store. All other feature integrations described in the Developer Guide are optional.

## Onboarding

Before you can get started or integrate any portion of the Platform SDK, you’ll need to define your app in the Developer Center. The App ID created by this process is required to successfully initialize the SDK. Information about how to create your application can be found on the [Creating and Managing Apps](/distribute/latest/concepts/publish-create-app/) page of the Publishing section if you have not done so already.

Once you’ve created your application in the Developer Center, go to the [API](https://dashboard.oculus.com/app/api) page, retrieve the App Id, and start integrating the SDK. 

All developers, including mobile developers, need to install the Oculus runtime from [https://www.oculus.com/setup/](https://www.oculus.com/setup/).

## Before You Integrate

Before you start integrating, there are two concepts that you should familiarize yourself with: [Requests and Messages](/documentation/platform/latest/concepts/sdkgs-requestsnmessages/) and [Server-to-Server API Basics](/documentation/platform/latest/concepts/pgsg-s2s-basics/). The Requests and Messages page describes how native applications use the message queue to interact with the Platform SDK. The Server-to-Server API Basics reviews how to interact with the Oculus REST API that some features use.

If you’re upgrading the Platform SDK from an old version (v1.9 or earlier), please review the information on the [Migrating from a Previous Version](/documentation/platform/latest/concepts/release-migration/) page.

## The Basics

Once you’ve completed the onboarding steps and reviewed the stuff you should know, you can download the SDK, configure your development environment and integrate the required functionality of the Platform SDK.

First things first, download the latest version of the Platform SDK from the [Platform SDK Download](/downloads/package/oculus-platform-sdk/) page.

Once you’ve downloaded the SDK, you can configure your development environment, initialize the SDK, and implement the Entitlement Check. Please see the [Native Development Getting Started](/documentation/platform/latest/concepts/pgsg-native-gsg/), [Unity Development Getting Started](/documentation/platform/latest/concepts/pgsg-unity-gsg/), or [Unreal Development Getting Started](/documentation/platform/latest/concepts/pgsg-unreal-gsg/) guides for information about how to get started with your development platform.

## Integrating the Features

Once you’ve finished the getting started and onboarding process, you can visit the [Developer Guide](/documentation/platform/latest/concepts/book-dg/) and start integrating the SDK features.

* **[Server-to-Server API Basics](/documentation/platform/latest/concepts/pgsg-s2s-basics/)**  
Some platform features use server-to-server (S2S) REST API calls to perform actions not appropriate to be sent from client devices. These APIs are provided to ensure a secure interaction between your back-end servers and the Oculus Platform.
* **[Requests and Messages](/documentation/platform/latest/concepts/sdkgs-requestsnmessages/)**  
The Platform SDK uses a message queue to interact with Native apps. This page describes the concept of the queue and how to retrieve messages and information.
* **[Migrating from a Previous Version](/documentation/platform/latest/concepts/release-migration/)**  

* **[Native Development Getting Started](/documentation/platform/latest/concepts/pgsg-native-gsg/)**  
The native getting started guide will walk you through the basics of setting up your development environment, initializing the SDK, and checking the user's entitlement. 
* **[Unity Development Getting Started](/documentation/platform/latest/concepts/pgsg-unity-gsg/)**  
The Unity getting started guide will walk you through the basics of setting up your development environment, initializing the SDK, and checking the user's entitlement. 
* **[Unreal Development Getting Started](/documentation/platform/latest/concepts/pgsg-unreal-gsg/)**  
The Unreal getting started guide will walk you through the basics of setting up your development environment and checking the user's entitlement. 

