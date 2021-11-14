l = [1, 0, 5]

for i in range(30):
    a = sum(l[i: i+3])
    l.append(a)
print(l[29])