import sys
sys.stdin = open('input.txt')

'''
1. 모든 수 1로만 더해진 수로 우선 표현 가능하므로 
   n의 범위인 1~10000 까지의 DP값을 우선 1로 초기화 한다
   
2. 2이상의 수는 각 수에서 2를 뺀 값에서 2를 더해 만들 수 있으므로 현재 경우의 수에 
   2, 10000까지의 모든 수에 대해 2를 뺀 값의 경우의 수를 더한다
   
3. 3이상의 수도 마찬가지로 현재 경우의 수에
   3, 10000까지의 모든 수에 대해 3을 뺀 값의 경우의 수를 더한다
   
4. 정수 n에 대한 DP값을 출력한다
'''

t = int(input())

dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i-2]

for i in range(3, 10001):
    dp[i] += dp[i-3]

for tc in range(1, t+1):
    n = int(input())
    print(dp[n])