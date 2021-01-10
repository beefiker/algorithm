place = []
for i in range(10):
    place.append(list(map(int, input().split())))

# 오른쪽, 아래 이동
dx = [0, 1]
dy = [1, 0]
x, y = 1, 1

isThereHouse = False
direction = 0

place[x][y] = 9
while True:
    for i in range(10):
        for j in range(10):
            if place[i][j] == 2:
                isThereHouse = True
    
    if not isThereHouse:
        break

    if place[x+dx[direction]][y+dy[direction]] == 0:
        x += dx[direction]
        y += dy[direction]
        place[x][y] = 9
        direction = 0

    if place[x+dx[direction]][y+dy[direction]] == 1:
        direction += 1

    if place[x+dx[direction]][y+dy[direction]] == 2:
        x += dx[direction]
        y += dy[direction]
        place[x][y] = 9
        break

    if x >= 8 and y >= 8:
        break
    

for i in range(10):
    for j in place[i]:
        print(j, end=' ')
    print()
