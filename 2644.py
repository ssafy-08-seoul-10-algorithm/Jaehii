from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for i in range(n+1)]    # 부모자식 관계 기록
visited = [False] * (n+1)

for i in range(m):    # 부모자식 관계 기록
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

q = deque()
q.append((0, a))    # 0부터 시작해서 촌수 늘려감

def bfs():
    while q:
        num, x = q.popleft()
        visited[x] = True
        for i in graph[x]:    # x번 사람의 관계뒤지기
            if not visited[i]:    # 방문안했을경우에만
                q.append((num+1, i))
            if i == b:    # 도달하면
                return num+1    # 리턴
    return -1    # 큐 끝날때까지 도달안했으면 -1

print(bfs())
