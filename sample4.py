n = int(input())
squre = [[x*n+y+1 for y in range(n)]for x in range (n)]
for i in range(n) :
    for j in range(n) :
        print(squre[i][j] , end = '\t')
    print()
