ans = 0
n = 2
while ans < 9.0:
    ans = 0
    for i in range(1, n):
        ans += 1/i
    n += 1
print(ans)
print(n)