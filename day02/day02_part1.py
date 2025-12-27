#!/usr/bin/python3
import sys


def get_ids(file) -> list:
    with open(file) as file: 
        ids = sum([line.strip(",\n").split(",") for line in file], [])
    return ids

def find_invalid_ids(ids: str) -> list:

    [start, end] = ids.split("-")
    start_int = int(start)
    end_int = int(end)
    invalid_ids = []
    n = start_int

    while n in range(start_int, end_int+1):
        n_digits = len(str(n))
        if n_digits % 2 != 0:
            n += 1
            continue
        first_half = str(n)[0:int(n_digits/2)]
        second_half = str(n)[int(n_digits/2):n_digits]
        if first_half == second_half:
            invalid_ids.append(n)
            n = int(str(int(first_half)+1) + str(int(second_half)+1))
            continue
        n += 1
    
    return invalid_ids


if __name__ == "__main__":
    all_ranges = get_ids(sys.argv[1])
    all_invalid = sum([find_invalid_ids(x) for x in all_ranges], [])
    print("The sum of all the invalid IDs is", sum(all_invalid))
