"""
n = int(input())
arr = [300, 60, 10]
sub = n    # 나머지
arr2 = []   # A,B,C 개수 넣을 배열

for i in arr:
    if sub == 0:    # 다 나눠졌다면 탈출
        break
    var = sub//i    # 몇번씩 나눠지는지
    arr2.append(var)    # ABC 각각의 개수를 배열에 넣기
    sub -= i*var    # 나머지

if sub != 0:    # 안떨어짐
    print(-1)
else:
    for i in arr2:
        print(i, end=' ')
"""

num = int(input())
if num%10 != 0:    # 가장작은 C가 10인데 그걸로도 안나눠지면 안나눠지는거
    print(-1)
else:
    A = num//300
    B = (num%300)//60   # %로 나머지 출력!
    C = (num%300)%60//10
    print(A, B, C)