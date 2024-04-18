from queue import Queue, Empty
from threading import Thread
from socket import socket
from asyncio import new_event_loop, set_event_loop

from BaseClass import *
from SocketsFramework.SocketClientListenerThread import *
from EncryptionFramework.EncryptionHandler import *

#This class will be used for the main thread of the client, so that it can interact with the
#socket server
class SocketClientThread(BaseClass, Thread):
    def __init__(self, ip, port, algorithm, key, name):
#Prepare the thread and also get the base functions from BaseClass
        Thread.__init__(self)
        super().__init__()

#Define variables that will be needed throughout the class
        self.socket = None
        self.ip = ip
        self.port = port
        self.name = name
        self.usernames = []

#Define variables related to encryption
        self.algorithm = algorithm
        self.key = key
        self.encryptionHandler = EncryptionHandler()

#Define variables related to threading
        self.queue = Queue()
        self.exit = False

#Start the thread
        self.start()

#If a funciton is requested, add it to the queue so it can be executed later
    def onThread(self, function, *args, **kwargs):
        self.queue.put((function, args, kwargs))

#If the thread is told to exit, do so accordingly
    def stop(self):
        self.exit = True

#Execute this function as the thread is running
    def run(self):
#Create the socket and connect to the host server, if a connection cannot be established, notify the user
#and stop the thread from running
        self.socket = socket()
        try:
            self.socket.connect((self.ip, self.port))
            self.output(f"Established connection to {self.ip}:{self.port}")
        except:
            self.output("Failed to establish connection, closing thread")
            self.stop()

#Notify the server of the client username that is used, with the use of encryption
        self.handleSocketEncryption(0, self.socket, f"[CLIENTINFO]{self.name}[USERNAME]")

#Initialise the thread that is used to recieve messages from the server
        SocketClientListenerThread(self, self.socket)

#Create an async event loop and run it, this is so functions can be requested from outside the thread
        loop = new_event_loop()
        set_event_loop(loop)
        loop.run_until_complete(self.runEventLoopAsync())

#Run the event loop whilst the thread is not told to exit
    async def runEventLoopAsync(self):
        while not self.exit:
#Attempt to execute the next function within the queue if there is one, if not, loop again
            try:
                function, args, kwargs = self.queue.get(timeout=1.0/60)
                await function(*args, **kwargs)
            except Empty:
                pass

#Once self.exit = true, close the connection to the server so the thread can be destroyed
        self.closeSocketServerConnection()

#Send defined message to the server
    async def sendMessageAsync(self, message):
#Format the message so the server knows what type of info is being sent
        outboundMessage = f"[MESSAGE]{message}"
#Send the message to get encrypted and then sent to the specified socket
        self.handleSocketEncryption(0, self.socket, outboundMessage)

#This is used to call the sendMessageAsync function from outside the thread
    def sendMessage(self, message):
        self.onThread(self.sendMessageAsync, message)

#This is used to encrypt outbound messages, and then encode and send the message to the defined socket
    def handleSocketEncryption(self, action, socket, message):
#If the action is 0, encode and then send the message
        if action == 0:
#Encrypt the message using the key and algorithm specified
            message = self.encryptionHandler.doAction(action, self.algorithm, self.key, message)
            message = message.encode()
            try:
                socket.send(message)
            except:
                self.output("Disconnected from server")
                self.stop()

#If action is 1, decode and then return message
        elif action == 1:
            message = message.decode()
#Encrypt the message using the key and algorithm specified
            message = self.encryptionHandler.doAction(action, self.algorithm, self.key, message)
            return message

#Close the socket connection to the server
    def closeSocketServerConnection(self):
        self.socket.close()
