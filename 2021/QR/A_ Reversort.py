def solve(cid):
    ans = 0
    n = int(raw_input())
    a = map(int, raw_input().split())
    for i in xrange(n-1):
        idx = i
        for j in xrange(i, n):
            if a[j] < a[idx]:
                idx = j
        a[i:idx+1] = a[i:idx+1][::-1]
        ans += idx - i + 1
    print 'Case #{}: {}'.format(cid, ans)

for cid in xrange(1, int(raw_input())+1):
    solve(cid)
