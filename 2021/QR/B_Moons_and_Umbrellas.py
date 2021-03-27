def solve(cid):
    x, y, s = raw_input().split()
    n = len(s)
    x, y = map(int, [x, y])
    dp = [[0, 0] for _ in xrange(n+1)]
    dp[1][0] = float('inf') if s[0] == 'J' else 0
    dp[1][1] = float('inf') if s[0] == 'C' else 0
    for i in xrange(2, n+1):
        if s[i-1] == '?':
            dp[i][0] = min(dp[i-1][0], dp[i-1][1]+y)
            dp[i][1] = min(dp[i-1][1], dp[i-1][0]+x)
        elif s[i-1] == 'C':
            dp[i][0] = min(dp[i-1][0], dp[i-1][1]+y)
            dp[i][1] = float('inf')
        else:
            dp[i][0] = float('inf')
            dp[i][1] = min(dp[i-1][1], dp[i-1][0]+x)
    print 'Case #{}: {}'.format(cid, min(dp[n]))

for cid in xrange(1, int(raw_input())+1):
    solve(cid)
