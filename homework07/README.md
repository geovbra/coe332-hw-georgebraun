# ISS Data App Diagram

## Overview

This folder contains an image showing how the functions used for data management inside of the ISS data application here (https://github.com/geovbra/iss-data-tracker) interact with each other.

## Diagram Explanation

The diagram consists of 11 functions used to interact with the databases inside the ISS application, and 8 of these can be directly accessed by the user via their routes. However, these 8 routed functions perform one of two different tasks:
. Listing options inside the database (the functions beginning with `all_`)
. Displaying data for one of the options (the functions ending with `_data`)
In order to minimize redundant code, the two non-routed functions `all_key_values` and `all_key_value_data` perform these tasks respectively, only requiring a list of dictionaries and a key (as well as a value for the second function) as inputs.

Finally, the last function `is_data_loaded` simply checks if the databases being used are loaded into the Flask application's memory. Because every routed function uses this one (again, to minimize redundant code), I attempted to make it a decorator but ran into issues adding decorators alongside the route decorator.