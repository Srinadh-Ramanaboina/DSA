class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        n = len(nums)

        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):

            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:

                total = nums[i] + nums[j] + nums[k]

                if abs(total - target) < abs(closest - target):
                    
                    closest = total 

                if total < target :

                    j +=1

                elif total > target :
                    k -=1

                else : 
                    return total 

        return closest 

obj = Solution()

ex1 = obj.threeSumClosest([-1,2,1,-4],1)

ex2 = obj.threeSumClosest([0,0,0],1)

print(ex1)

print(ex2)


                

        
            