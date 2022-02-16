import json
import logging
import math

logging.basicConfig(level=logging.INFO)

SAFE_WATER_THRESHOLD = 1.
DECAY_FACTOR = .02

def calculate_average_turbidity(dict_list: list, calibration_key: str, current_key: str) -> float:
    """
    Calculates the average turbidity (T) in NTU units of any number of data points. The turbidity
    for each data point is calculated by simply multiplying the calibration constant with the
    90 degree detector current.

    Args:
        dict_list: A list of data dictionaries representing data points.
        calibration_key: A string representing the key for the calibration constant, a0.
        current_key : A string representing the key for the 90 degree detector current, I90.

    Returns:
        A float representing the average water turbidity of the data points.
    """

    count = 0
    turbidity_sum = 0
    for i in dict_list:
        count += 1
        turbidity_sum += i[calibration_key] * i[current_key]
    return turbidity_sum / count

def calculate_minimum_safe_time(current_turbidity: float) -> float:
    """
    Calculates the minimum time required before water turbidity decays to a safe level.
    The turbidity decay follows a standard exponential decay function with respect to time,
    so the function returns the time at which the current turbidity equals the safe threshold.

    Args:
        current_turbidity: A float representing the current turbidity of the water.
    
    Returns:
        A float representing the minimum time needed for the water turbidity to decay to a safe level.
    """

    return math.log(SAFE_WATER_THRESHOLD/current_turbidity) / math.log(1 - DECAY_FACTOR)

def main():
    with open('turbidity_data.json', 'r') as f:
        data = json.load(f)
    last_five_samples = data['turbidity_data'][-5:]
    
    average_turbidity = calculate_average_turbidity\
                        (last_five_samples, 'calibration_constant', 'detector_current')
    print(f'Average Turbidity based on most recent five measurements = %.4f NTU' % average_turbidity)
    
    if average_turbidity < SAFE_WATER_THRESHOLD:
        logging.info('Turbidity is below threshold for safe use')
        safe_time = 0
    else:
        logging.warning('Turbidity is above threshold for safe use')
        safe_time = calculate_minimum_safe_time(average_turbidity)
    print(f'Minimum time required to return below a safe threshold = %.2f hours' % safe_time)

if __name__ == '__main__':
    main()
