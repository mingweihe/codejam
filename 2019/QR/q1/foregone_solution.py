def solve(N):
  a, b = '', ''
  for c in N:
    if c == '4':
      a += '3'
      b += '1'
    else:
      a += c
      b += '0'
  return a, int(b or '0')


T = int(raw_input())
for i in xrange(1, T+1):
  N = raw_input()
  a, b = solve(N)
  print 'Case #{}: {} {}'.format(i, a, b)
