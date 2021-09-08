x, y = input().split('.')
# 0≤Y≤2 ならば、X-
# 3≤Y≤6 ならば、X
# 7≤Y≤9 ならば、X+
if int(y) >= 0 and int(y) <=2:
    print(x + '-')
elif int(y) >= 3 and int(y) <=6:
    print(x)
else:
    print(x + '+')
