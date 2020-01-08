def solve(n):
    inf = n
    for j in range(len(str(n))):
        inf = inf + int(str(n)[-1])
    return inf

print(solve(33))



