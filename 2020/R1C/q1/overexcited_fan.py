def solve(x, y, m):
    if x == y == 0: return 0
    # res = float('inf')
    for i, c in enumerate(m, 1):
        if c == 'N':
            y += 1
        elif c == 'E':
            x += 1
        elif c == 'S':
            y -= 1
        else:
            x -= 1
        min_req = abs(x) + abs(y)
        if(min_req <= i):
            return i
    # if(res == float('inf')):
    #     return 'IMPOSSIBLE'
    return 'IMPOSSIBLE'


T = int(raw_input())
for i in xrange(1, T+1):
    X, Y, M = raw_input().split()
    res = solve(int(X), int(Y), M)
    print 'Case #{}: {}'.format(i, res)
