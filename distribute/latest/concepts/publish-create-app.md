---
title: App Submission and Store Review
---
This guide will review the process to upload and submit an app to the Oculus Dashboard.

 Before you can upload an app, you'll need to define your app on the Oculus Dashboard (and create your Organization if you have not done so already, see [Account Management](/distribute/latest/concepts/book-publish-account-management/)).## Creating an App Page

First, you'll need to create your Gear VR or Rift app page. Multi-platform apps need separate app pages for their Rift and Gear VR versions.

To create an app page in the Oculus Store:

1. Log on to the Oculus Developer Dashboard at [https://dashboard.oculus.com](https://dashboard.oculus.com/).
2. Click **Create New App**.
3. Select **Gear VR** or **Oculus Rift**
4. Enter the name of your app. The name is permanent and cannot be changed.
If you made a mistake naming your app, repeat the steps to create a new app using the correct name. You can delete the misnamed app from the **My Apps** page by clicking the **X** in the top-right corner of any app thumbnail.

## Grouping Apps (optional)

Group apps together that share settings to simplify management and deploy universal changes.

Create a grouping:

1. Log on to the Oculus Developer Dashboard at [https://dashboard.oculus.com](https://dashboard.oculus.com/). Choose the organization that contains the app grouping you would like to edit, open the **Settings** menu, and select **App Groupings**.
2. Click the **Create a New App Grouping** link. The Create App Grouping dialog box appears.
3. Enter a name and select **Submit**. The new group will appear in the list.
Add apps:

1. Hover over an app and select **Migrate** to another grouping. The Migrate Application dialog box appears.
2. Select a destination group and click **Submit**. The app is moved to the new group and will inherit its settings.
Change group settings:

1. Locate the App Grouping to update and select **Manage** to open the settings page for the App Grouping.
2. Update the desired setting for the group. The changes will be made for all apps within that grouping.
## Submit your App

The following pages will walk you through the app submission and upload process.

* **[App Upload and Store Submission](/distribute/latest/tasks/publish-submit-app-review/)**  
The process for distributing your app begins by uploading your build to the Oculus Dashboard.
* **[Uploading Gear VR and Go Apps](/distribute/latest/concepts/publish-uploading-mobile/)**  
Mobile apps have a stringent set of packaging requirements and any app you upload must be packaged accordingly. The upload validator rejects apps that do not meet these requirements.
* **[Uploading Rift Apps](/distribute/latest/concepts/publish-uploading-rift/)**  
 Rift apps are packaged as .zip files if uploading through the web interface. If uploading through the command line interface, your app is uploaded using its native file and folder structure. Uploads that do not meet these requirements are rejected by the upload validator. 
* **[Oculus Platform Command Line Utility](/distribute/latest/concepts/publish-reference-platform-command-line-utility/)**  
The Oculus Platform Command Line Utility lets you upload builds to your release channels much faster than using the Oculus dashboard web interface. It also allows you to incorporate automated uploads into your existing build system.
