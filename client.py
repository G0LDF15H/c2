import socket

HOST = ""
PORT = 80
# client
def main():
    HOST = raw_input("give me a host to connect to :3: ") # for python 2.7.5
    print("running client side with: " + HOST + " and " + str(PORT))
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