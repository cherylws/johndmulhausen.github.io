---
title: Unity-SDK Version Compatibility
---

This reference describes the relationship between Unity versions, Oculus PC and Mobile SDKs, and Oculus Unity plugin and Utilities packages.

We currently support Unity 5.6.x, 2017.1.x, 2017.2.x, 2017.3.x, 2017.4.x, 2018.1.x, and 2018.2.x. Our [Release Notes](/documentation/unity/latest/concepts/release-archive/) describe known issues with any version.

We recommend using Unity version 2017.4.11f1 for all Oculus development.

If you must use a different version, our tests show that the following builds have the best performance and least number of issues for that version.

* 5.6.6f2* (Does not support Dash)
* 2017.1.4f1*
* 2017.2.3p4
* **2017.4.11f1 (Most recommended)**
* 2018.1.9f2*
* 2018.2.7f1
 *No longer supported by Unity. 

The following chart describes which Oculus SDKs are included in each OVRPlugin version, and which Oculus SDKs they utilize. Any Unity version may be updated to a later version of Oculus support by importing the Utilities package. OVRPlugin is released first with Utilities for Unity, and is typically bundled in the next Unity Editor version one to three weeks later. For more information, see [OVRPlugin](/documentation/unity/latest/concepts/unity-utilities-overview/#unity-utilities-ovrplugin). 

| Release Date | Utilities Version | OVRPlugin Version | PC SDK | Mobile SDK |             Min. Required Unity Version             |
|--------------|-------------------|-------------------|--------|------------|-----------------------------------------------------|
|  12/14/2017  |      1.21.0      |      1.21.0      | 1.19.0 |   1.11.0   |   2017.3.x.2017.2.x, 2017.1.p5, 5.6.4p2 or later   |
|  11/14/2017  |      1.20.0      |      1.20.0      | 1.19.0 |   1.9.0   | 2017.2.x, 2017.1.p5, 5.6.x, 5.5.x, 5.4.4f1 or later |
|  10/26/2017  |      1.19.0      |      1.19.0      | 1.17.0 |   1.9.0   | 2017.2.x, 2017.1.p5, 5.6.x, 5.5.x, 5.4.4f1 or later |
|  9/15/2017  |      1.18.1      |      1.18.1      | 1.17.0 |   1.8.0   |      2017.1.p5, 5.6.x, 5.5.x, 5.4.4f1 or later      |
|  9/14/2017  |      1.18.0      |      1.18.0      | 1.18.0 |   1.8.0   |      2017.1.p5, 5.6.x, 5.5.x, 5.4.3p4 or later      |
|  6/29/2017  |    1.16.0-beta    |      1.16.0      | 1.16.0 |   1.6.0   |           5.4.3p4 or later, 5.5.x, 5.6.x           |
|   6/3/2017   |      1.15.0      |      1.14.1      | 1.15.0 |   1.5.0   |           5.4.3p4 or later, 5.5.x, 5.6.x           |
|   5/2/2017   |      1.14.0      |      1.14.0      | 1.14.0 |   1.5.0   |           5.4.3p4 or later, 5.5.x, 5.6.x           |

## Legacy Compatibility

This section describes Oculus SDK and Integration compatibility with Unity Editor versions prior to the Oculus 1.14.0 release, when we began shipping OVRPlugin in the Utilities for Unity package. 

## Utilities for Unity 5.x Versions

| Release Date | OVRPlugin / Utilities | PC SDK | Mobile SDK |             Unity             |
|--------------|-----------------------|---------|------------|-------------------------------|
|   4/8/2017   |        1.13.0        | 1.13.1 |   1.5.0   |       5.6.0p3 or later       |
|  4/25/2017  |        1.13.0        | 1.13.1 |   1.5.0   |       5.5.3p2 or later       |
|  4/27/2017  |        1.12.0        | 1.12.0 |  1.0.4.5  |       5.4.5p1 or later       |
|  3/30/2017  |        1.13.0        | 1.12.0 |  1.0.4.5  |       5.6.0f3 or later       |
|  3/30/2017  |        1.13.0        | 1.12.0 |  1.0.4.5  |       5.5.2p3 or later       |
|  3/30/2017  |        1.13.0        | 1.12.0 |  1.0.4.5  |       5.4.5f1 or later       |
|  3/10/2017  |        1.12.0        | 1.12.0 |  1.0.4.5  |       5.5.2p3 or later       |
|  3/10/2017  |        1.12.0        | 1.12.0 |  1.0.4.5  |       5.4.5f1 or later       |
|  3/10/2017  |        1.12.0        | 1.12.0 |  1.0.4.5  | 5.3.8f1 or later (deprecated) |
|   2/1/2017   |        1.11.0        | 1.11.0 |  1.0.4.5  |       5.5.1p2 or later       |
|   2/8/2017   |        1.11.0        | 1.11.0 |  1.0.4.5  |       5.4.4p3 or later       |
|   2/1/2017   |        1.11.0        | 1.11.0 |  1.0.4.5  | 5.3.7p4 or later (deprecated) |
|  11/28/2016  |        1.10.0        | 1.10.0 |   1.0.4   |       5.5.0p1 or later       |
|  11/28/2016  |        1.10.0        | 1.10.0 |   1.0.4   |       5.4.3p3 or later       |
|  11/28/2016  |        1.10.0        | 1.10.0 |   1.0.4   |       5.3.7p2 or later       |
|  11/1/2016  |         1.9.0         |  1.9.0  |   1.0.4   |       5.4.2p2 or later       |
|  11/1/2016  |         1.9.0         |  1.9.0  |   1.0.4   |       5.3.6p8 or later       |
|  9/15/2016  |         1.8.0         |  1.8.0  |   1.0.3   |       5.4.1p1 or later       |
|  9/15/2016  |         1.8.0         |  1.8.0  |   1.0.3   |       5.3.6p5 or later       |
|  8/18/2016  |         1.7.0         |  1.7.0  |   1.0.3   |       5.4.0p3 or later       |
|  8/18/2016  |         1.7.0         |  1.7.0  |   1.0.3   |       5.3.6p3 or later       |
|  7/28/2016  |         1.6.0         |  1.5.0  |   1.0.3   |       5.4.0b16 or later       |
|  7/28/2016  |         1.6.0         |  1.6.0  |   1.0.3   |       5.3.6p1 or later       |
|  6/30/2016  |         1.5.0         |  1.5.0  |   1.0.3   |      5.4.0b16 and later      |
|  6/30/2016  |         1.5.0         |  1.5.0  |   1.0.3   |       5.3.4p5 and later       |
|  4/20/2016  |         1.3.2         |  1.3.2  |  1.0.0.1  |      5.4.0b11 and later      |
|  4/20/2016  |         1.3.2         |  1.3.2  |  1.0.0.1  |       5.3.3p3 and later       |
|  3/28/2016  |         1.3.0         |  1.3.0  |  1.0.0.1  |            5.3.4p1            |
|  10/30/2015  |     0.1.3.0 Beta     | 0.8.0.0 |  0.6.2.0  |            5.2.2p2            |
|  10/1/2015  |     0.1.2.0 Beta     | 0.7.0.0 |  0.6.2.0  |            5.2.1p2            |
|   7/6/2015   |     0.1.0.0 Beta     | 0.6.0.1 |   0.5.0   |             5.1.1             |

## Unity 4.x Integration Versions

| Release Date | Integration | PC SDK | Mobile SDK |  Unity  |
|--------------|-------------|---------|------------|---------|
|  3/28/2016  |    1.3.0    |  1.3.0  |  1.0.0.1  | 4.7.0f1 |
|  10/30/2015  |   0.8.0.0   | 0.8.0.0 |   1.0.0   | 4.6.9p1 |
|  9/08/2015  |   0.6.2.0   | 0.7.0.0 |  0.6.2.0  | 4.6.7+ |
|  8/14/2015  |   0.6.1.0   | 0.6.0.1 |  0.6.1.0  | 4.6.7+ |
|   8/7/2015   |   0.6.0.2   | 0.6.0.1 |  0.6.0.1  |  4.6.7  |
|  6/25/2015  |  D 0.6.0.1  | 0.5.0.1 |  0.6.0.1  |   4.6   |
|  6/12/2015  |  M 0.6.0.1  | 0.5.0.1 |  0.6.0.1  |   4.6   |
|  5/15/2015  |  D 0.6.0.0  | 0.5.0.1 |   0.5.0   |   4.6   |
|  3/31/2015  |   M 0.5.0   | 0.5.0.1 |   0.5.0   |   4.6   |
|  3/26/2015  |  D 0.5.0.1  | 0.5.0.1 |   0.5.0   |   4.6   |
|  3/20/2015  |  M 0.4.3.1  |  0.4.4  |  0.4.3.1  |   4.5   |
|  2/27/2015  |   M 0.4.3   |  0.4.4  |   0.4.3   |   4.5   |
|  1/23/2015  |   M 0.4.2   |  0.3.2  |   0.4.2   |   4.5   |
|   1/7/2015   |   M 0.4.1   |  0.3.2  |   0.4.1   |   4.4   |
|  12/4/2014  |   D 0.4.4   |  0.4.4  |   0.4.0   |   4.6   |
|  11/12/2014  |   M 0.4.0   |  0.3.2  |   0.4.0   |   4.4   |
|  11/10/2014  |  D 0.4.3.1  | 0.4.3.1 |    N/A    |   4.5   |
|  10/24/2014  |   D 0.4.3   |  0.4.3  |    N/A    |   4.5   |
|   9/4/2014   |   D 0.4.2   |  0.4.2  |    N/A    |   4.5   |
|  8/11/2014  |   D 0.4.1   |  0.4.1  |    N/A    |   4.4   |
|  7/24/2014  |   D 0.4.0   |  0.4.0  |    N/A    |   4.4   |
|  5/22/2014  |   D 0.3.2   |  0.3.2  |    N/A    |   4.3   |
|  4/14/2014  |   D 0.3.1   |  0.3.1  |    N/A    |   4.3   |
|  10/10/2013  |   D 0.2.5   |  0.2.5  |    N/A    |   4.3   |
