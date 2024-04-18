from threading import Thread

from BaseClass import *

#This class will be used to host a thread that will be used for the client to listen for messages that are
#incoming from the host socket
class SocketClientListenerThread(BaseClass, Thread):
    def __init__(self, parent, socket):
#Prepare the thread and also get the base functions from BaseClass
        Thread.__init__(self)
        super().__init__()

#Define variables that will be needed throughout the class
        self.parent = parent
        self.socket = socket
        self.daemon = True

#Start the thread
        self.start()

#Execute this function as the thread is running
    def run(self):
#Run this as long as the thread is running
        while True:
            try:
#Try to recieve a message from the socket
                messageEncoded = self.socket.recv(1024)
#If one is recieved, decode the message and then do logic surrounding it
                if messageEncoded:
                    message = self.parent.handleSocketEncryption(1, None, messageEncoded)

#If the message is a relay of another client, then simply output it to the user
                    if message.startswith("[MESSAGERELAY]"):
                        message = message.replace("[MESSAGERELAY]", "")
                        self.output(f"{message}")

#If the message is the server directly telling the user, output it to the user
                    elif message.startswith("[MESSAGESERVER]"):
                        message = message.replace("[MESSAGESERVER]", "")
                        self.output(f"[Server] {message}")

#If the message is a client connecting to the session, notify the user and append it to the connected users list
#for the client to keep track
                    elif message.startswith("[CONNECTED]"):
                        message = message.replace("[CONNECTED]", "")
                        self.output(f"[{message}] Connected to the chatroom")
                        self.parent.username.append(message)

#If the message is a client disconnecting from the session, notify the user and also remove it from the
#connected users list
                    elif message.startswith("[DISCONNECTED]"):
                        message = message.replace("[DISCONNECTED]", "")
                        self.output(f"[{message}] Disconnected from the chatroom")
                        self.parent.username.remove(message)

#If the recieved message is uncategorised, notify the user accordingly and output the message
                    else:
                        self.output(f"[Client] Recieved uncategorised message {message}")
#If the client disconnects, notify the user and close the socket, as well as ending the thread
                else:
                    self.output(f"[Disconnect] Client disconnected.")
                    self.socket.close()
                    break
            except:
                continue