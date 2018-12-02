



def get_file_content():
    input = open('input/day01.input', 'r')
    lines = input.read().splitlines()
    return lines

def part_a():
    lines = get_file_content()
    lines_as_ints = map(lambda i: int(i),lines)
    result = reduce(lambda acc, val: acc+val,lines_as_ints)
    return result



def part_b():

    lines = get_file_content()
    result = 0
    result_history = []
    result_not_found = True
    while result_not_found:
        for entry in lines:
            result= result + int(entry)
            if result in result_history:
                result_not_found = False
                break
            else:
                result_history.append(result)

    return result


if __name__ == "__main__":

    print 'Result part A: ' + str(part_a())
    print 'Result part B: ' + str(part_b())

