t = int(input())

def f(x: int):
    return x*x + 2*x + 3

ans = f(f(f(t)) + f(f(t) + t))
print(ans)