def solve(intervals):
    res = []
    J_ava, C_ava = 0, 0
    intervals.sort()
    for s, e, j in intervals:
        if s >= J_ava:
            res += [j, 'J'],
            J_ava = e
        elif s >= C_ava:
            res += [j, 'C'],
            C_ava = e
        else:
            return 'IMPOSSIBLE'
    res = [p for _, p in sorted(res)]
    return ''.join(res)


T = int(raw_input())
for i in xrange(1, T+1):
    N = int(raw_input())
    intervals = []
    for j, _ in enumerate(xrange(N)):
        S, E = map(int, raw_input().split())
        intervals += [S, E, j],
    res = solve(intervals)
    print 'Case #{}: {}'.format(i, res)
