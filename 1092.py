import sys
n = int(input())    # 크레인 수
c_arr = map(int, sys.stdin.readline().split())
m = int(input())    # 박스 수
b_arr = map(int, sys.stdin.readline().split())

c_arr = sorted(c_arr, reverse=True)    # 내림차순 정렬
b_arr = sorted(b_arr, reverse=True)    # 내림차순 정렬

if c_arr[0] < b_arr[0]:
# 박스무게가 크레인의 최대제한무게보다 크면
    print(-1)
    exit()

c_check = [0 for _ in range(len(c_arr))]    # 사용크레인 체크
# cnt = 0    # 옮겨지는 박스의 수
# turn = 0    # 시간
ans = 0
while len(b_arr) > 0:
    for i in c_arr:    # 크레인의 제한무게. 크레인 다쓰면 다음턴으로 넘어가서 ans에 1 더해줌
        for j in range(len(b_arr)):
            if i >= b_arr[j]:
                del b_arr[j]
                break
    ans += 1
print(ans)




'''
<내가 짜고 실패>
for i in range(len(b_arr)):
    if len(b_arr) == 0:
        break
    for j in range(len(c_arr)):
        if len(b_arr) == 0:
            break
        i = 0    # 마지막에 해줘서 애먹음.. 계속 인덱스 에러뜸..
        # print("before:", i, j, b_arr[i], c_arr[j])
        if cnt == len(c_arr):    # 크레인 다썼으면
            break
        if b_arr[i] <= c_arr[j] and c_check[j] == 0:    # 작거나 같게 하는거 중요
            # 박스 무게가 크레인에 들어갈 수 있고 그 크레인을 아직 사용하지 않았다면
            # print("after:", i, j)
            cnt += 1
            del b_arr[i]    # 박스옮김
            c_check[j] = 1    # 사용크레인 체크
    # if cnt == len(c_arr):    # 주석한 이유 : 크레인 다 안썼어도 b_arr가 없어지면 turn 올려야돼서
    turn += 1    # 시간 1 늘림
    cnt = 0    # 박스 초기화
    c_check = [0 for _ in range(len(c_arr))]    # 크레인도 초기화
    # print("turn: %d i: %d j: %d" % (turn, i, j))
    # print(b_arr)
print(turn)

---> 계속 for문에서 i=0으로 초기화시켜주면서 b_arr가 빌 때까지 돌게 하는 방법인데 이렇게 할바엔 while에서 돌게하는게 나음
'''