# 0<A かつ B=0 なら「純金」
# A=0 かつ 0<B なら「純銀」
# 0<A かつ 0<B なら「合金」

a, b = map(int, input().split())
if a > 0 and b == 0:
    print('Gold')
elif a == 0 and b > 0:
    print('Silver')
else:
    print('Alloy')