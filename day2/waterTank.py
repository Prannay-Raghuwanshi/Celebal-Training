n = int(input())
inflows = list(map(int, input().split()))

capacity = 1000
water = 0

for i in range(n):
    water += inflows[i]

    if water > capacity:
        print(i + 1)
        break