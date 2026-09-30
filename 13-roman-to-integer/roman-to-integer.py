class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        romans = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        n = len(s)

        total = 0

        for i in range(n):

            crr = romans[s[i]]

            if i + 1 < n and crr < romans[s[i+1]]:

                total -= crr

            else :
                
                total += crr

        return total

obj = Solution()

ex1 = obj.romanToInt("III")

ex2 = obj.romanToInt("LVIII")

ex3 = obj.romanToInt("MCMXCIV")