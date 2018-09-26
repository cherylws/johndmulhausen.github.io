---
title: Unreal Development Getting Started
---

The Unreal getting started guide will walk you through the basics of setting up your development environment and checking the user's entitlement. 

Using the Platform SDK is a bit different than using the SDK in other development environments. Different Platform features will be invoked in different ways either by using OSS Blueprints, Oculus Blueprints, or the native C APIs. Each of the feature pages in the Developer Guide will detail how to use the feature.

Header files for the Oculus OSS APIs can be found once you build your dev environment in Visual Studio (`Engine &gt; UE4 &gt; Plugins &gt; Online &gt; OnlineSubsystemOculus &gt; Source &gt; Private`).

## Create an App

Before you can integrate the Platform SDK, you'll need to create an app if you have not done so already. To create an app see the information on the [Creating and Managing Apps](/documentation/publish/latest/concepts/publish-create-app/) page.

## Configure Your Development Environment

First, review the basic Oculus onboarding for Unreal development, found in the [Unreal](/documentation/unreal/latest/concepts/unreal-engine/) guide. Once you’re comfortable with using Unreal to develop Oculus apps, you can start to implement Platform features.

There are two steps to configuring your development environment.

First, enable the Online Subsystems (OSS) Plugin. To enable the OSS plugin, select **Edit &gt; Plugins &gt; Online Platform &gt; Online Subsystem Oculus**, and check **Enabled**. You will be prompted to restart Unreal Editor. 

Then, to access Oculus Platform features through Online Subsystems, you must adjust your `defaultEngine.ini` file to use Oculus:

```
[OnlineSubsystem]
DefaultPlatformService=Oculus
                
[OnlineSubsystemOculus]
bEnabled=true
OculusAppId=&lt;app_id_here&gt;
```

Where `&lt;app_id_here&gt;` is the unique App Id you've retrieved from the [API](https://dashboard.oculus.com/app/api/) page on the Oculus Dashboard.

```
[OnlineSubsystemOculus]
RiftAppId= &lt;rift app id here&gt;
GearVRAppId= &lt;gear vr app id here&gt;
```

**Additional Gear VR Configuration**

If you're building an app for Gear VR, you'll also need to add the following to `AndroidEngine.ini`.

```
[OnlineSubsystem]
DefaultPlatformService=Oculus
```

## Configuring Your App for Local Development

The configuration steps in this section will allow developers to run local builds of the application during the development process. This process is required, otherwise local versions of the app will not pass the entitlement check that you'll integrate below.

1. Add the user(s) to your org. See the [Manage Your Organization and Users](https://developer.oculus.com/distribute/latest/concepts/publish-account-management-intro/) for information about managing your organization.
2. If some of your developers are not part of the application's organization, and they need to run your application outside the normal install directory. Add the registry key AllowDevSideloaded as DWORD(1) to the registry folder at HKLM\SOFTWARE\Wow6432Node\Oculus\OculusThis does not bypass having a valid entitlement, it just bypasses the directory check.


Once the steps above are completed the entitlement check will succeed when running a local build of your application.

## Using OSS

Several Oculus Platform features may be accessed through Unreal’s Online Subsystems (OSS) interface in Unreal Engine 4.19. For more information on available UE4 versions and compatibility, see our [Unreal Engine](/documentation/unreal/latest/concepts/unreal-engine/) page.

For each supported feature, only a subset of functionality may be exposed by the Online Subsystems interface. Developers who wish to use Platform features not available through Online Subsystems should code against the native C headers located in `Engine\Source\ThirdParty\Oculus\LibOVRPlatform` and include them in their build. We’ll review how to do that in the next section.

Each Platform feature in the [Developer Guide](/documentation/platform/latest/concepts/book-dg/) will have specific instructions about how to use that feature in Unreal.

You can read more about the OSS interface in Epic’s [Online Subsystem Overview](https://docs.unrealengine.com/latest/INT/Programming/Online/). Some features listed there may not be available for use on Oculus. 

## Using the Native C APIs in Unreal

Some features aren’t available in OSS, or you may want to use a more custom implementation of a feature than is currently available in OSS. You can use any `ovr_*` API with the Oculus OSS directly for anything that isn't covered by the OSS Interface.

First, you'll add the required modules to your app build.cs file. You only need to do this once for all Platform features.

```
using UnrealBuildTool;

public class OculusPlatformSample : ModuleRules
{
	public OculusPlatformSample(ReadOnlyTargetRules Target) : base(Target)
	{
		PublicDependencyModuleNames.AddRange(new string[] 
		{ 
                        ...
			"LibOVRPlatform",
		});
		
		PrivateDependencyModuleNames.AddRange(new string[]
		{
			"OnlineSubsystem",
			"OnlineSubsystemOculus",
		});
	}
}
```

Then you can use OSS to call the native C APIs by adding code similar to the following example to your app. This example demonstrates how to call `ovr_User_GetAccessToken()` to retrieve an access token for use with the Oculus REST APIs.

```
include OnlineSubsystemOculus.h

........

void GetAccessToken()
{
	ovrRequest RequestId = ovr_User_GetAccessToken();
	FOnlineSubsystemOculus* OSS = static_cast&lt;FOnlineSubsystemOculus*&gt;(IOnlineSubsystem::Get());
	OSS-&gt;AddRequestDelegate(Req     uestId, FOculusMessageOnCompleteDelegate::CreateLambda([this](ovrMessageHandle Message, bool bIsError)
	{
		Test.TestFalse(TEXT("Was not Successful"), bIsError);
			
		UE_LOG(LogEngineAutomationTests, Display, TEXT("Access Token: %s"), *FString(ovr_Message_GetString(Message)));

		bIsCompleted = true;
	}));
}
```

## Checking the Entitlement

One of the first things you must do when a user launches your app is verify that they own a legitimate copy of your app.

In Unreal, this is as simple as adding a blueprint. In the Oculus OSS plugin you enabled earlier there is a `Verify Entitlement` node. Add this action to your blueprint.

For example, in our OculusPlatformSample that ships in the Platform SDK we check the entitlement in the `OSSIdentityActor_Blueprint`:



![](/images/documentationplatformlatestconceptspgsg-unreal-gsg-0.png)



**What is the Entitlement Check?**

Verifying that the user is entitled to your app is required to sell an app on the Oculus Store. This check verifies that the copy of your app is legitimate. The entitlement check does not require the user to be connected to the Internet. In the event of a failed check, you should handle the situation in your app. For example, show the user an error message and quit the app. A failed entitlement check won’t result in any action on its own.

Additional user verification is available if you want to verify the identity of the user to your back-end server. [User Verification](/documentation/platform/latest/concepts/dg-ownership/) provides a cryptographic nonce you can pass to verify that the user's identity. This method does not replace the entitlement check. 

Entitlement verification is required to distribute apps through the Oculus Store.
