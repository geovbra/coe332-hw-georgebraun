# Meteorite Investigation Trip Calculator

## General Overview

This project randomly generates meteorite landing sites on a small portion of the surface of Mars and tasks a robot to drive to and take samples at these sites sequentially. The time taken to drive from one site to the next as well as the time required to take samples of different meteorite types are taken into account, and these are summed into a total time that the robot will take to complete the trip. The trip immediately ends when the robot reaches and finishes sampling the last meteorite. This calculator is a bit limited in that it only simulates one possible path that the robot could take, which is simply the order of the landing sites in the data dictionary from first to last.

## Script Description

This project consists of 2 python files. The first, `generate_sites.py`, randomly generates data for 5 meteorite landing sites and stores it in a JSON file named `sites.json`. The second, `calculate_trip.py`, which will sequentially analyze the data of each landing site and calculate the time the robot must take to drive to and sample each of the meteorites. Each leg of the journey (starting when the robot leaves a site and ending when the robot finishes sampling the next site) is printed out on a separate line along with the time taken to complete it. After the trip is completed, the total time and number of legs are printed.

## Instructions

To run this project, first run the file `generate_sites.py`, which randomly generates data for 5 meteorite landing sites and stores it in a JSON file named `sites.json`. Next, run the file `calculate_trip.py`.

## Sample Output

`
leg = 1, time to travel = 8.51 hr, time to sample = 3 hr
leg = 2, time to travel = 6.55 hr, time to sample = 3 hr
leg = 3, time to travel = 5.88 hr, time to sample = 3 hr
leg = 4, time to travel = 5.42 hr, time to sample = 3 hr
leg = 5, time to travel = 4.29 hr, time to sample = 3 hr
============================================================
number of legs = 5, total time elapsed = 7.29 hr
`
