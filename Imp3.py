size = 8
dxys = [(-1, 2), (-1, -2), (1, 2), (1, -2), (-2, -1), (-2, 1), (2, -1), (2, 1)]
arr = [[0] * size for i in range(size)]
cnt = 0

x = input()
col = int(x[1])-1
row = str(x[0])
row_arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i in range(len(row_arr)):
    if row == row_arr[i]:
        row = i
        break
    else:
        continue

print(row, col)
for dxy in dxys:
    next_row = row + dxy[0]
    next_col = col + dxy[1]
    if next_row < 0 or next_col < 0 or next_row > 7 or next_col > 7:
        continue
    cnt += 1

print(cnt)