"""
1. DFS 깊이우선탐색으로 모든 정점을 방문하는 방법으로 시작 정점으로부터 아직 방문하지 않은 정점을 선택하고 방문 표시를 함
2. 한 번 왔던 지점은 T로 변형시켜 백트래킹을 사용하여 보다 효율적인 코드를 작성하려고 함

3. DFS 를 통해 한 번 왔던 지점은 T로 변형시켜 백트래킹을 사용함
이동 횟수가 k이면 cnt에 +1을 해주고 다시 재귀하여 다른 방향 탐색 가능하도록 함

4. 메모리 31256 KB | 실행시간 164ms
"""

import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
graph = [list(input()) for i in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

cnt = 0

def DFS(x, y, z) :
    global cnt
    # 도착 지점 : (0, c-1) | 거리 : k 이면 가짓수에 +1
    if k == z and x == 0 and y == c-1:
        cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.':
            graph[nx][ny] = 'T'
            DFS(nx, ny, z+1)
            graph[nx][ny] = '.'

graph[r-1][0] = 'T'
DFS(r-1, 0, 1)
print(cnt)

