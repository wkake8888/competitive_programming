s = input()
ans = ""
for i in range(len(s)):
    if s[i] == "6":
        ans += "9"
    elif s[i] == "9":
        ans += "6"
    else:
        ans += s[i]

t = ""
for i in range(len(ans)):
    t += ans[len(ans) - (i + 1)]

print(t)