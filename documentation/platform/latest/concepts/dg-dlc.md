---
title: DLC and Asset Files
---

Downloadable Content, or DLC, and Asset Files allow you to add whole new experiences, characters, levels, and more to your app for sale that you may not have included as part of the original experience. 

DLC also offers the ability to manage the size of your initial download. Instead of downloading and installing a large package at the initial download, you can use DLC to download later content as a user proceeds in a game. Apps that use DLC or Asset Files must identify themselves as **Internet connection required** in the App Specifications.

## Engine Support

Unity and Unreal have built-in support for DLC and are directly compatible with the Asset Files on the Oculus Mobile Platform. Please refer to the following pages for more information:

* [AssetBundles](https://docs.unity3d.com/Manual/AssetBundlesIntro.html) in Unity
* [Packaging Projects](https://docs.unrealengine.com/en-us/Engine/Basics/Projects/Packaging) in Unreal


## Define your DLC IAP (if paid)

First, you'll need to define your paid DLC as an IAP item on the Oculus Platform. Please see the [Commerce (IAP)](/documentation/platform/latest/concepts/dg-iap/) page for information about defining IAP.

## Uploading a Binary with DLC or Asset Files

To upload your binary with DLC, you’ll need to use the CLI uploader, and not the Web UI. 

1. Download and install the utility found on the [Oculus Platform Command Line Utility](https://dashboard.oculus.com/tools/cli) page.
2. Upload your build with the supported asset files.* Add --assets\\_dir to your upload command to indicate that this package contains DLC/Asset Files. Youâ€™ll need your App Id and App Secret, review the S2S page for information about using the App Id and Secret. For example: ovr-platform-util upload-mobile-build -a &lt;app-id&gt; -s &lt;app-secret&gt; --apk &lt;path-to-apk&gt; --assets\\_dir &lt;path-to-dir-with-dlcs&gt; -c &lt;channel&gt; * If you plan to sell the DLC, then also add --asset\\_file\\_iap\\_configs where you can identify the DLC object. For example:--asset\\_file\\_iap\\_configs '[{"filename": "Asset1.obb", "sku": "Asset1\\_IAP"}, ...]'Alternately, you can also append --asset\\_file\\_iap\\_configs\\_file which is a path to a file containing the JSON config. Note that the SKU must equal the SKU you defined on the Dashboard in the previous section. 


3. Manage your app on the Dashboard. Navigate to &lt;https://dashboard.oculus.com/&gt;, Select **Manage Builds** from the nav, then **View Expansion Files** for the build you just uploaded.


## Integrate DLC or Asset File Support

**Handling downloads initiated in the Oculus App**

To check and install items purchased in the Oculus App.

1. On startup, call ovr\_AssetFile\_GetList to retrieve a list of available asset files. The array returned contains information about the iap\_status and download\_status.
	1. The iap\_status will be one of the following: free, entitled, or not-entitled.
	2. The download\_status will be one of the following: installed meaning you can mount the file, available meaning you can download the file, or in-progress meaning the file is being downloaded or is installing.
	
2. If there is a file that is available to download, iap\_status = free or entitled, and download\_status = available, you can initiate the download by calling ovr\_AssetFile\_DownloadById using the ID returned by the initial GetList call.
3. You'll receive an immediate DownloadResult response with the path to the asset as a confirmation that the request was successful. You should also listen for DownloadUpdate notifications which return info about transferred bytes, and a complete flag that notifies you when the download is complete.


**Initiating purchase and downloads in-app**

To allow users to initiate the download in-app, either purchased or free. Alternatively, these steps can be used to install an expansion file at a certain point in your app. For example, you only want to make the user download the first 2 levels of your game, then install the 3rd and 4th when needed. 

1. Call ovr\_AssetFile\_GetList to retrieve a list of available asset files. The array returned contains information about the iap\_status and download\_status.
	1. The iap\_status will be one of the following: free, entitled, or not-entitled.
	2. The download\_status will be one of the following: installed meaning you can mount the file, available meaning you can download the file, or in-progress meaning the file is being downloaded or is installing.
	
2. (Non-Free DLC Only) Use the [Commerce (IAP)](/documentation/platform/latest/concepts/dg-iap/ "In-app purchases (IAP) allow users to purchase items without leaving your app.") APIs to allow the user to complete the purchase flow. Call ovr\_IAP\_LaunchCheckoutFlow with the SKU you defined. 
3. Call ovr\_AssetFile\_DownloadById() to initiate the download, passing the file name of the DLC/Asset File you defined at upload.
4. You'll receive an immediate DownloadResult response with the path to the asset as a confirmation that the request was successful. You should also listen for DownloadUpdate notifications which return info about transferred bytes, and a complete flag that notifies you when the download is complete.

