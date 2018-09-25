---
title: Audio SDK 0.11 Release Notes
---
This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Audio SDK.

## 0.11.3

## Bug Fixes

* Fixed spurious warnings in debug output window.
## 0.11

## Overview of Major Changes

This release introduces the OculusHQ spatializer provider, which combines the quality of the former High Quality Provider with the performance of the Simple Provider. Plugins no longer require the selection of HQ or Simple paths. Old implementations use OHQ by default, with reflections enabled. 

## New Features

* Minor VST changes.
* Added AAX.
* Added Wwise 2015.1 support.
* Improved PC and Android performance.
## Known Issues

* FastPath is currently not supported for Android. As of this release, it cannot be disabled in Unity 5.1 which will cause intermittent audio issues. To workaround this, use Unity 4.6 until the next 5.1 patch release. 
