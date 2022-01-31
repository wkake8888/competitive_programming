import math

def cal_line_segment_length(a:list, b:list):
    return math.sqrt(pow(b[0] - a[0], 2) + pow(b[1] - a[1], 2))

n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

max_val = -1
for i in range(n - 1):
    for j in range(i + 1, n):
        a = l[i]
        b = l[j]
        length = cal_line_segment_length(a, b)
        if length > max_val:
            max_val = length

print(max_val)
