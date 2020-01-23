import string
alphabet = string.ascii_lowercase
N = int(input())
for i in range(N):
    word = input()
    for alpha in alphabet:
        for wd in word:
            wordcheck = list()
            if wd == alpha:
                wordcheck.append(alphabet.index(alpha))
                if 


