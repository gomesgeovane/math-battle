import pygame as pg
from utils import *
import sys

from scripts.grid import Grid

class MathBattle:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Math Battle')
        self.settings = read_settings()
        self.screen = pg.display.set_mode(self.settings['size'])
        self.clock = pg.Clock()
        self.running = True

        self.grid = Grid(self.screen)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            self.grid.events(event)

    def update(self):
        pass

    def render(self):
        self.screen.fill(self.settings['color'])
        self.grid.render()
        pg.display.flip()

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.render()
            self.clock.tick(self.settings['fps'])
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    app = MathBattle()
    app.run()