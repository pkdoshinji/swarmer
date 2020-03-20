#!/usr/bin/env python3

'''
Swarm starter

Author: Patrick Kelly
Email: patrickyunen@gmail.com
Last revised: March 20, 2020
'''

import argparse
from swarmer import Swarm


def occupied_ports():
    num = int(input('Number of occupied ports: '))
    occupied = []
    for i in range(1, num + 1):
        port = int(input(f'Occupied port {i}: '))
        occupied.append(port)
    return occupied


def port_range():
    low = int(input('Lowest port number (inclusive): '))
    high = int(input('Highest port number (inclusive): ')) + 1
    return low, high

def get_lifetime():
    lifetime = int(input('Port lifetime (seconds): '))
    return lifetime

def get_number(swarm_num):
    lifetime = int(input(f'Number of ports in Swarm {swarm_num + 1}: '))
    return lifetime

def main():

    # Command line options (-o,-n) with argparse module:
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--occupied", action="store_true", help="occupied ports that should not be used")
    parser.add_argument("-n", "--number", type=int, default=1, help="number of swarms to launch")
    args = parser.parse_args()

    # Set variables with command-line inputs
    occupied = args.occupied
    swarmnumber = args.number

    # Get port numbers of occupied ports
    if occupied:
        occupied_list = occupied_ports()
    else:
        occupied_list = []

    # Instantiate Swarm object
    s = Swarm(occupied_list)

    # Get parameters for each swarm
    for swarm in range(swarmnumber):
        print(f'\n***Swarm {swarm + 1}***')
        number = get_number(swarm)
        low, high = port_range()
        lifetime = get_lifetime()
        s.launch(low, high, lifetime, number)
        print(f'***Swarm {swarm + 1} launched!***')


if __name__ == '__main__':
    main()



