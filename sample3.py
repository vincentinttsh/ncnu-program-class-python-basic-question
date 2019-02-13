n = int(input())
for x in range(0,n) :
    for y in range(x+1) :
        print(chr(65+(x%26)) , end = ' ')
    print()