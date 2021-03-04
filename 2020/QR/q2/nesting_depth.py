def solve(S):
    res = []
    require = 0
    for c in S:
        num = int(c)
        while require > num:
            res += ')',
            require -= 1
        while require < num:
            res += '(',
            require += 1
        res += c,
    while require > 0:
        res += ')',
        require -= 1
    return ''.join(res)


T = int(raw_input())
for i in xrange(1, T+1):
    S = raw_input()
    res = solve(S)
    print 'Case #{}: {}'.format(i, res)
