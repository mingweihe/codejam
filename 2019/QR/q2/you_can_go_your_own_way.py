def solve(P):
    res = []
    for c in P:
        if c == 'S': res += 'E'
        else: res += 'S'
    return ''.join(res)


T = int(raw_input())
for i in xrange(1, T+1):
    N = int(raw_input())
    P = raw_input()
    ans = solve(P)
    print 'Case #{}: {}'.format(i, ans)
