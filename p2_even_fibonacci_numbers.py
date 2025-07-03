f0 = 1
f1 = 2
sum = 0

while f1 <= 4e6:
    if f1 % 2 == 0:
        sum += f1
    f2 = f1 + f0
    if f2 > 4e6:
        break
    f0 = f1
    f1 = f2

print(sum)