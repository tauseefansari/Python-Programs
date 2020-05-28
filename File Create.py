with open("Test.txt","w") as f:
    f.write(input("Enter The Content of File : "))
with open("Test.txt","r") as f1:
    print(f1.read())
