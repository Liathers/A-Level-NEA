from queue import Queue, Empty
from threading import Thread
from socket import socket
from asyncio import new_event_loop, set_event_loop

from BaseClass import *
from SocketsFramework.SocketClientListenerThread import *

class SocketClientThread(BaseClass, Thread):
    def __init__(self, ip, port, name):
        Thread.__init__(self)
        super().__init__()

        self.socket = None
        self.ip = ip
        self.port = port
        self.name = name
        self.usernames = []

        self.queue = Queue()
        self.exit = False

        self.start()

    def onThread(self, function, *args, **kwargs):
        self.queue.put((function, args, kwargs))

    def stop(self):
        self.exit = True

    def run(self):
        self.socket = socket()
        self.socket.connect((self.ip, self.port))
        self.output(f"Established connection to {self.ip}:{self.port}")

        self.socket.send(f"[CLIENTINFO]{self.name}[USERNAME]".encode())
        self.output("Notified server of username")

        SocketClientListenerThread(self, self.socket)

        loop = new_event_loop()
        set_event_loop(loop)
        loop.run_until_complete(self.runEventLoopAsync())

    async def runEventLoopAsync(self):
        while not self.exit:
            try:
                function, args, kwargs = self.queue.get(timeout=1.0/60)
                await function(*args, **kwargs)
            except Empty:
                pass

        self.closeSocketServerConnection()

    async def sendMessageAsync(self, message):
        outboundMessage = f"[MESSAGE]{message}"
        outboundMessageEncoded = outboundMessage.encode()
        self.socket.send(outboundMessageEncoded)
        self.output(f"Sent message \"{message}\" to server")

    def sendMessage(self, message):
        self.onThread(self.sendMessageAsync, message)

    def closeSocketServerConnection(self):
        self.socket.close()
        self.output("Closed socket")
