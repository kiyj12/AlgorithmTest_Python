pos = input()

xstr = pos[0]
y = int(pos[1])

xlist = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h']

x = xlist.index(xstr) + 1

cnt = 0

steps = [(2, -1), (2, 1), (-1, -2), (1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2)]

for step in steps:
    next_x = x + step[0]
    next_y = y + step[1]

    if (next_x >= 1) and (next_x <= 8) and (next_y >= 1) and (next_y <= 8):
        cnt += 1

print(cnt)