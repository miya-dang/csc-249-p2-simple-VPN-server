#!/usr/bin/env python3

import socket
import arguments
import argparse

# Run 'python3 VPN.py --help' to see what these lines do
parser = argparse.ArgumentParser('Send a message to a server at the given address and prints the response')
parser.add_argument('--VPN_IP', help='IP address at which to host the VPN', **arguments.ip_addr_arg)
parser.add_argument('--VPN_port', help='Port number at which to host the VPN', **arguments.vpn_port_arg)
args = parser.parse_args()

VPN_IP = args.VPN_IP  # Address to listen on
VPN_PORT = args.VPN_port  # Port to listen on (non-privileged ports are > 1023)

def parse_message(message):
    """
    # Parse the application-layer header into the destination SERVER_IP, destination SERVER_PORT,
    # and message to forward to that destination

    Args:
    message (bytes): Message received from the client.

    Returns:
    tuple: (SERVER_IP, SERVER_PORT, message)
    """
    message = message.decode("utf-8")
    
    # Split the message into parts, assuming the format is: "SERVER_IP SERVER_PORT message"
    msg_sections = message.split(' ', 2)
    SERVER_IP = msg_sections[0]
    SERVER_PORT = int(msg_sections[1])
    msg = msg_sections[2]
    
    return SERVER_IP, SERVER_PORT, msg
    
    

### INSTRUCTIONS ###
# The VPN, like the server, must listen for connections from the client on IP address
# VPN_IP and port VPN_port. Then, once a connection is established and a message recieved,
# the VPN must parse the message to obtain the server IP address and port, and, without
# disconnecting from the client, establish a connection with the server the same way the
# client does, send the message from the client to the server, and wait for a reply.
# Upon receiving a reply from the server, it must forward the reply along its connection
# to the client. Then the VPN is free to close both connections and exit.

# The VPN server must additionally print appropriate trace messages and send back to the
# client appropriate error messages.
print("VPN server starting - listening for connections at IP", VPN_IP, "and port", VPN_PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.bind((VPN_IP, VPN_PORT))
    client_socket.listen()

    conn, addr = client_socket.accept()
    with conn:
        print(f"Connection established with {addr}")
        data = conn.recv(1024)
        print(f"Received client message: '{data!r}' [{len(data)} bytes]")

        # Parse the message
        SERVER_IP, SERVER_PORT, message = parse_message(data)

        # Establish connection to the server and send the message
        print("VPN server connecting to destination server at IP", SERVER_IP, "and port", SERVER_PORT)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_IP, SERVER_PORT))
            print(f"connection established, sending message '{message}'")
            s.sendall(bytes(message, 'utf-8'))
            print("message forwarded, waiting for reply")
            reply = s.recv(1024)
            print(f"Received server response: '{reply!r}' [{len(reply)} bytes]")
            print("sending reply back to client")
            conn.sendall(reply)
print("VPN is done!")