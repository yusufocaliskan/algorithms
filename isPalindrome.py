class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        rev = ""
        for num in reversed(x):
            rev += str(num)
            
            if(rev == x):
                return True
        
print(Solution().isPalindrome(21000012))