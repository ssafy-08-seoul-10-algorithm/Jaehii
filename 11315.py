def check():
    dx = [0, 1, 1, 1]  # 오른쪽, 아래, 오아대각선, 왼아대각선
    dy = [1, 0, 1, -1]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':    # o인경우만
                for dir in range(4):    # 네가지 방향 각각으로 쭉
                    x = i
                    y = j
                    cnt = 0    # 방향 바뀔때마다 초기화
                    while 0 <= x < n and 0 <= y < n and arr[x][y] == 'o':    # while문에 조건 3개할 수 있었다닝..
                        cnt += 1
                        x += dx[dir]
                        y += dy[dir]
                        if cnt >= 5:
                            return "YES"
    return "NO"


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(str, input())) for _ in range(n)]    # 한줄에 다 붙어있어서 split() X
    print("#%d %s" % (tc, check()))



'''
cnt = 0    # 연속갯수 담을 것
    for i in range(n):
        chk = 0
        for j in range(n):
            if arr[i][j] == 'o':
                cnt += 1
                if cnt >= 5:
                    chk = 1
                    break    # 이중포문인거 반드시 생각해서 break 또해줘야함 ㅜㅜㅜ!!
            else:
                cnt = 0
        if chk == 1:
            break
    if cnt >= 5:
        print('#%d YES' % tc)
    else:
        cnt = 0
        for j in range(n):
            chk = 0
            for i in range(n):
                if arr[i][j] == 'o':
                    cnt += 1
                    if cnt >= 5:
                        chk = 1
                        break
                else:
                    cnt = 0
            if chk == 1:
                break
        if cnt >= 5:
            print('#%d YES' % tc)
        else:
            cnt = 0
            k = 0    # i 줄여줄라고
            chk = 0    # 이중포문 나오기위함
            for i in range(n):
                k = i    # 넣어놨다가
                for j in range(n-1, -1, -1):
                    print(i, j)
                    if arr[i][j] == 'o':
                        cnt += 1
                        print(i, j)
                        if cnt >= 5 or i >= n or i < 0:
                            if cnt >= 5:
                                print(i, j)
                            chk = 1
                            break
                        i += 1
                    else:
                        cnt = 0
                if cnt >= 5 and chk == 1:
                    break
                i = k    # 다시돌려받음
                cnt = 0    # i가 달라지면 cnt초기화
            if cnt >= 5:
                print('#%d YES' % tc)
            else:
                print('#%d NO' % tc)
'''