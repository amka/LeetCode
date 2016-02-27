#!/usr/bin/env python


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: list of int
        :rtype: int
        """
        if nums:
            return sum(range(len(nums) + 1)) - sum(nums)

if __name__ == '__main__':
    s = Solution()
    print s.missingNumber([1, 0, 2, 3, 5, 6])
