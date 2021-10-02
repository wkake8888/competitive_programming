li = []

a = [7, 39, 51]
l, r = 10, 724
for i in range(3):
    for j in range(1, r // a[i] + 1):
        if (a[i]*j) not in li and (a[i]*j) >= l:
            li.append(a[i]*j)

print(r-l + 1 - len(li))