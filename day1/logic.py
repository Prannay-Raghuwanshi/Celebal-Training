student=[
    ["John",85],
    ["Alice",92],
    ["Bob",78],
    ["Charlie",90]
]
above_80=list(filter(lambda x:x[1]>80,student))
print("Above 80",above_80)
above_40=list(filter(lambda x:x[1]>40,student))
print(len(above_40))
top = max(student, key = lambda x :x[1])
print(top)