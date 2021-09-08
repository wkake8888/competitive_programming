n = int(input())
name_list = []
label = 0
for i in range(n):
    family_name, first_name = input().split(' ')
    name = family_name + ':' + first_name
    if name not in name_list:
        name_list.append(name)
    else:
        label = 1
        break

if label == 0:
    print("No")
else:
    print("Yes")