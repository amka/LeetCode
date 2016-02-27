#!/usr/bin/env python


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: list of int
        :type val: int
        :rtype: int
        """
        [nums.remove(x) for x in list(nums) if x == val]
        return len(nums)

if __name__ == '__main__':
    s = Soliution()
    print s.removeElements([1, 2, 3, 5, 7, 2, 6, 2], 6)
