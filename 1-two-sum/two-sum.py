class Solution(object):
    def twoSum(self, nums, target):
        """
        starting the series in leetcode
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
      
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


obj = Solution()

Result = obj.twoSum([2, 7, 9, 11, 15], 9)

print(Result)
                
        