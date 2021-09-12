n = int(input())
s = ''

while n > 0:
    parity = n % 2
    if parity == 0:
        s += 'B'
    else:
        s += 'AB'
    n //= 2
print(s[::-1])