T = int(input())
for tc in range(1, T+1):
    num = int(input())    # 들어야하는 수업개수
    arr = list(map(int, input().split()))
    min_val = 1e9    # 최솟값

    for i in range(7):
        if arr[i] == 1:    # 1인거 찾아서 한번씩 다 돌려보고 비교
            idx = i    # 1인거부터 시작해야하니까 인덱스 필요
            temp_n = num
            ans = 0
            while temp_n:    # n이 0이 될때까지
                if arr[idx] == 1:
                    temp_n -= 1    # 들은 수업일수 하나 줄이고
                ans += 1    # 수업없는날이어도 일수 늘려줘야됨
                idx = (idx + 1) % 7    # 이렇게 하면 돌리기 편함 !!

            if min_val > ans:    # 최솟값 갱신
                min_val = ans

    print('#%d %d' % (tc, min_val))    # 다해놓고 ans로 적어서 몇번 틀림






'''
idx = []
    cnt = 0    # 들은 수업수
    ans = 0    # 몇일인지
    for i in range(0, 7):
        if arr[i] == 1:
            idx.append(i)    # 1인 인덱스
    n = len(idx)    # 일주일의 수업개수
    min_val = 1e9
    for a, i in enumerate(idx):
        print("a:%d i:%d" %(a, i))
        while True:
            ans += 1    # 일수 증가
            if arr[i] == 1:
                cnt += 1
            if cnt == num:    # 다 채웠다면
                print("end")
                break
            if i == 6:    # 다시돌기
                i = 0
            else:
                i += 1
        print("tc:%d cnt:%d" % (tc, ans))
        if min_val > ans:
            min_val = ans
    print("#%d %d" % (tc, ans))
'''

'''
    if (num//n-1) == 1:    # 중간거 필요X
        ans = (7 - idx[0]) + (idx[(num % n) - 1] + 1)
    else:
        if num//n != 1:
            ans = (7 - idx[0]) + 7 * (num // n - 1) + (idx[(num % n) - 1] + 1)
        else:
            ans = (idx[(num % n) - 1] + 1)
    print("#%d %d" % (tc,ans))
'''




