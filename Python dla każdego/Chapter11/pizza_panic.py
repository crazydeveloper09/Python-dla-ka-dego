#!/usr/bin/env python3
# Autor: Maciej Kuta
# Data utworzenie: 12.10.2020
# Cel: Pizza panic

from superwires import games, color
import pygame, random

games.init(screen_width = 640, screen_height = 480, fps=50)

wall_image = games.load_image("sciana.jpg")
games.screen.background = wall_image

class Pizza(games.Sprite):
    image = games.load_image("pizza.bmp")
    speed = 1
    def __init__(self, x, y=90):
        super(Pizza, self).__init__(image = Pizza.image,
                                x = x, y=y,
                                dy = Pizza.speed)
    def update(self):
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()
    def handle_collide(self):
        self.destroy()
    def end_game(self):
        end_message = games.Message(value = "Koniec gry", size = 90, color = color.red,
                                    x = games.screen.width/2, y = games.screen.height/2,
                                    lifetime= 5 * games.screen.fps,
                                    after_death= games.screen.quit)
        games.screen.add(end_message)


class Pan(games.Sprite):
    image = games.load_image("patelnia.bmp")
    def __init__(self):
        super(Pan, self).__init__(image = Pan.image,
                                x = games.mouse.x,
                                bottom = games.screen.height)
        self.score = games.Text(value=0, size=25, color = color.black,
                                top =5, right = games.screen.width - 10)
        games.screen.add(self.score)
    def update(self):
        self.x = games.mouse.x
        if self.left < 0:
            self.elft = 0
        if self.right > games.screen.width:
            self.right = games.screen.width    
        self.check_collide()
    def check_collide(self):
        for pizza in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            pizza.handle_collide()
class Chef(games.Sprite):
    image = games.load_image("kucharz.bmp")
    def __init__(self, y = 55, speed = 2, odds_change = 200):
        super(Chef, self).__init__(image = Chef.image,
                                x = games.screen.width/2, y=y,
                                dx = speed)

        self.odds_change = odds_change
        self.time_til_drop = 0
    def update(self):
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx
        self.check_drop()
    def check_drop(self):
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_pizza = Pizza(x = self.x)
            games.screen.add(new_pizza)
            self.time_til_drop = int(new_pizza.height * 1.3 / Pizza.speed) +1    
def main():
   
    chef = Chef()
    games.screen.add(chef)
   
    pan = Pan()
    games.screen.add(pan)
    games.mouse.is_visible = False
    games.screen.event_grab = True


    games.screen.mainloop()

main()