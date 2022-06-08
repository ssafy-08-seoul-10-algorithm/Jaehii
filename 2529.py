num = int(input())
op = input().split()
mx, mn = "", ""    # 최대, 최소숫자
check = [False]*10    # 백트래킹 체크할 배열

def verify(a, b, c):    # 해당 자리에 숫자가 들어갈 수 있는지 검증
    if c == '>':
        return a>b
    else:
        return a<b

def fun(depth, s):    # 재귀함수 호출 DFS
    global mx, mn

    if depth == num+1:    # 끝까지 도달했을때
        if len(mn) == 0:    # 0부터 9로 가다보니 처음성공한게
            mn = s    # 제일 최소
        else:
            mx = s    # 최대는 계속 갱신
        return

    for i in range(10):    # 0 - 9 까지
        if not check[i]:
            if depth == 0 or verify(s[len(s)-1], str(i), op[depth-1]):    # depth가 0이면 오류나서
                check[i] = True    # 체크하고
                fun(depth+1, s+str(i))    # 재귀부르고
                check[i] = False    # 재귀 끝나면 체크해제

fun(0,"")    # 무에서 시작
print(mx)
print(mn)


