s1 = input()
s2 = input()
s3 = input()
t = input()

dic = {'1': s1, '2': s2, '3': s3}

answer = ''
for i in t:
    answer += dic[i]

print(answer)