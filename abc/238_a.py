import math

n = int(input())

print('Yes') if n > (2 * math.log(n, 2)) else print('No')
