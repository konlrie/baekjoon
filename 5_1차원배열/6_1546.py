N = int(input())
a = list(map(int, input().split()))
b = list()
for i in range(N):
    new = a[i]/max(a)*100
    b.append(new)
print(sum(b)/len(b))
print(b[0])
print(b[1])
print(b[2])