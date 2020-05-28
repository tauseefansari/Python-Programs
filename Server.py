import socket
s=socket.socket()
s.bind(("localhost",5555))
s.listen(1)
con,addr=s.accept()
print("Server Connected")
while True:
    msg=con.recv(1024)
    if not msg:
        break
    print("Client : ",msg.decode())
    msgsent=input("Server : ")
    if msgsent.lower() == "bye":
        break
    con.send(msgsent.encode())
con.close()
