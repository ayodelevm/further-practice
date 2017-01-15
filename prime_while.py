c = 2
while c < 20:
    k = 2
    count = 0
    while k < c:
        if c % k == 0:
            count = 1
        k += 1
    if count == 0:
        print(c, 'is a prime number')
    c += 1
