class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if sorted(s) == sorted(t):

            return True

        else :

            return False

obj = Solution()

ex1 = obj.isAnagram("anagram","nagaram")

ex2 = obj.isAnagram("rat","car")

print(ex1)

print(ex2)