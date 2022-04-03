## spritesheet.py

Spritesheet dissects an image into a 2D array of equally-sized sprites. Members of a Spritesheet may be accessed with `__getitem__` so you can focus on filtering the sheet into an appropriate data structure.

```python
from sprites import Spritesheet
import pygame

# The dimensions of an individual tile or sprite
width = 10
height = 15

img = pygame.image.load("path/to/img.png")

ss = Spritesheet(img, width, height)
```

A Spritesheet may be scaled up.
```python
ss.scale(width=2)
ss.scale(height=3)
ss.scale(2, 3)  # Scale both
```

This must be done *before* adding sprites to a reference.

Dimensions according to scale can be retrieved.
```python
dim = ss.get_size()
width = ss.get_width()
height = ss.get_height()
```
