# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 10:22:24 2023

@author: Naman Yash
"""

import socket

def authenticate(username, password):
    # Replace with your own username and password validation logic
    valid_username = "namanyash"
    valid_password = "namanpass"
    return username == valid_username and password == valid_password

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

        # Receive username from the client
        username = client_socket.recv(1024).decode()
        print(f"username {username}")
        
        # Simulate server processing
        # In practice, you should replace this with your authentication logic
        client_socket.send(b"Username received")

        # Receive password from the client
        password = client_socket.recv(1024).decode()
        print(f"password {password}")
        
        if authenticate(username, password):
            print("Success: Authentication successful")
            client_socket.send(b"Success: Authentication successful")
        else:
            client_socket.send(b"Failure: Authentication failed")
            print("Failure: Authentication Failed")

        client_socket.close()

if __name__ == "__main__":
    main()
