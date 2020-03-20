#!/usr/bin/env python3

'''
Swarm main

Author: Patrick Kelly
Email: patrickyunen@gmail.com
Last revised: March 20, 2020
'''

import sys
import socket
import random
import time
import threading


class Swarm:
    def __init__(self, occupied_ports):
        self.occupied_ports = occupied_ports

    #Start up a server at a random port, avoiding numbers in the 'occupied_ports' attribute
    def server(self, low, high, lifetime):
        while True:
            port = random.randrange(low, high) # portnumber space to be used; can range from 1 - 65535
            if port in self.occupied_ports:
                continue
            self.occupied_ports.append(port)
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                server.bind(('', port))
                server.listen(5)
            except OSError: # raised when a port is already in use
                continue
            time.sleep(lifetime)
            server.close()
            self.occupied_ports.remove(port)

    def launch(self, low=1, high=400, lifetime=5, number=5):
        ports_dict = {}  #Create a dictionary of thread names, one for each port
        for i in range(number):
            ports_dict[i] = f't{i}'

        for index in ports_dict: #Create and run a thread for each entry in jumping_ports_dict
            ports_dict[index] = threading.Thread(target=self.server, args=(low,high,lifetime))
            ports_dict[index].start()


