import sys
input =sys.stdin.readline
dp = [0]*5001
n = int(input())
dp[3] = 1
dp[5] = 1
for i in range(6,n+1):
    if dp[i-5] !=0 and dp[i-3] != 0:
        dp[i] = min(dp[i-5], dp[i-3]) +1
    elif dp[i-5] != 0:
        dp[i] = dp[i-5] +1
    elif dp[i-3] != 0:
        dp[i] = dp[i-3] +1
    else:
        dp[i] = 0
if dp[n] == 0:
    print(-1)
else:
    print(dp[n])