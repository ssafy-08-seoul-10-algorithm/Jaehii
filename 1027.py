def left(curr):    # 왼쪽에 있으면 기울기가 현재보다 작아야만 볼 수 있음
    l_cnt = 0    # 보이는 건물 수
    max_g = float("inf")
    for i in range(curr-1, -1, -1):    # 거꾸로!!!!!!!!!!꼭
        gradient = (arr[curr]-arr[i])/(curr-i)
        if gradient < max_g:    # 현기울기보다 작으면 보이고 최소기울기는 계속 갱신
            max_g = gradient    # 갱신
            l_cnt += 1    # 보이면 +1
    return l_cnt


def right(curr):    # 오른쪽에 있으면 기울기가 현재보다 커야만 볼 수 있음
    r_cnt = 0    # 보이는 건물 수
    min_g = -float("inf")
    for i in range(curr+1, N):
        gradient = (arr[curr]-arr[i])/(curr-i)
        if gradient > min_g:    # 현기울기보다 크면 보이고 최대기울기는 계속 갱신
            min_g = gradient    # 갱신
            r_cnt += 1    # 보이면 +1
    return r_cnt


N = int(input())
arr = list(map(int, input().split()))
ans = 0    # 보이는 건물수 비교할 값
for i in range(N):
    sum = left(i) + right(i)
    if sum > ans:
        ans = sum
print(ans)
'''
a = [[] for i in range(N)]    # 기울기, y절편
    comb = [i for i in range(N)]    # combination 위함
    for i, j in combinations(comb, 2):
        gradient = arr[j]-arr[i]/j-i    # 기울기 구하기
        k = arr[j] - gradient*j    # y절편 구하기
        a[i].append([j, gradient, k])
        a[j].append([i, gradient, k])
        print(i, j)
    for i in range(len(a[0])):
        gradient = a[0][i][1]
        k = a[0][i][2]
        for a
'''