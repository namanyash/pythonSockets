# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 10:25:59 2023

@author: Naman Yash
"""

import socket

def main():
    server_host = "127.0.0.1"  # Listen on the localhost
    server_port = 7879  # Choose a port number

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    print("Connected to server")

    username = "namanyash"
    password = "namanpass"
    
    
    client_socket.send(username.encode())
    print("Username sent to the server")
    print("Server Acknowledgement: {client_socket.recv(1024).decode()}")
    
    client_socket.send(password.encode())
    
    print("Password sent to the server")

    response = client_socket.recv(1024).decode()
    print("Result")
    print(response)

    client_socket.close()

if __name__ == "__main__":
    main()
