size = int(input())
arr = list(map(str, input().split()))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x, y = 1, 1

for i in range(0, len(arr)):
    if arr[i] == 'R':
        j = 0
    elif arr[i] == 'U':
        j = 1
    elif arr[i] == 'L':
        j = 2
    elif arr[i] == 'D':
        j = 3

    nx = x + dx[j]
    ny = y + dy[j]
    if nx < 1 or ny < 1 or nx > size or ny > size:
        continue
    x = nx
    y = ny

print(x, y)
