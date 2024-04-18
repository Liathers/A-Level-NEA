from pyfiglet import Figlet
from time import sleep
from sys import argv

from BaseClass import *
from SocketsFramework.SocketServerThread import *
from SocketsFramework.SocketClientThread import *

#TODO Create list of different sources for program, this can be summarised in the Documentation Bibliography, includes things like w3schools and also the NEA guide eBook
#TODO End user "role" is communicator

class Main(BaseClass):
    def __init__(self):

        self.title = self.__class__.__name__
        self.figletFont = Figlet(font='small')

        print(self.figletFont.renderText('ACommunicateSecure'))

        self.processLaunchArgs()

        print("Welcome! You can either connect to a currently active chatroom or host a chatroom yourself.")
        self.askActionInput()

    def processLaunchArgs(self):
        arguments = argv
        arguments.pop(0)
        if len(arguments) > 0:
            self.output(f"Found arguments: {arguments}")
            try:
                if arguments[0] == "server":
                    self.output("Server being launched based on starting args")
                    print(self.figletFont.renderText('Hosting Server'))
                    SocketServerThread("0.0.0.0", int(arguments[1]), arguments[2], arguments[3])

                    while True:
                        1 == 1
                    
                if arguments[0] == "client":
                    self.output("Client being launched based on starting args")
                    print(self.figletFont.renderText('Chat Client'))
                    clientThread = SocketClientThread(arguments[1], int(arguments[2]), arguments[3], arguments[4], arguments[5])
                    
                    connected = True
                    while connected:
                        message = input()
                        if message.lower() == "!leave":
                            clientThread.stop()
                            print("\Disconnected from server.")
                            connected = False
                            self.askActionInput()
                        else:
                            clientThread.sendMessage(message)
                            sleep(0.5)
            except:
                pass
        else:
            pass

    def askActionInput(self):
        action = None

        print("\nActions:")
        print("- Host a chatroom (1)")
        print("- Connect to a chatroom (2)")
        print("- Exit program (3)")

        while action == None:
            actionInput = input("What would you like to do? ")

            try:
                actionInput = int(actionInput)
            except:
                print("[Error] Invalid input. Input something different")
                continue

            if actionInput == 1:
                self.actionHost()
                break
            elif actionInput == 2:
                self.actionJoin()
                break
            elif actionInput == 3:
                self.actionExit()
                break
            else:
                print("[Error] Invalid action recieved. Input something different.")
                continue

    def actionHost(self):
        print("Initialising the creation of a server.")

        properties = self.askProperties(False)

        print("Creating the socket server.\n")
        print(self.figletFont.renderText('Hosting Server'))
        SocketServerThread("0.0.0.0", properties[1], properties[2], properties[3])
        while True:
            1 == 1

    def actionJoin(self):
        print("Initialising the connection to a server")
        
        properties = self.askProperties(True)

        print("Connecting to server..")
        print(self.figletFont.renderText('Chat Client'))
        print("To disconnect from the server, type \"!leave\"")
        clientThread = SocketClientThread(properties[0], properties[1], properties[2], properties[3], properties[4])

        connected = True
        while connected:
            message = input()
            if message.lower() == "!leave":
                clientThread.stop()
                print("\Disconnected from server.")
                connected = False
                self.askActionInput()
            else:
                clientThread.sendMessage(message)
                sleep(0.5)

    def askProperties(self, client):
        ip = None
        port = None
        algorithm = None
        key = None
        name = None

        if client:
            while ip == None:
                print("What IP Address do you wish to connect to?")
                ip = input("IP Address: ")

        print("\nWhat port do you wish to use? The value must be between 0 and 65535.")
        while port == None:
            portInput = input("Port: ")
            try:
                portInput = int(portInput)
                if portInput >= 0 and portInput <= 65535:
                    port = portInput
                else:
                    print("[Error] Port input not within correct range. Input something different.")
                    continue
            except:
                print("[Error] Invalid input. Input something different.")
                continue
        
        print("\Encryption Algorithms:")
        print("- Caesar Cipher (1)")
        while algorithm == None:
            algorithmInput = input("Algorithm: ")
            try:
                algorithmInput = int(algorithmInput)
                if algorithmInput == 1:
                    algorithm = "caesarcipher"
                else:
                    print("[Error] Invalid algorithm. Input something different.")
                    continue
            except:
                print("[Error] Invalid input. Input something different.")
                continue

        print("\nWhat do you want the key to be? This will need to coincide with the selected algorithm.")
        while key == None:
            keyInput = input("Key: ")
            if algorithm == "caesarcipher":
                try:
                    key = int(keyInput)
                except:
                    print("[Error] The key provided will not work with the selected algorithm.")
                    continue
            else:
                print("[Error] An algorithm has not been selected. Therefore a key cannot be defined.")
                self.askActionInput()

        if client:
            print("\nWhat username do you wish to use? You have a limit of 16 characters.")
            while name == None:
                nameInput = input("Username: ")
                if len(nameInput) < 1:
                    print("[Error] Username too short. Input a username.")
                    continue
                elif len(nameInput) >= 16:
                    print("[Error] Username too long. Input a shorter username.")
                    continue
                name = nameInput

        return [ip, port, algorithm, key, name]
                

    def actionExit(self):
        print("Exiting program!")
        exit(0)

Main()