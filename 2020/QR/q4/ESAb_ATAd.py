#! /usr/bin/env python2
import sys


def solve(B):
    res = []
    for i in xrange(1, B+1):
        print i
        sys.stdout.flush()
        response = raw_input()
        if not response.isdigit():
            exit()
        res += response,
    print ''.join(res)
    sys.stdout.flush()


T, B = map(int, raw_input().strip().split())
for _ in xrange(T):
    solve(B)
