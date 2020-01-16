def progression(x):
    cnt=0
    for x in range(1,x+1):
        setsub = set()
        for y in range(int(len(str(x)))-1):
            a = int(str(x)[y])-int(str(x)[y+1])
            setsub.add(a)
        if len(setsub)==0 or len(setsub)==1:
            cnt+=1
    print(cnt)

progression(int(input()))