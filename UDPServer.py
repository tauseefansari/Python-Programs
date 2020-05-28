import socket
ss=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host="localhost"
port=6789
ss.bind((host,port))
rmsg,adr=ss.recvfrom(1024)
while rmsg:
    print("Received From Client : ",rmsg.decode())
    rmsg,addr=ss.recvfrom(1024)
ss.close()
