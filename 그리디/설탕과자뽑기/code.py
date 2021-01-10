h, w = map(int, input().split())
place = [[0] * w for _ in range(h)]

n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    for i in range(l):
        if d == 0:
            place[(x-1)][(y-1)+(i)] = 1
        else:
            place[(x-1)+(i)][(y-1)] = 1


for i in range(h):
    for j in place[i]:
        print(j, end=' ')
    print()
