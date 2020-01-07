N = int(input())
for i in range(N):
    ox = input()
    cnt = 0
    score = 0
    for j in ox:
        if j == "O":
            cnt += 1
        elif j == "X":
            cnt = 0
        score += cnt
    print(score)


# oxlist = list()
# for i in range(N):
#     try:
#         ox = input()
#         oxlist.append(ox)
#     except:
#         break

# scorelist = list()
# for i in range(len(oxlist)):
#     score = 0
#     for j in range(len(oxlist[i])):
#         if oxlist[i][j] == 'O':
#             score += 1
#     scorelist.append(score) 
# print(scorelist)



# for i in range(len(oxlist)):
#     for j in range(80):
#         oxlist[i].count('O'*j)
