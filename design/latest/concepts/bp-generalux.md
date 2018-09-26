---
title: General User Experience
---

The general user experience (UX) best practices focus on the basic interaction between users and your VR environment.

Allow the user to define their own **session duration**. VR requires a unique physicality that is absent in other display technologies, as users are wearing a device on their head and are often standing and/or moving their bodies. Developers should be mindful of the user’s need to take breaks from engaging with their content. Users should always have the freedom to suspend their game, then return to the exact point where they left off at their leisure. Well-timed suggestions to take a break, such as at save points or breaks in the action, are also a good reminder for users who might otherwise lose track of time. 

Incorporating **resting positions** into your VR experience may help minimize the fatigue users may feel during extended gameplay sessions.

The more time users accumulate in VR, the less likely they are to experience discomfort. This **learned comfort** is a result of the brain learning to reinterpret visual anomalies that previously induced discomfort, and user movements become more stable and efficient to reduce vection (we'll discuss vection in more detail in the [Locomotion](/design/latest/concepts/bp-locomotion/) section of this guide).

1. Developers who test their own games repeatedly are often more resistant to discomfort than new users. We strongly recommend always testing apps with a novice population with a variety of susceptibility levels to VR discomfort to assess how comfortable the experience will be for a wide audience of users.
2. Users should not be thrown immediately into intense game experiences. Start with more sedate, slower-paced interactions that ease them into the game.
3. Apps that contain intense virtual experiences should provide users with warning of the content in the game so they may approach it as they feel most comfortable.


Optimize your application for short **load times**. Loading screens or interstitials in VR may be unavoidable, but users should experience them for as brief an amount of time as possible. Unlike traditional games or applications where users can do something else during a loading screen, such as check their phone or get a drink of water, VR users are captive to your loading experience. When you do have to show a loading screen, we recommend loading a 3D overlay cubemap. This provides a better experience for a user during the loading process with a minimal amount of development required. 
