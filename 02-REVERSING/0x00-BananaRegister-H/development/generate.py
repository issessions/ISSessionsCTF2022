flag = list("sillylittlemonkeyonatree".lower())

for i in range(len(flag)):
    flag[i] = ord(flag[i]) + i

flag.reverse()

print(flag)

