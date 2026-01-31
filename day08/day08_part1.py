#!/usr/bin/python3
import sys
import numpy as np
import math
from itertools import combinations


def get_coordinates(file) -> list:
    with open(file) as file: 
        coords = [tuple(int(n) for n in line.strip("\n").split(","))
                  for line in file]
    return coords

def calc_distance(a: tuple, b: tuple) -> np.float64:
    distance = np.linalg.norm(np.array(a) - np.array(b))
    return distance

def get_distances(points: list) -> list:
    combos = [{"combo": combo, "distance": calc_distance(combo[0], combo[1])} 
              for combo in combinations(points, 2)]
    combos_sorted_by_distance = sorted(combos, 
                                       key=lambda combo: combo["distance"])
    return combos_sorted_by_distance


if __name__ == "__main__":

    coordinates = get_coordinates(sys.argv[1])
    all_distances = get_distances(coordinates)

    circuits = []

    for pair in all_distances[:1000]:
        
        boxes = pair["combo"]

        matches = [i for i, circuit in enumerate(circuits) 
                   if boxes[0] in circuit or boxes[1] in circuit]

        if len(matches) < 1:
            circuits.append([*boxes])
        elif len(matches) == 1:
            circuits[matches[0]] = list(set(circuits[matches[0]] + [*boxes]))
        elif len(matches) == 2 and matches[0] != matches[1]:
            connect_circuits = circuits.pop(matches[1]) + circuits.pop(matches[0])
            circuits.append(connect_circuits)

    circuit_sizes = [len(circuit) for circuit in circuits]
    circuit_sizes.sort(reverse=True)

    print("The product of the sizes of the three largest circuits is", 
          math.prod(circuit_sizes[:3]))
