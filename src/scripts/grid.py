import pygame as pg
from utils import *

class Grid:
    def __init__(self, screen:pg.Surface):
        pg.font.init()
        self.font = pg.font.SysFont('Arial', 14)
        self.screen = screen
        self.width, self.height = self.screen.get_size()
        self.center_x, self.center_y = self.width // 2, self.height // 2

        self.zoom_factor = 1.15
        self.scale = 50.0
        self.min_scale = 10.0
        self.max_scale = 300.0

        self.dragging = False
        self.last_mouse_pos = (0, 0)

    def events(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.dragging = True
                self.last_mouse_pos = event.pos
        elif event.type == pg.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pg.MOUSEMOTION and self.dragging:
            current_x, current_y = event.pos
            dx = current_x - self.last_mouse_pos[0]
            dy = current_y - self.last_mouse_pos[1]

            self.center_x += dx
            self.center_y += dy
            self.last_mouse_pos = event.pos
        elif event.type == pg.MOUSEWHEEL:
            if event.y > 0:
                if self.scale < self.max_scale:
                    self.scale *= self.zoom_factor
            elif event.y < 0:
                if self.scale > self.max_scale:
                    self.scale /= self.zoom_factor

    def render(self):
        self.screen.fill(COLOR_BG)
        step = self.scale

        start_x = self.center_x % step
        for x in range(int(start_x), self.width, int(step)):
            pg.draw.line(self.screen, COLOR_GRID, (x, 0), (x, self.height), 1)

        start_y = self.center_y % step
        for y in range(int(start_y), self.height, int(step)):
            pg.draw.line(self.screen, COLOR_GRID, (0, y), (self.width, y), 1)

        pg.draw.line(self.screen, COLOR_AXIS, (0, self.center_y), (self.width, self.center_y), 2)
        pg.draw.line(self.screen, COLOR_AXIS, (self.center_x, 0), (self.center_x, self.height), 2)

        math_x_start = -self.center_x / self.scale
        math_x_end = (self.width - self.center_x) / self.scale

        interval = 1
        if self.scale < 25:
            interval = 5
        elif self.scale > 150:
            interval = 0.5

        val = int(math_x_start)
        while val <= math_x_end:
            if val != 0:
                screen_x = self.center_x + (val * self.scale)
                if 0 <= screen_x <= self.width:
                    pg.draw.line(self.screen, COLOR_AXIS, (screen_x, self.center_y - 4), (screen_x, self.center_y + 4), 1)
                    txt = self.font.render(str(val), True, COLOR_TEXT)
                    self.screen.blit(txt, (screen_x - txt.get_width() // 2, self.center_y + 6))
            val += interval

        math_y_start = (self.center_y - self.height) / self.scale
        math_y_end = self.center_y / self.scale

        val_y = int(math_y_start)
        while val_y <= math_y_end:
            if val_y != 0:
                screen_y = self.center_y - (val_y * self.scale)
                if 0 <= screen_y <= self.height:
                    pg.draw.line(self.screen, COLOR_AXIS, (self.center_x - 4, screen_y), (self.center_x + 4, screen_y), 1)
                    txt = self.font.render(str(val_y), True, COLOR_TEXT)
                    self.screen.blit(txt, (self.center_x + 8, screen_y - txt.get_height() // 2))
            val_y += interval