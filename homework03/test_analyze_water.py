from analyze_water import calculate_average_turbidity
from analyze_water import calculate_minimum_safe_time
import pytest

def test_calculate_average_turbidity_math():
    assert calculate_average_turbidity([{'a': 1, 'b': 2}], 'a', 'b') == 2    # list length 1
    assert calculate_average_turbidity([{'a': 1, 'b': 2}, {'a': 1, 'b': 2}, {'a': 1, 'b': 2}], 'a', 'b') == 2    # list length > 1
    assert calculate_average_turbidity([{'a': 1, 'b': 2}, {'a': 2, 'b': 3}, {'a': 3, 'b': 4}, {'a': 4, 'b': 5}], 'a', 'b') == 10    # list length > 1, different values

def test_calculate_average_turbidity_exceptions():
    with pytest.raises(KeyError):
        calculate_average_turbidity([{'a': 1, 'b': 2}], 'c', 'd')    # wrong keys
    with pytest.raises(KeyError):
        calculate_average_turbidity([{'a': 1, 'b': 2}, {'c': 1, 'd': 2}], 'a', 'b')    # inconsistent keys
    with pytest.raises(TypeError):
        calculate_average_turbidity([{'a': 'a', 'b': 'b'}], 'a', 'b')    # wrong data types (not floats)

def test_calculate_minimum_safe_time_math():    # assumes safe water threshold = 1, decay constant == 0.02
    assert calculate_minimum_safe_time(1) == 0    # current turbidity = safe threshold (unused in analyze_water)
    assert calculate_minimum_safe_time(0.5) < 0    # current turbidity < safe threshold (unused in analyze_water)
    assert round(calculate_minimum_safe_time(1.5)) == 20    # current turbidity > safe threshold

def test_calculate_minimum_safe_time_exceptions():
    with pytest.raises(ZeroDivisionError):
        calculate_minimum_safe_time(0)    # current turbidity = 0
    with pytest.raises(TypeError):
        calculate_minimum_safe_time('0')    # wrong data type (not float)


