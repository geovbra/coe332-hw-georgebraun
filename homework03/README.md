# Analyzing Mars Lab Water Turbidity

## Overview

This homework takes a dictionary of data points collected hourly from a water source on Mars and calculates the water's turbidity to determine whether it's safe to use for analyzing meteorite samples. The program uses the five most recent data points to calculate an average turbidity to mitigate measurement error. If the water is too cloudy, then collecting data from the meteorite samples will be ineffective.

## Requirements

To run this program, first enter the following line into your terminal:

```
   wget https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json
```

This retrieves the most up-to-date data dictionary of the water samples and stores it in turbidity_data.json. The program relies upon this to run.

## Script Explanation

The project consists of two python scripts. The first, analyze_water.py, takes the dictionary stored in turbidity_data.json and isolates the five most recent data points (also the last data points in the dictionary). The average turbidity of these data points is then calculated and evaluated to see if the water is safe to use (less than 1 NTU). If not, the program then calculates the minimum time required for the turbidity to decay to a safe level.

The second script, test_analyze_water.py, is simply a unit tester for analyze_water.py. It checks the most of the common cases and errors for the functions inside the first script, but there may still be a few ways to slip past the tester.

## Running the Program

To run the program, run the analyze_water.py script through the python interpreter:

```
   python3 analyze_water.py
```

The program will return the calculated turbidity of the water, whether it's safe to use or not, and the number of hours to wait until the water is usable.
Sample output:

```
    Average Turbidity based on most recent five measurements = 1.1542 NTU
    WARNING:root:Turbidity is above threshold for safe use
    Minimum time required to return below a safe threshold = 7.10 hours
```

**NOTE:** If the water turbidity is below the safe threshold, the minimum time will simply be 0 hours.