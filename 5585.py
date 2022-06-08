x = int(input())
y = 1000 - x
ans = 0
arr = [500, 100, 50, 10, 5, 1]

for i in arr:
    if y == 0:
        break
    var = y//i
    ans += var
    y = y - (i*var)

print(ans)