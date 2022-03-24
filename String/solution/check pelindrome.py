a=input("enter any sentence:")
b=[]
for i in a.split():
    if(i==i[::-1]):
        b.append(i)
print()
for i in range(len(b)):
       print(b[i])
print()
print("Total {} panlidrome words in string:{}".format(len(b),b))
