#! /usr/bin/env python2
# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Qualification Round - Problem D. Dat Bae
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881de
#
# Time:  O(NlogB)
# Space: O(N)
#

import sys


def clear_file():
    with open('output.txt', 'w') as f:
        f.write('')


def write_out(line):
    with open('output.txt', 'a') as f:
        f.write('%s\n' % line)


def dat_bae():
    N, B, F = map(int, raw_input().strip().split())
    write_out('intput: %d %d %d' % (N, B, F))
    # find the smallest Q s.t. 2**Q > B
    # p.s. if 2**Q <= B, when the whole 2**Q block is missing,
    #      we cannot tell which block is lost
    Q = B.bit_length()  # floor(log2(B))+1
    assert(2**Q > B and Q <= F)

    idxs = [0]*(N-B)
    for j in xrange(Q):  # floor(log2(B)) + 1 times
        query = [((i % (2**Q)) >> j) & 1 for i in xrange(N)]
        guess = "".join(map(str, query))
        write_out('guess    : %s' % guess)
        print guess
        sys.stdout.flush()
        response = raw_input()
        write_out('response : %s' % response)
        response = map(int, response)
        for i in xrange(len(response)):
            idxs[i] |= (response[i]) << j

    result = []
    i, pow_Q_of_2 = 0, 2**Q
    for idx in xrange(N):
        if idxs[i] != (idx % pow_Q_of_2):
            result.append(str(idx))
        elif i+1 < len(idxs):
            i += 1

    ans = " ".join(result)
    write_out('ans: {}\n'.format(ans))
    print ans
    sys.stdout.flush()
    verdict = input()
    if verdict == -1:  # error
        exit()


clear_file()
for case in xrange(input()):
    dat_bae()
