def solve(a):
    s = 0
    for i in a:
        s += i
    return s


a = [1,2,3,4,5]
print(solve(a))
print(sum(a))