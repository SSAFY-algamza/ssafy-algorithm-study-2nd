"""
1. DP 동적계획법 : 반복되는 연산을 활용하여 빠르게 풀 수 있는 것 => 주로 작은 문제에서 반복이 일어나고 같은 문제는 항상 정답이 같을 경우에 사용
메모이제이션 : 한 번 계산한 문제는 다시 계산하지 않도록 저장해두고 활용하는 방식 
! 점화식을 도출하여 동적 계획법을 적용시키는 것이 핵심 !

2. 직접 손으로 풀어보며 점화식을 구해봄

3. 반복문을 통해 dp 리스트의 나머지 값을 계산 => 인덱스 i가 4부터 10000까지 증가하며
dp[i]를 dp[i-1]과 (dp[i-2] - dp[i-3])의 합으로 설정 dp[i]가 1일때, dp[0] 값이 나오므로 이것 역시 1로 지정해둠

4. 메모리 31256KB | 실행 시간 44ms
"""

import sys
input = sys.stdin.readline

T = int(input())

# number은 n값을 입력받아 저장하는 리스트
number = []

for _ in range(T):
    n = int(input())
    number.append(n)

# dp 리스트를 초기화하는 부분으로 dp[i]는 i를 만들기 위한 경우의 수
dp = [0 for _ in range(10001)]
dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 3

# dp 리스트를 계산하는 부분
for i in range(4, 10001):
    dp[i] = dp[i-1] + (dp[i-2] - dp[i-3])
    if i % 3 == 0:
        dp[i] += 1

for n in number:
    print(dp[n])