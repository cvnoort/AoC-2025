#!/usr/bin/python3
import sys
import numpy as np
import numpy.typing as npt


def get_diagram(file) -> npt.NDArray:
    with open(file) as file: 
        diagram = np.array( [list(line.strip("\n")) for line in file] )
    return diagram

def find_start_coord(diagram: npt.NDArray) -> tuple:
    start = np.where(diagram == "S")
    return start

def move_beam(diagram: npt.NDArray, coord: tuple) -> list:
    x, y = coord
    if diagram[(x+1,y)] == "^":
        new_coord = [(x+1, y-1), (x+1, y+1)]
    else:
        new_coord = [(x+1, y)]
    return new_coord


if __name__ == "__main__":
    splitter_diagram = get_diagram(sys.argv[1])
    beams = [find_start_coord(splitter_diagram)]
    splits = 0
    for row in range(0, len(splitter_diagram) - 1):
        prev_count = len(beams)
        beams = sum([move_beam(splitter_diagram, beam) for beam in beams], [])
        splits += (len(beams) - prev_count)
        for i, beam in reversed(list(enumerate(beams))):
            if beam in beams[:i]:
                beams.pop(i)

    print("Number of times the beam will be split:", splits)
