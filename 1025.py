import math

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input())))

ans = -1

for i in range(N):
    for j in range(M):
        for n in range(-N, N):
            for m in range(-M, M):
                if m == 0 and n == 0:    # 공차가 0이면 무한반복이어성
                    continue
                x = i
                y = j
                cnt = 0    # 공차에 곱해줄 수
                val = ''    # 문자열
                while 0<=x<N and 0<=y<M:
                    val += str(arr[x][y])    # 현재값을 문자열에 합쳐줌
                    cnt += 1
                    value = int(val)
                    value_sqrt = math.sqrt(value)
                    value_decimal = value_sqrt - int(value_sqrt)
                    if value_decimal == 0 and ans < value:   # 제곱수이고 최대면
                        ans = value
                    x = i + cnt*n
                    y = j + cnt*m
print(ans)

