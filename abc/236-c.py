local, exp = list(map(int, input().split()))
local_sta = input().split()
exp_sta = input().split()
exp_count = 0
for i in range(len(local_sta)):
    if local_sta[i] == exp_sta[exp_count]:
        print('Yes')
        exp_count += 1
    else:
        print('No')
