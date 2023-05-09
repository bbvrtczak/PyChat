#Chat Application
This is a simple chat application that allows multiple clients to connect to a server and communicate with each other.

#Getting Started
Follow these steps:

1. Clone this repository to your local machine.
2. Open a terminal or command prompt and navigate to the directory where you cloned the repository.
3. Start the server by running python server.py. The server will start listening for client connections on port 8000.
4. Start the client by running python client.py. You will be prompted to enter your nickname, which will be used to identify you in the chat.
5. If you want to run the client on a different computer than the server is hosted, change the 'SERVER_HOST' variable in the 'client.py' script to the IP address of the server's computer.
6. Start chatting! You can send messages to other clients by typing in the client console and pressing Enter.
7. You can disconnect using the 'exit' message.

#Features
Multiple clients can connect to the server and communicate with each other.
The server sends a message to all clients when a new client joins the chat.
The client shows the nickname of the sender before the message in the client console.
