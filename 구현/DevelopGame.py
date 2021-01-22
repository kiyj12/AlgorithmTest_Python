# p.118 나중에 다시 한 번 풀어볼 것. 
# 질문 있음.


n, m = map(int, input().split())    # 첫줄 map 정보 입력받기

d = [[0]*m for i in range(n)]       # 게임 map 창조

x, y, direction = map(int, input().split())
d[x][y] = 1     # 가본 육지는 바다와 동일한 1로 바꾸어 가지 못하게 한다.
count = 1
turn = 0

# 전체 맵 정보 array로 input
arr = []
for i in range(n):
    arr.append(list(map(int, input().split() )))

xmove = [-1, 0, 1, 0]   # 북 동 남 서 이동 ex) 북쪽 바라보고 있으면 왼쪽 한 칸
ymove = [0, 1, 0, -1]

# 갈 수 있으면 일단 감
fl = [x, y]

while True:
    direction -= 1
    if direction < 0:
        direction = 3
    fl[0] = x + xmove[direction]
    fl[1] = y + ymove[direction]

    if arr[fl[0]][fl[1]] == 0:
        x = fl[0]
        y = fl[0]
        count += 1
        turn = 0
        continue
    
    else:
        turn += 1
    
    # 사방이 다 막혀있을 때 = 4번 다 돌아봤을 때
    if turn == 4:
        direction += 1          ###### 질문~!!! 이거 왜 안 필요한지..? 바라보는 방향을 유지한다는 게 왼쪽 돈 상태 고대로?
        if direction > 3:
            direction = 0
        fl[0] = x - xmove[direction]    # 생각이 짧았다.
        fl[1] = y - ymove[direction]

        if arr[fl[0]][fl[1]] == 0:
            x = fl[0]
            y = fl[1]
            count += 1
        else:
            break
        turn = 0

print(count)





# 방향

