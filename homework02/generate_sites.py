import json
import random
import math

def generate_data(num_of_data):
    sites = []
    for i in range(num_of_data):
        meteorite = {}
        meteorite['site_id'] = i
        meteorite['latitude'] = random.random() * 2 + 16
        meteorite['longitude'] = random.random() * 2 + 82
        comp_list = ['stony', 'iron', 'stony-iron']
        comp_type = random.random() * 3
        while (comp_type == 3.0):
            comp_type = random.random() * 3
        meteorite['composition'] = comp_list[ math.floor(comp_type) ]
        sites.append(meteorite)
    return sites

data = generate_data(5)
with open('sites.json', 'w') as output:
    json.dump(data, output, indent = 2)
