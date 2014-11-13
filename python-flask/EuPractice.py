#Practice for Palindrome
m =100
n =100
numLS = []
while len(str(m))==3:
    while len(str(n))==3:
        prod = m*n
        prodStr= str(prod)
        prodRev= prodStr[::-1]
        if prodStr == prodRev:
            numLS.append(prod)
        n = n+1
    m = m+1