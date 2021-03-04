def filtering(Q, R, P):
    if len(Q) == len(R):
        cur_poss = set(range(1, int(Q[0])+1))
        if R[0] in P:
            P[R[0]] = P[R[0]] & cur_poss
        else:
            P[R[0]] = cur_poss


def solve(P):
    res = []
    for k, v in P.items():
        res += [v.pop(), k],
    return ''.join([c for _, c in sorted(res)])


T = int(raw_input())
for i in xrange(1, T+1):
    U = int(raw_input())
    possibilities = {}
    for _ in xrange(10000):
        Q, R = raw_input().split()
        filtering(Q, R, possibilities)
    res = solve(possibilities)
    print 'Case #{}: {}'.format(i, res)