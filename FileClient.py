import socket
s=socket.socket()
s.connect(("localhost",5005))
with open("File2.txt","wb") as f2:
    while True:
        data=s.recv(1024)
        f2.write(data)
        if not data:
            break
    print("File Received")
s.close()
with open("File2.txt","r") as file:
    print(file.read())
