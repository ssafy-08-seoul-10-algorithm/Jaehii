import sys

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

lst = sorted(lst, key=lambda x:(x[1], -x[0]))    # 낮은가격부터, 무거운 무게부터

def fun():
    sum = 0
    for i in range(n):
        sum += lst[i][0]
    if sum < m:
        return -1

    ans = sys.maxsize
    weight = 0
    same_price = 0

    for i in range(n):    # 낮은 가격 순으로 돌림
        weight += lst[i][0]    # i번째 낮은 가격의 무게 합해감
        if i > 0 and lst[i][1] == lst[i-1][1]:    # 바로 전 가격과 같다면
            same_price += lst[i][1]    # 현 가격과 동일한 전 가격 더해줌
        else:
            same_price = 0    # 아니라면 초기화

        if weight >= m:    # 무게가 채워졌다면
            ans = min(ans, lst[i][1] + same_price)    # 비교
    return ans

print(fun())
