x = list()

while True:
    try:
        a = int(input())
        b = a%42
        x.append(b)
        c = set(x)
        c = list(c)
    except:
        break

print(len(c))

# set(x)