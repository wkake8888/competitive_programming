n = int(input())
rest_sum = sum(list(map(int, input().split())))
s = 0
for i in range(1, n):
    s += 4 * i
print(s - rest_sum)
