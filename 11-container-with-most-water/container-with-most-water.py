class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1

        maximum = 0

        while left < right:

            distance = right - left

            shorter_wall = min(height[left], height[right])

            water = distance * shorter_wall

            maximum = max(maximum, water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maximum


obj = Solution()

Ex1 = obj.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])

Ex2 = obj.maxArea([1, 1])

print(Ex1)
print(Ex2)