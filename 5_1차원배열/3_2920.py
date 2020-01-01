music = list()

a = list(map(int, input().split()))

if a == [1,2,3,4,5,6,7,8]:
    print("ascending")
elif a == [8,7,6,5,4,3,2,1]:
    print("descending")
else:
    print("mixed")

# for i in range(len(a)):
#     if a[i] == i+1:
#         print("ascending")
#     elif a[i] == len(a)-i:
#         print("descending")
#     else:
#         print("mixed")
