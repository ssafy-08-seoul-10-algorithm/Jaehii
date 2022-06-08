import math
T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    c = 2*b + 1
    ans = math.ceil(a/c)
    print('#%d %d' % (test_case, ans))