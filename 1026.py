# GREEDY

x = input()
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
sum = 0

arr2.sort(reverse=True)    # B배열은 큰것부터
arr1.sort()    # A배열은 작은것부터

for i, j in zip(arr1, arr2):
    k = i * j
    sum += k

print(sum)
