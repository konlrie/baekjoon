import collections

word = list(input().upper())
count = collections.Counter(word)
max_num = max(list(count.values()))

answer = []
for key in list(count.keys()):
    if count[key] == max_num:
        answer.append(key)

if len(answer) == 1:
    print(answer[0])
else:
    print("?")

# word = input()
# word = word.upper()
# wordlist = list()
# for z in word:
#     wordlist.append(word)
# wordnum = set(wordlist)
# # print(wordnum)
# cnt = list()
# numcnt = list()
# for i in wordnum:
#     num = word.count(i)
#     cnt.append(num)
#     numcnt.append(i)
# # print(cnt)
# cntset = set(cnt)
# if len(cnt) == len(cntset):
#     idx = cnt.index(max(cnt))
#     print(numcnt[idx])
#     # print(word[idx])
# else:
#     print('?')

# for j in range(len(cnt)):
#     for k in range(len(cnt)):
#         if cnt[i] == cnt[j]:
#             print('?')
#             break
#         else:
#             print(max(cnt))
#             break