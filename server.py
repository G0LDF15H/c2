import socket

HOST = "localhost"
PORT = 3790
BUFFER = 1024


# server set up
def main():
    print('running shell')

    # AF_INET is the address family ipv4, SOCK_STREAM is the socket protocol TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind((HOST, PORT))

    while True:
        connect, address = sock.accept()
        data = connect.recv(BUFFER).decode()

        if len(data) > 0:
            print("Received data: " + data)
        
        break

    connect.close()
        



    
    

if __name__ == "__main__":
    main()