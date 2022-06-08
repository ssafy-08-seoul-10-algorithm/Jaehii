T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())    # map 꼭 써주기 !!
    ans = (a+b)%24
    print('#%d %d' % (tc, ans))