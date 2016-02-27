#!/usr/bin/env python


class Solution(object):
    def trap(self, height):
        """
        :type height: list of int
        :rtype: int
        """
        water = 0
        height_len = len(height)
        if height_len < 3:
            return water

        max_level = max(height)
        max_level_index = height.index(max_level)

        prev_level = height[0]
        for x in range(max_level_index):
            level = height[x]

            if level < prev_level and level < max_level:
                water += (prev_level - level)
            else:
                prev_level = level

        prev_level = height[-1]
        for x in range(height_len-1, max_level_index, -1):
            level = height[x]

            if level < prev_level and level < max_level:
                water += (prev_level - level)
            else:
                prev_level = level

        return water


if __name__ == '__main__':
    s = Solution()

    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print s.trap(height)
