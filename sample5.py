n = int(input())
squre = [[0 for y in range(n)]for x in range (n)]
x1 , y1 = map(int , input().split())
x2 , y2 = map(int , input().split())
for i in range(min(y1,y2) , max(y1,y2)+1) :
    for j in range(min(x1,x2) , max(x1,x2)+1) :
        squre[i][j]=1
for i in range(n) :
    for j in range(n) :
        print(squre[i][j] , end = '\t')
    print()
