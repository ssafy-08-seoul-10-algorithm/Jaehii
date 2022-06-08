n, s = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0

def fun(num, sum):
    global cnt

    if num >= n:
        return

    sum += lst[num]

    if sum == s:
        cnt += 1

    fun(num+1, sum)
    fun(num+1, sum - lst[num])

fun(0,0)
print(cnt)