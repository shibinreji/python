def word_count(str):
    count=dict()
    words=str.split()
    for i in words:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    print(count)
a=input("enter a string:")
word_count(a)
    
