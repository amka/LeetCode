#!/usr/bin/env python


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: list of int
        :rtype: int
        """
        num = 0
        for x in range(len(nums)):
            num ^= nums[x]

        return num

if __name__ == '__main__':
    s = Solution()
    print s.singleNumber([1, 2, 1, 5, 5, 6, 7, 2, 7])
