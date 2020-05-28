import socket
s=socket.socket()
s.connect(("localhost",5555))
print("Client Connected")
while True:
    stri=input("Client : ")
    if stri.lower() == "bye":
        break
    s.send(stri.encode())
    msg=s.recv(1024)
    if not msg: 
        break
    print("Server : ",msg.decode())
s.close()
