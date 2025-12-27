#!/usr/bin/python3
import sys


def get_banks(file) -> list:
    with open(file) as file: 
        banks = [[int(battery) for battery in line.strip("\n")] for line in file]
    return banks

def calc_joltage(a: int, b: int) -> int:
    joltage = int(str(a) + str(b))
    return joltage

def find_max_joltage(bank: list):
    first_digit = max(bank[:len(bank)-1])
    first_digit_idx = bank.index(first_digit)
    second_digit = max(bank[first_digit_idx+1:])
    max_joltage = calc_joltage(first_digit, second_digit)
    return max_joltage


if __name__ == "__main__":
    banks = get_banks(sys.argv[1])
    max_joltages = [find_max_joltage(bank) for bank in banks]
    print("The total output joltage is ", sum(max_joltages))
