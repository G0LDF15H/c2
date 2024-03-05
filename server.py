import socket

HOST = "127.0.0.1"
PORT = 80
BUFFER = 1024


# server set up
def main():
    print('running shell')

    # AF_INET is the address family ipv4, SOCK_STREAM is the socket protocol TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.sendetsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind((HOST, PORT))
    sock.listen(5) # number of client connections we can accept

    while True:
        connect, address = sock.accept()
        data = connect.recv(BUFFER).decode()

        if len(data) > 0:
            print("Received data: " + data)
        
        break

    connect.close()
        



    
    

if __name__ == "__main__":
    main()