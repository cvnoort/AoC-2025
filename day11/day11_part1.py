#!/usr/bin/python3
import sys


def get_devices(file) -> dict:
    devices = {}
    with open(file) as file: 
        for line in file:
            device, connections = line.split(":")
            devices[device] = connections.strip().split(" ")
    return devices

def follow_path(paths, devices) -> list:
    for i, device in enumerate(paths):
        if device != "out":
            paths[i] = devices[device]
        else:
            paths[i] = [device]
    return paths


if __name__ == "__main__":

    devices = get_devices(sys.argv[1])
    paths = ["you"]

    while not all(device == "out" for device in paths):
        paths = sum(follow_path(paths, devices), [])

    print('There are', len(paths), 'paths from "you" to "out"')
