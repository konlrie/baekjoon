a, b = map(str, input().split())
a = a[::-1]
b = b[::-1]
num = list()
num.append(int(a))
num.append(int(b))
print(max(num))