import json
import math

mars_radius = 3389.5    # km

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float, mars_radius: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

def meteor_ride(robot_speed: float):
    with open('sites.json', 'r') as f:
        sites_data = json.load(f)
    start_position = [16.0, 82.0]    # latitude, longitude
    position = start_position    # latitude, longitude
    total_time = 0.0    # s
    leg = 0
    sample_time = {'stony': 1, 'iron': 2, 'stony-iron': 3}
    
    for meteorite in sites_data:
        leg = leg+1
        leg_travel_time = calc_gcd(position[0], position[1], meteorite['latitude'], meteorite['longitude']) / robot_speed
        leg_sample_time = sample_time[meteorite['composition']]
        print(f'leg = {leg}, time to travel = %.2f hr, time to sample = {leg_sample_time} hr' % leg_travel_time)
        total_time = leg_travel_time + leg_sample_time
        position = [meteorite['latitude'], meteorite['longitude']]
    print('============================================================')
    print(f'number of legs = {leg}, total time elapsed = %.2f hr' % total_time)

meteor_ride(10)
