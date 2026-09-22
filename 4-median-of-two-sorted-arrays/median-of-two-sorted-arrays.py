class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

       
        lo = 0
        hi = m

        while lo <= hi:

            
            i = (lo + hi) // 2

            
            j = (m + n + 1) // 2 - i

            
            if i > 0:
                left1 = nums1[i - 1]
            else:
                left1 = float('-inf')

            if i < m:
                right1 = nums1[i]
            else:
                right1 = float('inf')

            if j > 0:
                left2 = nums2[j - 1]
            else:
                left2 = float('-inf')

            if j < n:
                right2 = nums2[j]
            else:
                right2 = float('inf')

           
            if left1 <= right2 and left2 <= right1:

                
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))

               
                else:
                    left_max = max(left1, left2)
                    right_min = min(right1, right2)

                    return (left_max + right_min) / 2.0

            
            elif left1 > right2:
                hi = i - 1

        
            else:
                lo = i + 1



obj = Solution()


median1 = obj.findMedianSortedArrays([1, 3], [2])

print(median1)

median2 = obj.findMedianSortedArrays([1, 2], [3, 4])

print(median2)