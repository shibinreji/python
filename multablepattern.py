rows=int(input('enter the number of rows'))
for i in range(1,rows+1):
    print()
    for j in range(1,i+1):
        square=i*j
        print('{}  '.format(square),end='')
