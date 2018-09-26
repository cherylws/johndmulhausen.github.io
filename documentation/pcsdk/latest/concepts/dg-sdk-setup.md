---
title: Oculus Rift SDK Setup
---

This section describes how to set up the SDK.

## Installation

The latest version of the Oculus SDK is always available from the Oculus Developer Center.

To download the latest package, go to [https://developer.oculus.com/downloads/native-windows/](/downloads/native-windows/).

SDK versions use a **major**.**minor**.**patch** format. For example, 5.0.1 means Major 5, Minor 0, Patch 1.

## Compiler Settings

The LibOVR libraries do not require exception handling or RTTI support. 

Your game or application can disable these features for efficiency.

## Build Solutions

Developers can rebuild the samples and LibOVR using the projects and solutions in the Samples and LibOVR/Projects directories.

### Windows

Solutions and project files for Visual Studio 2010, 2012, 2013, 2015, and 2017 are provided with the SDK. Samples/Projects/Windows/VSxxxx/Samples.sln is the main solution that allows you to build and run the samples, and LibOVR itself.
