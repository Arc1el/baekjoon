values = input()
values = values.split()
n = int(values[0])
k = int(values[1])

bag = [[0,0]]

for _ in range(n):
    bag.append(list(map(int, input().split())))

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n + 1):
    for cap in range(1, k + 1):
        weight = bag[i][0]
        value = bag[i][1]

        if cap < weight:
            dp[i][cap] = dp[i-1][cap]
        else:
            dp[i][cap] = max(
                (dp[i-1][cap-weight] + value), dp[i-1][cap])

print(dp[n][k])
