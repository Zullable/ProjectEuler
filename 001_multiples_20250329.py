x = 0
c = 0

while c < 1000:
    if c % 3 == 0 or c % 5 == 0:
        x = x + c
    c += 1

print(x)
