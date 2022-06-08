T = int(input())
for tc in range(1, T+1):
    D, L, N = map(int, input().split())
    ans = 0
    for i in range(N):
        sum = D * (1 + i*L/100)
        ans += sum
    print("#%d %d" % (tc, ans))