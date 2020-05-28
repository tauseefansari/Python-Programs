from zipfile import ZipFile
f=ZipFile("Sample.zip","w")
f.write("File1.txt")
f.write("File2.txt")
f.close()
f2=ZipFile("Sample.zip","r")
for file in f2.namelist():
    print("Content of %s : "%file)
    fn=f2.open(file)
    print(fn.read())
    fn.close()
