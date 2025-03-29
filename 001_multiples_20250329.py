# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

x = 0
c = 0

while c < 1000:
    if c % 3 == 0 or c % 5 == 0:
        x = x + c
    c += 1

# Solution 233168
print(x)
