x = list()

while True:
    try:
        a = int(input())
        b = a%42
        x.append(b)
    except:
        break


# set(x)