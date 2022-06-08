import collections

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

def bfs():    # 중요) 가장자리 한번 녹을때마다 한번 호출
    queue = collections.deque()
    queue.append((0,0))   # 처음부터 시작
    visited = [[0] * m for _ in range(n)]    # 체크
    count = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:    # 자꾸 행과열 헷갈림 ㅜㅜㅜㅜㅜ
                if lst[nx][ny] == 0 and visited[nx][ny] == 0:    # 가장자리가 아닌 바깥
                    visited[nx][ny] = 1    # 체크하고
                    queue.append((nx, ny))    # 계속 가야하니까 큐에 넣는다
                elif lst[nx][ny] == 1 and visited[nx][ny] == 0:    # 가장자리면
                    lst[nx][ny] = 0    # 녹인다
                    visited[nx][ny] = 1    # 체크
                    count += 1    # 녹는개수 즉 가장자리 세기
    return count

ans = []
time = 0

while True:
    cnt = bfs()
    ans.append(cnt)
    if cnt == 0:    # 가장자리가 없으면, 즉 다녹으면
        break
    time += 1

print(time)
print(ans[-2])    # 뒤에서 두번째, 즉 녹기 바로 전