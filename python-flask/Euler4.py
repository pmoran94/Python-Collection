m = 100
n = 100
palList = []


while len(str(n))==3:
    while len(str(m))==3:
        ans = m * n
        ansStr = str(ans)
        ansRev = ansStr[::-1]
        if ansStr == ansRev:
            palList.append(ans)
        m = m + 1
    n = n + 1
        

print(palList)
    
        