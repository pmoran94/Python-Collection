i = 2
n = 600851475143

while i < n:
    if n%i == 0:
        n = n / i
    i = i + 1
print (n)