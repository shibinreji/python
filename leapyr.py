print("Leap Year")
start=int(input("Enter the start year"))
end=int(input("Enter the end year"))
print("List of leap year:")
for year in range(start,end+1):
    if(year%4==0)and(year%100!=0)or(year%400==0):
        print(year)
