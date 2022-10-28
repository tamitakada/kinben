from tkinter import *
import random
from colorsys import hls_to_rgb
from math import sqrt, pow


def hsl_to_hex(hsl):
    rgb = hls_to_rgb((hsl[0])/360, (hsl[2])/100, (hsl[1])/100)
    rgb_formatted = (
        int(rgb[0] * 255),
        int(rgb[1] * 255),
        int(rgb[2] * 255)
    )
    return '#%02x%02x%02x' % rgb_formatted


class RandomCircleBackground(Canvas):
    def __init__(
        self,
        root,
        width,
        height,
        circle_number
    ):
        bg_color = hsl_to_hex((
            random.randint(200, 280),
            random.randint(15, 40),
            random.randint(20, 40)
        ))
        super().__init__(width=width, height=height, bg=bg_color)
        
        circle_color = hsl_to_hex((
            random.randint(30, 350),
            random.randint(70, 90),
            random.randint(40, 70)
        ))
        min_circle_size = 100
        max_circle_size = 300
        
        circle_info = []
        
        for i in range(circle_number):
            reroll = True
            while reroll:
                x = random.randint(-50, width - 50)
                y = random.randint(-50, height - 50)
                
                x2 = random.randint(x + min_circle_size, x + max_circle_size)
                y2 = y + (x2 - x)
                
                radius = (x2 - x)/2
                center = (x + radius, y + radius)
                
                reroll = False
                for c in circle_info:
                    dist = sqrt(pow(c[0][0] - center[0], 2) + pow(c[0][1] - center[1], 2))
                    if dist <= radius + c[1] + 80:
                        reroll = True
                        break

                if not reroll:
                    circle_info.append((center, radius))
                    circle = self.create_oval(
                        x,
                        y,
                        x2,
                        y2,
                        width=10,
                        outline=circle_color
                    )
