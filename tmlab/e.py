
def a(n, ans=0):
    for c in range(1,n):
        for b in range(1,c):
            for a in range(1,b):
                if a*a+b*b==c*c and (a * b / 2 <= 8192):
                    ans += 1
                elif a*a+b*b==c*c and (a * b / 2 > 8192):
                    print(ans)
                    return

a(10000, 0)