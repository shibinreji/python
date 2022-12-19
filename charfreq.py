string=input("Enter a string")
d=dict()
for i in string:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)