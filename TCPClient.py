import socket
s=socket.socket()
host="localhost"
port=5050
conn=s.connect((host,port))
msg=input("Enter Message to be Send : ")
while msg.lower() != "bye":
    s.send(msg.encode())
    rmsg=s.recv(1024).decode()
    if not rmsg:
        break
    print("Receive From Server : ",rmsg)
    msg=input("Enter Message to be Send : ")
s.close()
