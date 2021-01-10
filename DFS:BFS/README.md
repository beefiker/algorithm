# 📒 Coding Note



1. [DFS](DFS/)

   1. [DFS 간단 예제](#dfs)
   
   
   
2. [BFS](BFS/)
   
   1. [BFS 간단 예제](#bfs)
   
      
   
      



## 📌 DFS와 BFS의 간단 예제

1. ### DFS (Depth-First-Search) <a name="dfs"></a>

   DFS는 `깊이 우선 탐색`이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.

   이 알고리즘은 특정한 경로로 탐색하다가 특정한 상황에서 최대한 깊숙이 들어가서 노드를 방문한 후, 다시 돌아가 다른 경로로 탐색하는 알고리즘이다.

   - 구체적인 동작 과정
     1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
     2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
     3. `2`번의 과정을 더 이상 수행할 수 없을 떄까지 반복한다.

   + 사용예제

     ```python
     # DFS 메서드 정의
     def dfs(graph, v, visited):
         # 현재 노드를 방문 처리
         visited[v] = True
         print(v, end=' ')
         
         # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
         for i in graph[v]:
             if not visited[i]:
               dfs(graph, i, visited)
     
     # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
     graph = [
         [],
         [2, 3, 8],
         [1, 7],
         [1, 4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6, 8],
         [1, 7]
     ]
     
     # 각 노드가 방문 여부를 리스트 자료형으로 표현(1차원 리스트)
     visited = [False] * 9
     
     # 정의된 DFS 함수 호출
     dfs(graph, 1, visited)
     ```
     
     

2. ### BFS (Breadth-First-Search) <a name="bfs"></a>

   BFS 알고리즘은 `너비 우선 탐색`이라는 의미를 가진다. 쉽게 말해 `가까운 노드부터 탐색하는 알고리즘`이다.

   DFS는 최대한 멀리 있는 노드를 우선으로 탐색했다면, BFS는 그 반대다.

   BFS는 선입선출 방식인 큐 자료구조를 이용하는 것이 정석이다. 인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면 자연스럽게 먼저 들어온 것이 먼저 나가게 되어, 가까운 노드부터 탐색을 진행하게 된다.

   - 구체적인 동작 과정
     1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
     2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
     3. `2`번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

   - 사용예제

     ``` python
     from collections import deque
     
     # BFS 메서드 정의
     def bfs(graph, v, visited):
         # 큐(Queue) 구현을 위해 deque 라이브러리 사용
         queue = deque([v])
     
         # 현재 노드를 방문 처리
         visited[v] = True

         # queue를 비울 때 까지 반복
         while queue:
             # 큐에서 하나의 원소를 뽑아서 출력
             popped = queue.popleft()
             print(popped, end=' ')
     
             # 뽑은 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입하고 방문 처리
             for i in graph[popped]:
                 if not visited[i]:
                     queue.append(i)
                     visited[i] = True
     
     # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
     graph = [
         [],
         [2, 3, 8],
         [1, 7],
         [1, 4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6, 8],
         [1, 7]
     ]
     
     # 각 노드의 방문 여부를 리스트 자료형으로 표현(1차원 리스트)
     visited = [False] * 9
     
     # 정의된 BFS 함수 호출
     bfs(graph, 1, visited)
     ```
     
     
