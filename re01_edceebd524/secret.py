cipher = "WikwaMgss[9}?_}>~VMZgJ%Wk`g"
for i in range(0, len(cipher), 1):
    c = ord(cipher[i]) ^ i
    print("%c"%(c),end="")