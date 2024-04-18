from pyfiglet import Figlet
from sys import argv

from BaseClass import *
from SocketsFramework.SocketServerThread import *

class Main(BaseClass):
    def __init__(self):

        self.title = self.__class__.__name__
        self.projectName = "ACommunicateSecure"
        self.figletFont = Figlet(font='small')

        print(self.figletFont.renderText('ACommunicateSecure'))

        self.launchArgs = self.processLaunchArgs()

        if self.launchArgs:
            while True:
                1 == 1
        elif self.launchArgs == False:
            print("Welcome! You can either connect to a currently active chatroom or host a chatroom yourself.")
            self.askActionInput()

    def processLaunchArgs(self):
        arguments = argv
        arguments.pop(0)
        self.output(f"Found arguments: {arguments}")
        if len(arguments) > 0:
            try:
                if arguments[0] == "server":
                    self.output("Server being launched based on starting args")
                    print(self.figletFont.renderText('Hosting Server'))
                    SocketServerThread("0.0.0.0", int(arguments[1]), arguments[2], arguments[3])
                    return True
                    
                if arguments[0] == "client":
                    print(self.figletFont.renderText('Chat Client'))
                    self.output("Client being launched based on starting args")
                    print("There is no client launch atm")
                    return True
            except:
                return False

    def askActionInput(self):
        action = None

        print()
        print("Actions:")
        print("- Host a chatroom (1)")
        print("- Connect to a chatroom (2)")
        print("- Exit program (3)")

        while action == None:
            actionInput = input("What would you like to do? ").lower()

            try:
                actionInput = int(actionInput)
            except:
                print("[Error] Invalid input. Input something different")
                continue

            if actionInput == 1:
                self.actionHost()
            elif actionInput == 2:
                self.output("do join")
            elif actionInput == 3:
                self.actionExit()
            else:
                print("[Error] Invalid action recieved. Input something different.")
                self.askActionInput()

    def actionHost(self):
        port = None
        algorithm = None
        key = None

        print("Initialising the creation of a server.")

        print("What port do you wish to use? The value must be between 0 and 65535.")
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
        
        print()
        print("Which encryption algorithm do you wish to use?")
        print("Options:")
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

        print()
        print("What do you want the key to be? This will need to coincide with the selected algorithm.")
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

        print("Creating the socket server.\n")
        print(self.figletFont.renderText('Hosting Server'))
        SocketServerThread("0.0.0.0", port, algorithm, key)
        while True:
            1 == 1

    def actionExit(self):
        print("Exiting program!")
        exit(0)

Main()