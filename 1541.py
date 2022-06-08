import re

arr = input()
num_arr = arr.replace('+', ' ').replace('-', ' ').split()   # 기호를 공백으로 바꾼후 split으로 공백과 수 분리
mark_arr = re.findall('[^0-9]', arr)    # re 라이브러리를 이용해서 숫자가 아닌 것만 모음

for i in range(len(mark_arr)):
    if i == (len(mark_arr)-1):    # i가 마지막 아이템이면 for문 탈출
        break
    if mark_arr[i] == '-' and mark_arr[i+1] == '+':    # - 뒤의 +는 다 -로 바꿈(그래야 최소됨)
        mark_arr[i+1] = '-'


ans = int(num_arr[0])   # ans 값 초기화

for i in range(len(num_arr)):
    if i == (len(num_arr)-1):    # i가 마지막 아이템이면 for문 탈출
        break
    if mark_arr[i] == '-':
        ans = ans - int(num_arr[i+1])
    else:
        ans = ans + int(num_arr[i+1])

print(ans)
