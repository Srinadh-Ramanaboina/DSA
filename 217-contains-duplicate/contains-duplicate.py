class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        seen = set()

        for i in nums:
            if i in seen:
                return True

            seen.add(i)

        return False


obj = Solution()

dup1 = obj.containsDuplicate([1, 2, 3, 1])
dup2 = obj.containsDuplicate([1, 2, 3, 4])

print(dup1)
print(dup2)