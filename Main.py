from pyfiglet import Figlet
from time import sleep
from sys import argv

from BaseClass import *
from SocketsFramework.SocketServerThread import *
from SocketsFramework.SocketClientThread import *

#TODO Create list of different sources for program, this can be summarised in the Documentation Bibliography, includes things like w3schools and also the NEA guide eBook
#TODO End user "role" is communicator

#This is the main class that is used to interact with the project
class Main(BaseClass):
    def __init__(self):

#Define required variables for use later
        self.title = self.__class__.__name__
        self.figletFont = Figlet(font='small')

#Output the title of the program using ascii text art
        print(self.figletFont.renderText('ACommunicateSecure'))

#Process any potential launch arguments, and start the appropriate functions
        self.processLaunchArgsAndStart()

#Process the launch arguments and start the program accordingly
    def processLaunchArgsAndStart(self):
#Obtain any launch arguments and remove entry 0, as it is useless for what it's needed for
        arguments = argv
        arguments.pop(0)
#If there are arguments, do this
        if len(arguments) > 0:
#Notify the user that arguments have been found
            self.output(f"Found arguments: {arguments}")
            try:
#If the launch arguments are intended to launch the server, do this
                if arguments[0] == "server":
#Notify the user, and print out role using ascii text art
                    self.output("Server being launched based on starting args")
                    print(self.figletFont.renderText('Hosting Server'))
#Start the thread that processes everything related to the socket server
                    SocketServerThread("0.0.0.0", int(arguments[1]), arguments[2], arguments[3])

#Loop indefinately to ensure that the program remains running
                    while True:
                        1 == 1

#If the launch arguments are intended to launch the client, do this
                if arguments[0] == "client":
#Notify the user, and print out role using ascii text art
                    self.output("Client being launched based on starting args")
                    print(self.figletFont.renderText('Chat Client'))
#Start the thread that processes everything related to the socket client, and assign it to a variable
                    clientThread = SocketClientThread(arguments[1], int(arguments[2]), arguments[3], arguments[4], arguments[5])

#Establish connected variable and loop whilst it remains true
                    connected = True
                    while connected:
#Ask for user input, and process what is sent
                        message = input()
#If leave command, disconnect from server, and ask user for further actions
                        if message.lower() == "!leave":
                            clientThread.stop()
                            print("\Disconnected from server.")
                            connected = False
                            self.askActionInput()
#If the input is not a command, send the message to the server using the client socket
                        else:
                            clientThread.sendMessage(message)
                            sleep(0.5)
#If invalid arguments are found, ignore them
            except:
                self.output("Invalid arguments have been found, starting normally.\n")
                print("Welcome! You can either connect to a currently active chatroom or host a chatroom yourself.")
                self.askActionInput()
                pass
#If no arguments are found, start the program normally
        else:
            print("Welcome! You can either connect to a currently active chatroom or host a chatroom yourself.")
            self.askActionInput()

#Ask the user what they want to do, whether that be start the server, start the client or exit the program
    def askActionInput(self):
#Define action as none, and print out options
        action = None

        print("\nActions:")
        print("- Host a chatroom (1)")
        print("- Connect to a chatroom (2)")
        print("- Exit program (3)")

#While action has not been defined, do this
        while action == None:
#Ask user for action, if it cannot be converted to int, throw error and ask again
            actionInput = input("What would you like to do? ")

            try:
                actionInput = int(actionInput)
            except:
                print("[Error] Invalid input. Input something different")
                continue

#Check through list of accepted actions, and perform the appropriate function
            if actionInput == 1:
                self.actionHost()
                break
            elif actionInput == 2:
                self.actionJoin()
                break
            elif actionInput == 3:
                self.actionExit()
                break
#If the action is invalud, notify user and ask again
            else:
                print("[Error] Invalid action recieved. Input something different.")
                continue

#This function is used to host a chat server
    def actionHost(self):
#Notify the user and ask for properties around the server
        print("Initialising the creation of a server.")
        properties = self.askProperties(False)

#Notify the user, and display title using ascii text art
        print("Creating the socket server.\n")
        print(self.figletFont.renderText('Hosting Server'))
#Start the socket server thread and loop indefinately
        SocketServerThread("0.0.0.0", properties[1], properties[2], properties[3])
        while True:
            1 == 1

#This function is used to establish a connection with a preexisting server
    def actionJoin(self):
#Notify the user and ask for properties around the client
        print("Initialising the connection to a server")
        properties = self.askProperties(True)

#Notify the user and display title using ascii art, also notify user of commands
        print("Connecting to server..")
        print(self.figletFont.renderText('Chat Client'))
        print("To disconnect from the server, type \"!leave\"")
#Start the socket client thread and assign it to a variable
        clientThread = SocketClientThread(properties[0], properties[1], properties[2], properties[3], properties[4])

#Establish connected variable and loop whilst it remains true
        connected = True
        while connected:
#Ask for user input, and process what is sent
            message = input()
#If leave command, disconnect from server, and ask user for further actions
            if message.lower() == "!leave":
                clientThread.stop()
                print("\Disconnected from server.")
                connected = False
                self.askActionInput()
#If the input is not a command, send the message to the server using the client socket and then wait 0.5 seconds
            else:
                clientThread.sendMessage(message)
                sleep(0.5)

#This function is used to ask for properties reguarding the client or server
    def askProperties(self, client):
#Define variables to None for use later
        ip = None
        port = None
        algorithm = None
        key = None
        name = None

#If client is asking for properties, ask for IP address from the user
        if client:
            while ip == None:
                print("What IP Address do you wish to connect to?")
                ip = input("IP Address: ")

#Ask user for the port to be connected to
        print("\nWhat port do you wish to use? The value must be between 0 and 65535.")
#Loop whilst port is None
        while port == None:
            portInput = input("Port: ")
#If port is not in range, or cannot be converted into an int, notify the user and ask again, if
#the input is valid, assign it to port variable
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

#Ask the user what encryption algorithm to use, print out the options
        print("\Encryption Algorithms:")
        print("- Caesar Cipher (1)")
        while algorithm == None:
#Attempt to convert input to int, if not valid, or within established range the notify the user and ask again, if
#input is valid then assign appropriate value to algorithm variable
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

#Ask the user what key to use for encryption
        print("\nWhat do you want the key to be? This will need to coincide with the selected algorithm.")
        while key == None:
            keyInput = input("Key: ")
#Check what algorithm is being used, and if it is in the correct format, if not, notify the user and ask again
            if algorithm == "caesarcipher":
                try:
                    key = int(keyInput)
                except:
                    print("[Error] The key provided will not work with the selected algorithm.")
                    continue
#If an algorithm somehow hasn't been defined, notify the user and ask for all inputs again
#THIS SHOULD NOT HAPPEN
            else:
                print("[Error] An algorithm has not been selected. Therefore a key cannot be defined.")
                self.askActionInput()

#Ask the client what username to use. If the length is not in correct range, notify the user and ask again, if
#input is valid, assign it to name variable
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

#Return the values that have been provided
        return [ip, port, algorithm, key, name]
                
#This function is used to exit the program
    def actionExit(self):
#Notify the user and exit the program
        print("Exiting program!")
        exit(0)

#Start the main class
Main()