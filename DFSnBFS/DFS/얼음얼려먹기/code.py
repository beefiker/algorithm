# 세로길이 N, 가로길이 M 입력받기
n, m = map(int, input().split())

graph = []
# 세로길이 N 만큼 입력받아 2차원 리스트 생성
for _ in range(n):
    graph.append(list(map(int, input().split())))

# DFS로 특정한 노드를 방문한 뒤 연결된 모든 노드를 재귀적으로 방문
def dfs(x, y):
    # 주어진 범위를 벗어나면 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드를 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우 위치의 노드도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False
    
count = 0

# 모든 노드에 대해 1 음료수 채우기
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            count += 1

print(count)