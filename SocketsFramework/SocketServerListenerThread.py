from threading import Thread

from BaseClass import *

class SocketServerListenerThread(BaseClass, Thread):
    def __init__(self, parent, socket):
        Thread.__init__(self)

        self.parent = parent
        self.connection = [socket, ""]
        self.info = self.connection[0].getpeername()
        self.daemon = True

        self.title = f"{self.__class__.__name__} {self.info[0]}:{self.info[1]}"

        self.start()

    def run(self):
        while True:
            try:
                messageEncoded = self.connection[0].recv(1024)
                if messageEncoded:
                    message = messageEncoded.decode()

                    if message.startswith("[CLIENTINFO]"):
                        message = message.replace("[CLIENTINFO]", "")
                        if message.endswith("[USERNAME]"):
                            self.connection[1] = message.replace("[USERNAME]", "")
                            self.parent.nameClient(self.connection[0], self.connection[1])
                            self.output(f"Client assigned username \"{self.connection[1]}\"")
                            self.parent.broadcastFromAuthorToClients(self.connection[0], f"[CONNECTED]{self.connection[1]}")


                    elif message.startswith("[MESSAGE]"):
                        message = message.replace("[MESSAGE]", "")
                        message = f"{self.connection[1]}: {message}"
                        self.output(f"[Recieved] {message}")
                        self.parent.broadcastFromAuthorToClients(self.connection[0], f"[MESSAGERELAY]{message}")
                    else:
                        self.output(f"[Unhandled] Recieved uncategorised message {message}")

                else:
                    self.output(f"Client {self.info[0]}:{self.info[1]} disconnected.")
                    self.connection[0].close()
                    self.parent.removeClient(self.connection[0])
                    break
            except:
                continue