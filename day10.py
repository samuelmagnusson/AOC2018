import re

import numpy as np

class Position:

    def __init__(self,x, y, vel_x, vel_y):

        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.update_position()

    def update_position(self):

        self.x =self.x + self.vel_x
        self.y =self.y + self.vel_y

    def get_x_y(self):
        return (self.x,self.y)

def get_file_content():
    input = open('input/day10.input', 'r')
    lines = input.read().splitlines()
    return lines

def parse_line(line):

    match = re.match(r'.*<(.*),(.*)>.*<(.*),(.*)>',line)
    return {(int(match.group(1)),int(match.group(2))):(int(match.group(3)),int(match.group(4)))}


def parse_lines():
    lines_list = []
    max_y = 0
    max_x = 0
    min_y = 10**5
    min_x = 10**5

    for line in get_file_content():
        parse = parse_line(line)
        x,y = parse.keys()[0]
        if x > max_x:
            max_x=x
        if y > max_y:
            max_y=y
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y

        lines_list.append(parse)
    return lines_list

def get_positions_list_from_dict(lines):
    positions = map(lambda l: l,lines)
    return positions

lines = parse_lines()
positions = []

for pos in lines:
    key = pos.keys()[0]
    positions.append(Position(key[0],key[1],pos[key][0],pos[key][1]))


def get_max_min(list_of_Position_objects):
    xy_for_coords = map(lambda xy: xy.get_x_y(), list_of_Position_objects)
    x = sorted(xy_for_coords,key=lambda x: x[0])
    y = sorted(xy_for_coords,key=lambda y: y[1])
    return {'min_x':x[0][0],'max_x':x[-1][0],'min_y':y[1][1],'max_y':y[-1][1]}





counter =0
def convex_hull_graham(points):
    '''
    Returns points on convex hull in CCW order according to Graham's scan algorithm.
    By Tom Switzer <thomas.switzer@gmail.com>.
    '''
    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

    def cmp(a, b):
        return (a > b) - (a < b)

    def turn(p, q, r):
        return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

    def _keep_left(hull, r):
        while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
            hull.pop()
        if not len(hull) or hull[-1] != r:
            hull.append(r)
        return hull

    points = sorted(points)
    l = reduce(_keep_left, points, [])
    u = reduce(_keep_left, reversed(points), [])
    return l.extend(u[i] for i in range(1, len(u) - 1)) or l

while True:
    [pos.update_position() for pos in positions]
    maxmins = get_max_min(positions)
    xy_for_coords = map(lambda xy: xy.get_x_y(), positions)

    hullist = convex_hull_graham(xy_for_coords)

    counter += 1
    if len(hullist)==4:
        val = ''
        maxmins = get_max_min(positions)
        for x in range(maxmins['min_y']-10, maxmins['max_y']+10):
            for y in range(maxmins['min_x']-10, maxmins['max_x']+10):
                if (x, y) in map(lambda xy: xy.get_x_y(), positions):
                    val = val + '#'
                else:
                    val = val + '.'

            val = val + '\n'
        print val
        print counter+1
        break




        




