# Overview

Welcome! This package collects the resources provided at [this link](https://linker.itch.io/adventure-tiles) and sorts them into easily-accessible objects.

All you need to do is clone/download this repository, and add the asset pack you purchased to `sprites/linker/img/tiles.png`. This gives you access to all of `LINKER`'s functionality in just a few steps.

We can break the entire process down as such:

* Slice the sprite sheet into equal-sized tiles
* Sort sprites into items (player cycles, vines, etc)
* Assign dictionary keys to each object

From there, you can access a set of related sprite pieces and frames to construct your object using the `LINKER` object created in `sprites/linker/assets.py`. **BUT** it's actually WAY easier than that! You don't have to access that dictionary at all, because every sprite has already been created. Instead, you can use the classes included in `assets.py` to create all your object. These classes include:

* Character (mechanics must be implemented on your own, but I handled the walk cycle!)
* NPC (this asset pack only contains a single NPC, the demon...or is it a fairy? Still not sure)
* Vines and signs whose dimensions may be set

