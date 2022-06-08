from collections import deque

N = int(input())
arr = list(map(int, input().split()))
del_n = int(input())    # 삭제 노드
cnt = 0    # 리프노드 개수
check = [0 for _ in range(N)]    # 노드의 삭제여부
tree = deque([] for _ in range(N))    # 트리[부모] = 자식들
for i in range(N):
    if arr[i] == -1:    # 루트면
        root = i
        continue
    else:
        tree[arr[i]].append(i)
check[del_n] = 1    # 삭제체크
queue = deque()    # dfs
queue.append(root)    # 0에서 시작하게
while queue:
    x = queue.popleft()
    if check[x] == 1:    # 삭제된 노드면
        continue
    if len(tree[x]) == 0:    # 리프노드면(자식이 없으면)
        cnt += 1
        continue
    n = len(tree[x])
    while tree[x]:    # 자식이 존재하면
        y = tree[x].pop()
        if n == 1 and check[y] == 1:    # 자식이 하나있는데 그게 삭제된거면
            cnt += 1
            break
        else:
            queue.append(y)    # 큐에 넣음
print(cnt)

# 리프노드인 경우 : 1. 자식이 없음 2. 삭제된 자식
# 주의 : 루트가 0이 아닐수도 있음 !