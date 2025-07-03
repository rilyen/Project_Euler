n = 600851475143
p = 2

while n > p:
    # found a factor
    if n % p == 0:
        n = n / p
        p = 2
    # check next p
    else:
        p += 1

print(p)