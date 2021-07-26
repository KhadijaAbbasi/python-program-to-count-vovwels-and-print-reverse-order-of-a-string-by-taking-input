text=input("Enter a string: ")
count=0
for i in text:
    if i=='a'or i=='e'or i=='i' or i=='o' or i=='u':
        count=count+1

print("No of Vowels: ",count) 

x=len(text)
while x>0:
    print(text[x-1])
    x=x-1
print(text[::-1])