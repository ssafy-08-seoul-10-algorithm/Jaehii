arr = input()
result = int(arr[0])

"""while True:
    i += 1
    if i == len(arr):
        break"""
for i in range(1, len(arr)):
    if result > 1 and int(arr[i]) > 1:
        result *= int(arr[i])
    else:
        result += int(arr[i])

print(result)
