sum = 0

for i in range(1, 30001):
    if i % 3 == 0 or str(i).count("3") != 0:
        sum += i
print(sum)