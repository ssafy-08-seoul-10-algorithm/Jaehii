n = int(input())
arr = list(map(int, input().split()))
arr.sort()
i = 0
num = 0

while True:
    if arr[i + (arr[i]-1)] > arr[i] or len(arr) < i + (arr[i]-1):
        break
    else:
        num += 1
        i = i + arr[i]

print(num)