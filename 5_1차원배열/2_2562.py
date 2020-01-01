a = list()

while True:
    try:
        x = int(input())
        a.append(x)
    except:
        break

print(max(a))
# print(a.index(max(a))+1)

for i in range(len(a)):
    if a[i] == max(a):
        print(i+1)


# import sys
# a = list()

# while True:
#     x = sys.stdin.readline()
#     if x != "\n":
#         x = int(x)
#         a.append(x)
#     else:
#         break

# print(max(a))
# print(a.index(max(a))+1)

# for i in range(len(a)):
#     if 