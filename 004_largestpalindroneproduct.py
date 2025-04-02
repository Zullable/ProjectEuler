# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


# Reverses number
def reverse_number(n):
    
    rev_n  = 0

    while n != 0:
        digit = n % 10
        rev_n = rev_n * 10 + digit
        n //= 10
    
    return rev_n

Digits = 3
c = (10 ** Digits - 1) ** 2
min = (10 ** (Digits - 1)) ** 2


while c > min:
    if c == reverse_number(c):  
            c_i = 10 ** (Digits - 1)
            while c_i <= 10 ** Digits - 1:
                if c % c_i == 0:
                    if c / c_i <= 10 ** Digits - 1:
                        print(c)
                        print(c_i)
                        print(c / c_i)
                        quit()
                c_i += 1
    c -= 1

# Solution 906609