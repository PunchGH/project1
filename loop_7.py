x = 1
times = int(input(">>>"))
for i in range(times):
    print(" " * (6 - i),"*" * x)
    x += 2
