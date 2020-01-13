dn_set = set()
for n in range(1,10001):
    dn = n
    for i in str(n):
        dn += int(i)
    dn_set.add(dn)
selfnumber_set = set(range(1,10001)) - dn_set
selfnumber_set = sorted(selfnumber_set)

for j in range(len(selfnumber_set)):
    print(selfnumber_set[j])


# def dn(n):
#     inf = n
#     for i in range(len(str(n))):
#         inf = inf + int(str(n)[-1])
#     return inf

# # print(dn(33))

# def constructor(n):
#     int(dn(n)) = n
#     for i in range(len(str(n))):
#         n = n - int(str(n)[-1])
#     return n

# # print(constructor(39))
 
# def selfnumber(n):
#     for i in range(1,n+1):
        
#         inf = n
#         inf = inf + int(str(n)[-1])
#     constructor = 
#     for j in range(len(str(n)))