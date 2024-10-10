#!/usr/bin/env python3

import socket
import arguments
import argparse

# Run 'python3 client.py --help' to see what these lines do
parser = argparse.ArgumentParser('Send a message to a server at the given address and print the response')
parser.add_argument('--server_IP', help='IP address at which the server is hosted', **arguments.ip_addr_arg)
parser.add_argument('--server_port', help='Port number at which the server is hosted', **arguments.server_port_arg)
parser.add_argument('--VPN_IP', help='IP address at which the VPN is hosted', **arguments.ip_addr_arg)
parser.add_argument('--VPN_port', help='Port number at which the VPN is hosted', **arguments.vpn_port_arg)
parser.add_argument('--message', default=['Hello, world'], nargs='+', help='The message to send to the server', metavar='MESSAGE')
args = parser.parse_args()

SERVER_IP = args.server_IP  # The server's IP address
SERVER_PORT = args.server_port  # The port used by the server
VPN_IP = args.VPN_IP  # The server's IP address
VPN_PORT = args.VPN_port  # The port used by the server
MSG = ' '.join(args.message) # The message to send to the server

def encode_message(message):
    """
    Encodes the message by adding an application-layer header that the VPN server can use to forward to the destination server.

    Parameters:
    message (str): The message to send to the destination server.

    Returns:
    str: The encoded message to send to the VPN server, format "SERVER_IP SERVER_PORT message".
    """
    messages = (SERVER_IP, str(SERVER_PORT), message)
    message = " ".join(messages)
    return message


print("client starting - connecting to VPN at IP", VPN_IP, "and port", VPN_PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((VPN_IP, VPN_PORT))
    print(f"connection established, sending message '{encode_message(MSG)}'")
    s.sendall(bytes(encode_message(MSG), 'utf-8'))
    print("message sent, waiting for reply")
    data = s.recv(1024).decode("utf-8")

print(f"Received response: '{data}' [{len(data)} bytes]")
print("client is done!")
