
import re

def calculateDistance(x1,y1,x2,y2):
     dist = abs(x2 - x1) + abs(y2 - y1)
     return dist

def get_file_content():
    input = open('input/day06.input', 'r')
    lines = input.read().splitlines()
    return lines


def parse_file_content(line):

    match = re.match('([0-9]*), ([0-9]*)',line)
    return (int(match.group(1)),int(match.group(2)))


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

coordinates = map(lambda coord: parse_file_content(coord),get_file_content())


eternal_points = convex_hull_graham(coordinates)



non_eternal_points = []
for coord in coordinates:
    if coord not in eternal_points:
        non_eternal_points.append(coord)



sorted_x = sorted(coordinates, key=lambda x: x[0])
sorted_y = sorted(coordinates, key=lambda y: y[1])


result_dict = {}
for c in coordinates:
    result_dict[c] = 0




for y in range(sorted_y[0][1],sorted_y[-1][1]):
    for x in range(sorted_x[0][0],sorted_x[-1][0]):
        currentcord = (x,y)
        lowest_manhattan_distance = 10**5
        for index,coord in enumerate(coordinates):
            manhattan_distance = round(calculateDistance(coord[0], coord[1], currentcord[0], currentcord[1]), 2)
            if currentcord == coord:
                result_dict[coord] +=1
                break
            if manhattan_distance == lowest_manhattan_distance:
                lowest_cord = None
            if manhattan_distance < lowest_manhattan_distance:
                lowest_cord = coord
                lowest_manhattan_distance = manhattan_distance
            if index == len(coordinates)-1:
                if lowest_cord is not None:
                    result_dict[lowest_cord] +=1


new_result_dict= {}
for key in result_dict.keys():
    if key not in eternal_points:
        new_result_dict[key] = result_dict[key]

print sorted(new_result_dict.items(), key=lambda kv: kv[1])[-1][1]


