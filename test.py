#!/usr/bin/env python
# -*- coding: utf-8 -*-

from langtons_ant.langtons_ant import LangtonsAnt
from matplotlib import pyplot as plt

grid = []
# Set grid size
grid_x = 30
grid_y = 30

# Populate grid with empty data
for _ in range(grid_x):
    row = []
    for _ in range(grid_y):
        row.append(False)

    grid.append(row)

game = LangtonsAnt(initial_state=grid, start_position=(grid_x // 2, grid_y // 2))

fig = plt.figure()
ax = fig.add_subplot(111)
plt.ion()

for i in range(3000):
    game.next_move()
    grid = game.state
    ax = fig.add_subplot(111)
    ax.imshow(grid, aspect='auto', interpolation='nearest', cmap=plt.get_cmap('gray'))
    plt.pause(0.0001)
    ax.cla()
