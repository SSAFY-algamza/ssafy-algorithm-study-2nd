# 2. 문제 풀이를 위한 접근 방식 설명

"""
1. 적용 알고리즘
깊이 우선 탐색(DFS)

====================================================

2. 문제 풀이를 위한 접근 방식 설명
깊이가 목표인 K에 도달했을 때 목적지에 있으면 카운트한다.

====================================================

3. 기본 코드에 대한 설명
아래 코드에 주석으로 설명

====================================================

4. 시간 복잡도, 공간 복잡도
시간 복잡도: O(RC)
공간 복잡도: O(RC)
"""


import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())
visited = [[cell == "T" for cell in input()] for _ in range(R)]  # T는 가지 못하는 곳이므로 이미 방문한 것으로 간주한다.

START, END = (R-1, 0), (0, C-1)  # 시작지점과 목적지
ds = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 네 방향

def DFS(current, depth):
    if depth == K:  # 거리가 K일 때
        return current == END  # 목적지에 도달했다면 True(1) 아니면 False(0)
    
    ans = 0   # 거리가 K일 때 목적지에 도달한 경우의 수
    r, c = current

    for dr, dc in ds:  # 각 방향에 대해
        if not (0 <= (nr:=r+dr) < R and 0 <= (nc:=c+dc) < C): continue  # 맵을 벗어나면 건너뜀
        if visited[nr][nc]: continue  # 이미 방문한 곳이면 건너 뜀

        visited[r][c] = True
        ans += DFS((nr, nc), depth + 1)  # 거리가 K일 때 목적지에 도달한 경우의 수를 더한다.
        visited[r][c] = False
    
    return ans  # 거리가 K일 때 목적지에 도달한 경우의 수 반환

print(DFS(START, 1))
