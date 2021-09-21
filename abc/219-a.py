# 0 点以上 40 点未満のとき、初級
# 40 点以上 70 点未満のとき、中級
# 70 点以上 90 点未満のとき、上級
# 90 点以上のとき、エキスパート

x = int(input())
if x < 40:
    print(40 - x)
elif x < 70:
    print(70 - x)
elif x < 90:
    print(90 - x)
else:
    print('expert')