vowels=["a","e","i","o","u"]
word=input("Enter a word:")
vowellist=[]
for i in word:
    if i in vowels:
        vowellist.append(i)
print(vowellist)
