import sys
with open(sys.argv[1], 'r') as f:
    x = int(f.readline())
    for i in range(x):
        n, money = [int(i) for i in f.readline().split()]
        
        l = [int(i) for i in f.readline().split()]
        l.sort()
        res = 0
        for h in l:
            if money < h:
                break
            money -= h
            res += 1
        print("Case #" + str(i+1) + ": " + str(res))
