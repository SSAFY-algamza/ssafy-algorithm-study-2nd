import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt')

def dfs(now):
    global result
    visited[now] = 1
    tmp.append(now)
    next = students[now]

    if visited[next]:
        if next in tmp:
            result += tmp[tmp.index(next):]
        return
    else:
        dfs(next)


t = int(input())
for tc in range(t):
    n = int(input())
    students = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)
    result = []

    for i in range(1, n+1):
        if not visited[i]:
            tmp = []
            dfs(i)

    print(n - len(result))