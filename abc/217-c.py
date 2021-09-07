n = int(input())
p = input().split()
q = [0] * n
for i in range(n):
    p[i] = int(p[i])
# print(p)
for i in range(n):
    q[p[i]-1] += i + 1
for i in range(n):
    if i == n-1:
        print(q[i])
    else:
        print(q[i], end=" ")

