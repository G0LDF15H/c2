import socket

HOST = ''
PORT = 3790
# client
def main():
    HOST = input("give me a host to connect to :3: ")
    print("running client side")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    # send something
    while True: 
        something = input("what do you wnant to send to this not evil thingy (enter Q to exit): ")
        if something == "Q":
            break
        client.send(something.encode())
        
    client.close()

if __name__ == "__main__":
    main()