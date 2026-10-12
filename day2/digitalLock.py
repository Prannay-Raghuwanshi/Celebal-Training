n = int(input())

while n >= 10:
    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n = n 

    n = total

print(n)