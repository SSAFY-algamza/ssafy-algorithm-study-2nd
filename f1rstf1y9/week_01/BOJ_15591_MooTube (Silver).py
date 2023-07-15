"""
1. 적용 알고리즘
너비 우선 탐색(BFS)

====================================================

2. 문제 풀이를 위한 접근 방식 설명
일단 두 영상 사이의 유사도가 주어지니까 graph[p]에 p와 연관 영상(q)들 사이의 유사도 r을 (q,r)의 리스트로 담자.
문제의 핵심은 v번 영상에 대해 그 영상과 usado가 k 이상인 모든 동영상의 개수를 구하는 것이다!
usado는 v번 영상에서 다른 영상까지 가는 경로 중에 존재하는 영상들과의 usado의 최솟값인데,
문제에서 "어떤 동영상에서 다른 동영상으로 가는 경로가 반드시 하나 존재한다"라고 했으므로
BFS 탐색을 통해 계속 usado를 최솟값으로 갱신해주면서 도착했을때 usado가 k이상인 경우를 구해주면 된다.


====================================================

3. 기본 코드에 대한 설명
아래 코드에 주석으로 설명

====================================================

4. 시간 복잡도, 공간 복잡도
시간 복잡도: O(N)
공간 복잡도: O(N)
"""


from collections import deque
import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
graph = [[] for i in range(N+1)]

for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

for _ in range(Q):
    k, v = map(int, input().split()) # v번 영상에 대해 그 영상과 usado가 k 이상인 모든 동영상의 개수 구하기


    visited = [False]*(N+1) # 방문리스트 초기화
    visited[v] = True # 출발 지점인 v번 영상 방문 처리
    ans = 0
    q = deque()

    for cur_v, cur_usado in graph[v]:
        q.append((cur_v, cur_usado)) # 출발지점인 v와 연결 관계에 있는 영상을 (영상, 유사도) 형태로 큐에 추가
        visited[cur_v] = True # 연결관계에 있는 영상들은 방문 처리

    while q:
        cur_v, cur_usado = q.popleft() # 큐에 남아있는 영상들 하나씩 꺼내기
        if cur_usado >= k: # 현재 영상의 유사도가 k 이상이면?
            ans += 1 # 정답 변수에 카운팅
            for v, usado in graph[cur_v]: # 현재 영상과 연결 관계에 있는 영상들 순회하기
                if not visited[v]: # 해당 영상이 방문한 영상이 아니라면,
                    visited[v] = True # 방문한 영상으로 바꿔주고
                    q.append((v, min(cur_usado, usado))) # 현재 영상의 유사도와 연결된 영상의 유사도 중 더 작은값으로 유사도를 갱신하고 큐에 추가

    print(ans)