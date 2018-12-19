import os
import time


def get_file_content():
    """
    :return: THE LINES OF THE INPUT FILE
    """
    input = open('input/day13.input', 'r')
    lines = input.read().splitlines()
    return lines


def create_path_matrix():
    """
    :return: a tuple (x length, y length and a dict where the key is a tuple of x,y coordinates and the a char
             representing the pathway at the given point as value
    """

    lines = get_file_content()
    max_line_len =len(max(lines))+1
    x = max_line_len
    y = len(lines)
    #This is to make the lines equally lenght
    for i,line in enumerate(lines):
        if len(line)< max_line_len:
            lines[i] = line.ljust(max_line_len)

    return (x,y,{(sx,sy):lines[sy][sx] for sx in range(x) for sy in range(y)})

def find_cart_positions_and_direction(matrix):
    """
    :param matrix: The {(x,y):'|',(x,y):'>'} dict
    :return: a tuple a dict of positions and initial direction.
    """
    chart_dict ={}
    for key in matrix.keys():
        if matrix[key] == '<':
            chart_dict[key] = 'LEFT'
            matrix[key] = '-'
        if matrix[key] == '^':
            chart_dict[key]= 'UP'
            matrix[key] = '|'
        if matrix[key] == '>':
            chart_dict[key] ='RIGHT'
            matrix[key] = '-'
        if matrix[key] == 'v':
            chart_dict[key] = 'DOWN'
            matrix[key] = '|'
    return (chart_dict,matrix)


class Cart():


    def __init__(self, current_position, initial_direction,matrix):


        self.current_position = current_position
        self.current_direction = initial_direction
        self.next_turn_direction = 'LEFT_TURN'
        self.matrix = matrix
        self.log = []

    def get_current_possition(self):
        return self.current_position

    def move(self):
        next_coordinates = self.evaluate_next_step_coordinates()
        if self.matrix[next_coordinates] == '+':
            self.set_current_direction()
            self.current_position = next_coordinates
        if self.matrix[next_coordinates] == "\\":
            if self.current_direction == 'LEFT':
                self.current_direction = 'UP'
            elif self.current_direction == 'DOWN':
                self.current_direction = 'RIGHT'
            elif self.current_direction == 'UP':
                self.current_direction = 'LEFT'
            elif self.current_direction == 'RIGHT':
                self.current_direction = 'DOWN'
            self.current_position = next_coordinates
        if self.matrix[next_coordinates] == "/":
            if self.current_direction == 'LEFT':
                self.current_direction = 'DOWN'
            elif self.current_direction == 'DOWN':
                self.current_direction = 'LEFT'
            elif self.current_direction == 'UP':
                self.current_direction = 'RIGHT'
            elif self.current_direction == 'RIGHT':
                self.current_direction = 'UP'
            self.current_position = next_coordinates
        if self.matrix[next_coordinates]  == '-':
            self.current_position = next_coordinates
        if self.matrix[next_coordinates]  == '|':
            self.current_position = next_coordinates
        self.log.append(self.current_position)

    def set_current_direction(self):
        if self.next_turn_direction == 'LEFT_TURN':
            if self.current_direction =='LEFT':
                self.current_direction = 'DOWN'
            elif self.current_direction == 'DOWN':
                self.current_direction ='RIGHT'
            elif self.current_direction == 'RIGHT':
                self.current_direction = 'UP'
            elif self.current_direction == 'UP':
                self.current_direction = 'LEFT'
            self.next_turn_direction = 'FORWARD'
        elif self.next_turn_direction == 'FORWARD':
            self.next_turn_direction = 'RIGHT_TURN'
        elif self.next_turn_direction == 'RIGHT_TURN':
            if self.current_direction == 'LEFT':
                self.current_direction = 'UP'
            elif self.current_direction == 'DOWN':
                self.current_direction = 'LEFT'
            elif self.current_direction == 'RIGHT':
                self.current_direction = 'DOWN'
            elif self.current_direction == 'UP':
                self.current_direction = 'RIGHT'
            self.next_turn_direction = 'LEFT_TURN'


    def evaluate_next_step_coordinates(self):
        x,y = self.current_position
        if self.current_direction =='LEFT':
            return (x-1,y)
        elif self.current_direction == 'RIGHT':
            return (x+1, y)
        elif self.current_direction == 'UP':
            return (x, y-1)
        elif self.current_direction == 'DOWN':
            return (x, y+1)

    def print_log(self):
        print '--LOG--'
        for log in self.log:
            print str(log)


def part_a():

    x,y,matrix = create_path_matrix()


    carts_initial_positions,matrix_without_carts = find_cart_positions_and_direction(matrix)

    cart_obj_list = []
    for cart in carts_initial_positions:
        cart_obj_list.append(Cart(cart,carts_initial_positions[cart],matrix_without_carts))

    continueIter=True
    while continueIter:


        for cart in sorted(cart_obj_list, key=lambda k: (k.current_position[1],k.current_position[0])):
            cart.move()

            if cart.get_current_possition() in [pos[1] for pos in filter(lambda tmp_cart: (id(cart),cart.get_current_possition())!=tmp_cart,[(id(c),c.get_current_possition()) for c in cart_obj_list])]:
                return cart.get_current_possition()


def part_b():
    x, y, matrix = create_path_matrix()

    carts_initial_positions, matrix_without_carts = find_cart_positions_and_direction(matrix)

    cart_obj_list = []
    for cart in carts_initial_positions:
        cart_obj_list.append(Cart(cart, carts_initial_positions[cart], matrix_without_carts))

    continueIter = True
    while continueIter:

        for cart in sorted(cart_obj_list, key=lambda k: (k.current_position[1], k.current_position[0])):
            crash_filter = filter(lambda tmp_cart: tmp_cart.get_current_possition()==cart.get_current_possition(),cart_obj_list)
            if len(crash_filter)==2:
                [cart_obj_list.remove(x) for x in crash_filter]
            if len(cart_obj_list) == 1:
                return cart_obj_list[0].get_current_possition()
            cart.move()



if __name__ == "__main__":

    print 'Result part A: ' + str(part_a()) #(139, 65)
    print 'Result part B: ' + str(part_b()) #(40, 77)


