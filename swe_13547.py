T = int(input())
for test_case in range(1, T+1):
    arr = input()
    cnt = 0
    for _ in arr:
        if _ == 'o':
           cnt += 1
    x = 15 - len(arr)
    ans = cnt + x
    if ans >= 8:
        print("#%d YES" % test_case)
    else:
        print("#%d NO" % test_case)