from threading import Thread

from BaseClass import *

class SocketClientListenerThread(BaseClass, Thread):
    def __init__(self, socket):
        Thread.__init__(self)
        super().__init__()

        self.socket = socket
        self.daemon = True

        self.start()

    def run(self):
        self.output("Listening for socket server messages")
        while True:
            try:
                messageEncoded = self.socket.recv(1024)
                if messageEncoded:
                    message = messageEncoded.decode()
                    messageFinal = message.replace("[SEPARATOR]", ": ")
                    self.output(f"[Server Sent] {messageFinal}")
                else:
                    self.output(f"[Disconnect] Client disconnected.")
                    self.socket.close()
                    break
            except:
                continue