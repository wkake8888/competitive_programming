n = int(input())
h = list(map(int, input().split()))

highest = h[0]

for i in range(n - 1):
    if h[i] < h[i + 1]:
        highest = h[i + 1]
    else:
        break

print(highest)