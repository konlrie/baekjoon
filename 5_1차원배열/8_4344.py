C = int(input())
for i in range(C):
    N = list(map(int, input().split()))
    avg = sum(N[1:])/N[0]
    cnt = 0
    for j in range(len(N)-1):
        if N[j+1] > avg:
            cnt += 1
    print(f'{cnt/int(len(N)-1)*100:.3f}%')
    # print("{}%".format("%0.3f" % cnt/int(len(N)-1)*100))

# C = int(input())
# pnlist = list()
# scorelist = list()
# for i in range(C):

# a = list(map(int, input().split()))
# pnlist = list()
# scorelist = list()
# pnlist.append(a[0])
# scorelist.append(a[1:5])
# print(pnlist)
# print(scorelist)
# print(type(scorelist))
# avg = sum(scorelist[0])/pnlist[0]
# count = 0
# if scorelist > avg:
#     count += 1