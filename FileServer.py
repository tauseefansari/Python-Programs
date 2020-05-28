import socket
s=socket.socket()
s.bind(("localhost",5005))
s.listen(1)
con,adr=s.accept()
print("Connected ... ",str(adr))
print("Sending File ... ")
with open("File1.txt","rb") as f1:
    while True:
        data=f1.read(1024)
        con.send(data)
        if not data:
            break
print("File Send Success")
s.close()

