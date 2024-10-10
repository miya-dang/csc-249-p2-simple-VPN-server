Client Trace
% python3 client.py

client starting - connecting to VPN at IP 127.0.0.1 and port 55554
connection established, sending message '127.0.0.1 65432 Hello, world'
message sent, waiting for reply
Received response: 'Hello, world' [12 bytes]
client is done!


VPN Trace
% python3 VPN.py

VPN server starting - listening for connections at IP 127.0.0.1 and port 55554
Connection established with ('127.0.0.1', 62840)
Received client message: 'b'127.0.0.1 65432 Hello, world'' [28 bytes]
VPN server connecting to destination server at IP 127.0.0.1 and port 65432
connection established, sending message 'Hello, world'
message forwarded, waiting for reply
Received server response: 'b'127.0.0.1 65432 Hello, world'' [28 bytes]
sending reply back to client
VPN is done!


Echo Server Trace
% python3 echo-server.py

server starting - listening for connections at IP 127.0.0.1 and port 65432
Connection established with ('127.0.0.1', 62841)
Received client message: 'b'Hello, world'' [12 bytes]
echoing 'b'Hello, world'' back to client
server is done!