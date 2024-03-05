import socket

HOST = "127.0.0.1"
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


    connect, address = sock.accept()

    with connect:
        print(f"Connected by {address}")
        while True:
            data = connect.recv(BUFFER).decode()
            if len(data) > 0:
                print("Received data: " + data)
            else:
                break

    connect.close()

        



    
    

if __name__ == "__main__":
    main()