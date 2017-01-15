c = 2
while c < 20:
    a = 2
    count = 0
    while a < c:
        if c % a == 0:
            count = 1
        a += 1
    if count == 0:
        print(c, 'is a prime number')
    c += 1
