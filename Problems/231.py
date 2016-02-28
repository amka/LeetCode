#!/usr/bin/env python


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n - 1)) == 0


if __name__ == '__main__':
    s = Solution()

    print s.isPowerOfTwo(1)
    print s.isPowerOfTwo(-8)
    print s.isPowerOfTwo(8)
    print s.isPowerOfTwo(133)
    print s.isPowerOfTwo(256)
