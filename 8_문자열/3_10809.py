import string
S = input()
for i in string.ascii_lowercase:
    if i in S:
        print(S.find(i))
    else:
        print(-1)