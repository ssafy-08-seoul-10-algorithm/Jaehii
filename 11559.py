from collections import deque

def dfs(x, y, step):    # 인접한 것들 터뜨리는 함수
    global check
    dx = [-1, 1, 0, 0]    # 방향벡터
    dy = [0, 0, -1, 1]
    cnt = 0    # 터뜨릴지 확인하는 용도
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<12 and 0<=ny<6 and lst[x][y] == lst[nx][ny] and lst[x][y] != 'x' and visited[nx][ny] == 0:
            # 범위안에 있고 방문되지않았고 같은 색깔인 경우(공백은 안침)
            queue.append((nx, ny))
            visited[nx][ny] = 1
            dfs(nx, ny, step+1)
            visited[nx][ny] = 0

            if step == 2:  # ㅓ, ㅏ, ㅗ, ㅜ 만들기위함!!!!!!!!!!!!!! 이것때문에 BFS가 편할 수 있을거같음 !!!!!!ㅠㅠㅠ
                visited[nx][ny] = 1
                dfs(x, y, step+1)    # 탐색은 현위치에서 다시
                visited[nx][ny] = 0
        else:
            cnt += 1    # 인접한것이 없으면 +1
    if step >= 4 and cnt == 4:    # 4개이상이고 더이상 인접한게 없으면
        while queue:    # 큐가 빌때까지
            xx, yy = queue.popleft()  # 터뜨릴좌표 꺼냄
            lst[xx][yy] = 'x'
            # print(step, xx, yy)
        # print("y")
        check = 1



def emp():    # 공백 비우는 함수
    for i in range(11, -1, -1):    # 꼭 밑에서부터 !!!
        for j in range(5, -1, -1):
            if lst[i][j] == 'x' and 0 < i:    # 공백이고 맨윗줄이 아니면
                n = 1
                for k in range(i-1, -1, -1):    # 위로 거슬러감
                    if lst[k][j] != 'x':
                        break
                    else:
                        n += 1    # 공백 세로 수
                for k in range(i, -1, -1):    # 공백 윗줄들
                    if k-n >= 0:
                        lst[k][j] = lst[k-n][j]    # 공백만큼 아래로 끌어옴
                    else:
                        lst[k][j] = '.'
            if lst[i][j] == 'x' and i == 0:    # 공백이고 맨 윗줄이면
                lst[i][j] = '.'


if __name__ == "__main__":
    # lst = [list(input().split()) for i in range(12)] ------> 이렇게 하면 안됨!!!!
    lst = [list(input()) for i in range(12)]
    visited = [[0 for i in range(6)] for j in range(12)]    # 방문체크
    queue = deque()    # 터뜨릴 좌표
    check = 1
    ans = 0
    while check == 1:    # 터지는게 있는동안만
        check = 0
        # print("start")
        for i in range(12):
            for j in range(6):
                if lst[i][j] != '.':
                    visited[i][j] = 1    # 초기값도 방문 꼭꼭
                    queue.append((i, j))    # 터뜨릴 좌표 큐에 현위치 넣어줌
                    dfs(i, j, 1)    # 리턴값
                    visited[i][j] = 0
                    queue.clear()    # 다음턴을 위해 큐 초기화
        # print("End, %d" % check)
        if check == 1:    # 전체 한번 돌았을때 터지는게 있다면
            emp()    # 공백 치우기
            ans += 1    # 횟수늘리기
            # print(lst)
        # else:
        #     break
    print(ans)