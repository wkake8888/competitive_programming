import sys
from collections import deque

INF = 100000000

lines = ['3 3', 'S##', '###', '..G']
n, m = map(int, lines[0].split())
maze = []
count = 0
# 迷路を表す文字列の配列
for i in range(1, n + 1):
    maze.append(list(lines[i]))
for x in range(n):
    for y in range(m):
        # スタートの座標
        if maze[x][y] == 'S':
            sx = x
            sy =y
        # ゴールの座標
        if maze[x][y] == 'G':
            gx = x
            gy = y
# 各点までの最短距離の配列(INFで初期化)
# 壁を何度超えてきたかを各点で保持
d = []
for i in range(n):
    nl = []
    for j in range(m):
        ll = [INF, 0]
        nl.append(ll)
    d.append(nl)

# 移動4方向のベクトル
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# (sx, sy)から(gx,gy)への最短距離を求める
# 辿り着けないとINF
que = deque()
# スタート地点を両端キューに入れ、その点の距離を0にする
que.append([sx, sy])
d[sx][sy][0] = 0
# 両端キューが空になるまでループ
while len(que) != 0:
    # キューの先端を取り出す
    p = que.popleft()
    # 取り出してきた状態がゴールなら探索をやめる
    if p[0] == gx and p[1] == gy:
        break
    # 移動4方向をループ
    for i in range(4):
        # 移動した後の点を(nx, ny)とする
        nx = p[0] + dx[i]
        ny = p[1] + dy[i]

        # 壁があるかの判定とすでに訪れたことがあるかの判定(d[nx][ny] != INFなら訪れたことがある)
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != '#' and d[nx][ny][0] == INF:
            # キューに入れ、その点の距離をpからの距離+1で確定する
            que.append([nx, ny])
            d[nx][ny][0] = d[p[0]][p[1]][0] + 1
        # 壁がある場合
        elif 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == '#' and d[nx][ny][0] == INF:
            # キューに入れ、その点の距離をpからの距離+1+（点Pにおける、これまで超えた壁の数）
            que.append([nx, ny])
            d[nx][ny][0] = d[p[0]][p[1]][0] + 1 + d[p[0]][p[1]][1]
            d[nx][ny][1] += 1

print(d[gx][gy][0])
