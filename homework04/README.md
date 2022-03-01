# Analyzing Data From Sets of Meteorites

## Overview

This folder contains instructions and resources to access and use a containerized program that analyzes data recorded from meteorite landing sites and returns a few general statistics about the sizes, locations, and types of meteorites in the list.

## Script Explanation

The project consists of two python scripts and a JSON file of sample data. The first python script, ml_data_analysis.py, requires a JSON file detailing the meteorites to be analyzed. The format for this data will be outlined later in the readme, but there is also sample data to test and refer to in Meteorite_landings.json. The python script takes this meteorite data and prints out:

* The average mass of the meteorites
* The number of meteorite landing sites in each of the Earth's quadrants
* The number of meteorites in different meteorite classes

The second script, test_ml_data_analysis.py, is simply a unit test suite for ml_data_analysis.py. It checks the most of the common cases and errors for the functions inside the first script and is a good way to verify that any future edits to these functions still produce correct results.

## Requirements

To use this container, you have to first pull it from Docker. Simply enter the following command into the terminal:

```
   docker pull geovbra/ml_data_analysis:hw04
```

This retrieves the container image from DockerHub and allows you to begin running the program.

Alternatively, you can run the `Dockerfile` included in this folder to build an image yourself, provided you have the two python scripts and the sample data in the same directory:

```
   docker build -t geovbra/ml_data_analysis:hw04 .
```

## Running the Program

If you want to simply run the container with the test data, use the following command:

```
   docker run --rm geovbra/ml_data_analysis:hw04 ml_data_analysis.py code/Meteorite_Landings.json
```

If you want to run the container with your own data or other data, use this command instead, making sure your JSON file is in the current directory and replacing "your_data_file" with the name of your file:

```
   docker run --rm -v $PWD:/data geovbra/ml_data_analysis:hw04 ml_data_analysis.py data/your_data_file.json
```

**NOTE:** Make sure that the meteorite data follows the format detailed below. Additional sample data can be found at this link:

https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json

This can be copied and pasted into a file or grabbed using 'wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json'

Sample output from sample data:

```
Summary data following meteorite analysis:

Average mass of 30 meteor(s):
83857.3 grams

Hemisphere Summary Data:
There were 21 meteors found in the Northern & Eastern quadrant
There were 6 meteors found in the Northern & Western quadrant
There were 0 meteors found in the Southern & Eastern quadrant
There were 3 meteors found in the Southern & Western quadrant

Class summary data:
The L5 class was found 1 times
The H6 class was found 1 times
The EH4 class was found 2 times
The Acapulcoite class was found 1 times
The L6 class was found 6 times
The LL3-6 class was found 1 times
The H5 class was found 3 times
The L class was found 2 times
The Diogenite-pm class was found 1 times
The Stone-uncl class was found 1 times
The H4 class was found 2 times
The H class was found 1 times
The Iron-IVA class was found 1 times
The CR2-an class was found 1 times
The LL5 class was found 2 times
The CI1 class was found 1 times
The L/LL4 class was found 1 times
The Eucrite-mmict class was found 1 times
The CV3 class was found 1 times

```
## Input Data

The input data should be structured as a data dictionary with the key "meteorite_landings" leading to a list of data dictionaries representing different meteorites, each containing the same keys for different details. Make sure that the data dictionaries you have use these specific keys to store these values:

* "mass (g)" - the mass of the meteorite
* "reclat" - the latitude of the meteorite landing site
* "reclong" - the longitude of the meteorite landing site
* "recclass" - the class of the meteorite

Sample input (just the first two meteorites of the sample data file):

```
{
  "meteorite_landings": [
    {
      "name": "Ruiz",
      "id": "10001",
      "recclass": "L5",
      "mass (g)": "21",
      "reclat": "50.775",
      "reclong": "6.08333",
      "GeoLocation": "(50.775, 6.08333)"
    },
    {
      "name": "Beeler",
      "id": "10002",
      "recclass": "H6",
      "mass (g)": "720",
      "reclat": "56.18333",
      "reclong": "10.23333",
      "GeoLocation": "(56.18333, 10.23333)"
    }
  ]
}
```

## Advanced Usage

To enter the container and make changes to the code, run this command:

```
docker run --rm -it geovbra/ml_data_analysis:hw04 /bin/bash
```

The scripts are located inside the `code` folder. After making changes to ml_data_analysis, run the unit test suite with the command `pytest` to ensure the functions still output correct values.