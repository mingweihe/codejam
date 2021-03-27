def solve(cid):
    n, c = map(int, raw_input().split())
    nums = range(1, n+1)
    ans = [0] * n
    c -= n - 1
    idx = 0
    while idx < n-1 and c > 0:
        if c >= n - idx - 1:
            c -= n - idx - 1
            nums[idx:n] = nums[idx:n][::-1]
        idx += 1
    if c != 0:
        print 'Case #{}: {}'.format(cid, 'IMPOSSIBLE')
        return
    for i, x in enumerate(nums):
        ans[x-1] = i + 1
    print 'Case #{}: {}'.format(cid, ' '.join(map(str, ans)))

for cid in xrange(1, int(raw_input())+1):
    solve(cid)
