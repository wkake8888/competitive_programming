s = input()
a, b = list(map(int, input().split()))
sa = s[a - 1]
sb = s[b - 1]
ans = s[:a - 1] + sb + s[a: b - 1] + sa + s[b:]
print(ans)