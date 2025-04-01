# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of 600851475143?


def isprime(n):
    if (n <= 1):
        return False
    x = 2
    while (x < n):
        if (n % x == 0):
            return False
        x += 1
    return True

Num = 600851475143
Counter = 0
Highest = 0

while (Num > 1):
    Counter += 1
    if isprime(Counter):
        if Num % Counter == 0:
            Highest = Counter
            Num = Num / Counter

# Solution 6857
print(Highest)