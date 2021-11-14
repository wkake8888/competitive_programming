n = int(input())
l = []
for i in range(n):
    a = list(map(int, input().split()))
    l.append(a)

target_group = {n - 1}
next_target_group = []
init_target = l[n - 1]
# 1000000000 4 1 2 3 4
def add_count(li):
    if len(li) == 2 and li[0] == 0:
        return
    else:
        for i in range(1, len(li)):
            target_group.add(li[i])
        next_target_group = li[1:]
        return add_count(next_target_group)

add_count(init_target)
sum = 0
for i in range(len(target_group)):
    if i != 0:
        sum += l[i - 1][0]
print(sum)