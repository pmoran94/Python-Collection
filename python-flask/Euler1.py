n = 0
total = 0
while n < 1000:
    if n%3 == 0:
        total += n
    elif n%5 == 0:
        total += n
    n += 1
print(total)