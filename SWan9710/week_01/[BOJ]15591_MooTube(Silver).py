'''
1. 적용 알고리즘 : 깊이 우선 탐색(BFS), 그래프 탐색
깊이 우선 탐색
한방향으로 쭉 가다 막히게 되면 가장 가까운 갈림길에서 꺽는 방식의 그래프 탐색 방식
====================================================================
2. 접근법
설명이 장황 하였지만 결국에는 입력받은 k보다 USADO가 높은 경우의 수를 찾는것
또한 힌트 부분을 보고 노드와 가중치 개념이란 걸 알고 한방향 탐색이란 말이 없으니
양방향 탐색으로 생각하고 서로의 노드를 이어준 뒤 깊이 우선 탐색을 실시해줌
====================================================================
3. 기본 코드에 대한설명
입력받은 값 들을 각각 그래프에 연결시켜줌 그러기 위해 빈 그래프를 우선 만들어줌
그 후 입력받은 k와 v중 k 보다 큰 USADO를 구하기 위해 시작지점이 v라 보고 BFS 실시
왔던길을 표시하기 위해 방문기록을 남길 배열을 만들어 주고 해당 방문 지점에 기록을 남긴 후 다음으로 넘어가면 해당 위치에 존재하는 v의 조건을 판별후 queue에 넣어주고 popleft로 꺼내는 방식으로 BFS를 끝까지 실시하게 됨
조건
첫줄에 N 과 Q 주어짐
N - 1 줄 동안 p, q, USADO 주어짐
Q 줄 동안 존의 질문 주어짐
USADO 가 k 보다 큰 경우를 찾는 단순 BFS 문제
====================================================================
4. 실행시간
python => 6588ms
pypy => 1100ms
'''
import sys
from collections import deque
input = sys.stdin.readline

N, Q = map(int, input().split())
graph = [[] for i in range(N+1)] # 빈 그래프

for _ in range(N-1):
    p, q, USADO = map(int, input().split())
    graph[p].append((q, USADO))
    graph[q].append((p, USADO))
    # 각각의 노드 연결

for _ in range(Q):
    k, v = map(int, input().split())
    # BFS 실행
    # k가 1인 경우 2번 동영상을 추천 -> 1, 2

    # 방문기록 표시할 배열
    visited = [0] * (N+1)

    # queue 생성
    queue = deque()

    # queue에 노드추가
    # v = 2
    queue.append(v)

    # 방문표시
    visited[v] = 1

    # USADO 가 k보다 큰 경우를 계산할 count
    count = 0 
    while queue:
        # 현재 queue에 들어있는 2를 꺼내옴
        v = queue.popleft()

        # 2번 노드와 연결된 노드들 탐색 -> 1,3,4
        for i in graph[v]:
            # 해당 노드가 방문기록이 없는경우
            if not visited[i[0]]:
                # 그 노드의 USADO가 k 보다 크거나 같다면
                if i[1] >= k:
                    # 해당 노드를 queue에 추가 해주고 count + 1, 방문기록 표시
                    queue.append(i[0])
                    count += 1
                    visited[i[0]] = 1
    # 질문이 끝났을 때 추천되는 동영상의 갯수
    print(count)