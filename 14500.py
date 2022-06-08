# 포인트 : 너무길면 함수로만들기, max_val로 계산해서 안될거같으면 재빨리 포기, dfs는 큐안쓰고 재귀
# 참고 : - map 사용법: https://koos808.tistory.com/34
def dfs(x, y, step, sum):
    global ans    # 함수 밖에서 선언된 전역변수의 접근위해
    if step == 4:
        ans = max(ans, sum)
        return
    if sum + max_val * (4-step) < ans:    # 후순에 큰게 나와도 최대보다 작으면
        return
    dx = [-1, 1, 0, 0]  # 방향벡터
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx, ny, step+1, sum+lst[nx][ny])
            visited[nx][ny] = 0
            if step == 2:  # ㅓ, ㅏ, ㅗ, ㅜ 만들기위함
                visited[nx][ny] = 1
                dfs(x, y, step + 1, sum + lst[nx][ny])    # 탐색은 현위치에서 다시
                visited[nx][ny] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for i in range(n)]
    visited = [[0 for i in range(m)] for j in range(n)]    # 방문체크
    max_val = max(map(max, lst))    # 최댓값
    ans = 0
    step = 1
    for i in range(n):
        for j in range(m):
            visited[i][j] = 1    # (i,j)가 첫블록이라서 이것도 방문처리해줘야
            dfs(i, j, 1, lst[i][j])
            visited[i][j] = 0
    print(ans)





