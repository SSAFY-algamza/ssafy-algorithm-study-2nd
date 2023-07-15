import sys
sys.stdin = open("input.txt")

'''
1. 한수가 출발하는 지역은 (R-1, 0), 집은 (0, C-1)로 둔다

2. 현재 지점이 도착지인지 확인하고,
   2-1. 만약 도착지이고, 거리가 K라면 결과 값 +1
   2-2. 아니라면 유망하지 않으므로 return

3. 위의 경우가 아니라면 현재 유망하므로 한수가 갈 수 있는 네 방향을 탐색하고,
   3-1. 아직 가지 않은 곳인지
   3-2. T가 아닌지
   3-3. RxC 의 범위안에 있는지
   를 확인해 가야할 방향을 정한다.
   
4. 진행할 방향의 위치의 값을 이전 지점 값 + 1 로 변경하고 함수를 다시 호출한다.

5. 함수에서 return 되었다면, 진행했던 위치의 값을 다시 . 으로 초기화 한다.

6. 전체 결과 값을 출력한다. 
'''

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def DFS(arr, i, j):
    global rlt

    if (i, j) == goal:
        if arr[i][j] == K:
            rlt += 1
            return
        else:
            return
    else:
        if arr[i][j] + 1 > K:
            return

    new_arr = [[0] for _ in range(R)]
    for l in range(R):
        new_arr[l] = arr[l][::]

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == '.' and arr[ni][nj] != 'T':
            new_arr[ni][nj] = arr[i][j] + 1
            DFS(new_arr, ni, nj)
            new_arr[ni][nj] = '.'

R, C, K = map(int, input().split())
arr = [[0] * C for _ in range(R)]
rlt = 0
for i in range(R):
    arr[i] = list(input())

start = (R-1, 0)
goal = (0, C-1)

arr[start[0]][start[1]] = 1

DFS(arr, start[0], start[1])

print(rlt)