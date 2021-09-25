x = input()
n = int(input())
s = []
for i in range(n):
    s.append(input())

d = {}
for i in range(26):
    d[x[i]] = str(i)

for i in range(n):
    word = []
    for x in s[i]:
        word.append(d[x])
    s[i] = word

s.sort()

for i in range(n):
    word = []
    for x in s[i]:
        key = [k for k, v in d.items() if v == x][0]
        word.append(key)
    s[i] = word

s.sort()
for i in range(len(s)):
    print(s[i])
