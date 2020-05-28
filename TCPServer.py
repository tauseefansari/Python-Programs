import socket
s=socket.socket()
host="localhost"
port=5050
s.bind((host,port))
s.listen(1)
conn,addr=s.accept()
print("Connected From : ",str(addr))
while True:
    rmsg=conn.recv(1024).decode()
    if not rmsg:
        break
    print("Receive From Client : ",rmsg)
    msg=input("Enter Message to be Send : ")
    conn.send(msg.encode())
s.close()
