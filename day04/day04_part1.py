#!/usr/bin/python3
import sys
import numpy as np
import numpy.typing as npt


def get_diagram(file) -> npt.NDArray:
    with open(file) as file: 
        diagram = np.array( [list(line.strip("\n")) for line in file] )
    return diagram

def find_accessible(diagram: npt.NDArray) -> list:
    accessible_coords = []
    for (x, y), roll in np.ndenumerate(diagram):
        if roll == "@":
            adjacent_rolls = 0
            for x_surrounding in range(x-1,x+2):
                for y_surrounding in range(y-1, y+2):
                    if (x_surrounding in range(0, diagram.shape[0]) 
                        and y_surrounding in range(0, diagram.shape[1])):
                        if diagram[x_surrounding][y_surrounding] == "@":
                            adjacent_rolls += 1
            if adjacent_rolls <= 4:
                accessible_coords.append((x, y))
    
    return accessible_coords


if __name__ == "__main__":
    diagram = get_diagram(sys.argv[1])
    accessible_rolls = find_accessible(diagram)
    print("Number of rolls of paper that can be accessed by forklift:", 
          len(accessible_rolls))
