"""n = 25
k = 3
count = 0

while n > 1:
    if n < k:   # k로 못나누니까 1빼는 방법뿐
        while n > 1:
            n = n-1
            count += 1
        break
    num1 = n//k   # 가장 가까운 k가 될때까지 1 빼려고
    num = n - k*num1
    count += num
    n = n-num    # 가장 가까운 k
    #print(n)
    n /= k   # 를 k로 나눈 횟수
    count += 1
    #print(n)

print(int(count))"""

n, k = map(int, input().split())

result = 0

while True:
    if n < k:
        break
    target = (n//k)*k
    result += n - target
    n = target
    n //= k
    result += 1

result += (n-1)    # 마지막으로 나온 수가 1이 될때까지 빼기

print(result)