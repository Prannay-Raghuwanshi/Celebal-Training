battery = 100
drain = int(input())

minutes = 0

while battery > 0:
    battery -= drain
    minutes += 1

print(minutes)