import operator
import re


def get_file_content():
    input = open('input/day03.input', 'r')
    lines = input.read().splitlines()
    return lines

def parse_input_line(line):
    match =  re.match(r'#([0-9]*)\s@\s([0-9]*),([0-9]*):\s([0-9]*)x([0-9]*)',line)
    id = match.group(1)
    claim_posX = int(match.group(2))
    claim_posY = int(match.group(3))
    claim_sizeX = int(match.group(4))
    claim_sizeY = int(match.group(5))

    return {"id":id,"posX":claim_posX,"posY":claim_posY,"sizeX":claim_sizeX,"sizeY":claim_sizeY}


def get_claim_by_id(claims,id):
    return filter(lambda claim: claim["id"] == id,claims)[0]

def get_claim_x_y_size(claim):
    clm = {}
    clm['x'] = (claim['claim_posX'] + claim['claim_sizeX'])
    clm['y'] = (claim['claim_posY']) + (claim['claim_sizeY'])
    clm['size'] =  clm['x'] * clm['y']
    return clm


def get_largest_claim(claims):
    clms = map(lambda claim: {"id": claim["id"], "size": get_claim_x_y_size(claim)['size']},claims)
    sorted_dict = sorted(clms, key=operator.itemgetter('size'), reverse=True)
    return sorted_dict[0]['id']


duplicates = []

def get_claim_coordinates(claim,full_coord_list):
    coord_list = []
    for x in range(claim['posX'], claim['posX'] + claim['sizeX']):
        for y in range(claim['posY'], claim['posY'] + claim['sizeY']):
            coord_set = (x,y)
            if coord_set not in duplicates:
                duplicates.append(coord_set)

            coord_list.append((x, y))



    return full_coord_list+coord_list


file_content = get_file_content()

parsed_claims = map(lambda claim: parse_input_line(claim),file_content)

full_coord_list = []
full_coord_list =  map(lambda claim: get_claim_coordinates(claim,full_coord_list),parsed_claims)
print duplicates



