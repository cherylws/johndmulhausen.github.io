---
title: OSP Version Migration in FMOD
---



To migrate to a new version of the Oculus Spatializer Plugin for FMOD, it is recommended to follow these steps:

1. Copy the new version of OculusSpatializerFMOD.dll from the Audio SDK over the existing version in the Plugins folder of your FMOD Studio project directory.
2. If the Plugins folder contains a file named ovrfmod.dll, delete it and copy OculusSpatializerFMOD.dll into the folder.
3. Copy the new OculusSpatializerFMOD.dll (32-bit or 64-bit, as appropriate) from the Audio SDK over the existing versions in your application directory.
4. Open your FMOD Studio project and build sound banks.
5. Launch your application and load the newly built banks.

