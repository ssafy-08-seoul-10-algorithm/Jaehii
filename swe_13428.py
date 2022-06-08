'''
N = int(input())
for test_case in range(1, N+1):
    s = input()
    min_arr = sorted(s)    # 작은순서정렬
    max_arr = sorted(s, reverse=True)    # 큰순서정렬
    # 최댓값만들기
    lst1 = list(s)
    for i in range(len(s)):
        if lst1[i] != max_arr[i]:    # 큰 순서대로 앞쪽에 있지않으면
            j = s.rfind(max_arr[i])    # 바꿔준 값의 원래위치(뒤서부터 찾기)
            tmp = lst1[i]
            lst1[i] = max_arr[i]
            lst1[j] = tmp
            break    # 바꾸어주고 탈출
        else:    # 이미 되어있으면 그 다음꺼 바꿔줌
            continue
    # 최솟값만들기
    lst2 = list(s)
    for i in range(len(s)):
        if lst2[i] != min_arr[i]:
            # 아래줄에서 2시간헤맴 min_arr[i]가 "문자"0이라서 안나왔던거임
            if (i == 0) and (min_arr[i] == '0'):    # 옮겼을때 맨앞이 0이되면
                a = min_arr.index(lst2[i])    # 현재 맨앞에꺼 찾아내서
                min_arr[a] = min_arr[i]    # 바꿔줌
                continue
            else:
                j = s.rfind(min_arr[i])    # 바꿔준 값의 원래위치
                tmp = lst2[i]
                lst2[i] = min_arr[i]
                lst2[j] = tmp
                break
        else:
            continue

    ans1 = "".join(lst1)    # 최댓값
    ans2 = "".join(lst2)    # 최솟값
    # 출력
    print("#%d %s %s" % (test_case, ans2, ans1))
'''
from itertools import combinations
t = int(input())

for tc in range(1, t + 1):
    data = list(map(str, input()))
    target = [i for i in range(len(data))]    # 조합으로 고를 인덱스 위함
    min_val, max_val = "".join(data), "".join(data)    # 리스트를 문자열로

    for idx in combinations(target, 2):
        i, j = idx    # 조합으로 고른 두개의 인덱스
        data[i], data[j] = data[j], data[i]
        if data[0] == '0':    # 숫자아니라 문자로 쓰는거 매우중요
            data[i], data[j] = data[j], data[i]    # 원상복구
            continue
        if int(''.join(data)) < int(min_val):
            min_val = ''.join(data)
        if int(''.join(data)) > int(max_val):
            max_val = ''.join(data)
        data[i], data[j] = data[j], data[i]    # 다음턴을 위해 원상복구

    print("#%d %s %s" % (tc, min_val, max_val))










