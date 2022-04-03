"""
assets.py builds and houses LINKER, an 8x8 dual-palette sprite dictionary
"""
import pygame
from sprites import Spritesheet

# The true dimension of each sprite in the sheet
d = 8

# The image we will be pulling from
sheet = pygame.image.load("sprites/linker/img/tiles.png")

# Change this to change the size of the sprites
scale = 3

# Create and scale the sheet which will be organized
comp = Spritesheet(sheet, d, d)
comp.scale_sheet(scale, scale)

"""
The dictionary is arranged such that the final argument when
retrieving a sprite set is the palette. For example:

["player"]["pico-8"]
["environment"]["statues"]["nes"]
["dust"]["nes"]

The only exception is tiles, where the palette is declared before the individual tiles.

["environment"]["tile"]["pico-8"]["x"]
["environment"]["tile"]["nes"]["pillar2"]

This is because the tiles are more general, so their implementation of LinkerSprite differs slightly.
"""
LINKER = {
    "player": {
        "pico-8": {
            "fade": [comp[0][8], comp[0][9], comp[0][10]],
            "idle": [comp[1][9]],
            "walk": [
                comp[0][10], comp[0][11], comp[0][12], comp[1][8], comp[1][9], comp[1][10], comp[1][11]
            ],
            "fall": [
                comp[2][8], comp[2][9], comp[2][10], comp[2][11], comp[2][12], comp[1][12]
            ]
        },
        "nes": {
            "fade": [comp[9][8], comp[9][9], comp[9][10]],
            "idle": [comp[10][9]],
            "walk": [
                comp[9][10], comp[9][11], comp[9][12], comp[10][8], comp[10][9], comp[10][10], comp[10][11]
            ],
            "fall": [
                comp[11][8], comp[11][9], comp[11][10], comp[11][11], comp[11][12], comp[10][12]
            ]
        }
    },
    "dust": {
        "pico-8": [comp[3][8], comp[3][9], comp[3][10], comp[1][12]],
        "nes": [comp[12][8], comp[12][9], comp[12][10], comp[10][12]]
    },
    "scroll": {
        "pico-8": {
            "tl": comp[0][1],
            "t": comp[0][2],
            "tr": comp[0][3],
            "ml": comp[1][1],
            "m": comp[1][2],
            "mr": comp[1][3],
            "bl": comp[2][1],
            "b": comp[2][2],
            "br": comp[2][3]
        },
        "nes": {
            "tl": comp[0][5],
            "t": comp[0][6],
            "tr": comp[0][7],
            "ml": comp[1][5],
            "m": comp[1][6],
            "mr": comp[1][7],
            "bl": comp[2][5],
            "b": comp[2][6],
            "br": comp[2][7]
        }
    },
    "bang": {
        "pico-8": {
            "tl": comp[0][13],
            "t": comp[0][14],
            "tr": comp[0][15],
            "ml": comp[1][13],
            "m": comp[1][14],
            "mr": comp[1][15],
            "bl": comp[2][13],
            "b": comp[2][14],
            "br": comp[2][15]
        },
        "nes": {
            "tl": comp[9][13],
            "t": comp[9][14],
            "tr": comp[9][15],
            "ml": comp[10][13],
            "m": comp[10][14],
            "mr": comp[10][15],
            "bl": comp[11][13],
            "b": comp[11][14],
            "br": comp[11][15]
        }
    },
    "item": {
        "pencil": {
            "pico-8": {
                "case": comp[5][9],
                "blue": comp[4][10],
                "red": comp[4][11]
            },
            "nes": {
                "case": comp[14][9],
                "blue": comp[13][10],
                "red": comp[13][11]
            }
        },
        "bomb": {
            "pico-8": [comp[3][11], comp[3][12], comp[3][13], comp[3][14]],
            "nes": [comp[12][11], comp[12][12], comp[12][13], comp[12][14]]
        },
        "key": {
            "pico-8": comp[4][14],
            "nes": comp[13][14]
        },
        "sack": {
            "pico-8": comp[4][12],
            "nes": comp[13][12]
        },
        "gem": {
            "pico-8": comp[3][15],
            "nes": comp[12][15]
        },
        "pearl": {
            "pico-8": comp[4][15],
            "nes": comp[13][15]
        },
        "relic": {
            "pico-8": comp[4][13],
            "nes": comp[13][13]
        },
        "ink": {
            "pico-8": {
                "vial": comp[6][9],
                "red": [
                    comp[5][10], comp[5][11], comp[5][12], comp[5][13], comp[5][14], comp[5][15]
                ],
                "blue": [
                    comp[6][10], comp[6][11], comp[6][12], comp[6][13], comp[6][14], comp[6][15]
                ]
            },
            "nes": {
                "vial": comp[15][9],
                "red": [
                    comp[14][10], comp[14][11], comp[14][12], comp[14][13], comp[14][14], comp[14][15]
                ],
                "blue": [
                    comp[15][10], comp[15][11], comp[15][12], comp[15][13], comp[15][14], comp[15][15]
                ]
            }
        },
        "map": {
            "pico-8": comp[4][8],
            "nes": comp[13][8]
        }
    },
    "filler": {
        "pico-8": {
            0: comp[5][3],
            1: comp[1][0],
            2: comp[5][2]
        },
        "nes": {
            0: comp[5][7],
            1: comp[1][4],
            2: comp[5][6]
        }
    },
    "environment": {
        "tiles": {
            "pico-8": {
                "facade1": comp[8][3],
                "facade2": comp[8][2],
                "x": [comp[2][0], comp[3][0], comp[5][0], comp[7][0]],
                "smallbrick": {
                    "dark": comp[6][3],
                    "light": comp[7][3]
                },
                "bigbrick": {
                    "dark": comp[6][2],
                    "light": comp[7][2]
                },
                "hole": comp[8][0],
                "pillar1": comp[5][1],
                "pillar2": comp[8][1],
                "cracked1": comp[4][3],
                "cracked2": comp[4][2],
                "smooth1": comp[3][3],
                "smooth2": comp[3][2]
            },
            "nes": {
                "facade1": comp[8][7],
                "facade2": comp[8][6],
                "x": [comp[2][4], comp[3][4], comp[5][4], comp[7][4]],
                "smallbrick": {
                    "dark": comp[6][7],
                    "light": comp[7][7]
                },
                "bigbrick": {
                    "dark": comp[6][6],
                    "light": comp[7][6]
                },
                "hole": comp[8][4],
                "pillar1": comp[5][5],
                "pillar2": comp[8][5],
                "cracked1": comp[4][7],
                "cracked2": comp[4][6],
                "smooth1": comp[3][7],
                "smooth2": comp[3][6]
            }
        },
        "statue": {
            "pico-8": {
                "horns1": [comp[9][0], comp[10][0]],
                "horns2": [comp[9][1], comp[10][1]],
                "eye1": [comp[9][2], comp[10][2]],
                "eye2": [comp[9][3], comp[10][3]],
                "a1": [comp[11][2], comp[12][2]],
                "a2": [comp[11][3], comp[12][3]],
                "plinth1": [comp[11][0], comp[11][1]],
                "plinth2": [comp[12][0], comp[12][1]]
            },
            "nes": {
                "horns1": [comp[9][4], comp[10][4]],
                "horns2": [comp[9][5], comp[10][5]],
                "eye1": [comp[9][6], comp[10][6]],
                "eye2": [comp[9][7], comp[10][7]],
                "a1": [comp[11][6], comp[12][6]],
                "a2": [comp[11][7], comp[12][7]],
                "plinth1": [comp[11][4], comp[11][5]],
                "plinth2": [comp[12][4], comp[12][5]]
            }
        }
    },
    "hand": {
        "pico-8": {
            "point": comp[5][8],
            "grab": comp[6][8]
        },
        "nes": {
            "point": comp[14][8],
            "grab": comp[15][8]
        }
    },
    "chest": {
        "pico-8": {
            "closed": comp[14][1],
            "open": comp[14][2]
        },
        "nes": {
            "closed": comp[14][5],
            "open": comp[14][6]
        }
    },
    "vine": {
        "pico-8": {
            "base": comp[15][0],
            0: comp[14][0],
            1: comp[13][0]
        },
        "nes": {
            "base": comp[15][4],
            0: comp[14][4],
            1: comp[13][4]
        }
    },
    "fairy": {
        "pico-8": [comp[13][1], comp[13][2]],
        "nes": [comp[13][5], comp[13][6]]
    },
    "pot": {
        "pico-8": {
            "empty": comp[15][1],
            "full": comp[15][2]
        },
        "nes": {
            "empty": comp[15][5],
            "full": comp[15][6]
        }
    },
    "accents": {
        "pico-8": {
            "grey": comp[3][1],
            "black": comp[4][1],
            "light": comp[6][1],
            "dark": comp[7][1]
        },
        "nes": {
            "grey": comp[3][5],
            "black": comp[4][5],
            "light": comp[6][5],
            "dark": comp[7][5]
        }
    },
    "stairs": {
        "pico-8": {
            0: comp[6][0],
            1: comp[4][0]
        },
        "nes": {
            0: comp[6][4],
            1: comp[4][4]
        }
    },
    "button": {
        "pico-8": comp[0][0],
        "nes": comp[0][4]
    },
    "shadow": {
        "pico-8": comp[4][9],
        "nes": comp[13][9]
    }
}
