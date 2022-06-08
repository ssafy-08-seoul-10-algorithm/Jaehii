from collections import deque

n, m = map(int, input().split())
lst = []
for i in range(n):
    lst.append(list(map(int, input())))    # 공백없어서 split()쓰면X

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if lst[nx][ny] == 0:
                continue

            if lst[nx][ny] == 1:
                lst[nx][ny] = lst[x][y] + 1
                q.append((nx, ny))

    return lst[n-1][m-1]


print(bfs(0,0))



