def fun(cnt, n, lst):
    for i in range(n):
        for j in range(n):
            if lst[i][j] == '#':
                x = 0  # 붙어있는 '#'의 수 세기위해
                y = 0
                for k in range(j + 1, n):  # 가로세기
                    if lst[i][k] == '#':
                        x += 1
                    else:
                        break
                for k in range(i + 1, n):  # 세로세기
                    if lst[k][j] == '#':
                        y += 1
                    else:
                        break
                if x != y:  # 가로세로 안같으면
                    return 'no'
                else:
                    chk = 0
                    for a in range(i, i + y + 1):
                        for b in range(j, j + x + 1):
                            if lst[a][b] != '#':
                                chk = 1
                            else:
                                cnt -= 1    # '#'갯수에서 하나씩 빼기
                    if chk == 1:
                        return 'no'
                    elif cnt != 0:    # 갯수가 맞지않는경우
                        return 'no'
                    else:
                        return 'yes'


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    lst = [list(map(str, input())) for _ in range(n)]    # 공백없어서 split X
    cnt = 0    # '#'의 갯수
    for i in range(n):
        for j in range(n):
            if lst[i][j] == '#':
                cnt += 1
    ans = fun(cnt, n, lst)
    print("#%d %s" % (test_case, ans))