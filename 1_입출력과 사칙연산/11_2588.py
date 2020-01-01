a = input()
b = input()
c = int(a)*int(b[2])
d = int(a)*int(b[1])
e = int(a)*int(b[0])
print(c)
print(d)
print(e)
d = str(d) + '0'
e = str(e) + '00'
print(c+int(d)+int(e))

# a = input()
# a1 = int(a[0])
# a2 = int(a[1])
# a3 = int(a[2])
# b = input()
# b1 = int(b[0])
# b2 = int(b[1])
# b3 = int(b[2])
# c = str(a1*b3+int(str(a2*b3+int(str(a3*b3)[0]))[0])) + str(a2*b3+int(str(a3*b3)[0]))[-1] + str(a3*b3)[-1]
# d = str(a1*b2+int(str(a2*b2+int(str(a3*b2)[0]))[0])) + str(a2*b2+int(str(a3*b2)[0]))[-1] + str(a3*b2)[-1]
# e = str(a1*b1+int(str(a2*b1+int(str(a3*b1)[0]))[0])) + str(a2*b1+int(str(a3*b1)[0]))[-1] + str(a3*b1)[-1]
# f = e[0] + str(int(d[-4])+int(e[-3])+int(str(int(c[-4])+int(d[-3])+int(e[-2]))[0]))[1] + str(int(c[-4])+int(d[-3])+int(e[-2])+int(str(int(c[-3])+int(d[-2])+int(e[-1]))[0]))[1] + str(int(c[-3])+int(d[-2])+int(e[-1])+int(str(int(c[-2])+int(d[-1]))[0]))[1] + str(int(c[-2])+int(d[-1]))[1] + c[-1]

# print(c)
# print(d)
# print(e)
# print(f)