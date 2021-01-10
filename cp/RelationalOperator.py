
f = open('input_relational.txt')
num = f.readline();
for i in range(int(num)):
    (x,y) = f.readline().split()
    if x > y:
        print(">")
    elif x < y:
        print("<")
    else:
        print("=")
