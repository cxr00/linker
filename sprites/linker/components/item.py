from sprites.linker.components.base import LinkerSprite
from sprites.linker.components.assets import LINKER


class Item(LinkerSprite):
    """
    Items are special sprites which are contained in some sort of inventory
    """
    def __init__(self, item_type, palette="pico-8"):
        super().__init__(LINKER["item"][item_type], palette)
        self.item_type = item_type


class Pencil(Item):
    """
    A pencil has a case and a fill color, either blue or red
    """
    def __init__(self, palette="pico-8", color="blue"):
        super().__init__("pencil", palette)
        self.color = color

    def change_color(self):
        if self.color == "blue":
            self.color = "red"
        else:
            self.color = "blue"


class Bomb(Item):
    """
    A bomb can be placed in order to destroy tiles. But be careful!
    """
    def __init__(self, palette="pico-8"):
        super().__init__("bomb", palette)


class Key(Item):
    """
    Keys can be used to unlock chests ... and maybe other things!
    """
    def __init__(self, palette="pico-8"):
        super().__init__("key", palette)


class Sack(Item):
    """
    Sacks contain items. This might be the inventory icon
    """
    def __init__(self, palette="pico-8"):
        super().__init__("sack", palette)


class Gem(Item):
    """
    Gems are a valuable treasure. Collect them all!
    """
    def __init__(self, palette="pico-8"):
        super().__init__("gem", palette)


class Pearl(Item):
    """
    Pearls are a valuable treasure. Collect them all!
    """
    def __init__(self, palette="pico-8"):
        super().__init__("pearl", palette)


class Relic(Item):
    """
    Relics are works of art from a long forgotten time
    """
    def __init__(self, palette="pico-8"):
        super().__init__("relic", palette)


class Ink(Item):
    """
    Ink is used to write colored messages in important places
    """
    def __init__(self, palette="pico-8", color="red"):
        super().__init__("ink", palette)
        self.color = color
        self.meter = self[self.color]

    def change_color(self):
        if self.color == "red":
            self.color = "blue"
        else:
            self.color = "red"
        self.meter = self[self.color]

