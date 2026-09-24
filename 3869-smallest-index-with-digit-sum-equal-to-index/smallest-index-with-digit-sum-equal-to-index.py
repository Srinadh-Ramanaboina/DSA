class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)

        for i in range(n):
            num = nums[i]
            sum1 = 0

            while num > 0:
                sum1 += num % 10
                num //= 10

            if sum1 == i:
                return i

        return -1

obj = Solution()

ex1 = obj.smallestIndex([1,3,2])

ex2 = obj.smallestIndex([1,10,11])

ex3 = obj.smallestIndex([1,2,3])

print(ex1)
print(ex2)
print(ex3)

           