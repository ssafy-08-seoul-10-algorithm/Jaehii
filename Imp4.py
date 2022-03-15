input_str = input()    # 입력받음
res = []    # 결과넣을 배열
sum = 0

for i in input_str:    # 하나씩 확인
    if i.isalpha():
        res.append(i)
    else:
        sum += int(i)

res.sort()    # 문자열 소트

if sum > 0:    # 숫자가 있다면
    res.append(str(sum))    # 문자열 뒤에 붙여줌

print(''.join(res))    # 빈칸없이 나오게