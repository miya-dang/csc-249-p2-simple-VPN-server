**Overview of Application**

This application consists of a client and a VPN server that forwards messages to a echo server. The VPN acts as an intermediary between the client and the remote server, forwarding client messages to the server and sending server responses back to the client.

**Client -> VPN Server Message**

Format: "SERVER_IP SERVER_PORT message"

Where:

SERVER_IP: The destination server's IP address.

SERVER_PORT: The destination server's port number.

message: The actual message that the client wants to send to the server.

Example: "127.0.0.1 8080 Hello, server!"


**VPN Server -> Client Message**

Format: The exact response as received by the destination server.

Example: If the destination server sends the message "Hello, server!", the message is returned exactly to the client: "Hello, server!".