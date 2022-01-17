# abc+bca+cab
i = "123"
abc = list(i)
a, b, c = abc[0], abc[1], abc[2]

ans = int(a + b + c) + int(b + c + a) + int(c + a + b)
print(ans)