def get_file_content():
    input = open('input/day08.example.input', 'r')
    content = input.read()

    split_content =  content.split(" ")
    return map(lambda x: int(x),split_content)

counter = 0




def part_a():

    file_content_list =  get_file_content()


    iterate = True
    result_list = []


    node_amount_index, meta_data_size_index = (0, 1)
    while iterate:


        if file_content_list[node_amount_index] > 0:
            parent = (node_amount_index, meta_data_size_index)
            node_amount_index+=2
            meta_data_size_index=node_amount_index+1
        if file_content_list[node_amount_index] == 0:
            file_content_list[parent[0]] -= 1
            result_list.append(file_content_list[meta_data_size_index+1:meta_data_size_index+file_content_list[meta_data_size_index]+1])
            file_content_list = file_content_list[:node_amount_index] + file_content_list[meta_data_size_index+file_content_list[meta_data_size_index]+1:]
            if len(file_content_list) ==0:
                break
            node_amount_index,meta_data_size_index = (0,1)

    print result_list
    return sum(sum(result_list,[]))


if __name__ == "__main__":
    print "Result part A: "+str(part_a()) #35852
   











