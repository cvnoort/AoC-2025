#!/usr/bin/python3
import sys


def get_ingredients(file) -> list:

    with open(file) as file: 
        all_lines = [line.strip("\n") for line in file]

        fresh_ranges = [[int(x) for x in fresh_range.split("-")] 
                        for fresh_range in all_lines[:all_lines.index("")]]

        available_ids = [int(line.strip("\n")) 
                             for line in all_lines[all_lines.index("")+1:]]
        
    return [fresh_ranges, available_ids]

def find_fresh(ingredient_ids: list) -> int:

    fresh_ids = [ingredient_id for ingredient_id in ingredient_ids 
                       if any(id_range for id_range in fresh_ingredients 
                              if id_range[0] <= ingredient_id <= id_range[1])]

    return len(fresh_ids)


if __name__ == "__main__":
    [fresh_ingredients, available_ingredients] = get_ingredients(sys.argv[1])
    available_and_fresh = find_fresh(available_ingredients)
    print("Number of available ingredients that are fresh:", 
          available_and_fresh)
