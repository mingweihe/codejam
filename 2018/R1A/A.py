def valid(c1, c2, hs, pre, target):
    for i in xrange(1, len(hs)):
        r1, r2 = hs[i-1], hs[i]
        if pre[r2][c2] - pre[r1][c2] - pre[r2][c1] + pre[r1][c1] != target:
            return False
    return True

def solve(cid):
    a = []
    r, c, h, v = map(int, raw_input().split())
    for _ in xrange(r):
        row = []
        for x in raw_input():
            if x == '.': row += 0,
            else: row += 1,
        a += row,
    pre = [[0] * (c+1) for _ in xrange(r+1)]
    for i in xrange(1, r+1):
        for j in xrange(1, c+1):
            pre[i][j] = a[i-1][j-1] + pre[i-1][j] + pre[i][j-1] - pre[i-1][j-1]

    if pre[r][c] == 0:
        print 'Case #{}: {}'.format(cid, 'POSSIBLE')
        return
    target, rem = divmod(pre[r][c], (h+1)*(v+1))
    if rem != 0:
        print 'Case #{}: {}'.format(cid, 'IMPOSSIBLE')
        return

    num_per_row = target * (v+1)
    hs = [0]
    for i in xrange(1, r+1):
        if pre[i][c] - pre[hs[-1]][c] == num_per_row:
            hs += i,
    if len(hs) != (h+2):
        print 'Case #{}: {}'.format(cid, 'IMPOSSIBLE')
        return

    vs = [0]
    for i in xrange(1, c+1):
        if valid(vs[-1], i, hs, pre, target):
            vs += i,
    if len(vs) != v+2:
        print 'Case #{}: {}'.format(cid, 'IMPOSSIBLE')
        return
    print 'Case #{}: {}'.format(cid, 'POSSIBLE')

for cid in xrange(1, int(raw_input())+1):
    solve(cid)
