import sys

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a==0 and b==0:
        break
    else:
        print(a+b)

# a, b = map(int, sys.stdin.readline().split())

# while a!=0 and b!=0:
#     print(a+b)
#     a, b = map(int, sys.stdin.readline().split())