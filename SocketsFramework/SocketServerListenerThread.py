from threading import Thread

from BaseClass import *

#This class is used to define a thread that will be used to listen for incoming message from a client to the server
class SocketServerListenerThread(BaseClass, Thread):
    def __init__(self, parent, socket):
#Prepare the thread and also get the base functions from BaseClass
        Thread.__init__(self)
        super().__init__()

#Define variables that will be needed throughout the class
        self.parent = parent
        self.connection = [socket, ""]
        self.info = self.connection[0].getpeername()
        self.daemon = True

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
                    try:
                        message = self.parent.handleSocketEncryption(1, None, messageEncoded)
                    except Exception as e:
                        self.output(f"[Error] {e}")

#If the message is client info, reming the header and see what type of client info it is
                    if message.startswith("[CLIENTINFO]"):
                        message = message.replace("[CLIENTINFO]", "")

#If the message is a username, name the connection within this thread and also the Server thread, and also
#notify the other connected clients of the fact another connection has been established
                        if message.endswith("[USERNAME]"):
                            self.connection[1] = message.replace("[USERNAME]", "")
                            self.parent.nameClient(self.connection[0], self.connection[1])
                            #self.output(f"Client {self.info[0]}:{self.info[1]} assigned username \"{self.connection[1]}\"")
                            self.parent.broadcastFromAuthorToClients(self.connection[0], f"[CONNECTED]{self.connection[1]}")

#If the incoming message is just a message, output it to the user, and also broadcase it to the other clients
#that are connected to the server
                    elif message.startswith("[MESSAGE]"):
                        message = message.replace("[MESSAGE]", "")
                        message = f"<{self.connection[1]}> {message}"
                        self.output(f"{message}")
                        self.parent.broadcastFromAuthorToClients(self.connection[0], f"[MESSAGERELAY]{message}")

#If the recieved message is uncategorised, notify the user accordingly and output the message
                    else:
                        self.output(f"[Unhandled] Recieved uncategorised message {message}")
#If unable to establish a connection, disconnect the client
                else:
                    self.parent.disconnectClient(self.connection[0], self.info)
                    break
#If unable to establish a connection, disconnect the client
            except:
                self.parent.disconnectClient(self.connection[0], self.info)
                break