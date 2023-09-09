# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 11:11:21 2023

@author: Naman Yash
"""

import socket
import os
import hashlib

def generate_challenge():
    # Generate a random challenge (for example, using os.urandom)
    challenge = os.urandom(16)
    return challenge

def authenticate(challenge, response, password):
    # Calculate the expected response based on the challenge and password
    expected_response = hashlib.sha256(challenge + password.encode()).digest()
    return response == expected_response

def main():
    server_host = "127.0.0.1"
    server_port = 7879

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(1)

    print(f"Server listening on {server_host}:{server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Generate and send a challenge to the client
        challenge = generate_challenge()
        client_socket.send(challenge)

        # Receive the client's response
        response = client_socket.recv(1024)

        # Simulate server processing
        if authenticate(challenge, response, "your_password"):
            print("Success: Authentication successful")
            client_socket.send(b"Success: Authentication successful")
        else:
            client_socket.send(b"Failure: Authentication failed")
            print("Failure: Authentication Failed")

        client_socket.close()

if __name__ == "__main__":
    main()
