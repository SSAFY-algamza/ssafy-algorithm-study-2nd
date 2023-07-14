"""
1. BFS 너비우선탐색은 루트 노드에서 인접한 노드부터 먼저 탐색 => 큐를 통해 구현
두 노드 사이의 최단 경로 혹은 임의의 경로를 찾고 싶을 때 사용하는 알고리즘

2. 속도를 줄이기 위해 deque를 사용

3. 길이를 계속 더해서 최단 경로를 구하는 것이 아니라 노드를 지날 때마다 최소 유사도로 변경해줘야 하는 것을 알고
방문 리스트와 현재 노드까지 측정된 유사도의 값을 가지고 동영상의 개수를 구함
문제에서 한 동영상에서 한 동영상으로 가는 경로가 반드시 하나인 점을 통해 트리구조로 만들어 알고리즘을 짬

4. 파이썬으로는 시간초과 해결이 안되어 pypy3으로 한 결과 메모리 123996KB | 실행 시간 1160ms

5. 파이썬으로 해결하는 방법을 알고싶습니다...
"""

from collections import deque
import sys
input = sys.stdin.readline

# n, q
n, q = map(int, input().split())
graph = [[] for _ in range(n+1)]

# a, b 동영상이 usado로 연결되어 있음을 뜻함 => 양방향 간선으로 추가해놓기!
for _ in range(n-1):
    a, b, usado = (map(int, input().split()))
    graph[a].append((b, usado))
    graph[b].append((a, usado))

# q개의 질문 
# 동영상 v 기준으로 유사도 k 이상인 동영상의 개수 구하기
for i in range(q):
    k, v = map(int, input().split())
    cnt = 0
    q = deque()

    visited = [0] * (n + 1)
    visited[v] = 1

    q.append((v, float('inf')))
    
    while q:
        x, c = q.pop()
        for nx, nc in graph[x]:
            # 최소 유사도 구하기 => 만약 방문하지 않은 동영상이고, 최소 유사도가 k 이상일 때 cnt 증가
            nc = min(c, nc)
            if not visited[nx] and nc >= k:
                cnt += 1
                visited[nx] = 1
                q.append((nx, nc))

    print(cnt)