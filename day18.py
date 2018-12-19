import copy
import matplotlib.pyplot as plt

def get_file_content(f):
    """
    :return: THE LINES OF THE INPUT FILE
    """
    input = open(f, 'r')
    lines = input.read().splitlines()
    return lines


def create_area(f):
    """
    :return: a tuple (x length, y length and a dict where the key is a tuple of x,y coordinates and the a char
             representing the pathway at the given point as value
    """

    lines = get_file_content(f)
    max_line_len =len(max(lines))
    x = max_line_len
    y = len(lines)

    return (x,y,{(sx,sy):lines[sy][sx] for sx in range(x) for sy in range(y)})



def get_adjacent_coordinate_areas(area,coordinate):
    """
    Function returning the adjecent cord of a given coordinate
    :param area: The lumber collection area as a dict of coordinates
    :param coordinate: The coordinate to find out adjecent cordinates for
    :return: a dict with the adjecent coordinates of the given coordinate and its value i.e. '|','#' or '-'
    """

    x,y = coordinate
    adjacent_dict = {}

    adjacent_coords = [(x-1,y-1),(x,y-1),(x+1,y-1),(x+1,y),(x + 1, y+1),(x, y + 1),(x-1, y + 1),(x - 1, y)]

    for coord in adjacent_coords:
        try:
            adjacent_dict[coord] = area[coord]
        except KeyError:
            pass

    return adjacent_dict


def evaluate_adjacent(adjacent_coords):
    """

    :param adjacent_coords: Sends the adjecent coord for a coordinates
    :return: returns a dict that counts the amount for each acre type '#','|','.', like this:
             {'|': 1,'#':2,'.':1}
    """

    count_dict = {}
    for acre_type in ['|','#','.']:
        count_dict[acre_type] = len(filter(lambda t: adjacent_coords[t]==acre_type, adjacent_coords.keys()))

    return count_dict




def part_a():
    x_len, y_len, area = create_area('input/day18.input')
    for i in range(0,10):
        round_dict = {}
        for sy in range(0,x_len):
            for sx in range(0,y_len):
                adj =  get_adjacent_coordinate_areas(area,(sx,sy))
                type_count = evaluate_adjacent(adj)
                k = area[(sx,sy)]
                if area[(sx,sy)] == '.' and type_count['|'] >= 3:
                    round_dict[(sx,sy)] = '|'
                elif area[(sx,sy)] == '|' and type_count['#'] >= 3:
                    round_dict[(sx,sy)] = '#'
                elif area[(sx,sy)] == '#':
                    if type_count['#'] >= 1 and type_count['|'] >=1:
                        round_dict[(sx,sy)] = '#'
                    else:
                        round_dict[(sx, sy)] = '.'
                else:
                    round_dict[(sx, sy)] = area[(sx,sy)]

        area = round_dict


    count_dict =  {'|':0,'#':0}

    for ky in range(0,x_len):
        for kx in range(0,y_len):
            if area[(kx,ky)] =='|':
                count_dict['|']+=1
            if area[(kx,ky)] =='#':
                count_dict['#']+=1

    return count_dict['|']*count_dict['#']


def part_b():
    """

    TODO: Merge common parts for part a and b into a function

    This overly complicated solution for for this problem starts by reading the input file.
    Calling create_area returns the len for x,y and the area as a dict with (x,y)-tuples as key,
    and its acre type as value

    I then loop thru the area and create a new dict in accordance to the rules in description:
    - An open acre will become filled with trees if three or more adjacent acres contained trees.
      Otherwise, nothing happens.
    - An acre filled with trees will become a lumberyard if three or more adjacent acres were lumberyards.
      Otherwise, nothing happens.
    - An acre containing a lumberyard will remain a lumberyard if it was adjacent to at
      least one other lumberyard and at least one acre containing trees. Otherwise, it becomes open.

    I then checksum the new dict and add it to a list in order to detect when a pattern seen before occurs again for
    the first time. Then I move the counter to as many iterations before 1000000000 needed in order
    to get the pattern cycle that covers 1000000000



    :return: The result for AOC day 18, second part
    """
    pattern = []
    x_len, y_len, area = create_area('input/day18.input')
    counter = 0
    find_out_first_pattern=True
    while counter<=1000000000-1:
        round_dict = {}
        for sy in range(0,x_len):
            for sx in range(0,y_len):
                adj =  get_adjacent_coordinate_areas(area,(sx,sy))
                type_count = evaluate_adjacent(adj)
                if area[(sx,sy)] == '.' and type_count['|'] >= 3:
                    round_dict[(sx,sy)] = '|'
                elif area[(sx,sy)] == '|' and type_count['#'] >= 3:
                    round_dict[(sx,sy)] = '#'
                elif area[(sx,sy)] == '#':
                    if type_count['#'] >= 1 and type_count['|'] >=1:
                        round_dict[(sx,sy)] = '#'
                    else:
                        round_dict[(sx, sy)] = '.'
                else:
                    round_dict[(sx, sy)] = area[(sx,sy)]

        area = round_dict

        chksum = reduce(lambda x,y : x^y, [hash(item) for item in round_dict.items()])
        if chksum not in map(lambda x: x[1],pattern):
            pattern.append((counter,chksum))
        else:
            if find_out_first_pattern==True:
                first_pattern_found_at_index =filter(lambda p: p[1] == chksum,pattern)[0][0]
                area = round_dict
                counter = 1000000000 - ((1000000000 - first_pattern_found_at_index) % (counter - first_pattern_found_at_index))
                find_out_first_pattern = False
        counter += 1

    count_dict = {'|': 0, '#': 0}


    for ky in range(0, x_len):
        for kx in range(0, y_len):
            if area[(kx, ky)] == '|':
                count_dict['|'] += 1
            if area[(kx, ky)] == '#':
                count_dict['#'] += 1
    result = count_dict['|'] * count_dict['#']

    return result #169106

    

if __name__ == "__main__":

    print 'Result part A: ' + str(part_a()) #653184
    print 'Result part B: ' + str(part_b()) #NOT 2688, NOT 165440: too low, Not 167564 too low, not 177160 BUT: 169106

