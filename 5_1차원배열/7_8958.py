N = int(input())
oxlist = list()
for i in range(N):
    try:
        ox = input()
        oxlist.append(ox)
    except:
        break

scorelist = list()
for i in range(len(oxlist)):
    score = 0
    for j in range(len(oxlist[i])):
        if oxlist[i][j] == 'O':
            score += 1
            if oxlist[i]
    scorelist.append(score) 
print(scorelist)

# for i in range(len(oxlist)):
#     for j in range(80):
#         oxlist[i].count('O'*j)
