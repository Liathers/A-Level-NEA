from threading import Thread

from BaseClass import *

class SocketClientListenerThread(BaseClass, Thread):
    def __init__(self, parent, socket):
        Thread.__init__(self)
        super().__init__()

        self.parent = parent
        self.socket = socket
        self.daemon = True

        self.start()

    def run(self):
        self.output("Listening for messages")
        while True:
            try:
                messageEncoded = self.socket.recv(1024)
                if messageEncoded:
                    message = messageEncoded.decode()

                    if message.startswith("[MESSAGERELAY]"):
                        message = message.replace("[MESSAGERELAY]", "")
                        self.output(f"{message}")

                    elif message.startswith("[MESSAGESERVER]"):
                        message = message.replace("[MESSAGESERVER]", "")
                        self.output(f"[Server] {message}")

                    elif message.startswith("[CONNECTED]"):
                        message = message.replace("[CONNECTED]", "")
                        self.output(f"[{message}] Connected to the chatroom")
                        self.parent.username.append(message)

                    elif message.startswith("[DISCONNECTED]"):
                        message = message.replace("[DISCONNECTED]", "")
                        self.output(f"[{message}] Disconnected from the chatroom")
                        self.parent.username.remove(message)
                        
                    else:
                        self.output(f"[Client] Recieved uncategorised message {message}")
                else:
                    self.output(f"[Disconnect] Client disconnected.")
                    self.socket.close()
                    break
            except:
                continue