# TODO
cid = int(raw_input())
_ = int(raw_input())
a = []
for _ in xrange(100):
    a += raw_input(),
corrects = 0
for i in xrange(100):
    for x in a[i]:
        corrects += x == '1'
p1 = float(corrects) / (100*10000)

ans = 0
print 'Case #{}: {}'.format(cid, ans)
