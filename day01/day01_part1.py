#!/usr/bin/python3
import sys


def get_instructions(file) -> list:
    with open(file) as file: 
        instructions = [line.strip("\n") for line in file]
    return instructions

def rotate_dial(dial: int, rotation: str) -> int:

    if rotation[0] == "L":
        dial -= int(rotation[1:])
    elif rotation[0] == "R":
        dial += int(rotation[1:])

    if dial < 0 or dial > 99:
        dial -= 100 * (dial // 100)
    
    return dial

def get_password(
        instructions: list, dial_start: int = 50, password_start: int = 0
    ) -> int:
    
    dial = int(dial_start)
    password = password_start

    for rotation in instructions:
        dial = rotate_dial(dial, rotation)
        if dial == 0:
            password += 1
    
    return password


if __name__ == "__main__":
    rotations = get_instructions(sys.argv[1])
    password = get_password(rotations)
    print("The password is", password)
