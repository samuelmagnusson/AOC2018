

def part_a():
    input = open('input/day01.input','r')
    lines = input.read().splitlines()
    lines_as_ints = map(lambda i: int(i),lines)

    result = reduce(lambda acc, val: acc+val,lines_as_ints)
    return result



if __name__ == "__main__":

    print 'Result part A: ' + str(part_a())
    

