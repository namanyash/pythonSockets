# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 11:11:53 2023

@author: Naman Yash
"""

import socket
import hashlib

def main():
    server_host = "127.0.0.1"
    server_port = 7879

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    # Receive the challenge from the server
    challenge = client_socket.recv(1024)

    # Calculate the response based on the challenge and password
    password = "your_password"
    response = hashlib.sha256(challenge + password.encode()).digest()

    # Send the response to the server
    client_socket.send(response)

    response = client_socket.recv(1024).decode()
    print(response)

    client_socket.close()

if __name__ == "__main__":
    main()
