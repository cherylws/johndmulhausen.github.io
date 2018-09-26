---
title: Installing to the Wwise Authoring Tool
---

Installing the OSP plugin for Wwise lets you add the Oculus Spatializer as a Wwise Mixer Plug-in to use in your soundbanks.

## Installing on Windows

1. Navigate to the download package folder that matches your version of Wwise.
2. If installing on 64-bit Windows, copy \x64\bin\plugins to Audiokinetic\Wwise{version}\Authoring\x64\Release\bin\plugins
3. If installing on 32-bit Windows, copy \Win32\bin\plugins to Audiokinetic\Wwise{version}\Authoring\Win32\Release\bin\plugins


## Installing on macOS

The Oculus Native Spatializer plugin for macOS is only compatible with Wwise 2016.

1. Open the Finder, and then go to the Applications/Audiokinetic/Wwise{version} folder where {version} is your Wwise 2016 version, for example: 2016.2.6098.
2. Control-click **Wwise.app**, and then select **Show Package Contents**
3. Go to the Contents/SharedSupport/Wwise2016/support/wwise/drive\_c/Program Files/Audiokinetic/Wwise/Authoring/Win32/Release/bin/plugins folder. This is your Wwise.app /plugins folder.
4. From a new Finder window, copy the contents of the Wwise2016/Win32/bin/plugins folder to the Wwise.app /plugins folder.
5. Open the Terminal application.
6. Enter cd /Applications/Audiokinetic/Wwise\ {version}/Wwise.app/Contents/SharedSupport/Wwise2016 where {version} is your Wwise 2016 version. Be sure to preserve the space in /Wwise\ {version}/.
7. Enter CX\_ROOT=/Applications/Audiokinetic/Wwise\ {version}/Wwise.app/Contents/SharedSupport/Wwise2016 WINEPREFIX=/Applications/Audiokinetic/Wwise\ {version}/Wwise.app/Contents/SharedSupport/Wwise2016/support/wwise ./bin/wineprefixcreate --snapshot where {version} is your Wwise 2016 version.

