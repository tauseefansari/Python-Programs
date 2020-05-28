count=0
str=input("Enter String : ")
for letter in str:
    if letter in "aeiouAEIOU":
        count+=1
print("Vowels : ",count)
