from itertools import cycle

def get_file_content():
    input = open('input/day05.input', 'r')
    content = input.read()
    return content


def reduce_pol(the_string_to_be_evaluated, remove_char):

    i = 0

    while True:

        #print the_string_to_be_evaluated
        a = the_string_to_be_evaluated[i]
        if i<=len(the_string_to_be_evaluated)-2:
            b = the_string_to_be_evaluated[i+1]
        else:
            if (a.lower() == remove_char):
                the_string_to_be_evaluated = the_string_to_be_evaluated[:i]

            break

        if(a.lower()==remove_char):
            the_string_to_be_evaluated = the_string_to_be_evaluated[:i]+the_string_to_be_evaluated[i+1:]
            if i>=2:
                i=i-2
        else:

            if (a.islower() and b.isupper() or a.isupper() and b.islower()) and (a.lower() == b.lower()):
                the_string_to_be_evaluated =  the_string_to_be_evaluated[:i] +the_string_to_be_evaluated[i+2:]
                if i>=2:
                    i = i-2
                else:
                    i=0
            else:
                i+=1
    return len(the_string_to_be_evaluated)


#dabAcCaCBAcCcaDA
def part_a():
    the_string_to_be_evaluated = get_file_content()
    return reduce_pol(the_string_to_be_evaluated,'')


def part_b():

    the_string_to_be_evaluated = get_file_content()
    chars_to_evaluate = list(set(the_string_to_be_evaluated.lower()))
    result_list = []
    for character in chars_to_evaluate:
        result_list.append({"char":character,"value":reduce_pol(the_string_to_be_evaluated,character)})
    return sorted(result_list,key=lambda k: k['value'])[0]["value"]

if __name__ == "__main__":
    print 'Result part A: ' + str(part_a())
    print 'Result part B: ' + str(part_b())

