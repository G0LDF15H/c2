import socket

HOST = "10.0.2.4"
PORT = 65432
# client
def main():
    # HOST = raw_input("give me a host to connect to :3: ") # for python 2.7.5
    print("running client side with: " + HOST + " and " + str(PORT))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))

        # send something
        while True: 
            something = input("what do you wnant to send to this not evil thingy (enter to exit): ")
            if something == "":
                break
            client.send(something.encode())
            
        client.close()

if __name__ == "__main__":
    main()