# 1 回目から 125 回目までは 4 問
# 126 回目から 211 回目までは 6 問
# 212 回目から 214 回目までは 8 問
n = int(input())
if n >= 1 and n <= 125:
    print(4)
elif n >= 126 and n <= 211:
    print(6)
else:
    print(8)