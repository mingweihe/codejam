def check(rows, cols, sum_k, N, K):
    pass


def solve(N, K):
    pass


T = int(raw_input().strip())
for i in xrange(1, T+1):
    N, K = map(int, raw_input().strip().split())
    res = solve(N, K)
    if res == 'IMPOSSIBLE':
        print 'Case #{}: {}'.format(i, res)
    else:
        print 'Case #{}: {}'.format(i, 'POSSIBLE')
        for line in res:
            print line
