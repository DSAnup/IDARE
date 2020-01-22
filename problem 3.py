# A left rotation operation on an array of size n shifts each of the array's elements.

import collections
def rotate_left(nums, d):
    q = collections.deque(nums)
    q.rotate(-d)
    return list(q)
#
nd = input().split()

n = int(nd[0])

d = int(nd[1])

a = list(map(int, input().rstrip().split()))
result = rotate_left(a, d)
print(' '.join(str(e) for e in result))