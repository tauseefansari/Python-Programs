import socket
host="localhost"
port=6789
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg=input("Enter Message to be Send : ")
while msg.lower() != "bye":
    s.sendto(msg.encode(),(host,port))
    msg=input("Enter Message to be Send : ")
msg=""
s.sendto(msg.encode(),(host,port))
s.close()
