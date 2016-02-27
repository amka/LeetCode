#!/usr/bin/env python


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: list of int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=lambda x: x == 0)


if __name__ == '__main__':
    s = Solution()

    nums = [1, 2, 0, 5, 0, 2, 0, 2]
    s.moveZeroes(nums)
    print nums
