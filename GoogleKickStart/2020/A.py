import sys
x = int(input())
for i in range(x):
    n, money = [int(i) for i in input().split()]
    
    l = [int(i) for i in input().split()]
    l.sort()
    res = 0
    for h in l:
        if money < h:
            break
        money -= h
        res += 1
    print("Case #" + str(i+1) + ": " + str(res))
