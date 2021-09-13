p = input().split()
answer = ''
num = 96
for i in range(26):
    alp = chr(int(p[i]) + num)
    answer += alp
print(alp)