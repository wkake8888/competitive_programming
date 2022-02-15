from decimal import MAX_EMAX


n = int(input())
a = list(map(int, input().split()))

l = [1] + [0] * 359
current_angle = 0

for i in range(n):
    angle = a[i]
    current_angle = (current_angle + angle) % 360
    l[current_angle] = 1

max_continuous_count = 0
count = 0
for i in range(len(l)):
    if l[i] == 1:
        count += 1
        if count > max_continuous_count:
            max_continuous_count = count
            count = 0
        else:
            count = 0
    else:
        count += 1

print(max([max_continuous_count, count + 1]))
