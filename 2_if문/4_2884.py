h, m = map(int, input().split())
hm = h*60 + m
if hm < 45:
    hm = 24*60 + hm
alarm = hm-45
alarmh = alarm//60
alarmm = alarm%60
print(alarmh, alarmm)