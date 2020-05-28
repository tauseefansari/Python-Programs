kl="abcdefghijklmnopqrstuvwxyz"
ku="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def encrypt(string,key):
    res=""
    for letter in string:
        if letter.isupper():
            res+=ku[(ku.index(letter) + key) % 26]
        elif letter.islower():
            res+=kl[(kl.index(letter) + key) % 26]
        elif letter.isspace():
            res+=" "
    return res
def decrypt(string,key):
    res=""
    for letter in string:
        if letter.isupper():
            res+=ku[(ku.index(letter) - key) % 26]
        elif letter.islower():
            res+=kl[(kl.index(letter) - key) % 26]
        elif letter.isspace():
            res+=" "
    return res
str=input("Enter String : ")
key=int(input("Enter Key : "))
print("Encrypted String : ",encrypt(str,key))
print("Decrypted String : ",decrypt(encrypt(str,key),key))
