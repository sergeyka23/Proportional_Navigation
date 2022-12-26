import math


class Missile:
    start_x = 0.0
    start_y = 0.0
    start_ang = 0.0
    a = 0.0
    start_pos = [start_x, start_y]
    prev_vx = 0.0
    prev_vy = 0.0
    current_vx = 0.0
    current_vy = 0.0
    prev_x = 0.0
    prev_y = 0.0
    current_x = 0.0
    current_y = 0.0
    current_pos = [current_x, current_y]


class Target:
    start_x = 0.0
    start_y = 0.0
    start_ang = 0.0
    start_pos = [start_x, start_y]
    v = 0.0
    enable = True

    prev_x = start_x
    prev_y = start_y
    current_x = 0.0
    current_y = 0.0
    current_pos = [current_x, current_y]
