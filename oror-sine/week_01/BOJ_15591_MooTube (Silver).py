"""
1. 적용 알고리즘
너비 우선 탐색(BFS)

====================================================

2. 문제 풀이를 위한 접근 방식 설명
어떤 동영상에서 다른 동영상으로 가는 경로가 반드시 하나 존재하므로
시작점에서부터 usado를 최솟값으로 갱신하며 너비 우선 탐색을 진행해 usado가 k이상인 경우를 구해준다.

====================================================

3. 기본 코드에 대한 설명
아래 코드에 주석으로 설명

====================================================

4. 시간 복잡도, 공간 복잡도
시간 복잡도: O(N)
공간 복잡도: O(N)
"""

import sys; input = sys.stdin.readline
from collections import deque, defaultdict

MAX_K = 1_000_000_000
N, Q = map(int, input().split())
U = defaultdict(list)

for i in range(N-1):
    p, q, r = map(int, input().split()); p -= 1; q -= 1
    U[p].append((q, r))
    U[q].append((p, r))

ans = ""
for i in range(Q):
    k, v = map(int, input().split()); v -= 1
    visited = [0]*N
    visited[v] = 1
    cnt = 0
    
    Q = deque([(v, MAX_K)])
    
    while Q:
        prev_v, prev_u = Q.popleft()
        for video, usado in U[prev_v]:
            if not visited[video] and (usado := min(prev_u, usado)) >= k:
                visited[video] = True
                Q.append((video, usado))
                cnt += 1

    ans += f"{cnt}\n"
    
print(ans)
