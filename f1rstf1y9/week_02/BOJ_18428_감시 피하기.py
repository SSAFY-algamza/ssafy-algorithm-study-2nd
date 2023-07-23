"""
1. 적용 알고리즘
백트래킹

====================================================


2. 문제 풀이를 위한 접근 방식 설명
3가지 장애물을 설치하는 모든 경우에 대해 백트래킹으로 조사해보면 되지 않을까?
선생님과 학생 위치를 제외한 공간에 하나씩 장애물을 설치하고 장애물이 3개가 되는 순간,
is_valid() 함수를 통해 선생님의 위치에서 상하좌우로 검사하면서 학생 위치에 도달하면 False를 반환하여 다른 장애물 위치를 탐색하고,
모든 선생님에 대해 네 방향 모두 검사했는데도 학생을 찾지 못했다면 True를 반환해서 YES를 출력하도록 하자.

====================================================

3. 기본 코드에 대한 설명
아래 코드에 주석으로 설명

====================================================

4. 시간 복잡도, 공간 복잡도
시간 복잡도: O(N^3)
공간 복잡도: O(N^2)

"""

N = int(input())
hall = [input().split() for _ in range(N)]

delta = [(1,0),(-1,0),(0,1),(0,-1)]

teacher = [] # 선생님 위치를 담을 리스트
for i in range(N):
    for j in range(N):
        if hall[i][j] == 'T':
            teacher.append((i,j))

def is_valid(): # 장애물 3개 설치 후 모든 학생들이 감시를 피할 수 있는지 확인
    for x, y in teacher:
        for dx, dy in delta: # 4방향에 대해 조사
            nx, ny = x + dx, y + dy
            while 0 <= nx < N and 0 <= ny < N: # 범위를 벗어나지 않을 때까지 한방향으로 쭉 이동
                if hall[nx][ny] == 'S': # 만약 학생을 찾았다면 바로 False 리턴
                    return False
                if hall[nx][ny] == 'O':
                    break
                nx, ny = nx + dx, ny + dy
    return True # 끝까지 학생 못 찾은 경우 True 리턴

isValid = False
def bt(n): # n은 현재까지 설치한 장애물 개수
    global isValid
    if isValid:
        return
    if n == 3: # 장애물 3개 설치한 경우 더이상 재귀를 호출하지 않도록 한다.
        if is_valid(): # is_valid()에서 True를 리턴 받은 경우 백트래킹 종료
            isValid = True
        return

    # 모든 위치에 장애물 설치 조사
    for i in range(N):
        for j in range(N):
            if hall[i][j] == 'X': # 해당 좌표에 선생님, 학생, 장애물이 없는 경우
                hall[i][j] = 'O'
                bt(n+1)
                hall[i][j] = 'X'

bt(0)
print("YES" if isValid else "NO")