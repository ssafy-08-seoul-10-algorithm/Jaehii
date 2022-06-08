n = int(input())    # 로프 수
arr = []    # 로프 담을 배열
for i in range(n):
    x = int(input())
    arr.append(x)

arr.sort()    # 오름차순으로 정렬
sum_ = 0    # 최대중량
num = 0    # 개수
for i in arr:
    if sum_ < i * (n-num):    # 더 크면
        sum_ = i * (n-num)    # 교체
    num += 1    # 뺄 개수 하나씩 늘리기

print(sum_)
