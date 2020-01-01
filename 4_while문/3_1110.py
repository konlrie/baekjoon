N = int(input())

a = 0
cycle = 0

while a != N:
    a = N
    if a < 10:
        a = str(0) + str(a)
        a = str(a)
        c = str(int(a[0])+int(a[1]))
        a = str(a[-1]) + str(c[-1])
        a = int(a)
        cycle += 1
    else:
        a = str(a)
        c = str(int(a[0])+int(a[1]))
        a = str(a[-1]) + str(c[-1])
        a = int(a)
        cycle += 1

print(cycle)
