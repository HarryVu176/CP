def insr2():
    s = input()
    return list(s[:len(s)])

uin = insr2()
for i in range(len(uin)):
    if uin[i] == "R":
        uin[i] = "S"
    elif uin[i] == "B":
        uin[i] = "K"
    elif uin[i] == "L":
        uin[i] = "H"
print("".join(uin))