#!/usr/bin/python3
import sys
from itertools import combinations


def get_coordinates(file) -> list:
    with open(file) as file: 
        coords = [tuple(int(n) for n in line.strip("\n").split(","))
                  for line in file]
    return coords

def calc_area(corner_a: tuple, corner_b: tuple) -> int:
    length_x = abs(corner_a[0] - corner_b[0]) + 1
    length_y = abs(corner_a[1] - corner_b[1]) + 1
    return length_x * length_y


if __name__ == "__main__":

    coordinates = get_coordinates(sys.argv[1])
    areas = [{"coords": combo, "area": calc_area(*combo)} 
             for combo in combinations(coordinates, 2)]
    
    max_area = max(areas, key=lambda combo: combo["area"])["area"]

    print("The largest possible area between two tiles is", max_area)
