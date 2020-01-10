T = int(input())
for i in range(T):
    R, S = map(str, input().split())
    R = int(R)
    P = str()
    for j in S:
        P += j * R
    print(P)