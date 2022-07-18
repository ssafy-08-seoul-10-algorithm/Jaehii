def get(x, y, dir, start):
    if start == 0:
        nx = x + n_dir[dir][0]
        ny = y + n_dir[dir][1]
        start = 1
    elif x <= -1 or x >= n or y <= -1 or y >= m:    # 범위 넘어가면
        ans.append((x, y))
        return (x, y)    # 현좌표
    else:
        # print("x, y : %d %d n, m : %d %d" % (x,y,n,m))
        if arr[x][y] == 1:    # 거울이 있으면
            nx = x + mir_dir[dir][0]
            ny = y + mir_dir[dir][1]
            if dir == 0:
                dir = 1   # 거울로 인해 변화됨
            elif dir == 1:
                dir = 0
            elif dir == 2:
                dir = 3
            elif dir == 3:
                dir = 2
        else:    # 거울 없다면
            nx = x + n_dir[dir][0]
            ny = y + n_dir[dir][1]
    # print(nx, ny)
    get(nx, ny, dir, start)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
n_dir = [[0,1], [-1,0], [0,-1], [1,0]]    # 거울없을때
mir_dir = [[-1,0], [0,1], [1,0], [0,-1]]    # 거울있을때
ans = []

for i in range(n):
    temp = get(i, -1, 0, 0)    # 좌표받음
    # ans.append(temp[0]+1)

for i in range(m):
    temp = get(n, i, 1, 0)
    # ans.append(n+1+temp[1])

for i in range(n-1, -1, -1):
    temp = get(i, m, 2, 0)
    # ans.append(m+n+(n-temp[0]))

for i in range(m-1, -1, -1):
    temp = get(-1, i, 3, 0)
    # ans.append(m+n+n+(m-temp[1]))

answer = []

for i in ans:
    x, y = i
    if x == -1:
        answer.append(y+1)
    if y == m:
        answer.append(n+x+1)
    if x == n:
        answer.append(n+m+(n-y))
    if y == -1:
        answer.append(2*n+m+(m-x))
print(answer)

# 재귀, dfs에서는 함수 리턴값이 메인으로 안 전해짐..


