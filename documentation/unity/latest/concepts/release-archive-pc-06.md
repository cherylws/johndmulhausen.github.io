---
title: 0.6 PC Unity Integration Release Notes
---
This document provides an overview of new features, improvements, and fixes included in the Oculus Unity Integration that shipped with 0.6 of the Oculus PC SDK.

## PC Unity Integration 0.6.0.0

## New Features

* Disabled eye texture anti-aliasing when using deferred rendering. This fixes the black screen issue.
* Eliminated the need for the DirectToRift.exe in Unity 4.6.3p2 and later.
* Removed the hard dependency from the Oculus runtime. Apps now render in mono without tracking when VR isn't present.
