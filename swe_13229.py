T = int(input())
for tc in range(1, T+1):
    day = input()
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    idx = days.index(day)
    ans = 6 - idx
    if ans == 0:
        ans = 7
    print("#%d %d" % (tc, ans))
