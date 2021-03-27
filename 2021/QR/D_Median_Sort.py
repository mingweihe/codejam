#!/usr/bin/python2
import sys

class Node:
    def __init__(self, val = 0, nx=None, prev=None):
        self.val = val
        self.next = nx
        self.prev = prev

def get_result(node):
    ans = []
    while node:
        ans += node.val,
        node = node.next
    return ans

def get_median(i, j, k, cache):
    key = tuple(sorted([i, j, k]))
    if key in cache: return cache[key]
    print i, j, k
    sys.stdout.flush()
    ans = int(raw_input())
    cache[key] = ans
    if ans == -1:
        exit()
    return ans

# approach 1, for each insertion: O(n)
def insert(i, head, cache):
    if head.next == None:
        head.next = Node(i)
        return head
    median = get_median(head.val, head.next.val, i, cache)
    if median == head.val:
        node = Node(i)
        node.next = head
        return node
    elif median == i:
        node = Node(i)
        tmp = head.next
        head.next = node
        node.next = tmp
        return head
    else:
        new_head = insert(i, head.next, cache)
        if new_head != head.next:
            head.next = new_head
        return head
        
# open('response.txt', 'w').close()
# open('output.txt', 'w').close()
t, n, q = map(int, raw_input().split())
for cid in xrange(1, t+1):
    cache = {}
    head = Node(1)
    nodes = [head]
    for i in xrange(2, n+1):
        # binary search insertion, for each insertion: O(log(n))
        l, r = 0, len(nodes)-1
        added = False
        mid = -1
        while l + 1 < r:
            mid = (l + r) / 2
            median = get_median(nodes[mid].val, nodes[mid+1].val, i, cache)
            if median == nodes[mid].val:
                r = mid
            elif median == nodes[mid+1].val:
                l = mid
            else:
                node = Node(i)
                tmp = nodes[mid].next
                nodes[mid].next = node
                node.prev = nodes[mid]
                node.next = tmp
                tmp.prev = node
                added = True
                break
        if not added:
            if l <= 3:
                head = insert(i, head, cache)
            else:
                node = Node(i)
                nodes[-1].next = node
                node.prev = nodes[-1]

        # sorted node list
        nodes = []
        node = head
        while node:
            nodes += node,
            node = node.next
    print ' '.join(map(str, get_result(head)))
    sys.stdout.flush()
    # with open('output.txt', 'a') as f:
    #     f.write('Case #{}: {}\n'.format(cid, ' '.join(map(str, get_result(head)))))
    correctness = int(raw_input())
    if correctness != 1:
        exit()
    # with open('response.txt', 'a') as f:
    #     f.write('Case #{}: {}\n'.format(cid, correctness))

