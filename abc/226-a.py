x = input()
index = x.find('.')
int_x = x[:index]
fdp = int(x[index + 1])

if fdp >= 5:
    print(int(int_x) + 1)
else:
    print(int(int_x))
