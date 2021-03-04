import string


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def iter_convert(A, num):
    for i, x in enumerate(A):
        A[i] = x / num
        num = A[i]
    return A


def get_original_nums(L, A):
    res = []
    idx, num = -1, -1
    for i in xrange(L-1):
        if A[i] != A[i+1]:
            idx, num = i, gcd(A[i], A[i+1])
            break
    left = iter_convert(A[:idx+1][::-1], num)
    right = iter_convert(A[idx+1:], num)
    return left[::-1] + [num] + right


def solve(L, A):
    nums = get_original_nums(L, A)
    arr = sorted(set(nums))
    dic = {}
    for i, c in enumerate(string.ascii_uppercase):
        dic[arr[i]] = c
    return ''.join(map(dic.get, nums))


T = int(raw_input())
for i in xrange(1, T+1):
    N, L = map(int, raw_input().split())
    A = map(int, raw_input().split())
    print 'Case #{}: {}'.format(i, solve(L, A))
