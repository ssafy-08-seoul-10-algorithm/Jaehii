n, m = map(int, input().split())
lst = [0] + list(map(int, input().split()))    # 눈덩이의 시작위치가 0인거 생각
ans = -1

def fun(idx, size, t):
    global ans

    if t > m:    # t 전까지는 유효
        return

    if t <= m:
        ans = max(size, ans)
    if idx+1 <= n:
        fun(idx+1, size+lst[idx+1], t+1)
    if idx+2 <= n:
        fun(idx+2, size//2 + lst[idx+2], t+1)

fun(0, 1, 0)
print(ans)
