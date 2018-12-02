


def get_file_content():
    input = open('input/day02.input', 'r')
    lines = input.read().splitlines()
    return lines

def get_not_unique(line):
    """
    :param line: A string
    :return: A list of chars of line that has more than one occerencies
    """
    not_uniques = [c for c in line if line.count(c)>1]
    return list(set(not_uniques))

def count_twos_and_threes(line_and_not_unique):
    """
    :param line_and_not_unique: A set containing a string, and a list of those chars of that string that are not unique for example:
    ('revtcubfniyhpsaxdoajdkqmlp', ['a', 'p', 'd'])
    :return: A dict like this  {'twos': 1, 'threes': 1}. In case the string contains a char that has exact 3 occurencies, threes becomes 1,
            if the string contains a char that has exact 2 occurencies, twos becomes 1.
    """
    line, not_unique_list = line_and_not_unique
    count_twos = 0
    count_threes = 0
    print line_and_not_unique
    for char in not_unique_list:
        amount_of_not_unique_char = filter(lambda c: c == char, [i for i in line])
        if len(amount_of_not_unique_char) == 2:
            count_twos = 1
        if len(amount_of_not_unique_char)== 3:
            count_threes = 1

    return {'twos': count_twos, 'threes': count_threes}


def part_a():
    """
    :return: The product of the amount of lines in file 'input/day02.input' that contains two of the same characters
    and/or three of the same characters.
    """
    lines =get_file_content()
    not_unique_items = map(lambda line: get_not_unique(line),lines)
    not_unique_per_line = zip(lines,not_unique_items)

    accumTwo = 0
    accumThree = 0

    for line in not_unique_per_line:
        countresult = count_twos_and_threes(line)
        accumTwo += countresult['twos']
        accumThree += countresult['threes']

    return accumTwo * accumThree

def check_similarity(current, compare_string):
    """
    :param current: A string
    :param compare_string: Another string to compare with
    :return: A list of the indexes of the string Current that does not contain the same char as "compare_string"
    """

    non_equal_chars_index_list = []
    for index in xrange(len(current)):
        if current[index] != compare_string[index]:
            non_equal_chars_index_list.append(index)

    return non_equal_chars_index_list





def part_b():
    """
    Here we iterate thru the list of strings. For each string, whe check the whole list again and match the
    current string of the outer loop against the one in the inner loop. As long as the index is not the same
    for both loops, we check for how similar the strings are. The right one, that we are looking for is the one
    that only differs one char. when this is found, we return the correct string without the "differing" char.

    :return: String that only differes one char
    """
    lines =get_file_content()

    for i in xrange(len(lines)-1):
        for k in xrange(len(lines)-1):
            if i != k:
               similarity_list = check_similarity(lines[i],lines[k])
               if len(similarity_list) == 1:
                   print lines[i]
                   return lines[i][:similarity_list[0]] + lines[i][similarity_list[0]+1:]




if __name__ == "__main__":
    print 'Result part A: '+ str(part_a())
    print 'Result Part B: ' + str(part_b())