---
title: Distribution Options
---
Oculus provides several distribution options to meet the needs of your app and development process. This page will review the various forms of distribution supported by our platform.

Start by uploading your app binary to the [Oculus Dashboard](https://dashboard.oculus.com/), a section of the Oculus Developer Center. Once uploaded, you can choose from the following three distribution methods, each with differences in the review processes and the abilities granted to you:

* Oculus Store
* Oculus Keys
* Release Channels
## Oculus Store

The Oculus Store is where your app is available publicly for download. It is the most straightforward method of distribution, but requires a thorough review of your app by Oculus. To distribute an app in this form, you will need to upload your app to the dashboard and submit it for review by our Store team. They will examine your app to ensure it meets the technical and content criteria outlined in [Designing for Distribution](/distribute/latest/concepts/publish-prep-app/). Once your app passes this review, it will appear in the Oculus Store in one of the following sections:

* Apps: utility applications such as video players and creativity tools.
* Games: interactive content with rules where the player can either win or lose.
* Entertainment: narrative-driven experiences that may be minimally or fully interactive, but lack the ruleset and win/lose state of a game.
* Early Access: content that is interesting, playable, and well on its way to being finished. This category provides a means for developers to charge for their work-in-progress, while giving early users the chance to be a part of the development process.
Any app that passes our review process is also granted the ability to generate Oculus Keys. We'll outline the submission and review process on the [App Distribution](/distribute/latest/concepts/publish-intro/ "This guide answers common questions about publishing and distributing apps and describes the operation of the Oculus Store.") page. 

## Oculus Keys

Oculus Keys are 25-letter-long download codes that you can generate as needed. Once you are granted the ability to generate Oculus Keys, generating and distributing the key allows users to download your app by entering the key into the **Redeem Code** section in the Oculus app. You may distribute the keys however you like, sell them, give them away, or print them out and distributing them offline. Keys can be useful, for instance, for giving out review copies to media.

You can request to distribute an app only through keys and not through the store. This is useful for enterprise-use apps, apps intended for attendees of a certain event, or other apps that require limited availability. You can request for keys-only reviews by going to your app dashboard and entering “Please review for keys only” in the **Message For Reviewers** text field before submitting.

In some instances, apps that do not meet our technical or quality standards are also designated as “keys only” applications. In these cases, we encourage you to use keys to solicit additional user feedback and further test their VR application before resubmitting for review.

To create Oculus Keys:

1. Log on to [https://dashboard.oculus.com](https://dashboard.oculus.com/).
2. On the My Apps page, hover the mouse over an app that has already been reviewed by Oculus and approved for release or key generation, and click Edit Details.
3. Click the Oculus Keys tab and then follow the on-screen instructions.
You can generate single keys or many in bulk. After you have obtained Oculus keys for your app, you can distribute the keys yourself or through other stores and websites such as [Amazon's Digital Software store](https://developer.amazon.com/mac-pc).

## Oculus Release Channels

Release Channels are another form of limited distribution and useful while your app is in development.

When you upload your app to the Developer Dashboard, you are given the choice of uploading into several “channels”, with names like STORE, ALPHA, BETA, and RC. With the exception of the STORE channel, you can grant or revoke user-level access to each by adding or removing a test user’s email address (tied to their Oculus ID) to or from specific channels. We'll review release channels in more detail in the [Release Channels](/distribute/latest/concepts/publish-release-channels/ "Release channels let you distribute early versions of your builds to limited audiences for testing or other purposes. You can invite different groups of people to different channels. When you are confident your app is ready for release, you can copy your build to the Store channel and then submit it for Oculus Store review.") section.

Note: STORE is a special channel which should be used only when submitting your app for Store review.Each Release Channel can have up to 100 users assigned to them. Since distribution through release channels do not require review, it comes in handy when you want to share your app with friends, or run a limited beta test.

When your app is ready for distribution to the general public, you copy it to the Store release channel and submit it to us for consideration.

## Off-Platform Distribution (Sideloading)

You can distribute your app outside the Oculus platform by a method known as "sideloading". To run such apps, users must enable Unknown Sources in the Settings menu of the Oculus app. See [Games and Apps From Unknown Sources](https://support.oculus.com/878170922281071).

Such builds are not updated through our platform. They do not appear in anyone's Oculus Home Libraries or have access to any other Oculus features or services.

Note: Off-platform builds must still meet our SDK license requirements. In particular, all reserved functions called out in the SDK license, such as home button functionality and menu operation, must be respected.