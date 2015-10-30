#for columns in range of 10 decreasing by one column with each for loop
for col in range(10, -1, -1):
    #for each iteration print a row of asteriks
    for c in range(col):
        print('*', end='')
    print('*')
