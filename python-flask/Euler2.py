n = 1
m = 1
totalEvs = 0
while n < 4000000:
    n = n + m
    m = n
    if n%2 == 0:
        totalEvs = totalEvs + n
        
print(totalEvs)
