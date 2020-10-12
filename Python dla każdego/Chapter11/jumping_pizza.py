#!/usr/bin/env python3
# Autor: Maciej Kuta
# Data utworzenie: 12.10.2020
# Cel: Sprawienie, że pizza się rusza

from superwires import games
import pygame

games.init(screen_width = 640, screen_height = 480, fps=50)

wall_image = games.load_image("sciana.jpg")
games.screen.background = wall_image

class Pizza(games.Sprite):
    def update(self):
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = - self.dy

pizza_image = games.load_image("pizza.bmp")
pizza = Pizza(image=pizza_image, 
                    x = games.screen.width/2,
                    y = games.screen.height/2,
                    dx = 1,
                    dy =1)
games.screen.add(pizza)

games.screen.mainloop()