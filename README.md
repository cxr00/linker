# Overview

Welcome! This package collects the resources provided at [this link](https://linker.itch.io/adventure-tiles) and sorts them into easily-accessible objects.

All you need to do is clone/download this repository, and add the asset pack you purchased to `sprites/linker/img/tiles.png`. This gives you access to all of `LINKER`'s functionality in just a few steps.

What I've done can be broken down into a few harder-than-they-seem steps:

* Slice the sprite sheet into equal-sized tiles
* Sort sprites into items (player cycles, vines, etc)
* Assign dictionary keys to each object (that's what `assets.py` does)
* Create classes for each sprite (as seen in `sprites.linker`)
* Add expected behavior (vine growth, player movement, animation frames) to each class

As you'll notice from those last two steps, I've made it WAY easy to use the assets in Linker's tileset. All you have to do is import the pre-made objects directly from `sprites` and use the pre-built functionality for each sprite's typical behavior. Keep reading for a breakdown of each of the available objects.

This README should have everything you need to work with this library, so I highly recommend putting it somewhere that's easy to find so you have a reference while you learn to use it.

You can see a sample of how this library works by running the `__main__` file in the top directory.

## Important note for new coders

Because you didn't write this library yourself, you're not going to be an expert on its ins and outs right away. And that's okay! I just want to warn you that there's a big chance that you'll encounter errors due simply to misspelling words somewhere in your code.

The most common error you will encounter using this library is a `KeyError`. If you are constructing tiles and objects and a `KeyError` gets thrown at you, then the error is *most likely* in the line of code where you set the type of a particular LinkerSprite. Make sure to look at the *top* of the stack trace (the red error message), and it will tell you what line you potentially mistyped something on.

You may also encounter a `ValueError` if you mistype "pico-8" or "nes" when setting the palette, but it's an easy fix! Just remember to look at the *top* of the stack trace first to find code you recognize as your own.

Best of luck! Adventure awaits!

# LinkerSprites

Every sprite which is implemented is based on the `LinkerSprite` class contained in `sprites.linker.base.py`. The important methods are as follows:

* `shift_palette()`: Changes whether the sprite is using the "pico-8" or "nes" palette
* `set_palette(palette)`: Explicitly sets the palette to either "pico-8" or "nes"
* `get_size()`: Gets the size of the pygame surface associated with the sprite
* `get_rect()`: Creates a Rect based on the Sprite's current position
* `colliderect(other_rect)`: Determines whether the sprite collides with a given rect
* `draw(surface)`: Draws the sprite to the desired surface

Every sprite in this library inherits these methods without changing them, so you can expect consistent behavior across all LinkerSprites. `get_rect` and `colliderect` are intentionally made to function as close to pygame's Sprites as possible.

## ScalableSprites

There are two types of sprite which can be of varying size of at least 2x2: the Scroll and Bang classes. They are constructed like so:

```python
from sprites import Scroll, Bang

scroll = Scroll(width=3, height=2, palette="nes", pos=(100, 100))
bang = Bang(width=2, height=5, palette="pico-8", pos=(10, 250))
```

They can be used as UI elements for text, dialogue, maps, inventory, you name it!

## The Player

The Player sprite is the most complex sprite built by the spritesheet. But don't worry, I've done my best to make it as easy to read and understand as possible.

```python
from sprites import Player

player = Player(palette="nes")  # It's really that easy!
player.change_state("walk")  # The default state is 'idle'
```

The Player has four states: `fade`, `idle`, `walk`, and `fall`.

Player direction can be set with `player.turn_left()` and `player.turn_right()`.

In order to animate the player, you must use `player.tick()`. It is programmed to play one animation frame every 5 ticks, which works well for an FPS of 60. If you use a lower or higher FPS, you can change `player.tick_rate` to whatever suits your purposes:

```python
player.tick_rate = 6  # Slightly slower animation speed
```

## Environment

These LinkerSprites are tiles meant for use in building the environment the player traverses. Remember that you can always specify `palette` and `pos` as keyword arguments.

```python
from sprites import Filler, Hole, Tile, CrossTile, BrickTile, Accent, Stairs,\
    Button, Chest, Pot, Statue, Plinth

filler = Filler(tile_type=0)  # Tile type between 0 and 2
hole = Hole()

# Possible tile types:
# "smooth1", "smooth2", "facade1", "facade2", "cracked1", "cracked2", "pillar1", "pillar2"
tile = Tile(tile_type="smooth1")

cross_tile = CrossTile(tile_type=0)  # between 0 and 3
brick_tile = BrickTile(size="small", shade="dark")  # "small" or "big" size, "dark" or "light" shade
accent = Accent(accent_type="grey")  # grey/gray, black, light, dark
stairs = Stairs(stair_type=0)  # 0 or 1

button = Button()
chest = Chest()  # Use chest.open() and chest.close() to change state
pot = Pot()  # Use pot.fill() and pot.empty() to change state

# Statues are made up of two tiles that are automatically put together for you
statue = Statue(statue_type="horns1")  # horns1, horns2, eye1, eye2, a1, a2

# Plinths also contain two tiles, but are constructed horizontally rather than vertically
plinth = Plinth(plinth_type=0)  # 0 or 1
```

The last of the environment sprites, which is a bit more complex, is the `Vine` class:

```python
from sprites import Vine

vine = Vine(height=1, palette="pico-8", pos=(100, 100))

vine.grow()  # Increase the height of the vines by 1
vine.shrink()  # Decrease the height of the vines by 1
```

When using the `Vine.draw` method, the position where it will be drawn is *relative to the upper-left corner of the base*, rather than the top-left of the vines themselves. This means that you don't have to manually recalculate the position of the vines if you want them to grow and shrink dynamically.

All of these sprites have `colliderect` but you'll have to implement the behavior which results from collisions yourself. But in general, Chest, Pot, Statue, Plinth, and Accent objects cannot be walked over, as well as the `facade` and `pillar` Tiles.

## Items

Several Items have unique behavior, so in lieu of a simple list, I will demonstrate them all in code:

```python
from sprites import Pencil, Bomb, Key, Sack, Gem, Pearl, Relic, Ink

pencil = Pencil(color="blue")  # Or red
pencil.change_color()  # Changes blue to red and vice versa
pencil.set_color("blue")  # Explicitly set color

bomb = Bomb()
bomb.tick()  # Ticks at a rate of 1 animation frame per 5 frames; set manually with bomb.tick_rate

# No special sprite behavior
key = Key()
sack = Sack()
gem = Gem()
pearl = Pearl()
relic = Relic()

ink = Ink(color="red")  # Or blue
ink.change_color()  # Swaps color
ink.set_color("blue")  # Explicitly set color

# Ink level is between 0 and 6
# If an invalid number is specified, an error is raised
ink.set_level(2)

ink.fill()  # Set the level to 6
ink.empty()  # Set the level to 0
```

## Miscellaneous

The final sprites are objects which don't really fit in anywhere else.

```python
from sprites import Hand, Dust, Shadow

hand = Hand()  # Can be used for tutorials or even for point-and-click style gameplay
hand.set_state("grab")  # States are "point" and "grab"; default state is point

dust = Dust()  # Simple particle effect
dust.tick()  # Tick rate set at default of 7

shadow = Shadow() # Undershadow for items on the overworld
```
