from threading import Thread

from BaseClass import *

#This class is used to define a thread that will be used to listen for incoming message from a client to the server
class SocketServerListenerThread(BaseClass, Thread):
    def __init__(self, parent, socket):
#Prepare the thread
        Thread.__init__(self)

#Define variables that will be needed throughout the class
        self.parent = parent
        self.connection = [socket, ""]
        self.info = self.connection[0].getpeername()
        self.daemon = True

#Change the title assigned to the class, so that outputting messages can be easier to destinguigh between connections
        self.title = f"{self.__class__.__name__} {self.info[0]}:{self.info[1]}"

#Start the thread
        self.start()

#Execute this function as the thread is executing
    def run(self):
#Run this as long as the thread is running
        while True:
#Attempt to recieve an incoming message from the client
            try:
                messageEncoded = self.connection[0].recv(1024)
#If a message is recieved, decode the message
                if messageEncoded:
                    message = messageEncoded.decode()

#If the message is client info, reming the header and see what type of client info it is
                    if message.startswith("[CLIENTINFO]"):
                        message = message.replace("[CLIENTINFO]", "")

#If the message is a username, name the connection within this thread and also the Server thread, and also
#notify the other connected clients of the fact another connection has been established
                        if message.endswith("[USERNAME]"):
                            self.connection[1] = message.replace("[USERNAME]", "")
                            self.parent.nameClient(self.connection[0], self.connection[1])
                            self.output(f"Client assigned username \"{self.connection[1]}\"")
                            self.parent.broadcastFromAuthorToClients(self.connection[0], f"[CONNECTED]{self.connection[1]}")

#If the incoming message is just a message, output it to the user, and also broadcase it to the other clients
#that are connected to the server
                    elif message.startswith("[MESSAGE]"):
                        message = message.replace("[MESSAGE]", "")
                        message = f"{self.connection[1]}: {message}"
                        self.output(f"[Recieved] {message}")
                        self.parent.broadcastFromAuthorToClients(self.connection[0], f"[MESSAGERELAY]{message}")

#If the recieved message is uncategorised, notify the user accordingly and output the message
                    else:
                        self.output(f"[Unhandled] Recieved uncategorised message {message}")
#If unable to establish a connection, notify the user of the disconnect, and remove the client from the list of
#connections as well as closing this thread
                else:
                    self.output(f"Client {self.info[0]}:{self.info[1]} disconnected.")
                    self.connection[0].close()
                    self.parent.removeClient(self.connection[0])
                    break
            except:
                continue