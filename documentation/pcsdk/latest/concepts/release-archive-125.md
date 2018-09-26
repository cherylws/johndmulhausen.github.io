---
title: Changes in Version 1.25.x
---



## New Features for 1.25.x

* There are no new features in this release.


## API Changes

* There are no breaking API changes in this release.


## Bug Fixes

* Fixed a bug in typedef union ovrLayer\_Union\_ where ovrLayerEyeMatrix was missing from the union. Users who wanted to use this union but found that ovrLayerEyeMatrix was missing can now use it.


## Known SDK Issues

* There's a bug affecting the Guardian System API by which color set operations to the visualized grid don't work if they are called while the HMD is not being worn.

