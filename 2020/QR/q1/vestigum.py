def solve(N, M):
    k, r = 0, 0
    cols = [set() for _ in xrange(N)]
    for i in xrange(N):
        row = set()
        for j in xrange(N):
            if i == j:
                k += M[i][j]
            row.add(M[i][j])
            cols[j].add(M[i][j])
        if len(row) != N:
            r += 1
    c = sum(len(x) != N for x in cols)
    return k, r, c


T = int(raw_input())
for i in xrange(1, T+1):
    N = int(raw_input())
    M = []
    for _ in xrange(N):
        row = map(int, raw_input().split())
        M += row,
    k, r, c = solve(N, M)
    print 'Case #{}: {} {} {}'.format(i, k, r, c)
