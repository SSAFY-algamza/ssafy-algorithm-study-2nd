import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

'''
1. USADO 그래프의 index를 비디오 쌍의 번호로써 값에 USADO를 저장한다.

2. 각 질문의 비디오 번호를 큐에 append, 0번 비디오는 존재하지 않으므로 방문 값을 1로 변경한다

3. 현재 비디오 번호를 큐에서 pop, 현재 위치의 방문 값을 1로 변경한다

4. 만약 방문 값이 모두 1인 경우 모두 방문한 것이므로 while문 종료

5. 현재 비디오 번호를 행 값으로 갖는 그래프에서
   5-1. USADO 값이 k 보다 큰 경우
   5-2. 아직 방문하지 않은 번호의 비디오인 경우
   큐에 append, 방문 값을 1로 변경하고, 결과 값을 + 1
   (가장 작은 USADO가 k보다 커야 하므로, k보다 작은 USADO의 경우 유망하지 않다고 생각했습니다)

6. 전체 결과 값을 출력한다.
'''

N, Q = map(int, input().split())
USADO = [[0] * (N+1) for _ in range(N+1)]

for i in range(N-1):
    p, q, r = map(int, input().split())
    USADO[p][q] = r
    USADO[q][p] = r

for i in range(Q):
    k, v = map(int, input().split())
    visited = [0] * (N+1)
    visited[0] = 1
    q = deque()
    q.append(v)
    rlt = 0

    while q:
        now = q.popleft()
        visited[now] = 1
        if all(visited):
            break
        for j in range(1, N+1):
            if not visited[j] and USADO[now][j] >= k:
                q.append(j)
                visited[j] = 1
                rlt += 1

    print(rlt)