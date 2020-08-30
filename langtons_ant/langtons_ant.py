#!/usr/bin/env python
# -*- coding: utf-8 -*-


class LangtonsAnt:
    def __init__(self, initial_state, start_position, start_direction=0):
        # start direction can be int value within list (0, 90, 180, 360)
        # True is black color in the grid and False is white
        self.grid = initial_state
        self.curr_direction = start_direction
        self.curr_position = start_position
        self.no_legal_move = False

    def cell_is_black(self):
        x, y = self.curr_position
        return self.grid[x][y]

    def flip_color(self):
        x, y = self.curr_position
        self.grid[x][y] = not self.grid[x][y]

    def turn_left(self):
        self.curr_direction -= 90
        if self.curr_direction < 0:
            self.curr_direction += 360

    def turn_right(self):
        self.curr_direction += 90
        if self.curr_direction >= 360:
            self.curr_direction -= 360

    def move_forward(self):
        try:
            x, y = self.curr_position
            if self.curr_direction == 0:
                x -= 1
            elif self.curr_direction == 90:
                y += 1
            elif self.curr_direction == 180:
                x += 1
            elif self.curr_direction == 270:
                y -= 1

            self.grid[x][y]
            self.curr_position = x, y
        except IndexError:
            self.no_legal_move = True
            return False

    def next_move(self):
        if self.no_legal_move:
            return False

        if self.cell_is_black():
            self.turn_left()
        else:
            self.turn_right()

        self.flip_color()

        return self.move_forward()

    @property
    def state(self):
        return self.grid
